# For engineers

Rules in `spec/` are [OpenFastTrace](https://github.com/itsallcode/openfasttrace)
(OFT) markdown. This page is the detail that product owners and leadership do not
need.

## Format rules

- Each rule is a `###` heading `AREA-TOPIC-NNN: Title`, with the OFT ID
  `` `req~AREA-TOPIC-NNN~R` `` on the **line directly after it**. The name in the
  heading and in the ID must match.
- IDs match `^[A-Z][A-Z0-9]*-[A-Z]+-\d{3}$`: area (letters, then letters or digits),
  topic (letters only), three-digit number. OFT sees the whole thing as one item
  name; the area/topic split is this repo's convention, explained in the README.
- One area per file. Each file declares `**Area code:**` and a **Topics** table
  before its first rule, and every rule in the file uses that area and one of those
  topics. The README's area table lists the same codes and topics.
- IDs are never reused, renamed or back-filled, even for rejected rules.
- The scenario is indented four spaces, not fenced, so OFT reads it as description.
- Sections are OFT keywords at the start of a line: `Rationale:`, `Comment:`,
  `Status:` (`draft`, `rejected`; omitted means approved) and `Needs:`.
- `Needs` values are OFT artifact types, one per place that must prove the rule:
  `ccl`, `server`, `nitro`, `nitroid`, `ios`, `macos`, `web`.
- List **every system a rule passes through**, not only where it starts and ends.
  Each repo's tests fake their neighbours, so a hop left out of `Needs` can break
  while every listed test still passes. `nitroid` exists for this reason: Nitro ID
  only relays people and groups from Nitro to Connect V3, but a relay that stops
  relaying breaks every Power membership rule. Tempo ID gets no type because it is
  a third-party product with no tests of ours.
- Even with every hop listed, each repo only proves its own step. Proving the whole
  path needs an end-to-end test, which is still undecided (below).
- Only `spec/` is traced. The README and `templates/` contain example IDs that are
  not rules.

## Proving a rule from a code repo

Tests live in the code repos, never here. A test proves a rule with an OFT coverage
tag in a comment, where the tag's type is the platform from `Needs`:

```swift
// [ios->req~MSG-SEND-002~1]
func test_failedMessageOffersRetry() { … }
```

```ts
// [web->req~MSG-SEND-002~1]
it("offers retry on a failed message", () => { … });
```

## Revisions

The trailing number is the revision. When a rule's meaning changes, product bumps
it. OFT then reports every tag still pointing at the old revision as **outdated**,
which is how a behavior change invalidates the tests written for the old behavior.
Wording fixes and `Needs` changes keep the revision.

## Not decided yet

- How each code repo runs OFT against this spec (pinned ref, submodule, or a nightly
  job here that checks out every repo).
- How "the tagged test passed" is counted, since OFT only proves a tag exists.
- Whether CI here should catch a meaning change made without a revision bump.
- Where end-to-end tests for rules that cross several systems live, and which tag
  type they use.
