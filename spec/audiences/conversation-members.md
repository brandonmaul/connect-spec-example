# Audiences: who is in a Room

A Room can have member filters (audiences), such as "all Foremen in
Philadelphia": rules by Territory, Department and Title that keep a private room's
membership updated. People who match the member filters are in the Room; people who
stop matching are taken out.

**Area code:** `AUD`

**Topics**

| Topic | Covers |
|---|---|
| `RULE` | What member filters are made of |
| `MEMBER` | People joining and leaving a Room as they start or stop matching its member filters |
| `EDIT` | Who can change member filters, and how |
| `REACH` | How many people member filters cover |
| `REMOVE` | Taking people out of a Room that has member filters |
| `SUMMARY` | How member filters are described in words |

Design: [Create a Room](https://huddle.powerapp.cloud/projects/628) · [Audiences 3.0](https://huddle.powerapp.cloud/projects/854) · [Room Info & Contact Cards](https://huddle.powerapp.cloud/projects/549)

### AUD-RULE-001: Member filters plus people added by name
`req~AUD-RULE-001~1`

A Room's members are everyone its member filters cover, by Territory, Department and
Title, plus people added by name.

    Given a Room with the member filter "Foremen in Philadelphia"
    And Wade added by name
    Then every Foreman in Philadelphia is in the Room
    And so is Wade

Rationale:
Most Rooms follow the org chart, with a few exceptions. Filters handle the first, names the second.

Needs: server

### AUD-RULE-002: How member filters combine
`req~AUD-RULE-002~1`

Within a filter, a person must match every part it sets, and may match any of the
values listed in each part. A person who matches any one filter is in.

    Given filter 1 is "Foremen or Supervisors, in Philadelphia"
    And filter 2 is "anyone in the Nitro department"
    Then a Philadelphia Supervisor is in
    And a Nitro developer in Atlanta is in
    But a Philadelphia Rep is not

Rationale:
"Foremen in Philly, plus the Nitro team" is the ordinary case, and these rules express it without anything more complicated.

Status: draft

Needs: server

### AUD-RULE-003: A filter needs at least one part
`req~AUD-RULE-003~1`

Every member filter sets at least one of Territory, Department or Title. A filter
with only Titles covers those titles everywhere.

    Given a Room Admin creates a filter with only the Title "Foreman"
    Then it covers every Foreman in every territory
    But a filter with nothing set cannot be saved

Rationale:
An empty filter has no clear meaning, and a mistake would put the whole company in the Room.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### AUD-RULE-004: Only Rooms have member filters
`req~AUD-RULE-004~1`

Member filters apply to Rooms only. People Conversations have none, and their
screens offer none.

    Given a person opens the members of a group conversation
    Then there is no member filters section

Rationale:
A People Conversation is defined by who is in it. Member filters would change what it is.

Needs: server, ccl, browser, pwa, macos, ios

### AUD-RULE-005: Member filters can cover the whole company
`req~AUD-RULE-005~1`

A Room's member filters can cover the entire company. The apps show when they do,
but cannot set it.

    Given a Room's member filters cover the entire company
    When a Room Admin views them
    Then they say the Room covers the entire company
    And there is no option to choose it

Rationale:
Choosing the whole company replaces every filter and every person added by name. That is too drastic to be one tap away.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### AUD-RULE-006: Web offers member filters only in private rooms
`req~AUD-RULE-006~1`

On Web, member filters are offered only for private rooms.

    Given a Room Admin opens Room Info for a public room in the Browser
    Then there is no member filters option
    And in a private room there is

Rationale:
Member filters exist to keep a private room's membership updated; anyone can already join a public room.

Needs: browser, pwa

### AUD-MEMBER-001: A person who starts matching is added
`req~AUD-MEMBER-001~1`

A person who starts matching a Room's member filters is added to it automatically.

    Given a Room whose member filter is "Foremen in Philadelphia"
    When a Foreman is reassigned to Philadelphia
    Then they are in the Room without doing anything

Rationale:
The member filters are the source of truth for who is in the Room.

Needs: nitro, nitroid, server

### AUD-MEMBER-002: A person who stops matching is removed
`req~AUD-MEMBER-002~1`

A person who stops matching a Room's member filters is taken out of it, unless they
were added by name.

    Given a Room whose member filter is "Foremen in Philadelphia"
    When a Foreman is reassigned out of Philadelphia
    Then they are no longer in the Room
    Unless they were added to it by name

Rationale:
A Room for one territory must not keep showing its messages to people who have moved on.

Needs: nitro, nitroid, server

### AUD-MEMBER-003: People added by name are kept
`req~AUD-MEMBER-003~1`

A person added to a Room by name stays in it even when they do not match its member
filters.

    Given a person was added to a Room by name
    When they do not match the Room's member filters
    Then they stay in the Room

Rationale:
Open: what happens to people added by name if the member filters are removed entirely?

Status: draft

Needs: server

### AUD-MEMBER-004: Member filter changes take effect within ten minutes
`req~AUD-MEMBER-004~1`

When a change in the directory changes who matches a Room's member filters, the Room
reflects it within ten minutes, including on the busiest days.

    Given it is New Hire Monday and thousands of Rooms need updating
    When a new hire's title and territory are set
    Then within ten minutes they are in every Room whose member filters they now match

Rationale:
A new hire who cannot see their team's Rooms on day one thinks Connect is broken. Open: what is the agreed time limit?

Status: draft

Needs: server

### AUD-EDIT-001: Only Room Admins change member filters
`req~AUD-EDIT-001~1`

Only a Room's Room Admins can change its member filters.

    Given a person who is a member but not a Room Admin of a Room
    When they open Room Info
    Then they cannot change the member filters

Rationale:
Member filters decide who reads the Room. They belong with the people responsible for it.

Needs: server, browser, pwa, macos, ios

### AUD-EDIT-002: Changing the filters keeps people added by name
`req~AUD-EDIT-002~1`

Changing or removing a Room's member filters never removes the people added to it
by name.

    Given Wade was added to a Room by name
    When a Room Admin replaces all its member filters
    Then Wade is still in the Room

Rationale:
People added by name were added on purpose. Editing the filters should not quietly undo that.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### AUD-EDIT-003: The Room keeps at least one admin
`req~AUD-EDIT-003~1`

A member filter change that would leave a Room without a human Room Admin is
refused, and the person is told why.

    Given Dana is the only Room Admin of a Room
    When a member filter change would take Dana out of it
    Then the change is refused
    And Dana is told it would leave the Room with no admin

Rationale:
A Room with no admin can never be managed again.

Status: draft

Needs: server, browser, pwa, macos, ios

### AUD-EDIT-004: Order of Territories, Departments and Titles
`req~AUD-EDIT-004~1`

When building a member filter, Territories are listed in the order their offices
opened, and Departments and Titles A–Z.

    Given a Room Admin adds a Territory to a member filter
    Then the Territory whose office opened first is at the top
    And when they add a Department or Title, those are listed A–Z

Rationale:
Admins think of markets in the order Power opened them, and find departments and titles fastest alphabetically.

Needs: ccl, browser, pwa, macos, ios

### AUD-EDIT-005: Member filter changes in v3 reach v2
`req~AUD-EDIT-005~1`

In Nitro Connect only, a change to a Room's member filters made in v3 is the same in
v2.

    Given a Room exists in both v2 and v3
    When a Room Admin changes its member filters in v3
    Then the same member filters apply in v2

Rationale:
While both versions run, a Room has one set of member filters, wherever it was changed.

Status: draft

Needs: nitro, server

### AUD-EDIT-006: Only Room Admins see member filters
`req~AUD-EDIT-006~1`

Only a Room's Room Admins can see its member filters.

    Given a person who is a member but not a Room Admin of a Room
    When they open Room Info
    Then they cannot see its member filters

Rationale:
Open: should members who are not Room Admins be able to see why the Room includes them?

Status: draft

Needs: server, browser, pwa, macos, ios

### AUD-EDIT-007: Every Territory, Department and Title is offered
`req~AUD-EDIT-007~1`

When building a member filter, the whole company's Territories, Departments and
Titles are listed, not only ones the Room Admin has seen people from.

    Given a Room Admin adds a Territory to a member filter
    Then every Territory in the company is in the list

Rationale:
Leaving any out would make some member filters impossible to build.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### AUD-REACH-001: Member filters show how many people they cover
`req~AUD-REACH-001~1`

Member filters show how many people in the company they cover, in total and for each
filter, including people who do not use Connect.

    Given a Room Admin adds the member filter "Foremen in Philadelphia"
    Then the filter shows how many Foremen there are in Philadelphia

Rationale:
Before saving, a Room Admin needs to know whether they are about to message ten people or a thousand.

Status: draft

Needs: server, browser, pwa, macos, ios

### AUD-REMOVE-001: Room Admins can see why someone is in a Room
`req~AUD-REMOVE-001~1`

For each member, Room Admins can see whether they were added by name, are there
because they match the member filters, or neither is known.

    Given Rita matches the filter "Philadelphia" and Wade was added by name
    When a Room Admin views the Members List
    Then Rita is shown as matching the member filters
    And Wade as added by name

Rationale:
A Room Admin can only remove people added by name. To take out anyone else, they need to know it is the filters they must change.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### AUD-REMOVE-002: Removing someone takes away their place by name
`req~AUD-REMOVE-002~1`

Removing a person from a Room that has member filters takes away their place by
name. If they also match the filters, they stay in the Room.

    Given Rita was added to "Philly Roofing" by name
    And she also matches its filter "Philadelphia"
    When a Room Admin removes her
    Then she is no longer added by name
    But she is still in the Room, because she matches the filter

Rationale:
The member filters decide who belongs. Removing a person undoes only the exception a Room Admin made for them, never the filters.

Status: draft

Needs: server

### AUD-REMOVE-003: People there only by the filters are not removed one by one
`req~AUD-REMOVE-003~1`

A person who is in a Room only because they match its member filters cannot be
removed on their own. To take them out, a Room Admin changes the filters.

    Given Sam is in "Philly Roofing" only because he matches the filter "Philadelphia"
    When a Room Admin wants Sam out of the Room
    Then they cannot remove Sam on his own
    And they change the member filters instead

Rationale:
If one person could be removed while still matching the filters, the filters would no longer say who is in the Room.

Status: draft

Needs: server, browser, pwa, macos, ios

### AUD-SUMMARY-001: Member filters read as one sentence
`req~AUD-SUMMARY-001~1`

Member filters are summarised as "{Titles or employees} in {Departments} from
{Territories}", saying "employees" when no Title is set.

    Given a member filter for Foremen in Production from Philadelphia
    Then it reads "Foremen in Production from Philadelphia"
    And a filter with no Title reads "employees in Production from Philadelphia"

Rationale:
One plain sentence lets a Room Admin check at a glance who the Room is for.

Needs: browser, pwa, macos, ios
