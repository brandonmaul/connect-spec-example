# Connect V3 to V2 bridge

Things people do in Connect V3 must show up in Connect V2, so colleagues who are
still on V2 see the same conversation.

The opposite direction has its own rules: [V2 to V3 bridge](v2-to-v3.md).

**Area code:** `V3V2`

**Topics**

| Topic | Covers |
|---|---|
| `MSG` | Messages, edits and deletes |
| `REACT` | Reactions |
| `READ` | Read state |
| `ARCHIVE` | Archiving and unarchiving |

Design: <figma link> · Runway: <epic link>

### V3V2-MSG-001: Messages sent in V3 appear in V2
`req~V3V2-MSG-001~1`

A message sent in a Connect V3 conversation appears in the matching V2
conversation, from the same person. Text, GIFs and attachments all carry over.

    Given a conversation exists in both Connect V3 and V2
    When a person sends a message, a GIF or an attachment in V3
    Then it appears in V2 as sent by that person

Rationale:
People moving to V3 must still reach everyone on V2. Otherwise moving to V3 means dropping out of the conversation.

Needs: nitro, server

### V3V2-MSG-002: Edits in V3 appear in V2
`req~V3V2-MSG-002~1`

Editing a message in Connect V3 updates the same message in V2.

    Given a message exists in both Connect V3 and V2
    When its author edits it in V3
    Then V2 shows the edited text on the same message

Rationale:
An edit usually fixes something wrong. V2 readers must not keep seeing the version that was corrected.

Needs: nitro, server

### V3V2-MSG-003: Deletes in V3 remove the message in V2
`req~V3V2-MSG-003~1`

Deleting a message in Connect V3 removes it from V2.

    Given a message exists in both Connect V3 and V2
    When it is deleted in V3
    Then it is removed from the V2 conversation

Rationale:
A deleted message is usually one that should never have been sent. It must disappear everywhere.

Needs: nitro, server

### V3V2-MSG-004: Bridged messages appear once
`req~V3V2-MSG-004~1`

A message that started in V3 and was copied to V2 is not copied back into V3.

    Given a person sends a message in V3
    When it is copied to V2
    Then the V3 conversation still shows it exactly once

Rationale:
Copying it back would show every message twice, or loop forever.

Needs: nitro, server

### V3V2-REACT-001: Reactions in V3 appear in V2
`req~V3V2-REACT-001~1`

Adding or removing a reaction in Connect V3 does the same in V2. A 👍 in V3 is a
"like" in V2.

    Given a message exists in both Connect V3 and V2
    When a person reacts with 👍 in V3
    Then V2 shows a like from that person on the message
    And when they remove the 👍 in V3, the like is removed in V2

Rationale:
Reactions are often the whole reply ("seen it", "agreed"). Losing them loses the answer.

Needs: nitro, server

### V3V2-READ-001: Reading in V3 clears unread in V2
`req~V3V2-READ-001~1`

When a person reads a conversation in Connect V3, it stops showing as unread for
them in V2.

    Given a person has unread messages in a conversation in both versions
    When they read the conversation in V3
    Then V2 no longer shows those messages as unread

Rationale:
Reading something once should be enough. Badges that come back in the other version train people to ignore badges.

Needs: nitro, server

### V3V2-ARCHIVE-001: Archiving in V3 archives in V2
`req~V3V2-ARCHIVE-001~1`

Archiving or unarchiving a conversation in Connect V3 does the same in V2,
including conversations archived automatically for having no messages.

    Given a conversation exists in both Connect V3 and V2
    When it is archived in V3, by an admin or automatically
    Then it is archived in V2

Rationale:
A conversation that is closed in one version and open in the other splits the conversation.

Needs: nitro, server
