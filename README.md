# Connect Product Spec

> **Example repo.** The rules here show the format. They are not yet the agreed
> behavior of Connect, and the Figma and Runway links are placeholders.

This is where we write down **how Connect is supposed to behave**, one rule at a
time, in plain language. Product owns what the rules say. Engineering proves each
rule with automated tests in the app's own code.

## Why this exists

Today, how Connect should behave lives in Runway tickets, Connect threads, Huddle,
Figma and people's memories. That causes three problems this repo fixes:

- **Not everyone can say what "correct" is.** Here, every behavior has one written rule
  and a reason.
- **Behavior quietly breaks.** Once a rule here has a test behind it, it cannot
  change without someone noticing.
- **We cannot say when a project is done.** If connect-web has to follow 300 rules
  and 180 are proven, we know exactly what is left, and can put a date on it.

Because it is kept in GitHub, every change is reviewed and the full history of what
a rule used to say, and why it changed, is kept forever.

## Reading a rule

Every rule looks the same:

> ### MSG-SEND-002: Failed sends can be retried
> `req~MSG-SEND-002~1`
>
> A message that cannot be sent stays visible as failed, with Retry and Delete.
>
>     Given a user sends a message while the server is unreachable
>     When the send fails
>     Then the message stays in the timeline marked as failed
>     And it offers "Retry" and "Delete"
>
> Rationale:
> A failed message must be visible and recoverable, or the user believes it was delivered.
>
> Needs: ios, macos, web

| What you see | What it means |
|---|---|
| **MSG-SEND-002** | The rule's ID (see [rule IDs](#rule-ids)). It never changes, so tickets, threads and tests can refer to it. |
| **Failed sends can be retried** | A short title. |
| `req~MSG-SEND-002~1` | The ID stamp the checking tool reads. You can ignore it, except the number at the end (see [changing a rule](#changing-a-rule)). |
| The first sentence | The rule itself. |
| Given / When / Then | One worked example: the starting situation, what happens, and what the person should see. |
| **Rationale** | Why it works this way. |
| **Needs** | Which parts of Connect must follow this rule (see [words you will see](#words-you-will-see)). |

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

Three things never change, so links to a rule keep working:

- **An ID is never reused.** A retired rule keeps its number, and the next new rule
  takes the next number up.
- **An ID is never renamed.** If a rule turns out to belong in another topic, it
  keeps its old ID.
- **A number is never filled in.** If `003` is retired, the next rule is still `004`.

## Where the rules are

Each area is one file. Open it to see its topics and rules.

| Area | Code | Topics | What it covers |
|---|---|---|---|
| [Membership](spec/membership/connect-access.md) | `MEMBERSHIP` | `SOURCE` `ACCESS` `PROFILE` `LEAVE` `RETURN` | Who has Connect V2 and V3, and what happens when people join, change, leave and come back |
| [Account](spec/account/account.md) | `ACCOUNT` | `SIGNIN` `SESSION` `SIGNOUT` `DEVICE` `PRIVACY` | Signing in and out, staying signed in, and using several devices |
| [Settings](spec/settings/settings.md) | `SETTING` | `SORT` `DENSITY` `SYNC` | A person's own preferences, and how they follow them between devices |
| [Conversations](spec/conversations/conversations.md) | `CONV` | `LIST` `NAME` `SECTION` `ORDER` `HIDE` `JOIN` `LEAVE` `BROWSE` `PREVIEW` `EDIT` `ADD` `MENTION` `ARCHIVE` `DELETE` | The conversation list, names, sections, ordering, hiding, joining and leaving, finding and previewing, changing details, adding people, archiving |
| [Inside a conversation](spec/conversations/conversation-view.md) | `VIEW` | `SHOW` `OPEN` `DIVIDER` `SEEN` `SEARCH` `PIN` | What a person sees with a conversation open, where it opens, who has read what, search and pinned messages |
| [Direct and Group conversations](spec/conversations/direct-and-group.md) | `DM` | `START` `SIZE` `SELF` | Conversations between specific people, and each person's Self-DM Room |
| [Messages](spec/messaging/messages.md) | `MSG` | `SEND` `FAIL` `EDIT` `DELETE` `REACT` `MENTION` `ATTACH` `DRAFT` `READ` `RETAIN` | Sending, failures, editing, deleting, reactions, mentions, attachments, drafts, unread and read state, how long messages are kept |
| [Notifications](spec/notifications/notifications.md) | `NOTIFY` | `LEVEL` `TEXT` `TAP` `REPLY` `DEVICE` | What notifies a person, and acting on a notification |
| [People](spec/people/people.md) | `PEOPLE` | `DIRECTORY` `PROFILE` `STATUS` `MEMBERS` `ADMIN` | The company directory, profiles, online status, conversation members and admins |
| [Audiences](spec/audiences/conversation-members.md) | `AUD` | `RULE` `MEMBER` `EDIT` `REACH` `REMOVE` | Which conversations a person is in, when the conversation has an audience like "all Foremen in Philly", and how audiences are built |
| [Corporate events](spec/events/corporate-events.md) | `EVENT` | `SHOW` `ORDER` `TAP` `REFRESH` | Power's event banners and links above the conversation list |
| [Appointment cards](spec/appointments/appointment-cards.md) | `APPT` | `TAG` `CARD` `ACCESS` | Power's appointment details shown under messages that mention an appointment |
| [V2 to V3 bridge](spec/bridge/v2-to-v3.md) | `V2V3` | `MSG` `REACT` `READ` `DM` `PUBLIC` `AUD` `MENTION` `ARCHIVE` | What people do in Connect V2 showing up in V3 |
| [V3 to V2 bridge](spec/bridge/v3-to-v2.md) | `V3V2` | `MSG` `REACT` `READ` `ARCHIVE` | What people do in Connect V3 showing up in V2 |
| [Voice assistants](spec/voice/voice-assistants.md) | `VOICE` | `SEND` | Sending messages by voice, without opening Connect (Siri today) |

The same topic word can appear in several areas when it means the same thing. For
example, `ARCHIVE` is about archiving in Conversations and in both bridges.

### Behavior on only some devices

Areas are named for **what a person can do**, never for a device or platform. There
is no "Apple" or "web" area. Which devices a rule applies to is said by its
[`Needs`](#words-you-will-see):

| Behavior | Area it belongs in | Needs |
|---|---|---|
| Sending a message with Siri | Voice assistants | `ios` |
| Sharing a photo into Connect from another app | Sharing into Connect (a new area) | `ios, macos, web` |
| Installing Connect on the home screen from the browser | Installing Connect (a new area) | `web` |
| Reopening the conversation you had open when the browser tab closed | Inside a conversation | `web` |

This keeps a behavior in one place when it spreads to more devices. If Android
sharing arrives, the sharing rules stay where they are and gain one more word in
`Needs`. If a behavior needs different wording on different devices, write one rule
per device in the same area, each with its own `Needs`.

## Words you will see

**Needs** lists who must follow the rule:

| Word | Means |
|---|---|
| `ios` | Connect on iPhone and iPad |
| `macos` | Connect on Mac |
| `web` | Connect in the browser, and on Android |
| `ccl` | The shared engine inside every Connect app (the Connect client library). A rule here is built and tested once, and every app gets it. |
| `server` | Connect V3's back end |
| `nitro` | Connect V2, and Nitro itself (people, roles, permissions) |
| `nitroid` | Nitro ID, which passes people and groups from Nitro to Connect V3 |

So a rule that only makes sense on iPhone says `Needs: ios`. A rule every app shares
says `Needs: ios, macos, web`.

Every part a rule passes through is listed, not only where it starts and ends.
Each part tests only its own step, so a part left off the list could break without
any test noticing.

Other names you will see in rules:

| Name | Means |
|---|---|
| Nitro | Power's company system. People, roles, titles and territories live here. |
| Nitro ID | Power's company login. It also passes people and groups from Nitro to Connect. |
| Tempo ID | Stream Financial's company login and directory. It does the same job as Nitro ID. |

**Status** appears only when a rule is not settled:

| Status | Means |
|---|---|
| *(none)* | Agreed. This is how Connect should behave. |
| `Status: draft` | Still being decided. Nobody is held to it yet. |
| `Status: rejected` | No longer how Connect behaves. Kept for the record, never deleted. |

## How to add a rule

You do not need to know Git or markdown.

**Option 1: describe it, and an engineer writes it up.** Open the
[Issues](../../issues/new/choose) tab and pick **Propose a rule**. Fill in what
should happen, an example, and why. An engineer turns it into a rule and asks you
to approve it.

**Option 2: write it yourself in the browser.**
1. Open the area's file from the [table above](#where-the-rules-are) and click the
   pencil icon (Edit).
2. Pick the topic it belongs to from the list at the top of the file. If none fits,
   [add a topic](#adding-a-topic) first.
3. Copy an existing rule from that file and paste it at the end of the file.
4. Give it the next number in that topic, in **both** places: the heading and the
   stamp under it. The stamp ends in `~1`.
5. Fill in the rule, the example, the rationale and who it is for.
6. Click **Commit changes**, choose **Create a new branch and start a pull request**,
   and describe the change. Someone from engineering will review the format.

## Adding a topic

Add a topic when a new rule is about a theme that none of the area's topics cover.

1. Check the topics at the top of the area's file. A new rule that fits an existing
   topic goes there, even if the topic is small.
2. Look across the [other areas](#where-the-rules-are). If one already uses a word
   for the same idea, use the same word, so `ARCHIVE` always means archiving.
3. Choose one short word in capital letters, with no digits or dashes. Name the
   behavior, not a screen or feature name that might change: `READ`, not `BADGE`.
4. Add the topic, with a one-line description, to the topics list at the top of the
   area's file, and to the area's row in the [table above](#where-the-rules-are).
5. Its first rule is number `001`, for example `MSG-PIN-001`.

## Adding an area

Add an area for a part of Connect that has rules of its own and fits no existing
area. If it could be a topic in an existing area, make it a topic instead: fewer
areas are easier to find your way around.

1. Choose the area's code: short capital letters, digits allowed (`CONV`,
   `VOICE`, `V2V3`). It must not be used by any other area, now or in the past.
   Name the part of the product, not a team, project, release or device, because
   the code lasts as long as the rules do (see
   [behavior on only some devices](#behavior-on-only-some-devices)).
2. Copy [templates/new-area.md](templates/new-area.md) into `spec/`, in the folder for
   that part of Connect, or a new folder if none fits.
3. Fill in the area's name, what it covers and its first topics. Replace `AREA` and
   `TOPIC` in the example rule.
4. Add a row for it to the [table above](#where-the-rules-are).
5. Open a pull request the same way as for a rule.

## Changing a rule

Edit it the same way. Then ask yourself: **would an engineer who already tested the
old version need to look at it again?**

- **Yes, what should happen has changed.** Change the number at the end of the stamp
  from `~1` to `~2` (or `~2` to `~3`), and add a line under `Comment:` saying what
  changed and why. This is the signal that tells every team their tests need to be
  checked against the new behavior.
- **No, it is just clearer wording.** Leave the number alone.
- **Only who it is for has changed.** Edit `Needs` and leave the number alone.

To stop a rule applying, set `Status: rejected` and explain why in the rationale.
Never delete a rule.

## Writing a good rule

- **One behavior per rule.** If you wrote "and also", it is probably two rules.
- **Something you could watch happen.** "Messages are reliable" is a goal. "A failed
  message stays visible with Retry" is a rule.
- **Say what happens, not how it is built.** Leave out screens, code and systems.
- **Spell out the edge cases**, each as its own rule: limits, empty states, errors,
  being offline. These are where most bugs live.
- **Always say why.** It stops someone "cleaning up" a rule without knowing why it
  exists.

## More

- [Adoption plan](docs/adoption-plan.md): how we get from here to a full spec and a
  date for connect-web.
- [For engineers](docs/for-engineers.md): the file format rules and how tests point
  at rules.
