# For engineers

Rules in `spec/` are [OpenFastTrace](https://github.com/itsallcode/openfasttrace)
(OFT) markdown. This page is the detail that product owners and leadership do not
need: how rule IDs are built, how areas and topics are organised, the file format,
and how tests in the code repos point at rules.

## Rule IDs

Every rule ID has three parts:

```
MSG  -  READ  -  002
 │       │        │
 │       │        └── number: the rule's place in its topic
 │       └─────────── topic: the theme inside the area
 └─────────────────── area: the part of Connect
```

| Part | Looks like | Example | Means |
|---|---|---|---|
| **Area** | Capital letters, may include digits | `MSG`, `MEMBERSHIP`, `V2V3` | A part of Connect. Each area has its own file. |
| **Topic** | Capital letters only | `SEND`, `READ`, `ARCHIVE` | One theme inside an area. Each area lists its topics at the top of its file. |
| **Number** | Three digits | `001`, `002` | Counts up from `001` within each topic. |

So `MSG-READ-002` is the second rule about reading, in the Messages area.

IDs match `^[A-Z][A-Z0-9]*-[A-Z]+-\d{3}$`. OFT sees the whole ID as one item name;
the area/topic split is this repo's convention.

Three things never change, so links to a rule keep working:

- **An ID is never reused.** A retired rule keeps its number, and the next new rule
  takes the next number up.
- **An ID is never renamed.** If a rule turns out to belong in another topic, it
  keeps its old ID.
- **A number is never filled in.** If `003` is retired, the next rule is still `004`.

## Areas and topics

The list of areas is in the README, under
[Where the rules are](../README.md#where-the-rules-are). Each area is one file, and
its code and topics are declared at the top of that file, so that is the only
place to look them up. Every rule in the file uses that area code and one of those
topics.

The same topic word can appear in several areas when it means the same thing. For
example, `ARCHIVE` is about archiving in Conversations and in both bridges.

### Behavior on only some devices

Areas are named for **what a person can do**, never for a device or platform. There
is no "Apple" or "web" area. Which devices a rule applies to is said by its `Needs`:

| Behavior | Rule | Needs |
|---|---|---|
| Sending a message with Siri | VOICE-SEND-001 in Voice assistants | `ios` |
| Sharing a photo into Connect from another app | SHARE-PICK-001 in Sharing into Connect | `ios, macos, web` |
| Installing Connect on the home screen from the browser | APP-INSTALL-001 in The Connect app | `web` |
| Enter sends a message on a computer | MSG-COMPOSE-001 in Messages | `web` |
| Shortcuts from pressing and holding the app icon | APP-ICON-004 in The Connect app | `ios, web` |

This keeps a behavior in one place when it spreads to more devices. If Android
sharing arrives, the sharing rules stay where they are and gain one more word in
`Needs`. If a behavior needs different wording on different devices, write one rule
per device in the same area, each with its own `Needs`.

### Adding a topic

Add a topic when a new rule is about a theme that none of the area's topics cover.

1. Check the topics at the top of the area's file. A new rule that fits an existing
   topic goes there, even if the topic is small.
2. Look at the topics in the other areas' files. If one already uses a word for the
   same idea, use the same word, so `ARCHIVE` always means archiving.
3. Choose one short word in capital letters, with no digits or dashes. Name the
   behavior, not a screen or feature name that might change: `READ`, not `BADGE`.
4. Add the topic, with a one-line description, to the topics list at the top of the
   area's file.
5. Its first rule is number `001`, for example `MSG-PIN-001`.

### Adding an area

Add an area for a part of Connect that has rules of its own and fits no existing
area. If it could be a topic in an existing area, make it a topic instead: fewer
areas are easier to find your way around.

1. Choose the area's code: short capital letters, digits allowed (`CONV`, `VOICE`,
   `V2V3`). It must not be used by any other area, now or in the past. Name the part
   of the product, not a team, project, release or device, because the code lasts as
   long as the rules do (see [behavior on only some devices](#behavior-on-only-some-devices)).
   Check the top of every area's file to make sure the code is free.
2. Copy [templates/new-area.md](../templates/new-area.md) into `spec/`, in the folder
   for that part of Connect, or a new folder if none fits.
3. Fill in the area's name, what it covers and its first topics. Replace `AREA` and
   `TOPIC` in the example rule.
4. Add it to the area list in the [README](../README.md#where-the-rules-are).
5. Open a pull request.

## Format rules

- Each rule is a `###` heading `AREA-TOPIC-NNN: Title`, with the OFT ID
  `` `req~AREA-TOPIC-NNN~R` `` on the **line directly after it**. The name in the
  heading and in the ID must match.
- The scenario is indented four spaces, not fenced, so OFT reads it as description.
- Sections are OFT keywords at the start of a line, each after a blank line:
  `Rationale:`, `Comment:`, `Status:` (`draft`, `rejected`; omitted means approved)
  and `Needs:`.
- Rules in a file are ordered by the topic table, then by number.
- Only `spec/` is traced. The README and `templates/` contain example IDs that are
  not rules.

## Needs

`Needs` values are OFT artifact types, one per place that must prove the rule.
They are written in this order: `nitro`, `nitroid`, `server`, `ccl`, `ios`,
`macos`, `web`.

They fall into two groups, and the README gives each group a different owner:

| Group | Types | Who writes them | Answers |
|---|---|---|---|
| Apps | `ios`, `macos`, `web` | Product, when writing the rule | Where does a person see this? |
| Systems | `nitro`, `nitroid`, `server`, `ccl` | Engineering, in review | What has to work for it to happen? |

Product proposals often arrive with only the apps. Adding the systems is part of
reviewing the pull request.

### The CCL is a layer, not a platform

The CCL is built into the apps, so `ccl` never replaces an app in `Needs`. It is
added alongside them:

- **A rule a person can see names its apps**, whatever builds it underneath. The
  validation check rejects `ccl` without at least one app.
- **Add `ccl` when the CCL decides the outcome**: what is stored or cleared, order,
  retries, read state, what counts as unread. Leave it out when the CCL only passes
  data through and the app decides what to show.
- **Both are proved.** CCL tests fake the apps, and app tests fake the CCL. Signing
  out can clear everything in the CCL while an app still shows the old screen, so
  `ccl` proves the decision and each app proves the person sees it.

`Needs: ccl, ios, macos, web` does not say how each app gets the behavior, only
that each must have it. Today connect-web does not use the CCL, so it meets these
rules with its own code. When the web moves onto the CCL, those rules stay as they
are. What changes is how the `web` tests prove them, and many become checks that
the web shows what the CCL decided. The rules with both `ccl` and `web` are the
behavior the move must keep, so their `web` coverage tracks the move's progress.

### Every hop

- List **every system a rule passes through**, not only where it starts and ends.
  Each repo's tests fake their neighbours, so a hop left out of `Needs` can break
  while every listed test still passes. `nitroid` exists for this reason: Nitro ID
  only relays people and groups from Nitro to Connect V3, but a relay that stops
  relaying breaks every Power membership rule. Tempo ID gets no type because it is
  a third-party product with no tests of ours.
- Even with every hop listed, each repo only proves its own step. Proving the whole
  path needs an end-to-end test, which is still undecided (below).

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
