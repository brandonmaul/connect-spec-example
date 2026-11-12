# People

Finding people at the company, seeing who they are and whether they are around: the
Contact Card, the Corporate Directory, Presence, the people in each Conversation and
Room Admins.

**Area code:** `PEOPLE`

**Topics**

| Topic | Covers |
|---|---|
| `DIRECTORY` | Browsing and searching the Corporate Directory |
| `PROFILE` | What a person's Contact Card shows |
| `STATUS` | Presence: whether someone is online |
| `MEMBERS` | The members of a Conversation |
| `ADMIN` | Room Admins |
| `INACTIVE` | How people who are no longer active look |

Design: [Room Info & Contact Cards](https://huddle.powerapp.cloud/projects/549) · [Corporate Directory](https://huddle.powerapp.cloud/projects/501)

### PEOPLE-DIRECTORY-001: The Corporate Directory lists current employees
`req~PEOPLE-DIRECTORY-001~1`

The Corporate Directory lists everyone currently working at the company, and no one
who has left.

    Given Sam left the company last month
    When a person browses the Corporate Directory
    Then Sam is not listed

Rationale:
The Corporate Directory is for finding people to talk to now.

Status: draft

Needs: ccl, browser, pwa, ios

### PEOPLE-DIRECTORY-002: People are grouped under letter headers by last name
`req~PEOPLE-DIRECTORY-002~1`

The People tab of the Corporate Directory lists people by last name, under sticky
letter headers. The exact order is set by the Corporate Directory row of
[Sorting and naming](../sorting/sorting-and-naming.md).

    Given Alex Cruz and Grace Hopper
    When a person opens the People tab
    Then "Cruz, Alex" is under the letter header "C"
    And the "C" header stays at the top while its people scroll past

Rationale:
That is how people expect to look someone up, and the headers show where they are in a long list.

Needs: ccl, browser, pwa, ios

### PEOPLE-DIRECTORY-003: Search by name, filter by department and territory
`req~PEOPLE-DIRECTORY-003~1`

People in the Corporate Directory are searched by any part of their name, and can be
filtered by department and territory together.

    Given a person searches "ann" with the territory filter "Philadelphia"
    Then they see everyone in Philadelphia whose name contains "ann"

Rationale:
People often half-remember a name but know where someone works. Open: the Corporate
Directory has People, Departments and Territories tabs; is there also a name search,
and can department and territory be combined?

Status: draft

Needs: ccl, browser, pwa, ios

### PEOPLE-DIRECTORY-004: Bots people talk to can be added to conversations
`req~PEOPLE-DIRECTORY-004~1`

When adding people to a Conversation, bots people talk to, like the Nitro App bot,
can be picked alongside employees.

    Given a Room Admin adds people to a Room
    When they search "Nitro App"
    Then the Nitro App bot can be picked

Rationale:
Some bots are useful members of a Conversation.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### PEOPLE-DIRECTORY-005: New people and leavers show up promptly
`req~PEOPLE-DIRECTORY-005~1`

The Corporate Directory reflects people joining and leaving the company soon after
it happens, and can be refreshed on demand.

    Given a new hire started today
    When a colleague pulls to refresh the Corporate Directory
    Then the new hire is listed

Rationale:
On a new hire's first day, people need to find them.

Status: draft

Needs: ccl, browser, pwa, ios

### PEOPLE-DIRECTORY-006: The Corporate Directory opens from the User Menu
`req~PEOPLE-DIRECTORY-006~1`

The Corporate Directory is opened from the User Menu.

    Given a person opens the User Menu
    When they choose the Corporate Directory
    Then the Corporate Directory opens

Rationale:
The User Menu is where a person's tools that are not about one Conversation live.

Needs: browser, pwa, ios

### PEOPLE-DIRECTORY-007: The Corporate Directory has People, Departments and Territories tabs
`req~PEOPLE-DIRECTORY-007~1`

The Corporate Directory has three tabs: People, Departments and Territories.

    Given a person opens the Corporate Directory
    Then they see the tabs People, Departments and Territories

Rationale:
People look each other up by name, or by where in the company they work.

Needs: browser, pwa, ios

### PEOPLE-DIRECTORY-008: Corporate Directory on macOS
`req~PEOPLE-DIRECTORY-008~1`

The Corporate Directory is also available on macOS, the same as on iOS and Web.

    Given a person uses Connect on a Mac
    When they open the User Menu
    Then they can open the Corporate Directory

Rationale:
Open: should macOS have the Corporate Directory?

Status: draft

Needs: macos

### PEOPLE-PROFILE-001: A Contact Card shows only what the viewer may see
`req~PEOPLE-PROFILE-001~1`

A Contact Card shows only the details the viewer's permissions allow.

    Given a viewer without permission to see phone numbers
    When they open a colleague's Contact Card
    Then it shows the colleague's title and department
    But no phone number

Rationale:
Contact details are personal. Connect must not show more than the company's own systems would.

Needs: server, browser, pwa, macos, ios

### PEOPLE-PROFILE-002: Directory photos come first
`req~PEOPLE-PROFILE-002~1`

A person's photo comes from the company directory.

    Given a person has a photo in the company directory
    Then Connect shows that photo for them everywhere

Rationale:
One photo per person, kept where the company keeps it.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### PEOPLE-PROFILE-003: Any avatar opens a Contact Card
`req~PEOPLE-PROFILE-003~1`

Clicking or tapping any person's avatar opens their Contact Card.

    Given a person sees Dana's avatar beside one of her messages
    When they click it
    Then Dana's Contact Card opens

Rationale:
The avatar is the natural place to ask "who is this?".

Needs: browser, pwa, macos, ios

### PEOPLE-PROFILE-004: What a Contact Card shows
`req~PEOPLE-PROFILE-004~1`

A Contact Card shows the person's avatar, Presence, name, title, territory,
department, emails, office extension, phones and home address, as far as the
viewer's permissions allow.

    Given a viewer allowed to see all of Dana's details
    When they open Dana's Contact Card
    Then it shows her avatar, Presence, name, title, territory, department, emails, office extension, phones and home address

Rationale:
The Contact Card answers who someone is and how to reach them without leaving Connect.

Needs: server, browser, pwa, macos, ios

### PEOPLE-PROFILE-005: Territory shows in Nitro Connect only
`req~PEOPLE-PROFILE-005~1`

In Nitro Connect only, a Contact Card shows the person's territory. Tempo Connect
Contact Cards have no territory.

    Given a person using Tempo Connect
    When they open a colleague's Contact Card
    Then it shows no territory

Rationale:
Territories are how Power organises its people; Stream does not use them.

Needs: browser, pwa, macos, ios

### PEOPLE-PROFILE-006: Contact details open the matching app
`req~PEOPLE-PROFILE-006~1`

On a Contact Card, a phone number opens the phone app, an email opens the mail app,
and the home address opens the maps app.

    Given a person opens Dana's Contact Card
    When they tap her phone number
    Then the phone app opens ready to call her

Rationale:
People open a Contact Card to get in touch, so each detail should start that.

Needs: browser, pwa, macos, ios

### PEOPLE-PROFILE-007: On Web, Contact Card details can be copied
`req~PEOPLE-PROFILE-007~1`

On Web, each contact detail on a Contact Card has a copy icon.

    Given a person opens Dana's Contact Card in Connect Browser
    When they click the copy icon beside her email
    Then her email is copied

Rationale:
On a computer, details are often pasted into another app rather than opened.

Needs: browser, pwa

### PEOPLE-PROFILE-008: On Web, an office extension opens the softphone
`req~PEOPLE-PROFILE-008~1`

On Web, except in Safari, clicking an office extension on a Contact Card calls it in
the company softphone app.

    Given a person opens Dana's Contact Card in Connect Browser on Chrome
    When they click her office extension
    Then the softphone app opens calling that extension

Rationale:
Office extensions are dialled from the softphone, not a mobile phone.

Needs: browser, pwa

### PEOPLE-PROFILE-009: The Direct Message button stays in view
`req~PEOPLE-PROFILE-009~1`

A Contact Card has a Direct Message button that stays in view while the card
scrolls.

    Given a person opens a long Contact Card
    When they scroll to the bottom of it
    Then the Direct Message button is still visible

Rationale:
Messaging the person is the most common reason to open their Contact Card.

Needs: browser, pwa, macos, ios

### PEOPLE-STATUS-001: Green Presence means online with Connect open
`req~PEOPLE-STATUS-001~1`

A person's avatar shows a green Presence dot while they are online with Connect
open.

    Given Ana has Connect open
    Then her avatar shows a green Presence dot

Rationale:
Knowing whether someone is around sets how soon to expect a reply.

Needs: server, ccl, browser, pwa, macos, ios

### PEOPLE-STATUS-002: DMs show the other person's Presence live
`req~PEOPLE-STATUS-002~1`

A DM shows the other person's Presence, and updates it live.

    Given a person's DM with Ana
    When Ana comes online
    Then the DM shows her as online

Rationale:
That is where people decide whether to message someone now.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### PEOPLE-STATUS-003: A brief drop does not show someone offline
`req~PEOPLE-STATUS-003~1`

A person whose connection drops for a moment does not appear to go offline.

    Given Ana's phone loses signal for ten seconds
    Then the others keep seeing her as online

Rationale:
Presence that flickers is worse than none.

Status: draft

Needs: server, ccl, browser, pwa, macos, ios

### PEOPLE-STATUS-004: Gray Presence means logged out or asleep
`req~PEOPLE-STATUS-004~1`

A person's avatar shows a gray Presence dot when they are logged out or their device
is asleep.

    Given Ana's computer goes to sleep
    Then her avatar shows a gray Presence dot

Rationale:
Gray tells others not to expect a quick reply.

Needs: server, ccl, browser, pwa, macos, ios

### PEOPLE-STATUS-005: Nitro bots always show blue Presence
`req~PEOPLE-STATUS-005~1`

A Nitro bot's avatar always shows a blue Presence dot, because a bot is always
online.

    Given a person sees the Nitro App bot's avatar
    Then it shows a blue Presence dot

Rationale:
Bots never sleep, and blue sets them apart from people.

Needs: server, ccl, browser, pwa, macos, ios

### PEOPLE-MEMBERS-001: The members list updates live
`req~PEOPLE-MEMBERS-001~1`

A Conversation's Members List updates as people join, leave or become Room Admins.

    Given a person is looking at a Room's Members List
    When a Room Admin adds Bob
    Then Bob appears in the list

Rationale:
The list must show who can read the Conversation now.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### PEOPLE-MEMBERS-002: Members show who they are
`req~PEOPLE-MEMBERS-002~1`

Each member shows their name, photo, title, department and territory, and whether
they are a Room Admin, a bot or no longer at the company.

    Given a Conversation includes someone who has left the company
    When a person looks at its members
    Then that person is shown as no longer at the company

Rationale:
Knowing who is reading helps people decide what to say.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### PEOPLE-MEMBERS-003: The members list never shows as empty while loading
`req~PEOPLE-MEMBERS-003~1`

While a Conversation's members are still loading, the Members List shows that it is
loading, never an empty list.

    Given a person opens a large Room's Members List
    When its members are still loading
    Then a loading state is shown

Rationale:
An empty Members List looks like nobody is there.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### PEOPLE-MEMBERS-004: Removed members are told why
`req~PEOPLE-MEMBERS-004~1`

A person removed from a Room by a Room Admin is told they were removed by an admin.

    Given a Room Admin removes Sam from a Room
    Then Sam is told an admin removed him

Rationale:
A Conversation vanishing without explanation looks like a fault.

Status: draft

Needs: server, browser, pwa, macos, ios

### PEOPLE-MEMBERS-005: Members are listed A–Z by display name
`req~PEOPLE-MEMBERS-005~1`

A Conversation's members are listed A–Z by display name, in the same order in every
client, as set by the Members List row of
[Sorting and naming](../sorting/sorting-and-naming.md).

    Given a Room with 40 members
    When a person opens its Members List on their iPhone and in Connect Browser
    Then the members are A–Z by display name on both

Rationale:
Same behavior as SORT-LIST-003, which owns it. Kept for the record.
One predictable order lets people find someone and agree on what they see.

Status: rejected

Needs: ccl, browser, pwa, macos, ios

### PEOPLE-ADMIN-001: The creator of a Room is its Room Admin
`req~PEOPLE-ADMIN-001~1`

Whoever creates a Room is its Room Admin. Room Admins can promote other members to
Room Admin.

    Given Dana creates a Room
    Then she is its Room Admin
    And she can make Sam a Room Admin too

Rationale:
Someone has to be able to manage a Room from the moment it exists, and share that job.

Needs: server, ccl, browser, pwa, macos, ios

### PEOPLE-ADMIN-002: Room Admins demote members, never leaving no admin
`req~PEOPLE-ADMIN-002~1`

A Room Admin can make another Room Admin a regular member, but never leave the Room
without a human Room Admin.

    Given Dana and Sam are the Room Admins
    When Dana makes Sam a regular member
    Then Sam is a regular member
    But Dana cannot then make herself a regular member

Rationale:
A Room with no admin can never be managed again.

Status: draft

Needs: server

### PEOPLE-ADMIN-003: Bot admins cannot be changed by people
`req~PEOPLE-ADMIN-003~1`

People cannot demote or remove a bot that is a Room Admin, and the apps do not offer
it.

    Given a bot is a Room Admin
    When a Room Admin views the Room's members
    Then there is no option to demote or remove the bot

Rationale:
Some bots run the Room, for example keeping its Member filters applied. Removing them would break it.

Status: draft

Needs: server, browser, pwa, macos, ios

### PEOPLE-INACTIVE-001: Inactive people look inactive
`req~PEOPLE-INACTIVE-001~1`

A person who is inactive is shown in grayscale with an "Inactive" badge.

    Given Sam is inactive
    When a person opens Sam's Contact Card
    Then Sam's avatar is in grayscale
    And an "Inactive" badge is shown

Rationale:
People need to see straight away that this person cannot be reached in Connect.

Needs: server, browser, pwa, macos, ios

### PEOPLE-INACTIVE-002: Inactive people have no Direct Message button
`req~PEOPLE-INACTIVE-002~1`

An inactive person's Contact Card has no Direct Message button.

    Given Sam is inactive
    When a person opens Sam's Contact Card
    Then there is no Direct Message button

Rationale:
Inactive people cannot receive messages, so offering to message them would fail.

Needs: server, browser, pwa, macos, ios
