# v3 to v2 bridge

Things people do in v3 must show up in v2, through the Bridge, so colleagues who are
still on v2 see the same conversation. The Bridge exists in Nitro Connect only:
Stream never had v2, so Tempo Connect has no Bridge.

The opposite direction has its own rules: [v2 to v3 bridge](v2-to-v3.md).

**Area code:** `V3V2`

**Topics**

| Topic | Covers |
|---|---|
| `MSG` | Messages, GIFs, attachments, mentions, edits and deletes |
| `REACT` | Reactions |
| `READ` | Read state |
| `ARCHIVE` | Archiving and unarchiving |
| `TIMING` | How quickly changes cross the Bridge |
| `ADMIN` | Room Admins |
| `ROOM` | Changing Room details |
| `MEMBER` | People joining and leaving Rooms |
| `SORT` | The order of the Conversation List |

### V3V2-MSG-001: Messages sent in v3 appear in v2
`req~V3V2-MSG-001~1`

A message sent in a v3 conversation appears in the matching v2 conversation, from
the same person. Text, GIFs and attachments all carry over.

    Given a conversation exists in both v3 and v2
    When a person sends a message, a GIF or an attachment in v3
    Then it appears in v2 as sent by that person

Rationale:
People moving to v3 must still reach everyone on v2. Otherwise moving to v3 means dropping out of the conversation.

Needs: nitro, server

### V3V2-MSG-002: Edits in v3 appear in v2
`req~V3V2-MSG-002~1`

Editing a message in v3 updates the same message in v2.

    Given a message exists in both v3 and v2
    When its author edits it in v3
    Then v2 shows the edited text on the same message

Rationale:
An edit usually fixes something wrong. v2 readers must not keep seeing the version that was corrected.

Needs: nitro, server

### V3V2-MSG-003: Deletes in v3 remove the message in v2
`req~V3V2-MSG-003~1`

Deleting a message in v3 removes it from v2.

    Given a message exists in both v3 and v2
    When it is deleted in v3
    Then it is removed from the v2 conversation

Rationale:
A deleted message is usually one that should never have been sent. It must disappear everywhere.

Needs: nitro, server

### V3V2-MSG-004: Bridged messages appear once
`req~V3V2-MSG-004~1`

A message that started in v3 and was copied to v2 is not copied back into v3.

    Given a person sends a message in v3
    When it is copied to v2
    Then the v3 conversation still shows it exactly once

Rationale:
Copying it back would show every message twice, or loop forever.

Status: draft

Needs: nitro, server

### V3V2-MSG-005: Mentions in v3 stay mentions in v2
`req~V3V2-MSG-005~1`

An @mention in a message sent in v3 is a mention in v2, so the mentioned person on v2
is notified.

    Given a conversation exists in both v3 and v2
    When Dana mentions @Sam in a message in v3
    Then the message in v2 mentions Sam

Rationale:
A mention asks for someone's attention. If it turns into plain text in v2, the person on v2 never knows they were asked.

Needs: nitro, server

### V3V2-REACT-001: Reactions in v3 appear in v2
`req~V3V2-REACT-001~1`

Adding or removing a reaction in v3 does the same in v2.

    Given a message exists in both v3 and v2
    When a person likes it in v3
    Then v2 shows a like from that person on the message
    And when they remove the like in v3, it is removed in v2

Rationale:
Reactions are often the whole reply ("seen it", "agreed"). Losing them loses the answer.

Needs: nitro, server

### V3V2-READ-001: Reading in v3 clears unread in v2
`req~V3V2-READ-001~1`

When a person reads a conversation in v3, it stops showing as unread for them in v2.

    Given a person has unread messages in a conversation in both versions
    When they read the conversation in v3
    Then v2 no longer shows those messages as unread

Rationale:
Reading something once should be enough. Unread state that comes back in the other version trains people to ignore it.

Needs: nitro, server

### V3V2-ARCHIVE-001: Archiving in v3 archives in v2
`req~V3V2-ARCHIVE-001~1`

Archiving or unarchiving a Room in v3 does the same in v2, including Rooms archived
automatically for having no messages.

    Given a Room exists in both v3 and v2
    When it is archived in v3, by a Room Admin or automatically
    Then it is archived in v2

Rationale:
A Room that is closed in one version and open in the other splits the conversation.

Status: draft

Needs: nitro, server

### V3V2-TIMING-001: v3 changes reach v2 near-instantly
`req~V3V2-TIMING-001~1`

Something done in v3 appears in v2 near-instantly.

    Given a conversation exists in both v3 and v2
    When a person sends a message in v3
    Then it appears in v2 within a moment

Rationale:
People on v2 must be able to follow a conversation with people on v3 as it happens.

Needs: nitro, server

### V3V2-ADMIN-001: Room Admins set in v3 are admins in v2
`req~V3V2-ADMIN-001~1`

When someone is made a Room Admin in v3, they are an admin of the matching v2 room.

    Given a Room exists in both v3 and v2
    When Dana is made a Room Admin in v3
    Then Dana is an admin of the room in v2

Rationale:
A room has one set of admins, whichever version they use to manage it.

Needs: nitro, server

### V3V2-ROOM-001: Room changes in v3 appear in v2
`req~V3V2-ROOM-001~1`

Changes a Room Admin makes to a Room's details in v3, such as its name or topic,
appear in the matching v2 room.

    Given a Room exists in both v3 and v2
    When a Room Admin changes its topic in v3
    Then v2 shows the new topic

Rationale:
A room with different details in each version looks like two different rooms.

Needs: nitro, server

### V3V2-MEMBER-001: Membership changes in v3 appear in v2
`req~V3V2-MEMBER-001~1`

When someone is added to, removed from or leaves a Room in v3, the same happens in
the matching v2 room.

    Given a Room exists in both v3 and v2
    When a Room Admin adds Sam to it in v3
    Then Sam is a member of the room in v2

Rationale:
A room has one set of members, whichever version people use.

Needs: nitro, server

### V3V2-SORT-001: Self-Managed order is bridged to v2
`req~V3V2-SORT-001~1`

The Self-Managed order a person drags their Conversation List into in v3 is the
order of their conversations in v2.

    Given a person uses the Self-Managed sort in v3
    When they drag "Philly Roofing" to the top of ROOMS
    Then "Philly Roofing" is at the top of their rooms in v2

Rationale:
People who use both versions arrange their list once and expect it to hold everywhere.

Needs: nitro, server
