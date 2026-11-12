# Instructions for AI assistants

This repo is the single source of truth for what Connect is and how it behaves.
Read [README.md](README.md) first for the layout. If you only have the published
bundle, everything below is in it too.

## Rules for writing about Connect

1. Use the capitalized terms in the [glossary](glossary/); flag any term that
   isn't defined rather than guessing.
2. Never write "New Message Button" alone: say "(compose)" or "(jump)".
3. Name the system and tenant: v2 Browser and Connect Browser (v3) are different
   products; Nitro Connect and Tempo Connect can differ.
4. Scope requirements with a device/platform term (for example "Mobile PWA",
   "Desktop Large Screen"); if a request says only "mobile" or "the app", ask
   which.
5. Document behavior per client (Browser, PWA, macOS, iOS); never assume they
   match. Layout follows screen size; interaction follows platform.
6. Keep bold (unread) and the Notification Badge (notifying, or manually unread)
   distinct.
7. Note the v2 side effect of anything the Bridge syncs until the Bridge is
   retired.
8. Lists and searches follow [Sorting and naming](spec/sorting/sorting-and-naming.md);
   state the sort and tiebreaker in acceptance criteria.
9. New interactive UI must be keyboard reachable and define its Esc behavior.
10. Any new surface showing message text must say how Markdown renders there.
11. Check the [design projects in Huddle](context/projects.md#design-projects-in-huddle)
    for an existing handoff first; use Playbook and note any kit missing from PB
    Swift with its native fallback.
12. When a project changes terms, UI, clients, or architecture, propose the
    matching change to this repo (a rule, a glossary term, a design convention).

## Answering questions about Connect

- **"How does X behave?"** Answer from `spec/`, citing rule IDs
  (`MSG-SEND-002`). A rule with `Status: draft` is not confirmed: say so. If no
  rule covers it, say that too rather than guessing.
- **"What do we call X?"** Answer from `glossary/`.
- **"How should X look or read?"** Answer from `design/`.
- **"What's happening / shipping / open?"** Answer from `context/`, and say it is
  a snapshot with a last-reviewed date.

## Changing this repo

- Rules follow the format in [docs/for-engineers.md](docs/for-engineers.md).
  Rules describe observable product behavior only: no ticket or test IDs, PR
  numbers, dates, code or vendor names, or "not built yet" notes.
- Run `python3 scripts/build.py --check` before proposing a change. It rejects
  malformed rules and the things above.
- Never edit `dist/`; it is generated.
