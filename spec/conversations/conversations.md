# Conversations

Every conversation a person is in: how they are listed, how people are added by hand
or by being mentioned, and what happens to a conversation at the end of its life.
Who is in a Room because of its audience is covered in
[Audiences](../audiences/conversation-members.md), and Direct and Group
conversations in [Direct and Group conversations](direct-and-group.md).

There are four types of conversation:

| Type | What it is |
|---|---|
| Room | A conversation with a name, for a team, place or topic. It can be public or private, and can have an audience. |
| Direct | A conversation between two people. |
| Group | A conversation between three or more specific people, without a name of its own. |
| Self-DM Room | A person's conversation with only themselves. |

**Area code:** `CONV`

**Topics**

| Topic | Covers |
|---|---|
| `LIST` | The list of conversations on the home screen |
| `NAME` | How conversations are named and pictured |
| `SECTION` | The sections of the conversation list |
| `ORDER` | Arranging conversations in a custom order |
| `HIDE` | Hiding conversations, and how they come back |
| `JOIN` | Joining a conversation |
| `LEAVE` | Leaving a conversation |
| `BROWSE` | Finding public Rooms |
| `PREVIEW` | Looking at a public Room before joining |
| `EDIT` | Changing a conversation's name, description and privacy |
| `ADD` | Adding people to a Room by hand |
| `MENTION` | Adding people to a conversation by mentioning them |
| `ARCHIVE` | Archiving and unarchiving conversations |
| `DELETE` | Deleting conversations |

Design: <figma link> · Runway: <epic link>

### CONV-LIST-001: Most recent puts the newest activity first
`req~CONV-LIST-001~1`

When the list is sorted by Most recent, the conversation with the newest message or
latest edit is first. Opening or reading a conversation does not move it.

    Given a user has conversations A (last message 9:00) and B (last message 9:30)
    When the user opens the conversation list
    Then B is listed above A
    And opening A does not change the order

Rationale:
People scan for "what just happened". Ordering by read time makes rows jump under their finger.

Needs: ios, macos, web

### CONV-LIST-002: Unread badge
`req~CONV-LIST-002~1`

A conversation with unread messages shows how many, capped at "99+".

    Given a conversation has 120 unread messages
    When the user views the conversation list
    Then that row shows a "99+" badge

Rationale:
The count says how much was missed; the cap keeps the layout stable.

Needs: ios, macos, web

### CONV-LIST-003: Muted conversations stay quiet
`req~CONV-LIST-003~1`

A muted conversation never shows a count. It shows a quiet dot and adds nothing
to the app icon badge.

    Given a conversation is muted and has 5 unread messages
    When the user views the conversation list
    Then that row shows a dot, not "5"
    And the app icon badge total does not include those 5

Rationale:
Muting means "do not interrupt me". Counting muted conversations makes the icon badge meaningless.

Needs: ios, macos, web

### CONV-LIST-004: Archived conversations are hidden
`req~CONV-LIST-004~1`

An archived conversation is not listed, but can still be found by search and by link.

    Given a conversation has been archived
    When the user views the conversation list
    Then it is not listed
    But searching for its name finds it

Status: rejected

Rationale:
Mixed up hiding and archiving. Replaced by CONV-HIDE-001 (hidden conversations can still be found) and CONV-ARCHIVE-001 (archived conversations are gone for everyone, including from search).

Needs: ios, macos, web

### CONV-LIST-005: The list shows only conversations you are in
`req~CONV-LIST-005~1`

The conversation list shows only conversations the person has joined, not
conversations they have left.

    Given a person left a conversation yesterday
    When they open their conversation list
    Then it is not there

Rationale:
The list is "where I talk". Anything else is clutter.

Needs: ccl

### CONV-LIST-006: The list appears straight away
`req~CONV-LIST-006~1`

When Connect opens, the conversation list shows what the device last knew straight
away, then brings it up to date.

    Given a person opens Connect on a slow connection
    Then their conversation list shows immediately
    And updates as new messages come in

Rationale:
People open Connect to do one quick thing. A blank list while it loads stops them doing it.

Needs: ccl

### CONV-LIST-007: Unread conversations are bold
`req~CONV-LIST-007~1`

A conversation with anything unread is shown in bold, even when it shows no count,
such as a muted one.

    Given a muted conversation gets a new message
    Then it shows in bold
    But with no count

Rationale:
Muting stops interruptions, not awareness. The person can still see where something is new.

Needs: ccl, ios, macos, web

### CONV-LIST-008: Unread counts are right when the list opens
`req~CONV-LIST-008~1`

Each conversation's unread count is correct as soon as the list appears, and goes up
as messages arrive, without opening it.

    Given a Direct conversation has 58 unread messages
    When the person opens Connect
    Then it shows 58 straight away, not a smaller number that climbs
    And when one more arrives, 59

Rationale:
A count that climbs or is wrong teaches people to ignore counts.

Needs: ccl, server

### CONV-LIST-009: Unread counts only go down by reading
`req~CONV-LIST-009~1`

A conversation's unread count only goes down when the person reads it, on any
device.

    Given a conversation shows 5 unread
    When the person does anything other than read it
    Then it still shows 5

Rationale:
A count that drops on its own hides messages the person has not seen.

Needs: ccl

### CONV-NAME-001: Group Direct conversations are named after their members
`req~CONV-NAME-001~1`

In the list, a group Direct conversation is named by its members' first names, in the
order they joined. With the conversation open, full names are shown.

    Given a group Direct conversation with Alice Smith, Bob Jones and Corey Lee
    Then the list shows "Alice, Bob, & Corey"
    And the open conversation shows "Alice Smith, Bob Jones, & Corey Lee"

Rationale:
A short name fits the list. Once it is open there is space to be unambiguous.

Needs: ccl, ios, macos, web

### CONV-NAME-002: A Direct conversation is named after the other person
`req~CONV-NAME-002~1`

A Direct conversation is named after the other person's full name.

    Given a Direct conversation with Ana Ruiz
    Then it is called "Ana Ruiz" in the list and when open

Rationale:
You are talking to Ana. That is what the conversation is.

Needs: ccl

### CONV-NAME-003: Direct and Group conversations cannot be renamed
`req~CONV-NAME-003~1`

Direct and Group conversations cannot be given a name. Only Rooms have a name that
can be changed.

    Given a group Direct conversation
    When a member looks for Rename
    Then it is not offered

Rationale:
Their members are their name. A custom name would hide who is in them.

Needs: ccl

### CONV-NAME-004: Pictures come from the company directory
`req~CONV-NAME-004~1`

A Direct conversation shows the other person's directory photo. A group Direct conversation
shows its members' photos, with initials for anyone without one. Named
conversations have no picture.

    Given a group Direct conversation with Alice, Bob and Corey
    And Bob has no photo
    Then it shows Alice's photo, Bob's initials and Corey's photo

Rationale:
People recognise faces faster than names, and the directory is where everyone's photo already is.

Needs: ccl, ios, macos, web

### CONV-SECTION-001: The list has Favorites, Rooms and People
`req~CONV-SECTION-001~1`

The conversation list has three sections: Favorites, then Rooms, then People, which
holds Direct and Group conversations. Each conversation is in one section.

    Given a person has favorited a Direct conversation with Ana
    Then it is in Favorites
    And not in People

Rationale:
People find things faster in a few predictable places, and a conversation listed twice looks like two conversations.

Needs: ccl, ios, macos, web

### CONV-SECTION-002: Favorites are always at the top
`req~CONV-SECTION-002~1`

Favorites are shown above the other sections whatever sort the person chose.

    Given a person sorts alphabetically
    And has favorited "Zoning"
    Then "Zoning" is above "Accounts"

Rationale:
Favorites are the conversations the person said matter most.

Needs: ios, macos, web

### CONV-ORDER-001: Custom order is arranged by dragging
`req~CONV-ORDER-001~1`

With Custom sort, a person drags conversations into the order they want, within
their section.

    Given a person uses Custom sort
    When they drag "Philly Roofing" to the top of their conversations
    Then it stays at the top until they move it

Rationale:
Some people keep a fixed order of what matters to them, and it should not move by itself.

Needs: ccl, ios, macos, web

### CONV-ORDER-002: Dragging only works in Custom sort
`req~CONV-ORDER-002~1`

Conversations can only be dragged when the list uses Custom sort. Dragging never
switches the sort to Custom by itself.

    Given a person sorts by Most recent
    When they try to drag a conversation
    Then it does not move
    And the sort stays Most recent

Rationale:
Switching a person's sort without asking would throw away the order they chose.

Needs: ccl

### CONV-ORDER-003: New conversations go to the top of their section
`req~CONV-ORDER-003~1`

In Custom sort, conversations the person has not placed yet come first in their
section, alphabetically, above the ones they arranged.

    Given a person arranged Bravo then Alpha
    And joins two new conversations, Zebra and Apple
    Then the order is Apple, Zebra, Bravo, Alpha

Rationale:
Something new should be easy to spot, and easy to drag into place.

Needs: ccl

### CONV-ORDER-004: A conversation that comes back starts unplaced
`req~CONV-ORDER-004~1`

A conversation that is favorited, unfavorited, unhidden or rejoined loses its old
place and goes to the top of its section, on every device.

    Given a person's custom order is B, A
    When they hide A on their phone and unhide it on their Mac
    Then both devices show A, B

Rationale:
Its old place belonged to a different section or a different time. The top is where the person will notice it.

Needs: ccl

### CONV-ORDER-005: Dragging never overwrites another device's order
`req~CONV-ORDER-005~1`

Rearranging on one device never undoes a newer arrangement made on another.

    Given a person rearranged their list on their Mac a minute ago
    When they drag a conversation on their phone
    Then the Mac's arrangement is kept, with this one move added

Rationale:
Losing an arrangement because two devices disagreed is a quiet way to lose work.

Needs: ccl

### CONV-HIDE-001: Hiding takes a conversation out of the list
`req~CONV-HIDE-001~1`

A person can hide a conversation. It leaves their list on every device but they are
still in it, and can find it by search.

    Given a person hides "2023 Holiday Party"
    Then it is gone from their list on all their devices
    But searching for it still finds it

Rationale:
People are in conversations they rarely need. Hiding clears them away without leaving.

Needs: ccl, ios, macos, web

### CONV-HIDE-002: A hidden conversation comes back when it would notify you
`req~CONV-HIDE-002~1`

A hidden conversation comes back to the list when a message arrives that would
notify the person under that conversation's notification level.

    Given a person hid a conversation set to "Only mentions of me"
    When someone mentions them in it
    Then it is back in their list
    But an ordinary message would have left it hidden

Rationale:
Hiding means "I don't need this now", not "never tell me". Something addressed to the person brings it back.

Needs: ccl

### CONV-HIDE-003: A muted hidden conversation stays hidden
`req~CONV-HIDE-003~1`

A hidden conversation that is muted stays hidden whatever arrives in it.

    Given a person hid and muted a conversation
    When someone mentions them in it
    Then it stays hidden

Rationale:
Muted and hidden together means the person wants nothing from it.

Needs: ccl

### CONV-HIDE-004: Posting in a hidden conversation brings it back
`req~CONV-HIDE-004~1`

A hidden conversation comes back to the list when the person posts in it, from any
device.

    Given a person hid a conversation
    When they reply in it from a notification
    Then it is back in their list

Rationale:
The person is using it again.

Needs: ccl

### CONV-HIDE-005: Messages missed while closed still bring it back
`req~CONV-HIDE-005~1`

A notifying message that arrived while Connect was closed still brings a hidden
conversation back the next time Connect opens.

    Given a person's phone was off when someone mentioned them in a hidden conversation
    When they open Connect
    Then that conversation is back in their list

Rationale:
Whether the phone was on should not decide whether the person finds out.

Needs: ccl

### CONV-HIDE-006: Edits do not bring a hidden conversation back
`req~CONV-HIDE-006~1`

Edits to old messages never bring a hidden conversation back.

    Given a person hid a conversation
    When someone edits an old message in it
    Then it stays hidden

Rationale:
An edit is not something new for the person.

Needs: ccl

### CONV-HIDE-007: Hidden conversations cannot be favorites
`req~CONV-HIDE-007~1`

A hidden conversation cannot be favorited.

    Given a person hid a conversation
    When they look for Favorite on it in search
    Then it is not offered

Rationale:
Favorite means "keep this at the top", hidden means "keep this out of the way". It cannot be both.

Needs: ccl

### CONV-JOIN-001: Joining puts a conversation in your list
`req~CONV-JOIN-001~1`

Joining a public Room puts it in the person's list.

    Given a person finds "Philly Roofing" by browsing
    When they join it
    Then it is in their conversation list

Rationale:
Joining is how people say they want to follow a conversation.

Needs: ccl

### CONV-JOIN-002: People added to a conversation are in it straight away
`req~CONV-JOIN-002~1`

A person added to a conversation, by an admin, by an audience or by being
mentioned, is in it straight away. There is nothing to accept.

    Given an admin adds Sam to a Room
    Then the Room is in Sam's list
    And Sam can read and post in it

Rationale:
Who belongs in a conversation is decided for the person, by the company or by its admins. Asking them to accept would only leave people out by accident.

Needs: server, ccl

### CONV-LEAVE-001: People can leave public Rooms
`req~CONV-LEAVE-001~1`

A person can leave a public Room. They cannot leave a private Room, a Direct
conversation or a Group conversation.

    Given a person is in a public Room
    When they leave it
    Then it is gone from their list and stays gone after a restart

Rationale:
A public Room can be joined again at any time. Who is in a private Room is decided by its admins and audience, and a Direct or Group conversation is defined by who is in it.

Needs: server, ccl

### CONV-LEAVE-002: The only admin cannot leave
`req~CONV-LEAVE-002~1`

A conversation's only admin cannot leave it until they make someone else an admin.

    Given Dana is the only admin of a public Room
    When she tries to leave
    Then she is told to make someone else an admin first
    And the conversation stays in her list

Rationale:
A conversation with no admin can never be managed again.

Needs: server

### CONV-BROWSE-001: People can find public Rooms
`req~CONV-BROWSE-001~1`

A person can search the public Rooms by name or description, and the
results include conversations they are already in, even hidden ones.

    Given a person is in a hidden conversation "Ops"
    And a public Room "Ops Alerts" exists
    When they search "ops"
    Then both appear
    And "Ops" shows that they are in it

Rationale:
People look for a conversation by what it is about, whether or not they are already in it.

Needs: ccl, server

### CONV-PREVIEW-001: Public Rooms can be read before joining
`req~CONV-PREVIEW-001~1`

A person can read a public Room's recent messages, and scroll back, before
joining. They cannot post, react or appear as a reader until they join.

    Given a person finds a public Room they are not in
    When they open it
    Then they can read its messages
    But cannot post until they join

Rationale:
People decide whether to join by seeing what a conversation is like.

Needs: ccl

### CONV-PREVIEW-002: A preview shows who is in the conversation
`req~CONV-PREVIEW-002~1`

Before joining, a person can see who is in a public Room and who its admins
are.

    Given a person is previewing a public Room
    When they look at its members
    Then they see who is in it, with admins marked

Rationale:
Who is in a conversation says a lot about what it is for.

Needs: ccl

### CONV-EDIT-001: Conversation names are up to 80 characters
`req~CONV-EDIT-001~1`

A Room must have a name, which is not just spaces and is at most 80
characters.

    Given an admin renames a conversation to 81 characters
    Then it is refused
    And they are told the limit

Rationale:
Names are read in lists and headers. A long name gets cut off and stops being useful.

Needs: ccl

### CONV-EDIT-002: Descriptions are up to 100 characters
`req~CONV-EDIT-002~1`

A Room can have a description of at most 100 characters. Saving it
empty removes it.

    Given an admin writes a description of 120 characters
    Then it is refused
    And they are told the limit

Rationale:
A description is a one-line summary of what the conversation is for.

Needs: ccl

### CONV-EDIT-003: Only admins change a conversation's name and description
`req~CONV-EDIT-003~1`

Only a conversation's admins can change its name, description or privacy.

    Given a member who is not an admin
    When they open the conversation's details
    Then they cannot change its name or description

Rationale:
These describe the conversation for everyone in it.

Needs: server, ios, macos, web

### CONV-EDIT-004: Public to private is one way
`req~CONV-EDIT-004~1`

A public Room can be made private, but a private Room cannot be
made public.

    Given a private Room
    When an admin looks for "Make public"
    Then it is not offered

Rationale:
People wrote in a private Room expecting only its members to read it. Making it public would expose that.

Needs: ccl

### CONV-EDIT-005: A conversation is private until known to be public
`req~CONV-EDIT-005~1`

If Connect cannot tell whether a conversation is public, it treats it as private.

    Given Connect cannot yet tell whether a conversation is public
    Then it is shown as private

Rationale:
Wrongly showing a conversation as private is harmless. Wrongly showing it as public could lead people to share it.

Needs: ccl

### CONV-ADD-001: Only Room admins add people directly
`req~CONV-ADD-001~1`

Only a Room's admins can add a person to it by hand. This is true for public Rooms
too.

    Given a person who is not an admin of a Room
    When they try to add someone to it directly
    Then the person is not added
    And an admin of the same Room can add them

Rationale:
Who belongs in a conversation is set by its audience. Hand-picked additions are an exception, so they are kept to the people responsible for the conversation.

Needs: server

### CONV-MENTION-001: Mentioning someone in a public Room adds them
`req~CONV-MENTION-001~1`

When a member of a public Room mentions a person who is not in it, that
person is added to the conversation, whether or not the member is an admin.

    Given Dana is a member of the public Room "Philly Roofing"
    And Sam is not a member
    When Dana sends a message that mentions @Sam
    Then Sam is added to "Philly Roofing"
    And Sam can read the message that mentioned them

Rationale:
A mention is a request for someone's attention. If they cannot see the conversation, the mention does nothing and the person who wrote it does not know.

Needs: server

### CONV-MENTION-002: Only a new mention of a person adds them
`req~CONV-MENTION-002~1`

Mentioning only adds someone in a new message, in a public Room, naming a
specific person whose account is switched on.

    Given a public Room and a person who is not in it
    When they are mentioned in an edit, as part of a mention of everyone, in a private Room, or after their account was switched off
    Then they are not added

Rationale:
Edits and mentions of everyone would add people nobody meant to add. Private Rooms are only for the people added to them, on purpose. Switched-off accounts must stay out (MEMBERSHIP-LEAVE-001).

Needs: server

### CONV-ARCHIVE-001: Archiving closes a conversation for everyone
`req~CONV-ARCHIVE-001~1`

An archived conversation disappears for everyone, everywhere: from conversation
lists, from the public Rooms people can browse, and from search. Nobody can post in
it. Its messages are kept.

    Given a conversation with members and message history
    When it is archived
    Then it no longer appears in any member's conversation list
    And it no longer appears among the public Rooms people can browse
    And searching for it finds nothing
    And nobody can send messages to it
    And its messages are kept

Rationale:
Archiving is how a conversation that is no longer needed is put away without losing the record of what was said in it.

Needs: nitro, server

### CONV-ARCHIVE-002: Only conversation admins archive conversations
`req~CONV-ARCHIVE-002~1`

Only a conversation's admins and Connect administrators can archive or unarchive
it by hand.

    Given a person who is a member, but not an admin, of a conversation
    When they look for a way to archive it
    Then they cannot archive it

Rationale:
Archiving removes the conversation for everyone, so it belongs with the people responsible for it.

Needs: nitro, server

### CONV-ARCHIVE-003: Conversations with no messages for six months are archived automatically
`req~CONV-ARCHIVE-003~1`

A conversation is archived automatically once nobody has posted a message in it
for six months. Direct and Group conversations are never archived automatically.

    Given a conversation where the last message was sent more than six months ago
    When a week has passed
    Then the conversation has been archived
    But a Direct conversation with no messages for six months is left alone

Rationale:
Dormant conversations clutter conversation lists and search. Direct and Group conversations are personal history, and people expect them to be there when they come back.

Needs: server

### CONV-ARCHIVE-004: Unarchiving brings a conversation back
`req~CONV-ARCHIVE-004~1`

Unarchiving a conversation puts it back in the lists of everyone its audience
includes, and people can post in it again.

    Given a conversation was archived
    When an admin unarchives it
    Then everyone its audience includes is a member again
    And people can send messages to it

Status: draft

Rationale:
Product to decide: should people who only followed a public Room, rather than being in its audience, also come back?

Needs: nitro, server

### CONV-DELETE-001: Conversations are archived, never deleted
`req~CONV-DELETE-001~1`

Nobody can delete a conversation. Archiving is the only way to put one away.

    Given a person with every Connect permission
    When they want to get rid of a conversation
    Then they can archive it
    But they cannot delete it or its history

Rationale:
Deleting a conversation would also delete the record of decisions made in it. Archiving gives the same tidy result and can be undone.

Needs: nitro, server
