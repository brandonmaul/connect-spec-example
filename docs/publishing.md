# Publishing

Nobody reads the source folders directly unless they are changing them. Every
merge to `main` builds one bundle from them and publishes it, so every audience
reads the same content at the same commit.

## What gets published

`python3 scripts/build.py` writes `dist/`, and the
[workflow](../.github/workflows/publish.yml) publishes it to GitHub Pages:

| File | For | What it is |
|---|---|---|
| `llms-full.txt` | Claude and other AI tools | The whole repo as one Markdown file: glossary, design, every rule, context. **This is the link to give Claude.** |
| `llms.txt` | AI tools that browse | An index of every page, in the [llms.txt](https://llmstxt.org) format |
| `index.html` | People | The same content as a readable page, with diagrams |
| `pages/…` | Both | Each source page on its own |
| `views/client-browser.md` etc. | Each client team | Every rule its client must follow |
| `views/status.md` | Leadership | Rule counts by area and client |
| `rules.json` | Tools | Every rule's ID, status, Needs and text |

## Using it with Claude

**Claude Projects.** Put this in the project's instructions:

> Before starting, read the Connect source of truth:
> `<pages-url>/llms-full.txt`. Use its glossary terms, cite rule IDs, and say
> when a rule is a draft.

Or connect the GitHub repo to the project as a knowledge source, so Claude reads
the files directly and they stay in sync.

**Claude Code and other agents.** Working in this repo, they read
[AGENTS.md](../AGENTS.md) automatically. From another repo, point them at
`llms-full.txt`.

## Why not republish the guide artifact

A page edited by hand drifts from the rules, and a single URL can only serve one
audience. Building from the repo means each reader gets a view made for them
(Claude gets one plain file, people get a page, client teams get their rules), and
all of them come from the same commit.

## Before the bundle goes anywhere public

This repo is an example. Context pages name people, internal URLs and tickets.
The real repo should be private to the organization, and its Pages site should
be restricted to organization members (GitHub Enterprise private Pages) or
replaced with an internal host.
