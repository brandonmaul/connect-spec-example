#!/usr/bin/env python3
"""Check the repo and build the published bundle in dist/.

    python3 scripts/build.py           # check, then build dist/
    python3 scripts/build.py --check   # check only

Standard library only, so it runs anywhere Python 3.9+ does.

dist/ holds:
  llms.txt                  index of every page, for AI tools (llmstxt.org format)
  llms-full.txt             the whole repo as one Markdown file: the URL to give Claude
  pages/<path>.md           each source page, as the index links to it
  views/client-<x>.md       every rule that applies to one client
  views/status.md           rule counts by area and client
  index.html                the same content for people to read in a browser
"""
from __future__ import annotations

import html
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"

# Reading order of the bundle. A new file in one of these folders that is not
# listed is appended to its section, so nothing is ever silently left out.
SECTIONS = [
    ("How to use this", ["AGENTS.md"]),
    ("Glossary", ["glossary/systems.md", "glossary/interface.md", "glossary/devices.md"]),
    ("Design", ["design/design-and-voice.md", "design/error-messaging.md",
                "design/message-formatting.md"]),
    ("Behavior rules", [
        "spec/membership/connect-access.md",
        "spec/account/account.md",
        "spec/settings/settings.md",
        "spec/conversations/conversations.md",
        "spec/conversations/conversation-view.md",
        "spec/messaging/messages.md",
        "spec/messaging/formatting.md",
        "spec/notifications/notifications.md",
        "spec/sorting/sorting-and-naming.md",
        "spec/keyboard/keyboard.md",
        "spec/people/people.md",
        "spec/audiences/conversation-members.md",
        "spec/events/corporate-events.md",
        "spec/appointments/appointment-cards.md",
        "spec/bridge/v2-to-v3.md",
        "spec/bridge/v3-to-v2.md",
        "spec/sharing/sharing-into-connect.md",
        "spec/voice/voice-assistants.md",
        "spec/app/connect-app.md",
    ]),
    ("Context (snapshots)", ["context/system.md", "context/parity.md", "context/history.md",
                             "context/projects.md", "context/open-questions.md",
                             "context/sources.md"]),
]
SECTION_DIRS = {"Glossary": "glossary", "Design": "design", "Behavior rules": "spec",
                "Context (snapshots)": "context"}

SYSTEM_TARGETS = ["nitro", "nitroid", "server", "ccl"]
CLIENT_TARGETS = ["browser", "pwa", "macos", "ios"]
TARGETS = SYSTEM_TARGETS + CLIENT_TARGETS
STATUSES = {"draft", "rejected"}

# Rules describe product behavior only. These patterns catch the usual leaks.
PRODUCT_ONLY = [
    (re.compile(r"\b(?:ROGUE|RBLS|JEDI)-\d+"), "ticket ID"),
    (re.compile(r"\bC[AWS]-[A-Z]+-\d+"), "QA test ID"),
    (re.compile(r"\bPR ?#?\d+", re.I), "pull request"),
    (re.compile(r"\b20\d\d-\d\d(?:-\d\d)?\b"), "date"),
]

RULE_HEADING = re.compile(r"^### ([A-Z][A-Z0-9]*-[A-Z]+-\d{3}): (.+)$")
STAMP = re.compile(r"^`req~([A-Z][A-Z0-9]*-[A-Z]+-\d{3})~(\d+)`$")
AREA_CODE = re.compile(r"^\*\*Area code:\*\* `([A-Z][A-Z0-9]*)`", re.M)
TOPIC_ROW = re.compile(r"^\| `([A-Z]+)` \|", re.M)


@dataclass
class Rule:
    id: str
    title: str
    revision: int
    status: str  # "approved", "draft" or "rejected"
    needs: list[str]
    path: str
    line: int
    body: str

    @property
    def area(self) -> str:
        return self.id.split("-")[0]

    @property
    def topic(self) -> str:
        return self.id.split("-")[1]


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"{where}: {msg}")


# ---------------------------------------------------------------- reading rules

def parse_rules(path: Path, report: Report) -> list[Rule]:
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    area_match = AREA_CODE.search(text)
    area = area_match.group(1) if area_match else None
    if not area:
        report.error(rel, "no '**Area code:** `X`' line")
    topics = TOPIC_ROW.findall(text)

    starts = [i for i, l in enumerate(lines) if l.startswith("### ")]
    rules = []
    for n, start in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(lines)
        block = lines[start:end]
        where = f"{rel}:{start + 1}"
        heading = RULE_HEADING.match(block[0])
        if not heading:
            report.error(where, f"heading is not 'AREA-TOPIC-NNN: Title': {block[0]!r}")
            continue
        rid, title = heading.groups()
        stamp = STAMP.match(block[1]) if len(block) > 1 else None
        if not stamp or stamp.group(1) != rid:
            report.error(where, f"{rid}: the line after the heading must be `req~{rid}~N`")
            continue
        body = "\n".join(block[2:]).strip()
        rule = Rule(rid, title.strip(), int(stamp.group(2)), "approved", [], rel, start + 1, body)

        for l in block[2:]:
            if l.startswith("Status:"):
                rule.status = l.split(":", 1)[1].strip()
            elif l.startswith("Needs:"):
                rule.needs = [t.strip() for t in l.split(":", 1)[1].split(",") if t.strip()]
        check_rule(rule, area, topics, where, report)
        rules.append(rule)
    return rules


def check_rule(rule: Rule, area: str | None, topics: list[str], where: str,
               report: Report) -> None:
    if area and rule.area != area:
        report.error(where, f"{rule.id} is in area {area}'s file")
    if topics and rule.topic not in topics:
        report.error(where, f"{rule.id}: topic {rule.topic} is not in the area's topic table")
    if rule.status != "approved" and rule.status not in STATUSES:
        report.error(where, f"{rule.id}: Status must be draft or rejected, not {rule.status!r}")
    if not rule.needs:
        report.error(where, f"{rule.id}: no Needs line")
    unknown = [t for t in rule.needs if t not in TARGETS]
    if unknown:
        report.error(where, f"{rule.id}: unknown Needs target(s) {unknown}; use {TARGETS}")
    known = [t for t in rule.needs if t in TARGETS]
    if known != sorted(known, key=TARGETS.index):
        report.error(where, f"{rule.id}: Needs out of order; write them as {TARGETS}")
    if "ccl" in rule.needs and not any(t in CLIENT_TARGETS for t in rule.needs):
        report.error(where, f"{rule.id}: ccl is built into the apps, so name at least one client")
    for pattern, what in PRODUCT_ONLY:
        hit = pattern.search(rule.body) or pattern.search(rule.title)
        if hit:
            report.error(where, f"{rule.id}: rules describe behavior only, found a {what}: {hit.group(0)!r}")


def check_ids_unique(rules: list[Rule], report: Report) -> None:
    seen: dict[str, Rule] = {}
    for r in rules:
        if r.id in seen:
            report.error(f"{r.path}:{r.line}", f"{r.id} is also used at {seen[r.id].path}:{seen[r.id].line}")
        seen[r.id] = r


# ---------------------------------------------------------------- ordering pages

def ordered_pages(report: Report) -> list[tuple[str, list[str]]]:
    result = []
    for name, listed in SECTIONS:
        pages = [p for p in listed if (ROOT / p).exists()]
        for p in listed:
            if not (ROOT / p).exists():
                report.error("scripts/build.py", f"SECTIONS lists {p}, which does not exist")
        folder = SECTION_DIRS.get(name)
        if folder:
            extra = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / folder).rglob("*.md"))
            for p in extra:
                if p not in pages:
                    report.warn(p, f"not listed in SECTIONS; appended to '{name}'")
                    pages.append(p)
        result.append((name, pages))
    return result


# ---------------------------------------------------------------- building

def repo_url() -> str:
    if os.environ.get("REPO_URL"):
        return os.environ["REPO_URL"].rstrip("/")
    if os.environ.get("GITHUB_REPOSITORY"):
        return f"https://github.com/{os.environ['GITHUB_REPOSITORY']}"
    try:
        url = subprocess.run(["git", "remote", "get-url", "origin"], cwd=ROOT,
                             capture_output=True, text=True, check=True).stdout.strip()
        return re.sub(r"\.git$", "", re.sub(r"^git@github.com:", "https://github.com/", url))
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def absolute_links(text: str, page: str, base: str) -> str:
    """Point relative links at the repo, since a bundle has no folders."""
    here = (ROOT / page).parent

    def fix(m: re.Match) -> str:
        label, target = m.group(1), m.group(2)
        if re.match(r"^[a-z]+:|^#", target) or not base:
            return m.group(0)
        path, _, anchor = target.partition("#")
        resolved = (here / path).resolve()
        try:
            rel = resolved.relative_to(ROOT).as_posix()
        except ValueError:
            return m.group(0)
        kind = "tree" if resolved.is_dir() else "blob"
        return f"[{label}]({base}/{kind}/main/{rel}{'#' + anchor if anchor else ''})"

    return re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)", fix, text)


def demote_headings(text: str) -> str:
    """Nest a page's headings one level under its bundle section, outside code fences."""
    out, fenced = [], False
    for line in text.splitlines():
        if line.startswith("```"):
            fenced = not fenced
        if not fenced and re.match(r"^#{1,5} ", line):
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def page_title(page: str) -> str:
    for line in (ROOT / page).read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return page


def build_full(pages: list[tuple[str, list[str]]], rules: list[Rule], base: str, sha: str) -> str:
    counts = {s: sum(1 for r in rules if r.status == s) for s in ("approved", "draft", "rejected")}
    parts = [
        "# Connect: the source of truth",
        "",
        f"Generated from {base or 'the connect-spec repo'} at commit `{sha}`. "
        "Do not edit this file; change the repo. Everything about what Connect is, "
        "what its parts are called, how it should look, and how it must behave is here.",
        "",
        "How to read it:",
        "",
        "- **Glossary** names every part of Connect. Use these terms exactly.",
        "- **Design** says how Connect looks and sounds.",
        "- **Behavior rules** say what Connect must do, one rule per behavior. Each has a "
        "permanent ID (like `MSG-SEND-002`), an example, a reason, and `Needs`: the clients "
        f"(`{'`, `'.join(CLIENT_TARGETS)}`) and systems (`{'`, `'.join(SYSTEM_TARGETS)}`) that "
        "must follow it. A rule with no `Status` is agreed. `Status: draft` means not yet "
        "confirmed by Product; `Status: rejected` means it no longer applies or another rule covers it.",
        "- **Context** is a dated snapshot of projects, history and open questions. "
        "Prefer the rules when they disagree.",
        "",
        f"Rules: {counts['approved']} agreed, {counts['draft']} draft, {counts['rejected']} rejected.",
        "",
    ]
    for name, section_pages in pages:
        parts += [f"# {name}", ""]
        for page in section_pages:
            text = (ROOT / page).read_text(encoding="utf-8").strip()
            text = absolute_links(text, page, base)
            parts += [f"<!-- source: {page} -->", demote_headings(text), ""]
    return "\n".join(parts).rstrip() + "\n"


def build_index(pages: list[tuple[str, list[str]]], base: str, site: str) -> str:
    lines = [
        "# Connect",
        "",
        "> The single source of truth for Connect, Power's internal messaging product: "
        "its vocabulary, design conventions, behavior rules and current context. "
        "Read llms-full.txt for everything in one file.",
        "",
        f"- [Everything in one file]({site}llms-full.txt): start here",
        f"- [Rule counts by area and client]({site}views/status.md)",
        "",
    ]
    for name, section_pages in pages:
        lines += [f"## {name}", ""]
        for page in section_pages:
            lines.append(f"- [{page_title(page)}]({site}pages/{page})")
        lines.append("")
    lines += ["## Rules by client", ""]
    for c in CLIENT_TARGETS:
        lines.append(f"- [Every rule for {c}]({site}views/client-{c}.md)")
    lines.append("")
    return "\n".join(lines)


def build_client_view(client: str, rules: list[Rule], base: str) -> str:
    mine = [r for r in rules if client in r.needs and r.status != "rejected"]
    lines = [f"# Every rule for {client}", "",
             f"{len(mine)} rules list `{client}` in Needs "
             f"({sum(r.status == 'draft' for r in mine)} of them draft).", ""]
    current = None
    for r in mine:
        if r.path != current:
            current = r.path
            lines += [f"## {page_title(r.path)}", ""]
        flag = " *(draft)*" if r.status == "draft" else ""
        lines.append(f"- [{r.id}]({base}/blob/main/{r.path}#L{r.line}): {r.title}{flag}")
    return "\n".join(lines) + "\n"


def build_status(rules: list[Rule], pages: list[tuple[str, list[str]]]) -> str:
    order = [p for _, section_pages in pages for p in section_pages]
    areas: dict[str, list[Rule]] = {}
    for r in sorted(rules, key=lambda r: order.index(r.path) if r.path in order else len(order)):
        areas.setdefault(r.path, []).append(r)
    head = "| Area | Agreed | Draft | Rejected | " + " | ".join(CLIENT_TARGETS) + " |"
    lines = ["# Rule counts", "",
             "Agreed rules per area, and how many agreed rules each client must follow. "
             "Once code repos report test coverage, each client column becomes "
             "\"proven / required\".", "", head,
             "|---" * (4 + len(CLIENT_TARGETS)) + "|"]
    for path, rs in areas.items():
        agreed = [r for r in rs if r.status == "approved"]
        row = [page_title(path), str(len(agreed)), str(sum(r.status == "draft" for r in rs)),
               str(sum(r.status == "rejected" for r in rs))]
        row += [str(sum(c in r.needs for r in agreed)) for c in CLIENT_TARGETS]
        lines.append("| " + " | ".join(row) + " |")
    agreed = [r for r in rules if r.status == "approved"]
    total = ["**Total**", f"**{len(agreed)}**", f"**{sum(r.status == 'draft' for r in rules)}**",
             f"**{sum(r.status == 'rejected' for r in rules)}**"]
    total += [f"**{sum(c in r.needs for r in agreed)}**" for c in CLIENT_TARGETS]
    lines.append("| " + " | ".join(total) + " |")
    return "\n".join(lines) + "\n"


HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Connect Source of Truth</title>
<link rel="alternate" type="text/plain" href="llms-full.txt" title="Everything in one file">
<style>
:root{--bg:#fff;--fg:#1d1d1f;--muted:#6e6e73;--rule:#e5e5ea;--fill:#f5f5f7;--link:#0a66d6}
@media (prefers-color-scheme:dark){:root{--bg:#111;--fg:#f2f2f7;--muted:#a1a1a6;--rule:#2c2c2e;--fill:#1c1c1e;--link:#5aa8ff}}
body{background:var(--bg);color:var(--fg);font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;margin:0}
main{max-width:860px;margin:0 auto;padding:24px 16px 80px}
a{color:var(--link)}code{background:var(--fill);padding:1px 4px;border-radius:4px;font-size:.9em}
pre{background:var(--fill);padding:12px;border-radius:6px;overflow-x:auto}pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;display:block;overflow-x:auto;font-size:.92em}
th,td{border:1px solid var(--rule);padding:6px 8px;text-align:left;vertical-align:top}
h1{border-bottom:1px solid var(--rule);padding-bottom:6px;margin-top:48px}
.banner{background:var(--fill);border-radius:8px;padding:12px 14px;color:var(--muted);font-size:.9em}
</style>
</head>
<body>
<main>
<p class="banner">Generated from <a href="__REPO__">the repo</a> at <code>__SHA__</code>. To change anything, comment on it or open a pull request. For Claude, use <a href="llms-full.txt">llms-full.txt</a>.</p>
<div id="content">Loading…</div>
</main>
<script id="source" type="text/markdown">__MARKDOWN__</script>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>
const md = document.getElementById("source").textContent;
const out = document.getElementById("content");
out.innerHTML = marked.parse(md);
out.querySelectorAll("h1,h2,h3,h4,h5").forEach(h => {
  const m = h.textContent.match(/^([A-Z][A-Z0-9]*-[A-Z]+-\\d{3})/);
  h.id = m ? m[1] : h.textContent.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
});
out.querySelectorAll("code.language-mermaid").forEach(c => {
  const d = document.createElement("div"); d.className = "mermaid"; d.textContent = c.textContent;
  c.parentElement.replaceWith(d);
});
mermaid.initialize({startOnLoad:false, theme: matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "default"});
mermaid.run();
</script>
</body>
</html>
"""


def build_html(full: str, base: str, sha: str) -> str:
    safe = full.replace("</script", "<\\/script")
    return (HTML.replace("__MARKDOWN__", safe).replace("__REPO__", html.escape(base or "#"))
            .replace("__SHA__", html.escape(sha)))


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    report = Report()

    rules: list[Rule] = []
    for path in sorted((ROOT / "spec").rglob("*.md")):
        rules += parse_rules(path, report)
    check_ids_unique(rules, report)
    pages = ordered_pages(report)

    for w in report.warnings:
        print(f"warning: {w}")
    for e in report.errors:
        print(f"error: {e}")
    print(f"{len(rules)} rules: "
          + ", ".join(f"{sum(r.status == s for r in rules)} {s}" for s in ("approved", "draft", "rejected")))
    if report.errors:
        print(f"{len(report.errors)} error(s)")
        return 1
    if check_only:
        return 0

    base = repo_url()
    sha = os.environ.get("GITHUB_SHA") or subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True
    ).stdout.strip() or "unknown"
    sha = sha[:12]
    site = os.environ.get("SITE_URL", "").rstrip("/") + "/" if os.environ.get("SITE_URL") else ""

    full = build_full(pages, rules, base, sha)
    write(DIST / "llms-full.txt", full)
    write(DIST / "llms.txt", build_index(pages, base, site))
    for _, section_pages in pages:
        for page in section_pages:
            text = absolute_links((ROOT / page).read_text(encoding="utf-8"), page, base)
            write(DIST / "pages" / page, text)
    for c in CLIENT_TARGETS:
        write(DIST / "views" / f"client-{c}.md", build_client_view(c, rules, base))
    write(DIST / "views" / "status.md", build_status(rules, pages))
    write(DIST / "rules.json", json.dumps([r.__dict__ for r in rules], indent=1) + "\n")
    write(DIST / "index.html", build_html(full, base, sha))
    print(f"built {DIST.relative_to(ROOT)}/ ({len(full):,} characters in llms-full.txt)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
