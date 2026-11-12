# Membership: who gets Connect

Who has a Connect account, where that comes from, and what happens when people
join, change, leave and come back. Which Rooms a person is in is covered
separately in [Audiences](../audiences/conversation-members.md).

Connect does not keep its own list of people. It follows the company directory:

- **Power (Nitro Connect):** people and roles live in Nitro. Nitro ID, the company
  login, passes them to Connect.
- **Stream Innovations (Tempo Connect):** people live in Tempo ID, which passes them
  to Connect the same way.

**Area code:** `MEMBERSHIP`

**Topics**

| Topic | Covers |
|---|---|
| `SOURCE` | Where Connect accounts come from |
| `ACCESS` | Who is allowed to use Connect |
| `PROFILE` | Keeping names and details up to date |
| `LEAVE` | What happens when someone loses access |
| `RETURN` | What happens when someone comes back |

### MEMBERSHIP-SOURCE-001: Accounts come from the company directory
`req~MEMBERSHIP-SOURCE-001~1`

Every Connect account is created from the company directory, which Nitro ID or
Tempo ID passes to Connect. Nobody signs up for Connect, and nobody creates accounts
by hand.

    Given a person is added to the company directory with Connect access
    When the directory change reaches Connect
    Then they have a Connect account
    And they did not have to sign up or be added by anyone

Rationale:
The directory already knows who works here. A second list would drift from it, and people would end up with access they should not have, or none at all.

Needs: nitroid, server

### MEMBERSHIP-ACCESS-001: In Nitro Connect, a person's Nitro role decides who has Connect
`req~MEMBERSHIP-ACCESS-001~1`

In Nitro Connect, a person has Connect if, and only if, their role in Nitro includes
the Connect access permission. Being given or losing that permission takes effect
the same day, without waiting for a release.

    Given a Power employee does not have Connect
    When they are given a role in Nitro that includes Connect access
    Then they have a Connect account later that day

Rationale:
Access is decided in one place, Nitro roles, by the people who already manage roles. Open: access is moving to the Nitro ID "Connect Access" group (MEMBERSHIP-ACCESS-008); does the Nitro role still decide, or the group?

Comment:
If Connect cannot tell who has access, it lets nobody in rather than everybody. Nitro system administrators always have Connect.

Status: draft

Needs: nitro, nitroid, server

### MEMBERSHIP-ACCESS-002: In Tempo Connect, everyone active in Tempo ID has Connect
`req~MEMBERSHIP-ACCESS-002~1`

In Tempo Connect, every active person in Tempo ID who belongs to at least one group
has Connect.

    Given a person is active in Tempo ID and belongs to a group
    When Tempo ID passes them to Connect
    Then they have a Connect account

Rationale:
Stream Innovations has no separate Connect access group. Everyone who works there is expected to be on Connect.

Status: draft

Needs: server

### MEMBERSHIP-ACCESS-003: One permission covers both v2 and v3
`req~MEMBERSHIP-ACCESS-003~1`

In Nitro Connect, the same Connect access permission decides access to v2 and v3.
A person cannot have one without the other.

    Given a Power employee's role includes Connect access
    When they open v2 in Nitro, or a v3 app
    Then both let them in
    And when the permission is removed from their role, neither does

Rationale:
While both versions run, people move between them all day. Access that differs between them would cut people off from half of their conversations, with no clear reason why.

Status: draft

Needs: nitro, nitroid, server

### MEMBERSHIP-ACCESS-004: Losing access locks v2 straight away
`req~MEMBERSHIP-ACCESS-004~1`

v2 checks a person's access every time they use it. When their role loses the
Connect access permission, v2 stops working for them on their next action.

    Given a person is using v2
    When their role in Nitro loses Connect access
    Then their next action in v2, in the v2 Browser or the v2 apps, is refused

Rationale:
Someone whose access was removed must not keep reading company conversations, even for a few hours.

Comment:
v3 follows later the same day (MEMBERSHIP-ACCESS-001, MEMBERSHIP-LEAVE-001).

Status: draft

Needs: nitro

### MEMBERSHIP-ACCESS-005: Access given to a role applies to the roles beneath it
`req~MEMBERSHIP-ACCESS-005~1`

Giving or removing Connect access on a role in Nitro applies to everyone in that role
and in every role beneath it, unless a role beneath sets its own Connect access.

    Given the "Sales" role has roles beneath it, such as "Sales Rep"
    When Connect access is given to "Sales"
    Then everyone active in "Sales" and "Sales Rep" has Connect

Rationale:
Roles are managed as a tree. Whoever switches Connect on for a department expects it to reach the whole department, without editing every role in it.

Status: draft

Needs: nitro

### MEMBERSHIP-ACCESS-006: Power employees have Nitro Connect
`req~MEMBERSHIP-ACCESS-006~1`

Connect is for all employees of Power Home Remodeling, who use Nitro Connect (and,
until it is retired, v2).

    Given a person is a Power Home Remodeling employee
    Then they can use Nitro Connect

Rationale:
Connect is Power's internal messaging tool, so every employee needs to be reachable on it.

Needs: nitro, nitroid, server

### MEMBERSHIP-ACCESS-007: Stream Innovations employees have Tempo Connect only
`req~MEMBERSHIP-ACCESS-007~1`

Connect is for all employees of Stream Innovations, who use Tempo Connect. They
have no v2.

    Given a person is a Stream Innovations employee
    Then they can use Tempo Connect
    And they have no v2 access

Rationale:
Stream never had v2, so Tempo Connect is their only Connect.

Needs: server

### MEMBERSHIP-ACCESS-008: In Nitro Connect, the "Connect Access" group decides who has Connect
`req~MEMBERSHIP-ACCESS-008~1`

In Nitro Connect, a person has Connect if, and only if, they are in the Nitro ID
"Connect Access" group.

    Given a Power employee is added to the Nitro ID "Connect Access" group
    When the change reaches Connect
    Then they have a Connect account
    And when they are removed from the group, they lose it

Rationale:
Open: access is moving to the "Connect Access" group but this is not yet confirmed. Does it replace the Nitro role permission (MEMBERSHIP-ACCESS-001)?

Status: draft

Needs: nitroid, server

### MEMBERSHIP-PROFILE-001: Name changes in the directory show in Connect
`req~MEMBERSHIP-PROFILE-001~1`

When a person's name changes in the company directory, Connect shows the new name.

    Given a person's name is changed in the company directory
    When the change reaches Connect
    Then Connect shows their new name everywhere their name appears

Rationale:
People are found and recognised by name. A stale name makes them hard to find and can be hurtful.

Status: draft

Needs: nitroid, server

### MEMBERSHIP-LEAVE-001: Losing access switches the account off
`req~MEMBERSHIP-LEAVE-001~1`

When a person leaves the company or loses Connect access, their account is switched
off. They are signed out, cannot sign back in, and are removed from their
conversations.

    Given a person is using Connect
    When they leave the company or lose Connect access
    Then they can no longer use Connect on any device
    And they are no longer a member of any conversation

Rationale:
People who no longer work here, or are no longer allowed on Connect, must not keep reading company conversations.

Status: draft

Needs: nitroid, server

### MEMBERSHIP-LEAVE-002: A departed person's messages stay
`req~MEMBERSHIP-LEAVE-002~1`

When a person's account is switched off, the messages they already sent stay visible
to everyone else in those conversations.

    Given a person sent messages in a conversation
    When their account is switched off
    Then the other members still see those messages, under that person's name

Rationale:
Their messages are part of the record of decisions and work. Removing them would break the conversation for everyone who stayed.

Status: draft

Needs: server

### MEMBERSHIP-RETURN-001: Coming back restores the same account
`req~MEMBERSHIP-RETURN-001~1`

When a person whose account was switched off gets Connect access again, for example
a rehire, their original account is switched back on. They do not get a new one.

    Given a person's account was switched off when they left
    When they are rehired with Connect access
    Then they sign in to the same account they had before
    And their past messages are still theirs

Rationale:
A second account for the same person splits their history and confuses everyone looking them up.

Status: draft

Needs: nitroid, server

### MEMBERSHIP-RETURN-002: Coming back restores their conversations
`req~MEMBERSHIP-RETURN-002~1`

When a returning person's account is switched back on, they are back in the
conversations they are entitled to.

    Given a returning person's account has been switched back on
    When they sign in
    Then they are a member of every Room their member filters entitle them to, and their People Conversations

Rationale:
Open: should they get back only what their current role entitles them to, or also the private Rooms and People Conversations they had before?

Status: draft

Needs: server
