# Connect: the source of truth

> **Example repo.** This shows how the Connect context guide and the product spec
> work as one source. Rules confirmed by the context guide are agreed; the rest
> are drafts waiting for Product to confirm them.

Everything about what Connect is, what its parts are called, how it should look
and how it must behave lives here, once. Every audience reads a view built from
it: Claude reads one plain file, people read a web page, each client team gets the
rules for its client, and leadership gets counts.

## Why one source

Today Connect is described in Runway tickets, Connect threads, Huddle, Figma, QA
catalogs, a UX context guide, and people's memories. They drift apart, and the
three teams building Connect (Jedi Order, Rogue One, Rebel Alliance) end up
arguing about whose version is right. This repo fixes that:

- **One answer per question.** Each fact has exactly one home. Everything else is
  generated from it or links to it.
- **Everyone can say what "correct" is.** Every behavior has one written rule
  and a reason.
- **Behavior can't quietly break.** Once a rule has a test behind it, it cannot
  change without someone noticing.
- **"Done" is a number.** If connect-web has to follow 300 rules and 180 are
  proven, we know exactly what is left.

Because it is kept in GitHub, every change is reviewed, and the history of what
anything used to say, and why it changed, is kept forever.

## What lives where

| Layer | Folder | Owner | Holds |
|---|---|---|---|
| Vocabulary | [`glossary/`](glossary/) | UX | [System and tenant terms](glossary/systems.md), [interface terms](glossary/interface.md), [device and screen terms](glossary/devices.md) |
| Design | [`design/`](design/) | UX | [Design and voice](design/design-and-voice.md), [error messaging](design/error-messaging.md), [how Markdown looks](design/message-formatting.md) |
| Behavior | [`spec/`](spec/) | Product | One rule per behavior (below) |
| Context | [`context/`](context/) | Product and UX | [What Connect is](context/system.md), [parity](context/parity.md), [history](context/history.md), [projects](context/projects.md), [open questions](context/open-questions.md), [sources](context/sources.md). Dated snapshots, each naming its live source |
| Tooling | `scripts/`, `.github/` | Engineering | The checks and the [published bundle](docs/publishing.md) |

When two layers seem to disagree, the rule in `spec/` wins, and the other layer
gets fixed.

**To read it**, use the published bundle rather than these folders: see
[Publishing](docs/publishing.md). **To change it**, see
[Contributing](docs/contributing.md). **AI assistants** start at
[AGENTS.md](AGENTS.md).

## Reading a rule

Every rule looks the same:

> ### MSG-SEND-002: On Apple, a failed message turns red with Retry and Delete
> `req~MSG-SEND-002~1`
>
> On Apple, a message that cannot be sent stays in the Conversation View, turns red,
> and offers Retry and Delete.
>
>     Given a person sends a message on their iPhone while the server is unreachable
>     When the send fails
>     Then the message stays in the Conversation View in red
>     And it offers "Retry" and "Delete"
>
> Rationale:
> A failed message must be visible and recoverable, or the person believes it was delivered.
>
> Needs: ccl, macos, ios

The Browser and the PWA show a failed message differently, so each has its own
rule (MSG-FAIL-010 and MSG-FAIL-011) instead of sharing this one.

| What you see | What it means |
|---|---|
| **MSG-SEND-002** | The rule's ID. It never changes, so tickets, threads and tests can point to it. It reads as "Messages, sending, rule 2". |
| **On Apple, a failed message turns red…** | A short title. |
| `req~MSG-SEND-002~1` | A stamp for the checking tool. You can ignore it, except the number at the end (see [changing a rule](#changing-a-rule)). |
| The first sentence | The rule itself. |
| Given / When / Then | One worked example: the starting situation, what happens, and what the person should see. |
| **Rationale** | Why it works this way. For a draft, the question still to answer. |
| **Status** | Only on rules that aren't agreed (see [terms you will see](#terms-you-will-see)). |
| **Needs** | Which parts of Connect must follow this rule (see [terms you will see](#terms-you-will-see)). |

Words in rules are the [glossary](glossary/)'s words, used exactly.

## Where the rules are

Each area is one page. Open it to see its rules.

| Area | What it covers |
|---|---|
| [Membership](spec/membership/connect-access.md) | Who has Connect v2 and v3, and what happens when people join, change, leave and come back |
| [Account](spec/account/account.md) | Signing in and out, staying signed in, and using several devices |
| [Settings](spec/settings/settings.md) | A person's own preferences, like sort and layout, and how they follow them between devices |
| [Conversations](spec/conversations/conversations.md) | Rooms, People Conversations and the Self Message: the Conversation List, names, sections, Favorites, hiding, unread marks, starting, joining and leaving, Browse Rooms, Room settings, archiving |
| [Conversation View](spec/conversations/conversation-view.md) | What a person sees with a conversation open: where it opens, the New Message Indicator, marking read, search, pinned messages, links |
| [Messages](spec/messaging/messages.md) | Sending, the Message Composer, failures, editing, deleting, reactions, mentions, attachments, GIFs, drafts |
| [Formatting](spec/messaging/formatting.md) | Which Markdown Connect understands, and when it applies |
| [Notifications](spec/notifications/notifications.md) | What bolds, what badges, what notifies, notification levels, and acting on a notification |
| [Sorting and naming](spec/sorting/sorting-and-naming.md) | The order of every list and search, and how group conversations are named |
| [Keyboard](spec/keyboard/keyboard.md) | Keyboard shortcuts and moving around without a mouse |
| [People](spec/people/people.md) | Contact Cards, Presence, inactive people, the Corporate Directory |
| [Audiences](spec/audiences/conversation-members.md) | Member filters: which Rooms a person is in because of their territory, department or title |
| [Corporate events](spec/events/corporate-events.md) | The EVENTS section in Nitro Connect |
| [Appointment cards](spec/appointments/appointment-cards.md) | Appointment Hashtags and the Appointment Cards they show |
| [v2 to v3 bridge](spec/bridge/v2-to-v3.md) | What people do in v2 showing up in v3 |
| [v3 to v2 bridge](spec/bridge/v3-to-v2.md) | What people do in v3 showing up in v2 |
| [Sharing into Connect](spec/sharing/sharing-into-connect.md) | Sending photos, files and links to Connect from another app's share menu |
| [Voice assistants](spec/voice/voice-assistants.md) | Sending messages by voice, without opening Connect (Siri today) |
| [The Connect app](spec/app/connect-app.md) | Installing, updating, losing the connection, Help & Diagnostics, the Crash Screen |

Areas are named for what people do, not for a device. Something only iOS or only
the PWA does goes in the area for what it is, and its **Needs** says which clients
it is for.

## Terms you will see

**Needs** lists the **targets** of a rule: the parts of Connect that must follow it.
They come in two halves.

**Where people see it. You choose these.** These are the four
[clients](glossary/devices.md#clients). Behavior is written per client and no
client is assumed to match another; when they differ, there is one rule per
client.

| Target | Means |
|---|---|
| `browser` | Connect Browser: v3 in a web browser |
| `pwa` | Connect PWA: v3 installed from the browser; the Android app |
| `macos` | Connect for Mac |
| `ios` | Connect for iPhone and iPad |

Screen size isn't a target. A rule that depends on it says so in its text, with
the [screen terms](glossary/devices.md#platform-and-screen) ("On Small Screens,
…"). A rule for one tenant says so too ("In Nitro Connect, …").

**What makes it work. Engineering adds these, so leave them out.**

| Target | Means |
|---|---|
| `nitro` | v2, and Nitro itself (people, roles, permissions) |
| `nitroid` | Nitro ID, which passes people and groups from Nitro to v3 |
| `server` | v3's back end |
| `ccl` | The shared engine built into the Connect apps. It is part of the apps, never instead of them |

Targets are always written in this order: `nitro, nitroid, server, ccl, browser,
pwa, macos, ios`.

**Status** appears only when a rule is not settled:

| Status | Means |
|---|---|
| *(none)* | Agreed. This is how Connect should behave. |
| `Status: draft` | Still being decided, or not yet confirmed by Product. Nobody is held to it yet. |
| `Status: rejected` | No longer how Connect behaves, or covered by another rule. Kept for the record, never deleted. |

## How to add a rule

You do not need to know Git or Markdown. See [Contributing](docs/contributing.md)
for all three ways. To write one yourself in the browser:

1. Open the area from the [list above](#where-the-rules-are) and click the pencil
   icon (Edit).
2. Find the rules most like yours, copy one, and paste it after the last of them.
3. Give it the next number, in **both** places: the heading and the stamp under it.
   The stamp ends in `~1`.
4. Fill in the rule, the example, the rationale, and in `Needs` the clients it is for.
5. Click **Commit changes**, choose **Create a new branch and start a pull request**,
   and describe the change. Someone from engineering will review it and sort out the
   ID if needed.

If your rule does not fit any area, just say so in your pull request. Engineering
will find it a home.

## Changing a rule

Edit it the same way. Then ask yourself: **would an engineer who already tested the
old version need to look at it again?**

- **Yes, what should happen has changed.** Change the number at the end of the stamp
  from `~1` to `~2` (or `~2` to `~3`), and add a line under `Comment:` saying what
  changed and why. This tells every team their tests need to be checked against the
  new behavior.
- **No, it is just clearer wording.** Leave the number alone.
- **Only where it applies has changed.** Edit `Needs` and leave the number alone.

To confirm a draft, delete its `Status: draft` line. To stop a rule applying, set
`Status: rejected` and explain why in the rationale. Never delete a rule.

## Writing a good rule

- **One behavior per rule.** If you wrote "and also", it is probably two rules.
- **Something you could watch happen.** "Messages are reliable" is a goal. "A failed
  message stays visible with Retry" is a rule.
- **Say what happens, not how it is built.** Leave out code, systems, vendors,
  ticket numbers and dates. Exact on-screen wording, in quotes, is welcome.
- **Spell out the edge cases**, each as its own rule: limits, empty states, errors,
  being offline. These are where most bugs live.
- **Always say why.** It stops someone "cleaning up" a rule without knowing why it
  exists.

## More

- [Contributing](docs/contributing.md): who owns what, and three ways to propose a change.
- [Publishing](docs/publishing.md): what gets built, and how to point Claude at it.
- [Adoption plan](docs/adoption-plan.md): how we get from here to a full spec and a
  date for connect-web.
- [For engineers](docs/for-engineers.md): how rule IDs are built, areas and
  topics, the file format, the checks, and how tests point at rules.
