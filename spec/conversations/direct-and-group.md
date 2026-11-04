# Direct and Group conversations

Conversations between specific people, rather than Rooms set up for a team, place
or topic: Direct conversations between two people, Group conversations between
three or more, and each person's Self-DM Room.

**Area code:** `DM`

**Topics**

| Topic | Covers |
|---|---|
| `START` | Starting a Direct or Group conversation |
| `SIZE` | How many people a Group conversation can have |
| `SELF` | A person's Self-DM Room |

Design: <figma link> · Runway: <epic link>

### DM-START-001: There is one Direct conversation per pair of people
`req~DM-START-001~1`

Starting a Direct conversation with someone you already have one with opens the
existing conversation. It does not create a second one.

    Given Dana and Sam already have a Direct conversation
    When Dana starts a new Direct conversation with Sam
    Then Dana is taken to the conversation they already have

Rationale:
Two conversations with the same person split the history, and people lose track of where something was said.

Needs: ccl, server

### DM-START-002: No new conversations with switched-off accounts
`req~DM-START-002~1`

A Direct or Group conversation cannot be started with someone whose account has
been switched off.

    Given Sam has left the company and their account is switched off
    When Dana tries to start a Direct conversation with Sam
    Then no conversation is created

Rationale:
A message to someone who can no longer read it looks delivered but never will be.

Comment:
What Dana is shown is not specified yet.

Needs: server

### DM-START-003: Starting a hidden conversation again brings it back
`req~DM-START-003~1`

Starting a Direct or Group conversation that already exists but is hidden opens it
and puts it back in your list.

    Given Dana hid her Direct conversation with Sam
    When she starts a new Direct conversation with Sam
    Then the old one opens
    And it is back in her list

Rationale:
Starting a conversation means the person wants to see it.

Needs: ccl

### DM-START-004: Anyone in a Group conversation can add people
`req~DM-START-004~1`

Every member of a Group conversation can add more people to it.

    Given Dana, Sam and Ana have a Group conversation
    When Ana adds Bob
    Then Bob is in it

Rationale:
A Group conversation is a group of equals. Nobody owns it.

Needs: ccl

### DM-SIZE-001: A Group conversation has up to 11 people
`req~DM-SIZE-001~1`

A Group conversation has at most 11 people, including the person who starts it.

    Given a person picks 11 others for a new Group conversation
    Then it cannot be created
    And they are told the limit is 10 others

Rationale:
Beyond that, it is a group that deserves a Room with an audience.

Needs: server, ios, macos, web

### DM-SELF-001: Everyone has a Self-DM Room
`req~DM-SELF-001~1`

Every person has a Self-DM Room, a conversation with only themselves, for notes and
reminders, in their list.

    Given a new person signs in for the first time
    Then their list includes their Self-DM Room

Rationale:
People use it as a scratch pad, and to send themselves things between devices.

Needs: server, ccl
