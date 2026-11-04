# Audiences: who is in a conversation

A Room can have an audience, such as "all Foremen in Philadelphia". People
who match the audience are in the conversation; people who stop matching are taken
out.

**Area code:** `AUD`

**Topics**

| Topic | Covers |
|---|---|
| `RULE` | What an audience is made of |
| `MEMBER` | People joining and leaving a conversation as they start or stop matching its audience |
| `EDIT` | Who can change an audience, and how |
| `REACH` | How many people an audience covers |
| `REMOVE` | Taking people out of a conversation that has an audience |

Design: <figma link> · Runway: <epic link>

### AUD-RULE-001: An audience is rules plus people added by name
`req~AUD-RULE-001~1`

An audience is made of rules about the company directory, by territory, department
and title, plus people added by name. Everyone either covers is in the conversation.

    Given an audience with the rule "Foremen in Philadelphia"
    And Wade added by name
    Then every Foreman in Philadelphia is in the conversation
    And so is Wade

Rationale:
Most conversations follow the org chart, with a few exceptions. Rules handle the first, names the second.

Needs: server

### AUD-RULE-002: How audience rules combine
`req~AUD-RULE-002~1`

Within a rule, a person must match every part it sets, and may match any of the
values listed in each part. A person who matches any one rule is in.

    Given rule 1 is "Foremen or Supervisors, in Philadelphia"
    And rule 2 is "anyone in the Nitro department"
    Then a Philadelphia Supervisor is in
    And a Nitro developer in Atlanta is in
    But a Philadelphia Rep is not

Rationale:
"Foremen in Philly, plus the Nitro team" is the ordinary case, and these rules express it without anything more complicated.

Needs: server

### AUD-RULE-003: A rule needs at least one part
`req~AUD-RULE-003~1`

Every audience rule sets at least one of territory, department or title. A rule
with only titles covers those titles everywhere.

    Given an admin creates a rule with only the title "Foreman"
    Then it covers every Foreman in every territory
    But a rule with nothing set cannot be saved

Rationale:
An empty rule has no clear meaning, and a mistake would put the whole company in the conversation.

Needs: ccl

### AUD-RULE-004: Only Rooms have audiences
`req~AUD-RULE-004~1`

Audiences apply to Rooms only. Direct and Group conversations have no audience, and
their screens offer none.

    Given a person opens the details of a Direct or Group conversation
    Then there is no audience section

Rationale:
A Direct or Group conversation is defined by who is in it. An audience would change what it is.

Needs: ccl, server, ios, macos, web

### AUD-RULE-005: An audience can be the whole company
`req~AUD-RULE-005~1`

An audience can cover the entire company. The apps show when it does, but cannot
set it.

    Given a conversation's audience is the entire company
    When an admin views its audience
    Then it says the audience is the entire company
    And there is no option to choose it

Rationale:
Choosing the whole company replaces every rule and every person added by name. That is too drastic to be one tap away.

Needs: ccl, ios, macos, web

### AUD-MEMBER-001: A person who starts matching is added
`req~AUD-MEMBER-001~1`

A person who starts matching a conversation's audience is added to it
automatically.

    Given a conversation whose audience is "Foremen in Philadelphia"
    When a Foreman is reassigned to Philadelphia
    Then they are in the conversation without doing anything

Rationale:
The audience is the source of truth for who is in the conversation.

Needs: nitro, nitroid, server

### AUD-MEMBER-002: A person who stops matching is removed
`req~AUD-MEMBER-002~1`

A person who stops matching a conversation's audience is taken out of it, unless
they were added individually.

    Given a conversation whose audience is "Foremen in Philadelphia"
    When a Foreman is reassigned out of Philadelphia
    Then they are no longer in the conversation
    Unless they were added to it individually

Rationale:
A conversation for one territory must not keep showing its messages to people who have moved on.

Needs: nitro, nitroid, server

### AUD-MEMBER-003: Individually added people are kept
`req~AUD-MEMBER-003~1`

A person added to a conversation individually stays in it even when they do not
match its audience.

    Given a person was added to a conversation individually
    When they do not match the conversation's audience
    Then they stay in the conversation

Status: draft

Rationale:
Product still to decide what happens to them if the audience is removed entirely.

Needs: server

### AUD-MEMBER-004: Audience changes take effect within ten minutes
`req~AUD-MEMBER-004~1`

When a change in the directory changes who matches a conversation's audience, the
conversation reflects it within ten minutes, including on the busiest days.

    Given it is New Hire Monday and thousands of conversations need updating
    When a new hire's title and territory are set
    Then within ten minutes they are in every conversation whose audience they now match

Status: draft

Rationale:
A new hire who cannot see their team's conversations on day one thinks Connect is broken. Product to agree the number.

Needs: server

### AUD-EDIT-001: Only conversation admins see and change the audience
`req~AUD-EDIT-001~1`

Only the conversation's admins who are in it can see or change its audience.

    Given a person who is a member but not an admin of a conversation
    When they open its details
    Then they cannot see or change the audience

Rationale:
The audience decides who reads the conversation. It belongs with the people responsible for it.

Needs: server

### AUD-EDIT-002: Changing the rules keeps people added by name
`req~AUD-EDIT-002~1`

Changing or removing an audience's rules never removes the people added to it by
name.

    Given Wade was added to an audience by name
    When an admin replaces all its rules
    Then Wade is still in the conversation

Rationale:
People added by name were added on purpose. Editing the rules should not quietly undo that.

Needs: ccl

### AUD-EDIT-003: The conversation keeps at least one admin
`req~AUD-EDIT-003~1`

A change that would leave a conversation without a human admin is refused, and the
person is told why.

    Given Dana is the only admin of a conversation
    When an audience change would take Dana out of it
    Then the change is refused
    And Dana is told it would leave the conversation with no admin

Rationale:
A conversation with no admin can never be managed again.

Needs: server, ios, macos, web

### AUD-EDIT-004: Choosing territories, departments and titles
`req~AUD-EDIT-004~1`

When building a rule, the whole company's territories, departments and titles are
listed: territories oldest market first, departments and titles alphabetically.

    Given an admin adds a territory to a rule
    Then Philadelphia is at the top of the list
    And every territory in the company is there, not only ones the admin has seen people from

Rationale:
Admins think of markets in the order Power opened them. Leaving any out would make some audiences impossible to build.

Needs: ccl

### AUD-EDIT-005: Audience changes in V3 reach Connect V2
`req~AUD-EDIT-005~1`

A change to a conversation's audience made in Connect V3 is the same in Connect V2.

    Given a conversation exists in both versions
    When an admin changes its audience in V3
    Then the same audience applies in V2

Rationale:
While both versions run, a conversation has one audience, wherever it was changed.

Needs: server, nitro

### AUD-REACH-001: An audience shows how many people it covers
`req~AUD-REACH-001~1`

An audience shows how many people in the company it covers, in total and for each
rule, including people who do not use Connect.

    Given an admin adds the rule "Foremen in Philadelphia"
    Then the rule shows how many Foremen there are in Philadelphia

Rationale:
Before saving, an admin needs to know whether they are about to message ten people or a thousand.

Needs: server, ios, macos, web

### AUD-REMOVE-001: Admins can see why someone is in a conversation
`req~AUD-REMOVE-001~1`

For each member, admins can see whether they were added by name, are there because
they match the audience, or neither is known.

    Given Rita matches the rule "Philadelphia" and Wade was added by name
    When an admin views the members
    Then Rita is shown as matching the audience
    And Wade as added by name

Rationale:
An admin can only remove people added by name. To take out anyone else, they need to know it is the rules they must change.

Needs: ccl, ios, macos, web

### AUD-REMOVE-002: Removing someone takes away their place by name
`req~AUD-REMOVE-002~1`

Removing a person from a Room that has an audience takes away their place by name.
If they also match the audience's rules, they stay in the Room.

    Given Rita was added to "Philly Roofing" by name
    And she also matches its rule "Philadelphia"
    When an admin removes her
    Then she is no longer added by name
    But she is still in the Room, because she matches the rule

Rationale:
The audience decides who belongs. Removing a person undoes only the exception an admin made for them, never the rules.

Needs: server

### AUD-REMOVE-003: People there only by the rules are not removed one by one
`req~AUD-REMOVE-003~1`

A person who is in a Room only because they match its audience cannot be removed on
their own. To take them out, an admin changes the audience.

    Given Sam is in "Philly Roofing" only because he matches the rule "Philadelphia"
    When an admin wants Sam out of the Room
    Then they cannot remove Sam on his own
    And they change the audience's rules instead

Rationale:
If one person could be removed while still matching the rules, the audience would no longer say who is in the Room.

Needs: server, ios, macos, web
