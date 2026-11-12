# v2 to v3 bridge

Things people do in v2 must show up in v3, through the Bridge. v2 is the source of
truth until it is retired. The Bridge exists in Nitro Connect only: Stream never had
v2, so Tempo Connect has no Bridge.

The opposite direction has its own rules: [v3 to v2 bridge](v3-to-v2.md).

**Area code:** `V2V3`

**Topics**

| Topic | Covers |
|---|---|
| `MSG` | Messages, GIFs, attachments, edits and deletes |
| `REACT` | Reactions |
| `READ` | Read state |
| `DM` | People Conversations |
| `PUBLIC` | Following public Rooms |
| `AUD` | Member filter and membership changes |
| `MENTION` | People added by being mentioned |
| `ARCHIVE` | Archiving and unarchiving |
| `TIMING` | How quickly changes cross the Bridge |
| `ADMIN` | Room Admins |
| `ROOM` | Creating Rooms and changing their details |

### V2V3-MSG-001: Messages sent in v2 appear in v3
`req~V2V3-MSG-001~1`

A message sent in a v2 conversation appears in the matching v3 conversation, from
the same person, including attachments.

    Given a conversation exists in both v2 and v3
    When a person sends a message in v2
    Then the message appears in v3 as sent by that person
    And any attachment on it appears too

Rationale:
People switch between versions throughout the day. A message that exists in only one of them looks lost.

Needs: nitro, server

### V2V3-MSG-002: Edits in v2 appear in v3
`req~V2V3-MSG-002~1`

Editing a message in v2 updates the same message in v3.

    Given a message exists in both v2 and v3
    When its author edits it in v2
    Then v3 shows the edited text on the same message

Rationale:
An edit usually fixes something wrong. v3 readers must not keep seeing the version that was corrected.

Needs: nitro, server

### V2V3-MSG-003: Deletes in v2 remove the message in v3
`req~V2V3-MSG-003~1`

Deleting a message in v2 removes it from v3.

    Given a message exists in both v2 and v3
    When it is deleted in v2
    Then it is removed from the v3 conversation

Rationale:
A deleted message is usually one that should never have been sent. It must disappear everywhere.

Needs: nitro, server

### V2V3-MSG-004: GIFs sent in v2 appear in v3
`req~V2V3-MSG-004~1`

A GIF sent in a v2 conversation appears in the matching v3 conversation, from the
same person.

    Given a conversation exists in both v2 and v3
    When a person sends a GIF in v2
    Then the GIF appears in v3 as sent by that person

Rationale:
A GIF is often the whole reply. Losing it loses the answer.

Needs: nitro, server

### V2V3-MSG-005: Mentions in v2 stay mentions in v3
`req~V2V3-MSG-005~1`

An @mention in a message sent in v2 is an @mention in v3, so the mentioned person is
notified and highlighted the same way.

    Given a conversation exists in both v2 and v3
    When Dana mentions @Sam in a message in v2
    Then the message in v3 mentions @Sam

Rationale:
A mention asks for someone's attention. If it turns into plain text in v3, the person on v3 never knows they were asked.

Needs: nitro, server

### V2V3-REACT-001: Reactions in v2 appear in v3
`req~V2V3-REACT-001~1`

Adding or removing a reaction in v2 does the same in v3.

    Given a message exists in both v2 and v3
    When a person likes it in v2
    Then v3 shows a like from that person on the message
    And when they remove the like in v2, it is removed in v3

Rationale:
Reactions are often the whole reply ("seen it", "agreed"). Losing them loses the answer.

Needs: nitro, server

### V2V3-READ-001: Reading in v2 clears unread in v3
`req~V2V3-READ-001~1`

When a person reads a conversation in v2, it stops showing as unread for them in v3.

    Given a person has unread messages in a conversation in both versions
    When they read the conversation in v2
    Then v3 no longer shows the conversation in bold (unread)

Rationale:
Reading something once should be enough. Unread state that comes back in the other version trains people to ignore it.

Needs: nitro, server

### V2V3-DM-001: A new v2 People Conversation appears in v3
`req~V2V3-DM-001~1`

Starting a DM or group conversation in v2 creates the matching People Conversation in
v3 for everyone in it.

    Given two people who both use v3
    When one starts a DM with the other in v2
    Then both see that DM in v3

Rationale:
A People Conversation that exists only in v2 is invisible to anyone who has moved to v3.

Needs: nitro, server

### V2V3-PUBLIC-001: Bookmarking a public room in v2 makes you a member in v3
`req~V2V3-PUBLIC-001~1`

In v2 a person follows a public room by bookmarking it. A bookmark holder is a
member of the matching v3 Room, and removing the bookmark removes them.

    Given a public room exists in both v2 and v3
    When a person bookmarks it in v2
    Then they are a member of the Room in v3
    And when they remove the bookmark, they leave the Room in v3

Rationale:
The bookmark is how v2 users say "I follow this room". v3 has no bookmarks, so membership carries the same meaning.

Status: draft

Needs: nitro, server

### V2V3-AUD-001: v2 member filter and membership changes reach v3
`req~V2V3-AUD-001~1`

When a Room's member filters or individual members change in v2, the matching v3
Room reflects the same change.

    Given a Room exists in both v2 and v3
    When its member filters or individual members change in v2
    Then the matching v3 Room reflects the same change

Rationale:
Room membership is defined in v2 until it is retired.

Needs: nitro, server

### V2V3-MENTION-001: A person mentioned in a v2 public room joins it in v3
`req~V2V3-MENTION-001~1`

When an @mention in a v2 public room adds someone to it in v2, they are also added
to the matching v3 Room.

    Given a public room exists in both v2 and v3
    And Sam is not a member
    When Dana mentions @Sam in the room in v2
    Then Sam is a member of the room in both v2 and v3

Rationale:
Otherwise someone who has moved to v3 never sees the message that asked for their attention.

Needs: nitro, server

### V2V3-ARCHIVE-001: Archiving in v2 removes the Room from v3
`req~V2V3-ARCHIVE-001~1`

When a room is archived in v2 Connect Room Management, it disappears from v3 for
everyone.

    Given a Room exists in both v2 and v3
    When it is archived in v2 Connect Room Management
    Then it disappears from v3 for every member

Rationale:
A room closed in one version and still open in the other splits the conversation.

Needs: nitro, server

### V2V3-ARCHIVE-002: Unarchiving in v2 brings the Room back intact
`req~V2V3-ARCHIVE-002~1`

When an archived room is unarchived in v2, it returns to v3 intact, with its
messages and members.

    Given a Room was archived in v2 and disappeared from v3
    When it is unarchived in v2
    Then it is back in v3 for its members
    And its message history is as it was

Rationale:
Archiving must be safely reversible, or nobody would dare archive a room.

Needs: nitro, server

### V2V3-TIMING-001: v2 changes reach v3 within about 30 seconds
`req~V2V3-TIMING-001~1`

Something done in v2 appears in v3 within about 15–30 seconds.

    Given a conversation exists in both v2 and v3
    When a person sends a message in v2
    Then it appears in v3 within about 15–30 seconds

Rationale:
People on v3 must be able to follow a conversation with people on v2 without long gaps.

Needs: nitro, server

### V2V3-ADMIN-001: Room Admins set in v2 are Room Admins in v3
`req~V2V3-ADMIN-001~1`

When someone is made a Room Admin of a room in v2, they are a Room Admin of the
matching v3 Room.

    Given a Room exists in both v2 and v3
    When Dana is made an admin of it in v2
    Then Dana is a Room Admin of it in v3

Rationale:
A room has one set of admins, whichever version they use to manage it.

Needs: nitro, server

### V2V3-ROOM-001: Room changes in v2 appear in v3
`req~V2V3-ROOM-001~1`

Changes to a room's details in v2, such as its name or topic, appear in the matching
v3 Room.

    Given a Room exists in both v2 and v3
    When its name is changed in v2
    Then v3 shows the new name

Rationale:
A room with different names in each version looks like two different rooms.

Needs: nitro, server

### V2V3-ROOM-002: A room created in v2 arrives in v3 with no Room Admin
`req~V2V3-ROOM-002~1`

A room created in v2 appears in v3 with no Room Admin.

    Given Dana creates a room in v2
    When it appears in v3
    Then it has no Room Admin in v3, not even Dana

Rationale:
v2 rooms are managed in v2 Connect Room Management, so v3 does not assume who should manage them.

Needs: nitro, server

### V2V3-ROOM-003: Broadcasters set in v2 decide who posts in v3
`req~V2V3-ROOM-003~1`

The broadcasters set for a room in v2 Connect Room Management are the only people who
can post in the matching v3 Broadcast Room.

    Given a room's broadcasters are set in v2 Connect Room Management
    When a member who is not a broadcaster opens it in v3
    Then they see no Message Composer

Rationale:
A Broadcast Room has one set of broadcasters, set in one place.

Needs: nitro, server
