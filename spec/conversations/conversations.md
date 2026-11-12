# Conversations

Every **Conversation** a person is in: the **Conversation List** and its sections, how
conversations are named, favorited, hidden and marked read or unread, starting a new
conversation, and the life of a Room from creation to archive. Who is in a Room because
of its **Member filters** is covered in [Audiences](../audiences/conversation-members.md).
The EVENTS section is covered in [Corporate events](../events/corporate-events.md), and
how lists and searches are ordered in [Sorting and naming](../sorting/sorting-and-naming.md).

There are three kinds of conversation:

| Kind | What it is |
|---|---|
| Rooms | Multi-person channels with a name, public (globe icon) or private (padlock). |
| People Conversations | DMs (1:1) and group conversations of up to 10 other people plus you. |
| Self Message | A person's conversation with themselves. |

**Area code:** `CONV`

**Topics**

| Topic | Covers |
|---|---|
| `LIST` | The **Conversation List** and its rows |
| `NAME` | How conversations are named and pictured |
| `SECTION` | The sections of the **Conversation List** |
| `FAVORITE` | Favoriting conversations |
| `SEARCH` | The Search conversations field |
| `OPTIONS` | The **Conversation options menu** |
| `READ` | Marking a conversation read or unread |
| `ORDER` | Arranging conversations in a Self-Managed order |
| `HIDE` | Hiding conversations, and how they come back |
| `DIRECT` | DMs, and starting a People Conversation from the new message flow |
| `GROUP` | Group conversations |
| `SELF` | A person's **Self Message** |
| `CREATE` | Creating a Room |
| `JOIN` | Joining a conversation |
| `LEAVE` | Leaving a conversation |
| `BROWSE` | Finding Rooms in Browse Rooms |
| `PREVIEW` | Looking at a public Room before joining |
| `EDIT` | Changing a Room's settings: name, topic, privacy, Required Room |
| `ADD` | Adding people to a Room by hand |
| `MENTION` | Adding people to a conversation by @mentioning them |
| `ARCHIVE` | Archiving and unarchiving Rooms |
| `DELETE` | Deleting conversations |

Design: [Conversation List](https://huddle.powerapp.cloud/projects/495) · [Unreads](https://huddle.powerapp.cloud/projects/600) · [Pinning and Saving](https://huddle.powerapp.cloud/projects/561) · [Start a Message](https://huddle.powerapp.cloud/projects/497) · [Create a Room](https://huddle.powerapp.cloud/projects/628) · [Browse Rooms](https://huddle.powerapp.cloud/projects/517) · [Room Info & Contact Cards](https://huddle.powerapp.cloud/projects/549) · [Headers](https://huddle.powerapp.cloud/projects/518)

### CONV-LIST-001: Recent Activity puts the newest activity first
`req~CONV-LIST-001~1`

When the list is sorted by Recent Activity, the conversation with the newest message is
first. Opening or reading a conversation does not move it.

    Given a person has conversations A (last message 9:00) and B (last message 9:30)
    When they look at their Conversation List sorted by Recent Activity
    Then B is listed above A
    And opening A does not change the order

Rationale:
People scan for "what just happened". Ordering by read time makes rows jump under their finger.

Needs: browser, pwa, macos, ios

### CONV-LIST-002: The Notification Badge count is capped
`req~CONV-LIST-002~1`

A conversation's **Notification Badge** shows how many notifying messages it has, capped
at "99+".

    Given a conversation has 120 notifying messages
    When the person views the Conversation List
    Then that row shows a "99+" Notification Badge

Rationale:
The count says how much was missed; the cap keeps the layout stable.

Status: draft

Needs: browser, pwa, macos, ios

### CONV-LIST-003: No Notifications conversations show bold, with no badge
`req~CONV-LIST-003~1`

A Room set to No Notifications is shown **bold (unread)** when it has something unread,
but never shows a **Notification Badge**.

    Given a Room is set to No Notifications
    When 5 new messages arrive in it
    Then its row is bold
    But it shows no Notification Badge

Rationale:
Same behavior as NOTIFY-LEVEL-004, which owns it. Kept for the record.
No Notifications means "do not interrupt me", not "hide what is new".

Status: rejected

Needs: browser, pwa, macos, ios

### CONV-LIST-004: Archived conversations are hidden
`req~CONV-LIST-004~1`

An archived conversation is not listed, but can still be found by search and by link.

    Given a conversation has been archived
    When the person views the Conversation List
    Then it is not listed
    But searching for its name finds it

Rationale:
Mixed up hiding and archiving. Replaced by CONV-HIDE-001 (hidden conversations can still be found) and CONV-ARCHIVE-001 (archived conversations are gone for everyone, including from search).

Status: rejected

Needs: browser, pwa, macos, ios

### CONV-LIST-005: The list shows only conversations you are in
`req~CONV-LIST-005~1`

The **Conversation List** shows only conversations the person is in, not conversations
they have left.

    Given a person left a public Room yesterday
    When they open their Conversation List
    Then it is not there

Rationale:
The list is "where I talk". Anything else is clutter.

Needs: ccl, browser, pwa, macos, ios

### CONV-LIST-006: The list appears straight away
`req~CONV-LIST-006~1`

When Connect opens, the **Conversation List** shows what the device last knew straight
away, then brings it up to date.

    Given a person opens Connect on a slow connection
    Then their Conversation List shows immediately
    And updates as new messages come in

Rationale:
People open Connect to do one quick thing. A blank list while it loads stops them doing it.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-LIST-007: Unread conversations are bold
`req~CONV-LIST-007~1`

A conversation with a message from another person that has not been read is shown
**bold (unread)**, even when it shows no **Notification Badge**.

    Given a Room set to No Notifications gets a new message
    Then it shows bold
    But with no Notification Badge

Rationale:
Same behavior as NOTIFY-UNREAD-001 and NOTIFY-UNREAD-003, which owns it. Kept for the record.
Bold says something is new; the badge says something needs attention. Keeping them apart lets people quiet a conversation without losing track of it.

Status: rejected

Needs: ccl, browser, pwa, macos, ios

### CONV-LIST-008: Unread counts are right when the list opens
`req~CONV-LIST-008~1`

Each conversation's **Notification Badge** count is correct as soon as the list appears,
and goes up as messages arrive, without opening it.

    Given a DM has 58 unread messages
    When the person opens Connect
    Then it shows 58 straight away, not a smaller number that climbs
    And when one more arrives, 59

Rationale:
A count that climbs or is wrong teaches people to ignore counts.

Status: draft

Needs: server, ccl, browser, pwa, macos, ios

### CONV-LIST-009: Unread counts only go down by reading
`req~CONV-LIST-009~1`

A conversation's **Notification Badge** count only goes down when the person reads it,
or marks it read, on any device.

    Given a conversation shows 5
    When the person does anything other than read it or mark it read
    Then it still shows 5

Rationale:
A count that drops on its own hides messages the person has not seen.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-LIST-010: A failed send shows on the conversation's row
`req~CONV-LIST-010~1`

When a message in a conversation fails to send, that conversation's row in the
**Conversation List** shows an error indicator.

    Given a person sends a message that fails
    When they look at the Conversation List
    Then that conversation's row shows an error indicator

Rationale:
A person who has moved to another conversation must still be able to see that something they sent did not arrive.

Needs: ccl, browser, pwa, macos, ios

### CONV-NAME-001: Group conversations are listed by first names
`req~CONV-NAME-001~1`

In the **Conversation List**, a group conversation is named by its members' first names,
in the order they were added, with "&" before the last.

    Given a group conversation with Kelly, Rex, Ruby, Khin and Mitch, added in that order
    Then the Conversation List shows "Kelly, Rex, Ruby, Khin, & Mitch"

Rationale:
A short name fits the list, and a stable order keeps the name recognisable.

Needs: ccl, browser, pwa, macos, ios

### CONV-NAME-002: A DM is named after the other person
`req~CONV-NAME-002~1`

A DM is named after the other person's full name.

    Given a DM with Ana Ruiz
    Then it is called "Ana Ruiz" in the Conversation List and when open

Rationale:
You are talking to Ana. That is what the conversation is.

Needs: ccl, browser, pwa, macos, ios

### CONV-NAME-003: People Conversations cannot be renamed
`req~CONV-NAME-003~1`

People Conversations cannot be given a name. Only Rooms have a name that can be changed.

    Given a group conversation
    When a member looks for Rename
    Then it is not offered

Rationale:
Their members are their name. A custom name would hide who is in them.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-NAME-004: Classic group avatars show "+n" for the others
`req~CONV-NAME-004~1`

In the Classic layout, a group conversation with 2 others shows their two avatars
stacked. With more others, it shows one avatar plus "+n", where n is the number of others
not shown.

    Given a person uses the Classic layout
    And is in a group conversation with 9 others
    Then its row shows one avatar and "+8"
    And a group conversation with 2 others shows two stacked avatars

Rationale:
The avatar shows who is in the conversation, and "+n" says honestly how many more there are.

Needs: ccl, browser, pwa, macos, ios

### CONV-NAME-005: Group conversation names never include you
`req~CONV-NAME-005~1`

A group conversation's name never includes the person looking at it.

    Given Kelly is in a group conversation with Rex and Ruby
    When Kelly looks at her Conversation List
    Then it is named "Rex & Ruby"

Rationale:
Everyone knows they are in their own conversations; their own name only takes space.

Needs: ccl, browser, pwa, macos, ios

### CONV-NAME-006: The macOS group header shows avatars and full names
`req~CONV-NAME-006~1`

On macOS, a group conversation's **Conversation Header** shows up to 3 avatars plus "+n"
for the others not shown, then the members' full names.

    Given a group conversation with 5 others is open on macOS
    Then the Conversation Header shows 3 avatars and "+2"
    And then the members' full names

Rationale:
With the conversation open there is space to be unambiguous about who is in it.

Needs: macos

### CONV-NAME-007: The Message Composer placeholder names the group
`req~CONV-NAME-007~1`

In a group conversation, the **Message Composer** placeholder is "Message" followed by the
first five first names and "& n others", where n counts everyone not named, including you.

    Given Kelly is in a group conversation with Rex, Ruby, Khin, Mitch, Ana and Sam
    When she opens it
    Then the Message Composer placeholder reads "Message Rex, Ruby, Khin, Mitch, Ana & 2 others"

Rationale:
The placeholder reminds the person who will read what they are about to send.

Needs: ccl, browser, pwa, macos, ios

### CONV-SECTION-001: The list has EVENTS, Favorites, ROOMS and PEOPLE
`req~CONV-SECTION-001~1`

The **Conversation List** has these sections, top to bottom: EVENTS (Nitro Connect only),
Favorites, ROOMS and PEOPLE, which holds People Conversations. Each conversation is in
one section.

    Given a person has favorited their DM with Ana
    Then it is in Favorites
    And not in PEOPLE

Rationale:
People find things faster in a few predictable places, and a conversation listed twice looks like two conversations.

Needs: ccl, browser, pwa, macos, ios

### CONV-SECTION-002: Favorites are above Rooms and People whatever the sort
`req~CONV-SECTION-002~1`

Favorites are shown above ROOMS and PEOPLE whatever sort the person chose.

    Given a person sorts Alphabetical
    And has favorited "Zoning"
    Then "Zoning" is above the Room "Accounts"

Rationale:
Favorites are the conversations the person said matter most.

Needs: browser, pwa, macos, ios

### CONV-SECTION-003: Each section collapses
`req~CONV-SECTION-003~1`

Each section of the **Conversation List** can be collapsed and expanded from its header.

    Given a person's ROOMS section is expanded
    When they collapse it
    Then its conversations are hidden under the ROOMS header
    And expanding it shows them again

Rationale:
People can put away a section they don't need right now and keep the list short.

Needs: browser, pwa, macos, ios

### CONV-SECTION-004: A collapsed section totals its badges
`req~CONV-SECTION-004~1`

A collapsed section shows one **Notification Badge** with the total of its conversations'
badges.

    Given ROOMS holds one Room with a badge of 2 and another with a badge of 3
    When the person collapses ROOMS
    Then the ROOMS header shows a Notification Badge of 5

Rationale:
Collapsing a section must not hide that something in it needs attention.

Needs: ccl, browser, pwa, macos, ios

### CONV-FAVORITE-001: Any conversation can be favorited
`req~CONV-FAVORITE-001~1`

A person can favorite a conversation from the **Conversation options menu**. There is no
limit to how many.

    Given a person already has 30 Favorites
    When they favorite another conversation
    Then it is added to Favorites

Rationale:
Favorites are the person's own shortlist, and only they know how long it should be.

Needs: server, ccl, browser, pwa, macos, ios

### CONV-FAVORITE-002: A favorited conversation moves to Favorites
`req~CONV-FAVORITE-002~1`

A favorited conversation moves out of ROOMS or PEOPLE into Favorites, and goes back when
unfavorited.

    Given a person favorites the Room "Philly Roofing"
    Then it is in Favorites and no longer in ROOMS
    And when they unfavorite it, it is back in ROOMS

Rationale:
Each conversation lives in one place, so favoriting moves it rather than copying it.

Needs: ccl, browser, pwa, macos, ios

### CONV-FAVORITE-003: The Favorites section hides when empty
`req~CONV-FAVORITE-003~1`

The Favorites section is not shown when the person has no Favorites.

    Given a person has no Favorites
    When they look at their Conversation List
    Then there is no Favorites section

Rationale:
An empty section is clutter.

Needs: browser, pwa, macos, ios

### CONV-SEARCH-001: A Search conversations field sits at the bottom of the list
`req~CONV-SEARCH-001~1`

On macOS and the Connect Browser, a Search conversations field sits at the bottom of the
**Conversation List**.

    Given a person is using Connect on macOS or in the Browser
    When they look at the bottom of the Conversation List
    Then there is a Search conversations field

Rationale:
People with many conversations need to jump to one by name instead of scrolling.

Needs: browser, macos

### CONV-OPTIONS-001: The Conversation options menu offers Favorites and Mark as Read/Unread
`req~CONV-OPTIONS-001~1`

The **Conversation options menu** of a conversation offers Favorites and Mark as Read or
Mark as Unread.

    Given a person opens the Conversation options menu of a read conversation
    Then it offers to favorite it and to Mark as Unread

Rationale:
The things a person does to a conversation's place in their own list are kept together.

Needs: browser, pwa, macos, ios

### CONV-OPTIONS-002: On Desktop, the menu opens from an ellipsis on hover
`req~CONV-OPTIONS-002~1`

On Desktop, hovering over a conversation shows an ellipsis that opens the **Conversation
options menu**.

    Given a person is on Desktop
    When they hover over a conversation and click the ellipsis
    Then the Conversation options menu opens

Rationale:
Keeping the button hidden until hover keeps the list calm.

Needs: browser, pwa, macos

### CONV-OPTIONS-003: On iOS, swiping left to right shows the options
`req~CONV-OPTIONS-003~1`

On iOS, swiping a conversation from left to right shows the **Conversation options menu**.

    Given a person is on iOS
    When they swipe a conversation from left to right
    Then its Favorites and Mark as Read/Unread options appear

Rationale:
Swiping is how people act on a list row on iOS.

Needs: ios

### CONV-OPTIONS-004: In the PWA, the three-dot menu opens the options
`req~CONV-OPTIONS-004~1`

In the PWA, a conversation's three-dot menu opens the **Conversation options menu**. It
does not remove the conversation.

    Given a person is using the Connect PWA
    When they tap a conversation's three-dot menu
    Then the Conversation options menu opens
    And the conversation stays in the list

Rationale:
A menu button must open choices, never act on its own.

Needs: pwa

### CONV-READ-001: Mark as Unread shows an empty badge and bold
`req~CONV-READ-001~1`

A conversation marked unread shows **bold (unread)** and an empty **Notification Badge**
until a notifying message adds a count.

    Given a person marks a read DM as unread
    Then its row is bold with an empty Notification Badge
    And when a notifying message arrives, the badge shows 1

Rationale:
Mark as Unread lets people keep something on their to-do list; the empty badge says "you flagged this", not "someone wrote".

Needs: server, ccl, browser, pwa, macos, ios

### CONV-READ-002: A collapsed section shows an empty badge for a conversation marked unread
`req~CONV-READ-002~1`

A collapsed section that holds a conversation marked unread, and no notifying activity,
shows an empty **Notification Badge**.

    Given a person marked a Room unread
    And it has no notifying messages
    When they collapse ROOMS
    Then the ROOMS header shows an empty Notification Badge

Rationale:
Collapsing a section must not hide what the person flagged for themselves.

Needs: ccl, browser, pwa, macos, ios

### CONV-READ-003: Mark as Read clears unread
`req~CONV-READ-003~1`

Mark as Read clears a conversation's **bold (unread)** and **Notification Badge** without
opening it.

    Given a Room is bold with a Notification Badge of 4
    When the person chooses Mark as Read
    Then the row is no longer bold
    And it shows no Notification Badge

Rationale:
People can see from the list that they don't need to read something, and clear it without opening it.

Needs: server, ccl, browser, pwa, macos, ios

### CONV-ORDER-001: Self-Managed order is arranged by dragging
`req~CONV-ORDER-001~1`

With the Self-Managed sort, a person drags conversations into the order they want,
within their section.

    Given a person uses the Self-Managed sort
    When they drag "Philly Roofing" to the top of ROOMS
    Then it stays at the top until they move it

Rationale:
Some people keep a fixed order of what matters to them, and it should not move by itself.

Needs: ccl, browser, pwa, macos, ios

### CONV-ORDER-002: Dragging only works in Self-Managed
`req~CONV-ORDER-002~1`

Conversations can only be dragged when the list uses the Self-Managed sort. Dragging
never switches the sort to Self-Managed by itself.

    Given a person sorts by Recent Activity
    When they try to drag a conversation
    Then it does not move
    And the sort stays Recent Activity

Rationale:
Switching a person's sort without asking would throw away the order they chose.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-ORDER-003: New conversations go to the top of their section
`req~CONV-ORDER-003~1`

In the Self-Managed sort, conversations the person has not placed yet come first in
their section, alphabetically, above the ones they arranged.

    Given a person arranged Bravo then Alpha
    And joins two new conversations, Zebra and Apple
    Then the order is Apple, Zebra, Bravo, Alpha

Rationale:
Something new should be easy to spot, and easy to drag into place.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-ORDER-004: A conversation that comes back starts unplaced
`req~CONV-ORDER-004~1`

A conversation that is favorited, unfavorited, unhidden or rejoined loses its old place
and goes to the top of its section, on every device.

    Given a person's Self-Managed order is B, A
    When they hide A on their phone and it comes back on their Mac
    Then both devices show A, B

Rationale:
Its old place belonged to a different section or a different time. The top is where the person will notice it.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-ORDER-005: Dragging never overwrites another device's order
`req~CONV-ORDER-005~1`

Rearranging on one device never undoes a newer arrangement made on another.

    Given a person rearranged their list on their Mac a minute ago
    When they drag a conversation on their phone
    Then the Mac's arrangement is kept, with this one move added

Rationale:
Losing an arrangement because two devices disagreed is a quiet way to lose work.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-HIDE-001: Hiding takes a conversation out of the list without leaving it
`req~CONV-HIDE-001~1`

A person can **Hide** a conversation. It leaves their **Conversation List** on every
device, but they are still in it, and can find it by search.

    Given a person hides "2023 Holiday Party"
    Then it is gone from their Conversation List on all their devices
    But they are still a member
    And searching for it still finds it

Rationale:
People are in conversations they rarely need. Hiding clears them away without leaving.

Needs: ccl, browser, pwa, macos, ios

### CONV-HIDE-002: A hidden conversation comes back on the next notifying message
`req~CONV-HIDE-002~1`

A hidden conversation comes back to the list when a message arrives that notifies the
person under that conversation's notification level.

    Given a person hid a Room set to Direct Mentions Only
    When someone @mentions them in it
    Then it is back in their Conversation List
    But an ordinary message would have left it hidden

Rationale:
Hiding means "I don't need this now", not "never tell me". Something addressed to the person brings it back.

Needs: ccl, browser, pwa, macos, ios

### CONV-HIDE-003: A hidden No Notifications conversation stays hidden
`req~CONV-HIDE-003~1`

A hidden Room set to No Notifications stays hidden whatever arrives in it.

    Given a person hid a Room set to No Notifications
    When someone @mentions them in it
    Then it stays hidden

Rationale:
Nothing in a No Notifications Room notifies, so nothing brings it back.

Needs: ccl, browser, pwa, macos, ios

### CONV-HIDE-004: Posting in a hidden conversation brings it back
`req~CONV-HIDE-004~1`

A hidden conversation comes back to the list when the person posts in it, from any
device.

    Given a person hid a conversation
    When they reply in it from a notification
    Then it is back in their Conversation List

Rationale:
The person is using it again.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-HIDE-005: Messages missed while closed still bring it back
`req~CONV-HIDE-005~1`

A notifying message that arrived while Connect was closed still brings a hidden
conversation back the next time Connect opens.

    Given a person's phone was off when someone @mentioned them in a hidden conversation
    When they open Connect
    Then that conversation is back in their Conversation List

Rationale:
Whether the phone was on should not decide whether the person finds out.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-HIDE-006: Edits do not bring a hidden conversation back
`req~CONV-HIDE-006~1`

Edits to old messages never bring a hidden conversation back.

    Given a person hid a conversation
    When someone edits an old message in it
    Then it stays hidden

Rationale:
An edit is not something new for the person.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-HIDE-007: Hidden conversations cannot be favorites
`req~CONV-HIDE-007~1`

A hidden conversation cannot be favorited.

    Given a person hid a conversation
    When they look for Favorite on it in search
    Then it is not offered

Rationale:
Favorite means "keep this at the top", hidden means "keep this out of the way". It cannot be both.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-HIDE-008: On Desktop and Android, an x button hides a conversation
`req~CONV-HIDE-008~1`

On Desktop and on Android, a conversation is hidden with its x button.

    Given a person is on Desktop or using the PWA on Android
    When they click a conversation's x button
    Then the conversation is hidden

Rationale:
A close button is the familiar way to put something away without deleting it.

Needs: browser, pwa, macos

### CONV-HIDE-009: On Web, the x button is labeled "Close conversation"
`req~CONV-HIDE-009~1`

On Web, the x button that hides a conversation is labeled "Close conversation".

    Given a person is using the Connect Browser or PWA
    When they reach a conversation's x button
    Then it is labeled "Close conversation"

Rationale:
The label says what the button does, and tells people it is not a delete.

Needs: browser, pwa

### CONV-HIDE-010: On iOS, swiping right to left reveals the x icon
`req~CONV-HIDE-010~1`

On iOS, swiping a conversation from right to left reveals an x icon that hides it.

    Given a person is on iOS
    When they swipe a conversation from right to left
    Then an x icon appears
    And tapping it hides the conversation

Rationale:
Swiping is how people act on a list row on iOS, and the x icon matches the Desktop close button.

Needs: ios

### CONV-DIRECT-001: There is one DM per pair of people
`req~CONV-DIRECT-001~1`

Starting a DM with someone you already have one with opens the existing conversation.
It does not create a second one.

    Given Dana and Sam already have a DM
    When Dana starts a new DM with Sam
    Then Dana is taken to the DM they already have

Rationale:
Two conversations with the same person split the history, and people lose track of where something was said.

Status: draft

Needs: server, ccl, browser, pwa, macos, ios

### CONV-DIRECT-002: No new conversations with inactive users
`req~CONV-DIRECT-002~1`

A People Conversation that includes an inactive user cannot be started. The person sees
"Unable to Start Conversation. 1 or more members are inactive and cannot receive
messages."

    Given Sam has left the company and is inactive
    When Dana tries to start a conversation that includes Sam
    Then no conversation is created
    And Dana sees "Unable to Start Conversation. 1 or more members are inactive and cannot receive messages."

Rationale:
A message to someone who can no longer read it looks delivered but never will be.

Needs: server, browser, pwa, macos, ios

### CONV-DIRECT-003: Starting a hidden conversation again brings it back
`req~CONV-DIRECT-003~1`

Starting a People Conversation that already exists but is hidden opens it and puts it
back in your list.

    Given Dana hid her DM with Sam
    When she starts a new DM with Sam
    Then the old one opens
    And it is back in her Conversation List

Rationale:
Starting a conversation means the person wants to see it.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-DIRECT-004: The new message flow opens from compose or the "+" beside PEOPLE
`req~CONV-DIRECT-004~1`

The **New Message Button (compose)** and the "+" beside PEOPLE both open the new message
flow.

    Given a person wants to start a conversation
    When they click the New Message Button (compose) or the "+" beside PEOPLE
    Then the new message flow opens

Rationale:
Starting a conversation should be one tap from wherever the person is looking.

Needs: browser, pwa, macos, ios

### CONV-DIRECT-005: On macOS, File > New opens the new message flow
`req~CONV-DIRECT-005~1`

On macOS, File > New opens the new message flow.

    Given a person is using Connect on macOS
    When they choose File > New
    Then the new message flow opens

Rationale:
Mac users expect New in the File menu to start the main thing an app makes.

Needs: macos

### CONV-DIRECT-006: A Contact Card starts a conversation
`req~CONV-DIRECT-006~1`

A person can start a conversation with someone from their **Contact Card**.

    Given a person opens Ana's Contact Card
    When they choose Direct Message
    Then they are taken to a DM with Ana

Rationale:
People often decide to message someone while looking at who they are.

Needs: browser, pwa, macos, ios

### CONV-DIRECT-007: The PWA icon's quick action starts a new message
`req~CONV-DIRECT-007~1`

The PWA's app icon has a quick action that opens the new message flow.

    Given a person has the Connect PWA installed
    When they press and hold its icon and choose the new message quick action
    Then Connect opens in the new message flow

Rationale:
Sending a message is the most common reason to open Connect.

Needs: pwa

### CONV-DIRECT-008: On Apple, the five most recent DMs show before typing
`req~CONV-DIRECT-008~1`

On Apple, before the person types, the new message flow shows their 5 most recent DMs.

    Given a person opens the new message flow on macOS or iOS
    When they have not typed anything
    Then it shows their 5 most recent DMs

Rationale:
Most new messages go to someone the person talked to recently.

Needs: ccl, macos, ios

### CONV-DIRECT-009: On Web, Recent shows before typing
`req~CONV-DIRECT-009~1`

On Web, before the person types, the new message flow shows a Recent section of at most
5 conversations.

    Given a person opens the new message flow in the Connect Browser or PWA
    When they have not typed anything
    Then it shows Recent, with at most 5 conversations

Rationale:
Most new messages go to someone the person talked to recently.

Needs: browser, pwa

### CONV-DIRECT-010: Typing two characters shows Recent, People, Groups and Rooms
`req~CONV-DIRECT-010~1`

After the person types 2 characters, the new message flow shows matches in four
sections: Recent, People, Groups and Rooms.

    Given a person opens the new message flow
    When they type "an"
    Then matches are shown under Recent, People, Groups and Rooms

Rationale:
Searching starts once there is enough to match on, and sections tell people what kind of thing each result is.

Needs: browser, pwa, macos, ios

### CONV-DIRECT-011: Each section shows 5, and View More shows up to 25
`req~CONV-DIRECT-011~1`

Each section of the new message results shows up to 5 matches. View More shows up to 25.

    Given 40 people match "an"
    When the person looks at the People section
    Then it shows 5
    And View More shows 25

Rationale:
A short list keeps every section visible; View More is there when the person needs to look further.

Needs: browser, pwa, macos, ios

### CONV-DIRECT-012: Inactive users are not offered
`req~CONV-DIRECT-012~1`

Inactive users are left out of the new message flow's results.

    Given Sam is inactive
    When a person searches "Sam" in the new message flow
    Then Sam is not offered

Rationale:
Offering someone who can't receive messages only leads to a failed conversation.

Needs: server, browser, pwa, macos, ios

### CONV-GROUP-001: Anyone in a group conversation can add people
`req~CONV-GROUP-001~1`

Every member of a group conversation can add more people to it.

    Given Dana, Sam and Ana have a group conversation
    When Ana adds Bob
    Then Bob is in it

Rationale:
A group conversation is a group of equals. Nobody owns it.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-GROUP-002: A group conversation holds up to 10 others plus you
`req~CONV-GROUP-002~1`

A group conversation holds at most 10 other people plus the person starting it. Adding
an 11th shows "Conversation Full. For 10+ members please create a room."

    Given a person has picked 10 others for a new group conversation
    When they add an 11th
    Then they see "Conversation Full. For 10+ members please create a room."

Rationale:
Beyond that, it is a group that deserves a Room.

Needs: server, browser, pwa, macos, ios

### CONV-SELF-001: Everyone has a Self Message
`req~CONV-SELF-001~1`

Every person has a **Self Message**, a conversation with only themselves, for notes and
reminders, in their list.

    Given a new person signs in for the first time
    Then their Conversation List includes their Self Message

Rationale:
People use it as a scratch pad, and to send themselves things between devices.

Status: draft

Needs: server, ccl, browser, pwa, macos, ios

### CONV-CREATE-001: The "+" beside ROOMS offers Create a Room and Browse Rooms
`req~CONV-CREATE-001~1`

The "+" beside the ROOMS section header offers Create a Room and Browse Rooms.

    Given a person looks at their Conversation List
    When they click the "+" beside ROOMS
    Then they can choose Create a Room or Browse Rooms

Rationale:
Finding or making a Room starts from the section that lists Rooms.

Needs: browser, pwa, macos, ios

### CONV-CREATE-002: A new Room has a name and is public or private
`req~CONV-CREATE-002~1`

Creating a Room asks for its name and whether it is public or private.

    Given a person chooses Create a Room
    When they enter "Philly Roofing" and choose private
    Then a private Room named "Philly Roofing" is created

Rationale:
The name says what the Room is for, and privacy decides who can find and read it, so both are settled from the start.

Needs: server, browser, pwa, macos, ios

### CONV-CREATE-003: The creator is a Room Admin
`req~CONV-CREATE-003~1`

The person who creates a Room is its **Room Admin**.

    Given Dana creates a Room
    Then Dana is a Room Admin of it

Rationale:
Someone must be responsible for a Room from the moment it exists.

Needs: server, browser, pwa, macos, ios

### CONV-JOIN-001: Joining puts a Room in your list
`req~CONV-JOIN-001~1`

Joining a public Room puts it in the person's **Conversation List**.

    Given a person finds "Philly Roofing" in Browse Rooms
    When they join it
    Then it is in their Conversation List

Rationale:
Joining is how people say they want to follow a conversation.

Needs: ccl, browser, pwa, macos, ios

### CONV-JOIN-002: People added to a conversation are in it straight away
`req~CONV-JOIN-002~1`

A person added to a conversation, by a Room Admin, by **Member filters** or by being
@mentioned, is in it straight away. There is nothing to accept.

    Given a Room Admin adds Sam to a Room
    Then the Room is in Sam's Conversation List
    And Sam can read and post in it

Rationale:
Who belongs in a conversation is decided for the person, by the company or by its admins. Asking them to accept would only leave people out by accident.

Status: draft

Needs: server, ccl, browser, pwa, macos, ios

### CONV-LEAVE-001: People can leave public Rooms only
`req~CONV-LEAVE-001~1`

A person can leave a public Room. They cannot leave a private Room or a People
Conversation. Leaving removes them from the Room; hiding does not.

    Given a person is in a public Room
    When they leave it
    Then they are no longer a member
    And it is gone from their Conversation List and stays gone after a restart

Rationale:
A public Room can be joined again at any time. Who is in a private Room is decided by its admins and Member filters, and a People Conversation is defined by who is in it.

Needs: server, ccl, browser, pwa, macos, ios

### CONV-LEAVE-002: The only admin cannot leave
`req~CONV-LEAVE-002~1`

A Room's only **Room Admin** cannot leave it until they make someone else an admin. They
see "You must appoint another admin before leaving."

    Given Dana is the only Room Admin of a public Room
    When she tries to leave
    Then she sees "You must appoint another admin before leaving."
    And the Room stays in her Conversation List

Rationale:
A Room with no admin can never be managed again.

Needs: server, browser, pwa, macos, ios

### CONV-LEAVE-003: Leave Room is in Room Info
`req~CONV-LEAVE-003~1`

**Room Info** offers Leave Room in public Rooms.

    Given a person is in a public Room
    When they open Room Info
    Then it offers Leave Room
    And in a private Room it does not

Rationale:
Leaving is a decision about the Room, so it lives with the Room's details.

Needs: browser, pwa, macos, ios

### CONV-BROWSE-001: Browse Rooms lists public Rooms and yours
`req~CONV-BROWSE-001~1`

Browse Rooms lists every public Room plus the Rooms the person is in, which are tagged
Joined.

    Given a person is in the private Room "Ops"
    And a public Room "Ops Alerts" exists that they are not in
    When they open Browse Rooms
    Then both are listed
    And "Ops" is tagged Joined

Rationale:
People look for a Room by what it is about, whether or not they are already in it.

Needs: server, ccl, browser, pwa, macos, ios

### CONV-BROWSE-002: Browse Rooms shows member counts and badges
`req~CONV-BROWSE-002~1`

Each Room in Browse Rooms shows its member count, and Rooms the person is in show their
**Notification Badge**.

    Given a person opens Browse Rooms
    Then each Room shows how many members it has
    And a Joined Room with notifying messages shows its Notification Badge

Rationale:
Member count says how active a Room is, and the badge says where the person is already needed.

Needs: browser, pwa, macos, ios

### CONV-BROWSE-003: Browse Rooms can be searched
`req~CONV-BROWSE-003~1`

Browse Rooms has a search that narrows the list of Rooms.

    Given a person opens Browse Rooms
    When they type "roof" in its search
    Then only matching Rooms are listed

Rationale:
There are too many Rooms to find one by scrolling.

Needs: server, browser, pwa, macos, ios

### CONV-BROWSE-004: Browse Rooms sorts A–Z or Z–A
`req~CONV-BROWSE-004~1`

Browse Rooms can be sorted A–Z or Z–A by Room name.

    Given a person opens Browse Rooms
    When they choose Z–A
    Then Rooms are listed by name from Z to A

Rationale:
People look up a Room by name, from whichever end is closer.

Needs: browser, pwa, macos, ios

### CONV-PREVIEW-001: Public Rooms can be read before joining
`req~CONV-PREVIEW-001~1`

Opening a public Room the person is not in shows a read-only Room Preview. They can read
it but cannot post or react until they join.

    Given a person finds a public Room they are not in
    When they open it
    Then they can read its messages
    But cannot post or react until they join

Rationale:
People decide whether to join by seeing what a Room is like.

Needs: ccl, browser, pwa, macos, ios

### CONV-PREVIEW-002: A preview shows who is in the Room
`req~CONV-PREVIEW-002~1`

Before joining, a person can see who is in a public Room and who its Room Admins are.

    Given a person is previewing a public Room
    When they look at its members
    Then they see who is in it, with Room Admins marked

Rationale:
Who is in a Room says a lot about what it is for.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-PREVIEW-003: Room Preview has a Join button
`req~CONV-PREVIEW-003~1`

Room Preview shows a Join button that adds the person to the Room.

    Given a person is previewing a public Room
    When they click Join
    Then they are a member
    And they can post in it

Rationale:
Once a person has seen enough, joining should be one step from where they are.

Needs: server, browser, pwa, macos, ios

### CONV-EDIT-001: Room names are up to 80 characters
`req~CONV-EDIT-001~1`

A Room must have a name, which is not just spaces and is at most 80 characters.

    Given a Room Admin renames a Room to 81 characters
    Then it is refused
    And they are told the limit

Rationale:
Names are read in lists and headers. A long name gets cut off and stops being useful.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-EDIT-002: A Room topic is up to 100 characters
`req~CONV-EDIT-002~1`

A Room's topic is at most 100 characters.

    Given a Room Admin writes a topic of 120 characters
    Then it is refused
    And they are told the limit

Rationale:
A topic is a one-line summary of what the Room is for, shown in the Conversation Header.

Needs: ccl, browser, pwa, macos, ios

### CONV-EDIT-003: Only Room Admins change a Room's settings
`req~CONV-EDIT-003~1`

Only a Room's **Room Admins** can change its name, topic or privacy.

    Given a member who is not a Room Admin
    When they open Room Info
    Then they cannot change the Room's name, topic or privacy

Rationale:
These describe the Room for everyone in it.

Needs: server, browser, pwa, macos, ios

### CONV-EDIT-004: Public to private is one way
`req~CONV-EDIT-004~1`

A public Room can be made private, but a Room made private cannot be made public again.

    Given a private Room
    When a Room Admin looks for a way to make it public
    Then it is not offered

Rationale:
People wrote in a private Room expecting only its members to read it. Making it public would expose that.

Needs: ccl, browser, pwa, macos, ios

### CONV-EDIT-005: A Room is private until known to be public
`req~CONV-EDIT-005~1`

If Connect cannot tell whether a Room is public, it treats it as private.

    Given Connect cannot yet tell whether a Room is public
    Then it is shown as private

Rationale:
Wrongly showing a Room as private is harmless. Wrongly showing it as public could lead people to share it.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### CONV-EDIT-006: Emojis count as two characters in a topic
`req~CONV-EDIT-006~1`

Each emoji in a Room topic counts as 2 characters toward the 100-character limit.

    Given a Room Admin writes a topic of 98 letters
    When they add one emoji
    Then the topic is at the 100-character limit

Rationale:
The limit has to match what the topic takes up, and emojis take more room than a letter.

Needs: ccl, browser, pwa, macos, ios

### CONV-EDIT-007: Making a Room private asks for confirmation
`req~CONV-EDIT-007~1`

Before a Room is made private, the Room Admin is asked "Make room private?" with
"Private rooms cannot be changed back to public." and the buttons "Yes, Make Private" and
"No, Go back".

    Given a Room Admin chooses to make a public Room private
    Then they see "Make room private?"
    And "Private rooms cannot be changed back to public."
    And the buttons "Yes, Make Private" and "No, Go back"

Rationale:
The change cannot be undone, so the person must see the consequence and choose it on purpose.

Needs: browser, pwa, macos, ios

### CONV-EDIT-008: Room Admins on iOS can make a Room a Required Room
`req~CONV-EDIT-008~1`

On iOS, a Room's settings let a **Room Admin** mark it as a **Required Room**, one its
members are expected to stay in.

    Given a Room Admin opens a Room's settings on iOS
    Then they can mark it as a Required Room

Rationale:
Some Rooms carry information everyone in them must keep receiving.

Needs: ios

### CONV-ADD-001: Only Room Admins add people directly
`req~CONV-ADD-001~1`

Only a Room's **Room Admins** can add a person to it by hand. This is true for public
Rooms too.

    Given a person who is not a Room Admin of a Room
    When they try to add someone to it directly
    Then the person is not added
    And a Room Admin of the same Room can add them

Rationale:
Room Admins manage a Room's members. Hand-picked additions are kept to the people responsible for the Room.

Needs: server

### CONV-MENTION-001: @mentioning someone in a public Room adds them
`req~CONV-MENTION-001~1`

When a member of a public Room @mentions a person who is not in it, that person is added
to the Room, whether or not the member is a Room Admin.

    Given Dana is a member of the public Room "Philly Roofing"
    And Sam is not a member
    When Dana sends a message that @mentions Sam
    Then Sam is added to "Philly Roofing"
    And Sam can read the message that mentioned them

Rationale:
A mention is a request for someone's attention. If they cannot see the Room, the mention does nothing and the person who wrote it does not know.

Needs: server

### CONV-MENTION-002: Only a new @mention of a person adds them
`req~CONV-MENTION-002~1`

@mentioning only adds someone in a new message, in a public Room, naming a specific
person who is active.

    Given a public Room and a person who is not in it
    When they are mentioned in an edit, as part of @all, or after they became inactive
    Then they are not added

Rationale:
Edits and @all would add people nobody meant to add, and inactive users must stay out.

Status: draft

Needs: server

### CONV-MENTION-003: People outside a private Room cannot be @mentioned
`req~CONV-MENTION-003~1`

In a private Room, people who are not members cannot be @mentioned.

    Given Sam is not a member of a private Room
    When a member types "@Sam" in it
    Then Sam is not offered as a mention

Rationale:
Private Rooms are only for the people added to them on purpose; a mention must not let someone in.

Needs: server, browser, pwa, macos, ios

### CONV-ARCHIVE-001: Archiving a Room removes it from v3 for everyone
`req~CONV-ARCHIVE-001~1`

An archived Room disappears from v3 for everyone: from Conversation Lists, from Browse
Rooms and from search. Nobody can post in it. Its messages are kept.

    Given a Room with members and message history
    When it is archived
    Then it no longer appears in any member's Conversation List
    And it no longer appears in Browse Rooms
    And searching for it finds nothing
    And nobody can send messages to it
    And its messages are kept

Rationale:
Archiving is how a Room that is no longer needed is put away without losing the record of what was said in it.

Needs: nitro, server

### CONV-ARCHIVE-002: Only Room Admins archive Rooms
`req~CONV-ARCHIVE-002~1`

Only a Room's **Room Admins** and Connect administrators can archive or unarchive it by
hand.

    Given a person who is a member, but not a Room Admin, of a Room
    When they look for a way to archive it
    Then they cannot archive it

Rationale:
Archiving removes the Room for everyone, so it belongs with the people responsible for it.

Status: draft

Needs: nitro, server

### CONV-ARCHIVE-003: Rooms with no messages for six months are archived automatically
`req~CONV-ARCHIVE-003~1`

A Room is archived automatically once nobody has posted a message in it for six months.
People Conversations are never archived automatically.

    Given a Room where the last message was sent more than six months ago
    When a week has passed
    Then the Room has been archived
    But a DM with no messages for six months is left alone

Rationale:
Dormant Rooms clutter Conversation Lists and search. People Conversations are personal history, and people expect them to be there when they come back.

Status: draft

Needs: server

### CONV-ARCHIVE-004: Unarchiving brings a Room back intact
`req~CONV-ARCHIVE-004~1`

Unarchiving a Room brings it back to v3 for everyone, intact.

    Given a Room was archived
    When it is unarchived
    Then it is back in its members' Conversation Lists
    And its messages are all there
    And people can send messages to it

Rationale:
Archiving must be safe to undo; nothing is lost while a Room is put away.

Needs: nitro, server

### CONV-ARCHIVE-005: In Nitro Connect, Rooms are archived from v2
`req~CONV-ARCHIVE-005~1`

In Nitro Connect, Rooms are archived and unarchived in v2's Connect Room Management.

    Given a Room exists in v2 and v3
    When it is archived in v2 Connect Room Management
    Then it disappears from v3 for everyone

Rationale:
v2 is where Power manages Rooms while the Bridge is running, so one action puts a Room away in both.

Needs: nitro, server

### CONV-DELETE-001: Conversations are archived, never deleted
`req~CONV-DELETE-001~1`

Nobody can delete a conversation. Archiving is the only way to put one away.

    Given a person with every Connect permission
    When they want to get rid of a Room
    Then they can archive it
    But they cannot delete it or its history

Rationale:
Deleting a conversation would also delete the record of decisions made in it. Archiving gives the same tidy result and can be undone.

Status: draft

Needs: nitro, server
