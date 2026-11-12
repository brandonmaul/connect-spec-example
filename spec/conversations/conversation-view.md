# Conversation View

The Conversation View is what a person sees with a conversation open: its message history, Date Separators, the New Message Indicator and New Message Button (jump), when it is marked read, who has read what, search, pinned messages, links and the Members List.

**Area code:** `VIEW`

**Topics**

| Topic | Covers |
|---|---|
| `SHOW` | What appears in the Conversation View |
| `OPEN` | Opening a conversation and moving through it |
| `DIVIDER` | The New Message Indicator and the New Message Button (jump) |
| `READ` | When an open conversation is marked read |
| `SEEN` | Who has read what |
| `SEARCH` | Searching a conversation |
| `PIN` | Pinned messages and the Pinned Message Drawer |
| `LINK` | Opening links and addresses |
| `MEMBERS` | The Member Count, Members List and members popover |

Design: [Components](https://huddle.powerapp.cloud/projects/507) · [Headers](https://huddle.powerapp.cloud/projects/518) · [Basic Search](https://huddle.powerapp.cloud/projects/492) · [Pinning and Saving](https://huddle.powerapp.cloud/projects/561) · [Handoff Repository](https://huddle.powerapp.cloud/projects/489) · [Attachments](https://huddle.powerapp.cloud/projects/570)

### VIEW-SHOW-001: Messages of every kind are shown
`req~VIEW-SHOW-001~1`

Text, photos, files, audio, video, GIFs, notices and "/me" actions are all shown in
the Conversation View. A kind Connect does not know is shown as its plain text, never
hidden.

    Given someone sends a kind of message Connect does not know
    When others look at the conversation
    Then they see its plain text in its place

Rationale:
A message that silently vanishes is a message someone thinks was read.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### VIEW-SHOW-002: Changes to a conversation appear in its history
`req~VIEW-SHOW-002~1`

When a conversation's settings change, a line saying so appears in the message
history, in order with the messages.

    Given a Room Admin changes a Room's settings
    When members look at the Conversation View
    Then a line describing the change appears among the messages at the point it happened

Rationale:
Changes to a conversation change how people use it, so everyone needs to see when they happened.

Needs: ccl, browser, pwa, macos, ios

### VIEW-SHOW-003: Making a Room private is noted
`req~VIEW-SHOW-003~1`

When a Room is made private, a line in the history says so.

    Given a Room Admin makes a Room private
    When members look at the Conversation View
    Then they see "This room has been set to private. Only invited members can read and post messages here."

Rationale:
Who can read a Room changes what people should say in it. Everyone needs to see when that changes.

Needs: ccl, browser, pwa, macos, ios

### VIEW-SHOW-004: Connect's own automatic accounts never appear
`req~VIEW-SHOW-004~1`

Accounts Connect uses to run itself never appear anywhere: not in messages,
reactions, members or search. Bots people talk to do appear, marked as bots.

    Given the account that keeps a Room's Member filters applied adds people to it
    Then nobody sees that account in the conversation
    But the Nitro App bot appears in its conversations, marked as a bot

Rationale:
Behind-the-scenes accounts are not people. Showing them confuses everyone.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### VIEW-SHOW-005: Messages in a row from one person are grouped
`req~VIEW-SHOW-005~1`

Messages sent one after another by the same person can be grouped, with their name
and picture shown once.

    Given Ana sends three messages in a row
    Then her name and picture show once, above all three

Rationale:
Repeating the same name on every line is noise.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### VIEW-SHOW-006: A message is never shown twice
`req~VIEW-SHOW-006~1`

A message appears exactly once in a conversation.

    Given a busy conversation
    When messages arrive while older ones are loading
    Then no message appears twice

Rationale:
A duplicate looks like someone sent it twice, and people answer it twice.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### VIEW-SHOW-007: Senders are always named
`req~VIEW-SHOW-007~1`

Every message shows its sender's name, including people who have since left.

    Given a person who left the company sent messages last year
    When someone scrolls back to them
    Then the messages show that person's name, not a code

Rationale:
A message from a code instead of a name is useless as a record.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### VIEW-SHOW-008: Making a Room public is noted
`req~VIEW-SHOW-008~1`

When a Room is made public, including when it is created public, a line in the
history says so, and who did it.

    Given a Room Admin makes a Room public
    When members look at the Conversation View
    Then a line from that Room Admin says "This room has been set to public. Anyone can view and join this room. Only members can post messages."

Rationale:
Who can read a Room changes what people should say in it. Everyone needs to see when that changes.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### VIEW-SHOW-009: Wording of setting changes in group conversations
`req~VIEW-SHOW-009~1`

In a group conversation, a line about a setting change uses the word that fits the
conversation.

    Given a group conversation is set to private
    When its members look at the Conversation View
    Then the line says "This room has been set to private. Only invited members can read and post messages here."

Rationale:
Open: a group conversation on macOS shows "This room has been set to private. Only invited members can read and post messages here." Should group conversations say "conversation" instead of "room"?

Status: draft

Needs: ccl, browser, pwa, macos, ios

### VIEW-SHOW-010: The Welcome Screen shows when no conversation is open
`req~VIEW-SHOW-010~1`

On Desktop, when no conversation is open, the Conversation View shows the Welcome
Screen, "Welcome to Connect".

    Given a person on Desktop has no conversation open
    When they look at the Conversation View
    Then they see "Welcome to Connect"

Rationale:
An empty pane looks broken; the Welcome Screen tells the person to pick a conversation.

Needs: browser, pwa, macos

### VIEW-SHOW-011: Date Separators divide the history by day
`req~VIEW-SHOW-011~1`

A Date Separator marks the start of each day's messages and stays stuck at the top
of the Conversation View while that day's messages scroll past.

    Given a conversation has messages from Monday and Tuesday
    When a person scrolls through Monday's messages
    Then Monday's Date Separator stays at the top of the Conversation View
    And Tuesday's Date Separator replaces it when Tuesday's messages reach the top

Rationale:
People need to know which day a message is from without checking every timestamp.

Needs: browser, pwa, macos, ios

### VIEW-SHOW-012: Date Separator labels
`req~VIEW-SHOW-012~1`

A Date Separator is written in capitals: "TODAY" for today, "YESTERDAY" for
yesterday, and otherwise the weekday, date and month.

    Given a conversation has messages from today, yesterday and last week
    When a person scrolls through it
    Then the Date Separators read "TODAY", "YESTERDAY", and the weekday, date and month for last week's day

Rationale:
Relative words are quickest to read for recent days; older days need the full date.

Needs: browser, pwa, macos, ios

### VIEW-OPEN-001: A conversation opens fresh every time
`req~VIEW-OPEN-001~1`

Every time a conversation is opened it shows its current state, never what it
looked like last time.

    Given a person closed a conversation on their phone
    And then read it on their laptop
    When they reopen it on their phone
    Then it opens where they are now, with no out-of-date New Message Indicator

Rationale:
Showing the last visit for a moment and then jumping makes people lose their place.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### VIEW-OPEN-002: New messages are there on returning to the latest
`req~VIEW-OPEN-002~1`

Messages that arrive while a person is reading older history are there as soon as
they go back to the latest messages.

    Given a person is reading last week's messages
    When new messages arrive and they jump to the latest
    Then the new messages are already there, with no reload

Rationale:
Going back to the latest should be instant.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### VIEW-OPEN-003: A way back to the latest messages
`req~VIEW-OPEN-003~1`

While reading older messages, a person always has a way to jump back to the latest
ones.

    Given a person has scrolled back a long way
    Then a "jump to latest" control is shown

Rationale:
Scrolling back down through weeks of history is not a reasonable way back.

Status: draft

Needs: browser, pwa, macos, ios

### VIEW-OPEN-004: Opening a hidden conversation brings it back
`req~VIEW-OPEN-004~1`

Opening a conversation the person has hidden, from anywhere, puts it back in their
Conversation List.

    Given a person hid a conversation
    When they open it from search
    Then it is back in their Conversation List

Rationale:
Opening a conversation means the person wants it again.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### VIEW-OPEN-005: A public Room you cannot read asks you to join
`req~VIEW-OPEN-005~1`

If a public Room cannot be read without joining, the person is asked to join
instead of being shown an empty conversation.

    Given a person opens a public Room they are not in
    And it cannot be read without joining
    Then they are asked whether to join

Rationale:
An empty screen looks like an empty conversation.

Status: draft

Needs: browser, pwa, macos, ios

### VIEW-DIVIDER-001: The New Message Indicator stays while you read
`req~VIEW-DIVIDER-001~1`

The New Message Indicator stays where it is while the person reads, even once they
reach the newest message. It goes once the conversation is marked read.

    Given a person opens a conversation with the New Message Indicator above 5 new messages
    When they scroll down to the newest
    Then the New Message Indicator is still above those 5

Rationale:
An indicator that vanishes as you reach it makes it hard to find your place again.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### VIEW-DIVIDER-002: Your own reply moves the New Message Indicator
`req~VIEW-DIVIDER-002~1`

If a person posted after the last message they read, the New Message Indicator
comes after their own latest message.

    Given Dana read up to message 5
    And then replied with message 6
    And Bob sent message 7
    Then the New Message Indicator is between 6 and 7

Rationale:
Posting is reading. Dana obviously saw what she was replying to.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### VIEW-DIVIDER-003: A message arriving at the bottom shows a shrinking indicator
`req~VIEW-DIVIDER-003~1`

When a message from someone else arrives while the person has the conversation open
at the bottom, the message appears live with the New Message Indicator above it,
and the indicator shrinks away over 3 seconds.

    Given a person has a conversation open, scrolled to the bottom
    When Bob sends a message
    Then Bob's message appears live with the New Message Indicator above it
    And the indicator shrinks away over 3 seconds

Rationale:
People glance away and back. The indicator shows them what just came in without staying in the way.

Needs: ccl, browser, pwa, macos, ios

### VIEW-DIVIDER-004: The New Message Indicator marks the first unread message
`req~VIEW-DIVIDER-004~1`

The New Message Indicator is a thin "↓ New" line directly above the first unread
message.

    Given a conversation has 4 unread messages
    When the person opens it
    Then a thin "↓ New" line sits directly above the first of the 4

Rationale:
People need to see exactly where they left off.

Needs: ccl, browser, pwa, macos, ios

### VIEW-DIVIDER-005: Opening an unread conversation scrolls to the indicator
`req~VIEW-DIVIDER-005~1`

Opening a conversation that has unread messages scrolls it to the New Message
Indicator.

    Given a conversation has unread messages and is not open
    When the person opens it
    Then the Conversation View is scrolled to the New Message Indicator

Rationale:
The first unread message is where the person needs to start reading.

Needs: ccl, browser, pwa, macos, ios

### VIEW-DIVIDER-006: New messages while scrolled up show the New Message Button (jump)
`req~VIEW-DIVIDER-006~1`

When a message from someone else arrives while the person is scrolled up in the
open conversation, the New Message Button (jump), a blue "↓ New Messages" pill,
appears.

    Given a person has a conversation open and is scrolled up reading older messages
    When Bob sends a message
    Then a blue "↓ New Messages" pill appears

Rationale:
The person can't see the new message, so they need to be told it arrived without losing their place.

Needs: browser, pwa, macos, ios

### VIEW-DIVIDER-007: The New Message Button (jump) scrolls to unread
`req~VIEW-DIVIDER-007~1`

Tapping the New Message Button (jump) scrolls the Conversation View to the unread
messages.

    Given the New Message Button (jump) is showing
    When the person taps it
    Then the Conversation View scrolls to the unread messages

Rationale:
One tap should take the person to what they haven't read.

Needs: browser, pwa, macos, ios

### VIEW-READ-001: A message read live is marked read after 3 seconds
`req~VIEW-READ-001~1`

When a message arrives while the person has the conversation open at the bottom,
the conversation is marked read after 3 seconds.

    Given a person has a conversation open, scrolled to the bottom, with the app in focus
    When Bob sends a message
    And 3 seconds pass with the person still at the bottom
    Then the conversation is marked read

Rationale:
A short delay means a message that flashed past isn't counted as read, while one the person stayed on is.

Needs: ccl, browser, pwa, macos, ios

### VIEW-READ-002: Scrolling away resets the 3-second timer
`req~VIEW-READ-002~1`

If the person scrolls away from the bottom before the 3 seconds pass, the timer
starts again.

    Given a message arrived while the person was at the bottom
    When they scroll away before 3 seconds pass
    Then the conversation is not marked read
    And the 3 seconds start again when they return to the bottom

Rationale:
A person who scrolled away hasn't read the new message.

Needs: ccl, browser, pwa, macos, ios

### VIEW-READ-003: Tapping the composer or messages marks read at once
`req~VIEW-READ-003~1`

Tapping the Message Composer or the message area marks the conversation read at
once.

    Given a conversation is open with a new message the 3-second timer hasn't finished on
    When the person taps the Message Composer
    Then the conversation is marked read at once

Rationale:
Interacting with the conversation shows the person is looking at it.

Needs: ccl, browser, pwa, macos, ios

### VIEW-READ-004: Sending a message marks read at once
`req~VIEW-READ-004~1`

Sending a message in a conversation marks it read at once.

    Given a conversation has an unread message
    When the person sends a message in it
    Then the conversation is marked read at once

Rationale:
Replying means the person has read the conversation.

Needs: ccl, browser, pwa, macos, ios

### VIEW-READ-005: Scrolled up, a conversation stays unread until the bottom
`req~VIEW-READ-005~1`

A message that arrives while the person is scrolled up keeps the conversation
unread until the person reaches the bottom.

    Given a person is scrolled up in an open conversation
    When Bob sends a message
    Then the conversation stays unread
    And it is marked read when the person reaches the bottom

Rationale:
The person hasn't seen the new message until they scroll down to it.

Needs: ccl, browser, pwa, macos, ios

### VIEW-READ-006: Opening an unread conversation marks read at the bottom
`req~VIEW-READ-006~1`

Opening an unread conversation does not mark it read on its own. It is marked read
when the person reaches the bottom.

    Given a conversation has 20 unread messages
    When the person opens it at the New Message Indicator
    Then it stays unread
    And it is marked read when the person reaches the bottom

Rationale:
Opening a conversation isn't reading it; reaching the newest message is.

Needs: ccl, browser, pwa, macos, ios

### VIEW-READ-007: Nothing is marked read while the app is not in focus
`req~VIEW-READ-007~1`

A message that arrives while Connect is not in focus keeps the conversation unread
until Connect is in focus again.

    Given a person has a conversation open but Connect is not in focus
    When Bob sends a message
    Then the conversation stays unread
    And it is not marked read until Connect is in focus

Rationale:
A person can't read a message in a window they aren't looking at.

Needs: ccl, browser, pwa, macos, ios

### VIEW-SEEN-001: Everyone can see how far each member has read
`req~VIEW-SEEN-001~1`

Each member's name is shown at the newest message they have read, including members
who never post.

    Given Sam has read up to Dana's latest message but never posts
    When Dana looks at the conversation
    Then Sam's name is shown at her latest message

Rationale:
Knowing a message was seen saves people chasing for a reply.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### VIEW-SEARCH-001: Search covers a conversation's whole history
`req~VIEW-SEARCH-001~1`

Searching a conversation searches all of its history, and each result shows who sent
it, its current text, when, and whether it was edited.

    Given a person searches "invoice" in a two-year-old conversation
    Then results from any point in those two years appear

Rationale:
The message people search for is usually an old one.

Status: draft

Needs: server, ccl, browser, pwa, macos, ios

### VIEW-SEARCH-002: Search results can be sorted newest or oldest first
`req~VIEW-SEARCH-002~1`

Search results can be sorted Newest first or Oldest first.

    Given a search has many results
    When the person sorts Oldest first
    Then the oldest matches come first

Rationale:
Sometimes you want the latest mention, sometimes where something started.

Needs: ccl, browser, pwa, macos, ios

### VIEW-SEARCH-003: A result opens with 10 messages either side
`req~VIEW-SEARCH-003~1`

Opening a search result shows it with the 10 messages before it and the 10 messages
after it.

    Given a search result
    When the person opens it
    Then they see the result with the 10 messages before and the 10 messages after it

Rationale:
A single message rarely makes sense on its own.

Needs: ccl, browser, pwa, macos, ios

### VIEW-SEARCH-004: Search from the Conversation Header searches the open conversation
`req~VIEW-SEARCH-004~1`

The magnifying glass in the Conversation Header searches the open conversation.

    Given a person has a conversation open
    When they tap the magnifying glass in the Conversation Header and search "invoice"
    Then the results are messages from that conversation only

Rationale:
People usually remember which conversation something was said in.

Needs: server, ccl, browser, pwa, macos, ios

### VIEW-SEARCH-005: Search shows up to 25 results
`req~VIEW-SEARCH-005~1`

A search in a conversation shows at most 25 results.

    Given a conversation has 40 messages that match "invoice"
    When the person searches "invoice"
    Then 25 results are shown

Rationale:
A short list stays quick to scan; a person who needs more can search more precisely.

Needs: server, ccl, browser, pwa, macos, ios

### VIEW-PIN-001: Only Room Admins pin messages
`req~VIEW-PIN-001~1`

Only a Room Admin can pin messages, and only in Rooms. Messages cannot be pinned in
People Conversations.

    Given a member who is not a Room Admin
    When they look for Pin on a message
    Then it is not offered
    And in a People Conversation nobody is offered Pin

Rationale:
Pinned messages speak for the Room, so they are kept to the people responsible for it.

Needs: server, macos, ios

### VIEW-PIN-002: New pins are flagged until seen
`req~VIEW-PIN-002~1`

When a message is pinned, the pins are flagged as new for everyone until they open
the Pinned Message Drawer, except for the person who pinned it.

    Given a Room Admin pins a message
    Then other members see a "new pin" mark
    And the Room Admin who pinned it does not

Rationale:
A pin is meant to be seen. The person who pinned it already has.

Status: draft

Needs: ccl, macos, ios

### VIEW-PIN-003: Pinned messages are newest pin first
`req~VIEW-PIN-003~1`

The Pinned Message Drawer lists the most recently pinned message first.

    Given message A was pinned last week and B today
    When a person opens the Pinned Message Drawer
    Then B comes first

Rationale:
The newest pin is usually the most relevant one.

Needs: ccl, macos, ios

### VIEW-PIN-004: Pinned messages can be reacted to
`req~VIEW-PIN-004~1`

A person can react to a pinned message from the Pinned Message Drawer, even if it is
far back in the conversation.

    Given a message pinned months ago
    When a person reacts 👍 to it in the Pinned Message Drawer
    Then the 👍 is added to that message

Rationale:
Pins are often announcements. Reacting is how people say they have seen them.

Status: draft

Needs: ccl, macos, ios

### VIEW-PIN-005: A pin lasts until unpinned, deleted or 6 months old
`req~VIEW-PIN-005~1`

A pinned message stays pinned until it is unpinned, the message is deleted, or the
pin is 6 months old.

    Given a Room Admin pinned a message 6 months ago and nobody unpinned it
    When a person opens the Pinned Message Drawer
    Then that message is no longer listed

Rationale:
Pins are for what matters now; old pins drop off on their own so the drawer stays relevant.

Needs: server, macos, ios

### VIEW-PIN-006: There is no limit on pins
`req~VIEW-PIN-006~1`

A Room can have any number of pinned messages.

    Given a Room already has 30 pinned messages
    When a Room Admin pins another
    Then it is pinned and listed in the Pinned Message Drawer

Rationale:
Room Admins decide what is worth pinning; a cap would force them to drop something still relevant.

Needs: server, macos, ios

### VIEW-PIN-007: The pin in the Conversation Header opens the Pinned Message Drawer
`req~VIEW-PIN-007~1`

The pin (thumbtack) in a Room's Conversation Header opens the Pinned Message Drawer.

    Given a person has a Room open
    When they tap the thumbtack in the Conversation Header
    Then the Pinned Message Drawer opens

Rationale:
Pinned messages need one predictable place to be found from.

Needs: macos, ios

### VIEW-LINK-001: Links open without leaving Connect
`req~VIEW-LINK-001~1`

Links in Connect open in a new browser tab, so Connect stays open.

    Given a person is using Connect in a browser
    When they click a link in a message
    Then the link opens in a new tab
    And Connect stays where it was

Rationale:
Following a link should never cost the person their place in the conversation.

Status: draft

Needs: browser, pwa

### VIEW-LINK-002: Links without https still work
`req~VIEW-LINK-002~1`

A link written without "https://", like "powerhrg.com", still opens.

    Given a message says "see powerhrg.com"
    When a person clicks the link
    Then powerhrg.com opens

Rationale:
People type addresses the short way.

Status: draft

Needs: browser, pwa

### VIEW-LINK-003: Addresses open in the device's maps app
`req~VIEW-LINK-003~1`

Tapping an address opens Apple Maps on Apple devices and Google Maps everywhere else.

    Given an Appointment Card shows a homeowner's address
    When a person on an iPhone taps it
    Then it opens in Apple Maps
    But on Android, in Google Maps

Rationale:
Each person's maps app is the one they use for directions.

Status: draft

Needs: browser, pwa

### VIEW-LINK-004: Bare URLs become links
`req~VIEW-LINK-004~1`

A web address typed into a message on its own becomes a link.

    Given a person sends "Agenda is at https://example.com/agenda"
    When others look at the message
    Then "https://example.com/agenda" is a link they can open

Rationale:
People paste addresses as they are and expect to be able to open them.

Needs: browser, pwa, macos, ios

### VIEW-LINK-005: Links to YouTube, Stack Overflow and Figma show a preview
`req~VIEW-LINK-005~1`

A link to YouTube, Stack Overflow or Figma shows a link preview under the message.

    Given a person sends a link to a YouTube video
    When others look at the message
    Then a preview of the video's page shows under it

Rationale:
A preview lets people tell what a link is before they open it.

Needs: macos, ios

### VIEW-MEMBERS-001: The Member Count opens the Members List
`req~VIEW-MEMBERS-001~1`

The Conversation Header shows the conversation's Member Count, and tapping it opens
the Members List.

    Given a Room has 42 members
    When a person taps the Member Count in its Conversation Header
    Then the Members List opens

Rationale:
People need to see who will read what they post.

Needs: browser, pwa, macos, ios

### VIEW-MEMBERS-002: On Mobile the Member Count reads "N Members"
`req~VIEW-MEMBERS-002~1`

On Mobile, the Member Count in the Conversation Header reads "N Members".

    Given a person on Mobile opens a Room with 42 members
    Then the Conversation Header shows "42 Members"

Rationale:
On a small screen a bare number needs its label to be understood.

Needs: browser, pwa, ios

### VIEW-MEMBERS-003: A group conversation's header opens a members popover
`req~VIEW-MEMBERS-003~1`

On macOS, clicking a group conversation's Conversation Header opens a "Members (N)"
popover that lists every member, including you, A–Z.

    Given a person is in a group conversation with Kelly and Rex
    When they click the Conversation Header
    Then a "Members (3)" popover opens
    And it lists Kelly, Rex and the person themselves, A–Z

Rationale:
The header name never includes you, so the popover gives the full list of who is in the conversation.

Needs: macos
