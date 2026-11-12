# Adoption plan

## The problem

Connect's behavior lives in Runway, Connect threads, Huddle, Figma and people's
memory. Very little is pinned by a test that says why. Behavior regresses easily,
and nobody can say what "correct" is. The CCL work on Apple only revealed what was
undefined once it was underway, and connect-web is about to adopt the CCL with no
list of what "equivalent to Apple" means.

## Defining "done" for connect-web

Once the rules exist, "done" is a query:

> connect-web is done when every approved rule that applies to `browser`, `pwa` or
> `ccl` is proven by a passing test in its repo.

Count the rules that apply to `browser` and `pwa`, count the ones with a passing test, and the
difference is the work left. Divided by how fast the team closes rules, that is a
timeline. It also separates two questions that are blurred today: does the CCL
satisfy every `ccl` rule, and does connect-web render and behave correctly for every
`browser` and `pwa` rule. Work for only some clients, like Siri, never lists them, so
it never counts against web.

## Getting to the first few hundred rules

This repo has done one round of this already: the UX context guide was taken as
confirmed, every rule it supports was approved or corrected to match it, every
behavior it describes became a rule, and everything it couldn't confirm became a
draft. The drafts are Product's first triage queue.

1. **Harvest** candidates from connect-apple (the de facto definition), nitro-web V2,
   existing tests, Huddle flows, Figma and Runway acceptance criteria. An agent can
   draft one rule per observable behavior with its source linked.
2. **Land them as `Status: draft`.** Drafts count against nobody.
3. **Product triages**: confirm, correct, or retire each one. Disagreements with how
   Apple behaves are exactly the divergences that would otherwise surface late.
4. **Engineering links existing tests** to the approved rules they already prove.
5. **What is left unproven is the backlog.**

## Not decided yet

- **How code repos say which rules a test proves, and how a changed rule invalidates
  those tests.** This lives in the code repos, not here.
- **How "did the test pass" is counted.** Each repo already knows; the question is how
  it is reported centrally.
- **Granularity.** Agree an example of "too coarse" and "too fine" before seeding hundreds.
- **V2 scope.** V2 sunsets in 2027, so probably only what V3 must match, and the bridge.
- **Ownership.** Product owns `spec/`, UX owns `glossary/` and `design/`. Fill in
  `.github/CODEOWNERS` with real teams.
- **Context feeds.** `context/projects.md` and `context/parity.md` are kept by hand
  today. Projects could be generated from Runway and Huddle, and parity from each
  repo's rule coverage.
