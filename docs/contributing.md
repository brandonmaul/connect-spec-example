# Contributing

Anyone can propose a change. You don't need to know Git.

## Who owns what

Each layer has one owner, who approves changes to it. Owners are set in
[`.github/CODEOWNERS`](../.github/CODEOWNERS).

| Layer | Folder | Owner | Holds |
|---|---|---|---|
| Behavior | `spec/` | Product | One rule per behavior, with an example, a reason, and the clients it applies to |
| Vocabulary | `glossary/` | UX | Interface, device and system terms |
| Design | `design/` | UX | Playbook use, layout, look, voice, error patterns, how Markdown renders |
| Context | `context/` | Product and UX | System overview, release history, parity, projects, open questions. Snapshots, each with its live source |
| Tooling | `scripts/`, `.github/` | Engineering | The build, the checks, the published bundle |

## Three ways to propose a change

### 1. Comment on the published guide (lowest effort)

Comment on the section a change affects, one topic per comment, with a source if
you have one. Don't edit copies or send DMs.

Every 1–2 weeks the guide's editor asks Claude to process open comments. Claude
turns each into a pull request against this repo, using the right format for its
layer (a rule, a term, a design convention), and links the comment. The layer's
owner approves or edits the pull request. When it merges, Claude replies in the
comment thread with the link. Open threads are the backlog.

### 2. Open an issue

Use [Propose a rule](../../../issues/new/choose) for behavior. Describe what
should happen, an example and why. An engineer writes it up and asks you to
approve it.

### 3. Edit in the browser

Open the file, click the pencil icon, make the change, and choose **Create a new
branch and start a pull request**. For rules, see
[Changing a rule](../README.md#changing-a-rule).

## What happens after a merge

A merge to `main` rebuilds and republishes the bundle (see
[Publishing](publishing.md)). Every Claude Project, agent and reader pointed at it
sees the change on its next read. Git history replaces a hand-kept changelog:
every change says who made it, who approved it, and why.
