# Inside a conversation

What a person sees with a conversation open: the messages, where it opens, the "new messages" divider, who has read what, search and pinned messages.

**Area code:** `VIEW`

**Topics**

| Topic | Covers |
|---|---|
| `SHOW` | What appears among the messages |
| `OPEN` | Opening a conversation and moving through it |
| `DIVIDER` | The "new messages" divider |
| `SEEN` | Who has read what |
| `SEARCH` | Searching a conversation |
| `PIN` | Pinned messages |
| `LINK` | Opening links and addresses |

Design: <figma link> · Runway: <epic link>

### VIEW-SHOW-001: Messages of every kind are shown
`req~VIEW-SHOW-001~1`

Text, photos, files, audio, video, GIFs, notices and "/me" actions are all shown.
A kind Connect does not know is shown as its plain text, never hidden.

    Given someone sends a kind of message Connect does not know
    When others look at the conversation
    Then they see its plain text in its place

Rationale:
A message that silently vanishes is a message someone thinks was read.

Needs: ccl, ios, macos, web

### VIEW-SHOW-002: Joins, leaves and setting changes are not shown
`req~VIEW-SHOW-002~1`

People joining or leaving, and changes to settings, are not shown among the
messages.

    Given 40 people were added to a conversation by its audience
    When someone looks at the conversation
    Then they see no "joined" lines, only messages

Rationale:
In conversations with audiences, people come and go constantly. Showing it would drown the messages.

Needs: ccl

### VIEW-SHOW-003: Making a Room public or private is noted
`req~VIEW-SHOW-003~1`

When a Room is made public or private, including when it is created, a line among
the messages says so, and who did it. Only Rooms show this, since only Rooms can be
public.

    Given an admin makes a Room private
    Then a line from that admin says "This room has been set to private. Only invited members can read and post messages here."
    And making a Room public says "This room has been set to public. Anyone can view and join this room. Only members can post messages."

Rationale:
Who can read a Room changes what people should say in it. Everyone needs to see when that changes.

Needs: ccl

### VIEW-SHOW-004: Connect's own automatic accounts never appear
`req~VIEW-SHOW-004~1`

Accounts Connect uses to run itself never appear anywhere: not in messages,
reactions, members or search. Bots people talk to do appear, marked as bots.

    Given the account that manages audiences adds people to a conversation
    Then nobody sees it in the conversation
    But the Nitro App bot appears in its conversations, marked as a bot

Rationale:
Behind-the-scenes accounts are not people. Showing them confuses everyone.

Needs: ccl

### VIEW-SHOW-005: Messages in a row from one person are grouped
`req~VIEW-SHOW-005~1`

Messages sent one after another by the same person can be grouped, with their name
and picture shown once.

    Given Ana sends three messages in a row
    Then her name and picture show once, above all three

Rationale:
Repeating the same name on every line is noise.

Needs: ccl, ios, macos, web

### VIEW-SHOW-006: A message is never shown twice
`req~VIEW-SHOW-006~1`

A message appears exactly once in a conversation.

    Given a busy conversation
    When messages arrive while older ones are loading
    Then no message appears twice

Rationale:
A duplicate looks like someone sent it twice, and people answer it twice.

Needs: ccl

### VIEW-SHOW-007: Senders are always named
`req~VIEW-SHOW-007~1`

Every message shows its sender's name, including people who have since left.

    Given a person who left the company sent messages last year
    When someone scrolls back to them
    Then the messages show that person's name, not a code

Rationale:
A message from a code instead of a name is useless as a record.

Needs: ccl

### VIEW-OPEN-001: A conversation opens fresh every time
`req~VIEW-OPEN-001~1`

Every time a conversation is opened it shows its current state, never what it
looked like last time.

    Given a person closed a conversation on their phone
    And then read it on their laptop
    When they reopen it on their phone
    Then it opens where they are now, with no out-of-date "new messages" divider

Rationale:
Showing the last visit for a moment and then jumping makes people lose their place.

Needs: ccl

### VIEW-OPEN-002: New messages are there on returning to the latest
`req~VIEW-OPEN-002~1`

Messages that arrive while a person is reading older history are there as soon as
they go back to the latest messages.

    Given a person is reading last week's messages
    When new messages arrive and they jump to the latest
    Then the new messages are already there, with no reload

Rationale:
Going back to the latest should be instant.

Needs: ccl

### VIEW-OPEN-003: A way back to the latest messages
`req~VIEW-OPEN-003~1`

While reading older messages, a person always has a way to jump back to the latest
ones.

    Given a person has scrolled back a long way
    Then a "jump to latest" control is shown

Rationale:
Scrolling back down through weeks of history is not a reasonable way back.

Needs: ios, macos, web

### VIEW-OPEN-004: Opening a hidden conversation brings it back
`req~VIEW-OPEN-004~1`

Opening a conversation the person has hidden, from anywhere, puts it back in their
conversation list.

    Given a person hid a conversation
    When they open it from search
    Then it is back in their conversation list

Rationale:
Opening a conversation means the person wants it again.

Needs: ccl

### VIEW-OPEN-005: A public Room you cannot read asks you to join
`req~VIEW-OPEN-005~1`

If a public Room cannot be read without joining, the person is asked to join
instead of being shown an empty conversation.

    Given a person opens a public Room they are not in
    And it cannot be read without joining
    Then they are asked whether to join

Rationale:
An empty screen looks like an empty conversation.

Needs: ios, macos, web

### VIEW-DIVIDER-001: The divider stays while you read
`req~VIEW-DIVIDER-001~1`

The "new messages" divider stays where it is while the person reads, even once
they reach the newest message. It goes once the conversation is marked read.

    Given a person opens a conversation with a divider above 5 new messages
    When they scroll down to the newest
    Then the divider is still above those 5

Rationale:
A divider that vanishes as you reach it makes it hard to find your place again.

Needs: ccl

### VIEW-DIVIDER-002: Your own reply moves the divider
`req~VIEW-DIVIDER-002~1`

If a person posted after the last message they read, the divider comes after their
own latest message.

    Given Dana read up to message 5
    And then replied with message 6
    And Bob sent message 7
    Then the divider is between 6 and 7

Rationale:
Posting is reading. Dana obviously saw what she was replying to.

Needs: ccl

### VIEW-DIVIDER-003: A divider marks messages that arrive while you watch
`req~VIEW-DIVIDER-003~1`

When a new message arrives in a conversation the person has open and has read, a
divider marks where the new messages start.

    Given a person has a read conversation open
    When Bob sends a message
    Then a divider appears above it

Rationale:
People glance away and back. The divider shows them what came in.

Needs: ccl

### VIEW-SEEN-001: Everyone can see how far each member has read
`req~VIEW-SEEN-001~1`

Each member's name is shown at the newest message they have read, including members
who never post.

    Given Sam has read up to Dana's latest message but never posts
    When Dana looks at the conversation
    Then Sam's name is shown at her latest message

Rationale:
Knowing a message was seen saves people chasing for a reply.

Needs: ccl, ios, macos, web

### VIEW-SEARCH-001: Search covers a conversation's whole history
`req~VIEW-SEARCH-001~1`

Searching a conversation searches all of its history, and each result shows who sent
it, its current text, when, and whether it was edited.

    Given a person searches "invoice" in a two-year-old conversation
    Then results from any point in those two years appear

Rationale:
The message people search for is usually an old one.

Needs: ccl, server

### VIEW-SEARCH-002: Search results can be sorted newest or oldest first
`req~VIEW-SEARCH-002~1`

Search results can be sorted newest first or oldest first.

    Given a search has many results
    When the person sorts oldest first
    Then the oldest matches come first

Rationale:
Sometimes you want the latest mention, sometimes where something started.

Needs: ccl, ios, macos, web

### VIEW-SEARCH-003: A result can be seen in context
`req~VIEW-SEARCH-003~1`

A person can open a search result to read the messages around it.

    Given a search result
    When the person opens it in context
    Then they see the messages before and after it

Rationale:
A single message rarely makes sense on its own.

Needs: ccl, ios, macos, web

### VIEW-PIN-001: Only admins pin messages
`req~VIEW-PIN-001~1`

Only a Room's admins can pin messages. Messages cannot be pinned in Direct or Group
conversations.

    Given a member who is not an admin
    When they look for Pin on a message
    Then it is not offered

Rationale:
Pinned messages speak for the conversation, so they are kept to the people responsible for it.

Needs: server, ios, macos, web

### VIEW-PIN-002: New pins are flagged until seen
`req~VIEW-PIN-002~1`

When a message is pinned, the pins are flagged as new for everyone until they open
the pinned messages, except for the person who pinned it.

    Given an admin pins a message
    Then other members see a "new pin" mark
    And the admin who pinned it does not

Rationale:
A pin is meant to be seen. The person who pinned it already has.

Needs: ccl

### VIEW-PIN-003: Pinned messages are newest pin first
`req~VIEW-PIN-003~1`

Pinned messages are listed with the most recently pinned first.

    Given message A was pinned last week and B today
    When a person opens the pinned messages
    Then B comes first

Rationale:
The newest pin is usually the most relevant one.

Needs: ccl

### VIEW-PIN-004: Pinned messages can be reacted to
`req~VIEW-PIN-004~1`

A person can react to a pinned message from the pinned messages, even if it is far
back in the conversation.

    Given a message pinned months ago
    When a person reacts 👍 to it in the pinned messages
    Then the 👍 is added to that message

Rationale:
Pins are often announcements. Reacting is how people say they have seen them.

Needs: ccl

### VIEW-LINK-001: Links open without leaving Connect
`req~VIEW-LINK-001~1`

Links in Connect open in a new browser tab, so Connect stays open.

    Given a person is using Connect in a browser
    When they click a link in a message
    Then the link opens in a new tab
    And Connect stays where it was

Rationale:
Following a link should never cost the person their place in the conversation.

Needs: web

### VIEW-LINK-002: Links without https still work
`req~VIEW-LINK-002~1`

A link written without "https://", like "powerhrg.com", still opens.

    Given a message says "see powerhrg.com"
    When a person clicks the link
    Then powerhrg.com opens

Rationale:
People type addresses the short way.

Needs: web

### VIEW-LINK-003: Addresses open in the device's maps app
`req~VIEW-LINK-003~1`

Tapping an address opens Apple Maps on Apple devices and Google Maps everywhere else.

    Given an appointment card shows a homeowner's address
    When a person on an iPhone taps it
    Then it opens in Apple Maps
    But on Android, in Google Maps

Rationale:
Each person's maps app is the one they use for directions.

Needs: web
