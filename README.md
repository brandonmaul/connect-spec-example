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
| **MSG-SEND-002** | The rule's ID. It never changes, so tickets, threads and tests can point to it. `MSG-SEND-002` reads as "Messages, sending, rule 2". |
| **Failed sends can be retried** | A short title. |
| `req~MSG-SEND-002~1` | A stamp for the checking tool. You can ignore it, except the number at the end (see [changing a rule](#changing-a-rule)). |
| The first sentence | The rule itself. |
| Given / When / Then | One worked example: the starting situation, what happens, and what the person should see. |
| **Rationale** | Why it works this way. |
| **Needs** | Which parts of Connect must follow this rule (see [words you will see](#words-you-will-see)). |

## Where the rules are

Each area is one page. Open it to see its rules.

| Area | What it covers |
|---|---|
| [Membership](spec/membership/connect-access.md) | Who has Connect V2 and V3, and what happens when people join, change, leave and come back |
| [Account](spec/account/account.md) | Signing in and out, staying signed in, and using several devices |
| [Settings](spec/settings/settings.md) | A person's own preferences, and how they follow them between devices |
| [Conversations](spec/conversations/conversations.md) | The conversation list, names, sections, ordering, hiding, joining and leaving, finding and previewing, changing details, adding people, archiving |
| [Inside a conversation](spec/conversations/conversation-view.md) | What a person sees with a conversation open, where it opens, who has read what, search, pinned messages and opening links |
| [Direct and Group conversations](spec/conversations/direct-and-group.md) | Conversations between specific people, and each person's Self-DM Room |
| [Messages](spec/messaging/messages.md) | Sending, typing and pasting, failures, editing, deleting, reactions, mentions, attachments, drafts, unread and read state, how long messages are kept |
| [Notifications](spec/notifications/notifications.md) | What notifies a person, and acting on a notification |
| [People](spec/people/people.md) | The company directory, profiles, online status, conversation members and admins |
| [Audiences](spec/audiences/conversation-members.md) | Which Rooms a person is in when the Room has an audience like "all Foremen in Philly", and how audiences are built |
| [Corporate events](spec/events/corporate-events.md) | Power's event banners and links above the conversation list |
| [Appointment cards](spec/appointments/appointment-cards.md) | Power's appointment details shown under messages that mention an appointment |
| [V2 to V3 bridge](spec/bridge/v2-to-v3.md) | What people do in Connect V2 showing up in V3 |
| [V3 to V2 bridge](spec/bridge/v3-to-v2.md) | What people do in Connect V3 showing up in V2 |
| [Sharing into Connect](spec/sharing/sharing-into-connect.md) | Sending photos, files and links to Connect from another app's share menu |
| [Voice assistants](spec/voice/voice-assistants.md) | Sending messages by voice, without opening Connect (Siri today) |
| [The Connect app](spec/app/connect-app.md) | Installing Connect from the web, its icon and shortcuts, updates, losing the connection, fitting the screen |

Areas are named for what people do, not for a device. Something only the iPhone or
only the web does goes in the area for what it is, and its **Needs** says which
devices it is for.

## Words you will see

**Needs** lists which parts of Connect must follow the rule:

| Word | Means |
|---|---|
| `ios` | Connect on iPhone and iPad |
| `macos` | Connect on Mac |
| `web` | Connect in the browser, and on Android |
| `ccl` | The shared engine inside every Connect app. A rule here is built and tested once, and every app gets it. |
| `server` | Connect V3's back end |
| `nitro` | Connect V2, and Nitro itself (people, roles, permissions) |
| `nitroid` | Nitro ID, which passes people and groups from Nitro to Connect V3 |

So a rule that only makes sense on iPhone says `Needs: ios`. A rule every app shares
says `Needs: ios, macos, web`.

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
1. Open the area from the [list above](#where-the-rules-are) and click the pencil
   icon (Edit).
2. Find the rules most like yours, copy one, and paste it after the last of them.
3. Give it the next number, in **both** places: the heading and the stamp under it.
   The stamp ends in `~1`.
4. Fill in the rule, the example, the rationale and who it is for.
5. Click **Commit changes**, choose **Create a new branch and start a pull request**,
   and describe the change. Someone from engineering will review it and sort out the
   ID if needed.

If your rule does not fit any area, use Option 1, or just say so in your pull
request. Engineering will find it a home.

## Changing a rule

Edit it the same way. Then ask yourself: **would an engineer who already tested the
old version need to look at it again?**

- **Yes, what should happen has changed.** Change the number at the end of the stamp
  from `~1` to `~2` (or `~2` to `~3`), and add a line under `Comment:` saying what
  changed and why. This tells every team their tests need to be checked against the
  new behavior.
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
- [For engineers](docs/for-engineers.md): how rule IDs are built, how areas and
  topics are organised, adding new ones, the file format, and how tests point at
  rules.
