# People

Finding people at the company, seeing who they are and whether they are around, and the people in each conversation.

**Area code:** `PEOPLE`

**Topics**

| Topic | Covers |
|---|---|
| `DIRECTORY` | Browsing and searching the people at the company |
| `PROFILE` | What a person's profile shows |
| `STATUS` | Whether someone is online |
| `MEMBERS` | The members of a conversation |
| `ADMIN` | Conversation admins |

Design: <figma link> · Runway: <epic link>

### PEOPLE-DIRECTORY-001: The directory lists current employees
`req~PEOPLE-DIRECTORY-001~1`

The company directory lists everyone currently working at the company, and no
one who has left.

    Given Sam left the company last month
    When a person browses the directory
    Then Sam is not listed

Rationale:
The directory is for finding people to talk to now.

Needs: ccl

### PEOPLE-DIRECTORY-002: The directory is in phone-book order
`req~PEOPLE-DIRECTORY-002~1`

The directory is sorted by last name, then by full name.

    Given Ann Lee, Bob Lee and Grace Hopper
    Then they are listed Hopper, Ann Lee, Bob Lee

Rationale:
That is how people expect to look someone up.

Needs: ccl

### PEOPLE-DIRECTORY-003: Search by name, filter by department and territory
`req~PEOPLE-DIRECTORY-003~1`

People are searched by any part of their name, and can be filtered by department
and territory together.

    Given a person searches "ann" with the territory filter "Philadelphia"
    Then they see everyone in Philadelphia whose name contains "ann"

Rationale:
People often half-remember a name but know where someone works.

Needs: ccl, ios, macos, web

### PEOPLE-DIRECTORY-004: Bots people talk to can be added to conversations
`req~PEOPLE-DIRECTORY-004~1`

When adding people to a conversation, bots people talk to, like the Nitro App bot,
can be picked alongside employees.

    Given an admin adds people to a conversation
    When they search "Nitro App"
    Then the Nitro App bot can be picked

Rationale:
Some bots are useful members of a conversation.

Needs: ccl

### PEOPLE-DIRECTORY-005: New people and leavers show up promptly
`req~PEOPLE-DIRECTORY-005~1`

The directory reflects people joining and leaving the company soon after it
happens, and can be refreshed on demand.

    Given a new hire started today
    When a colleague pulls to refresh the directory
    Then the new hire is listed

Rationale:
On a new hire's first day, people need to find them.

Needs: ccl

### PEOPLE-PROFILE-001: A profile shows what the viewer may see
`req~PEOPLE-PROFILE-001~1`

A person's profile shows their title, department and territory, and their contact
details only if the viewer is allowed to see them.

    Given a viewer without permission to see phone numbers
    When they open a colleague's profile
    Then it shows the colleague's title and department
    But no phone number

Rationale:
Contact details are personal. Connect must not show more than the directory would.

Needs: server, ios, macos, web

### PEOPLE-PROFILE-002: Directory photos come first
`req~PEOPLE-PROFILE-002~1`

A person's photo comes from the company directory.

    Given a person has a photo in the company directory
    Then Connect shows that photo for them everywhere

Rationale:
One photo per person, kept where the company keeps it.

Needs: ccl

### PEOPLE-STATUS-001: People show as online, away or offline
`req~PEOPLE-STATUS-001~1`

Each person shows as online, away or offline. Someone whose status is not known
shows as offline.

    Given Ana has Connect open
    Then she shows as online
    And when she leaves it in the background, as away

Rationale:
Knowing whether someone is around sets how soon to expect a reply.

Needs: ccl, server

### PEOPLE-STATUS-002: Direct conversations show the other person's status
`req~PEOPLE-STATUS-002~1`

A Direct conversation shows the other person's status, and updates it live.

    Given a person's Direct conversation with Ana
    When Ana comes online
    Then the conversation shows her as online

Rationale:
That is where people decide whether to message someone now.

Needs: ccl, ios, macos, web

### PEOPLE-STATUS-003: A brief drop does not show someone offline
`req~PEOPLE-STATUS-003~1`

A person whose connection drops for a moment does not appear to go offline.

    Given Ana's phone loses signal for ten seconds
    Then the others keep seeing her as online

Rationale:
Status that flickers is worse than none.

Needs: ccl, server

### PEOPLE-MEMBERS-001: The members list updates live
`req~PEOPLE-MEMBERS-001~1`

A conversation's members list updates as people join, leave or become admins.

    Given a person is looking at a conversation's members
    When an admin adds Bob
    Then Bob appears in the list

Rationale:
The list must show who can read the conversation now.

Needs: ccl

### PEOPLE-MEMBERS-002: Members show who they are
`req~PEOPLE-MEMBERS-002~1`

Each member shows their name, photo, title, department and territory, and whether
they are an admin, a bot or no longer at the company.

    Given a conversation includes someone who has left the company
    When a person looks at its members
    Then that person is shown as no longer at the company

Rationale:
Knowing who is reading helps people decide what to say.

Needs: ccl, ios, macos, web

### PEOPLE-MEMBERS-003: The members list never shows as empty while loading
`req~PEOPLE-MEMBERS-003~1`

While a conversation's members are still loading, the list shows that it is loading,
never an empty list.

    Given a person opens a large conversation's members
    When they are still loading
    Then a loading state is shown

Rationale:
An empty members list looks like nobody is there.

Needs: ccl

### PEOPLE-MEMBERS-004: Removed members are told why
`req~PEOPLE-MEMBERS-004~1`

A person removed from a conversation by an admin is told they were removed by an
admin.

    Given an admin removes Sam from a conversation
    Then Sam is told an admin removed him

Rationale:
A conversation vanishing without explanation looks like a fault.

Needs: server, ios, macos, web

### PEOPLE-MEMBERS-005: The order members are listed in
`req~PEOPLE-MEMBERS-005~1`

A conversation's members are listed in an order that is the same in every app.

    Given a Room with 40 members
    When a person opens its members on their iPhone and on the web
    Then the members are in the same order on both

Status: draft

Rationale:
Product to decide the order, for example admins first, then alphabetical by last name.

Needs: ccl, ios, macos, web

### PEOPLE-ADMIN-001: Members are admins or regular members
`req~PEOPLE-ADMIN-001~1`

Each member of a conversation is either an admin or a regular member. Whoever
creates a conversation is an admin.

    Given Dana creates a conversation
    Then she is its admin

Rationale:
Two roles are easy to understand. Anything finer has not been needed.

Needs: ccl, server

### PEOPLE-ADMIN-002: Admins promote and demote members
`req~PEOPLE-ADMIN-002~1`

An admin can make a member an admin, or an admin a regular member, but never leave
the conversation without a human admin.

    Given Dana and Sam are the admins
    When Dana makes Sam a regular member
    Then Sam is a regular member
    But Dana cannot then make herself a regular member

Rationale:
A conversation with no admin can never be managed again.

Needs: server

### PEOPLE-ADMIN-003: Bot admins cannot be changed by people
`req~PEOPLE-ADMIN-003~1`

People cannot demote or remove a bot that is an admin of a conversation, and the
apps do not offer it.

    Given a bot is an admin of a conversation
    When an admin views its members
    Then there is no option to demote or remove the bot

Rationale:
Some bots run the conversation, for example keeping its audience up to date. Removing them would break it.

Needs: server, ios, macos, web
