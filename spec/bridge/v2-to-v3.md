# Connect V2 to V3 bridge

Things people do in Connect V2 must show up in Connect V3. V2 is the source of
truth until it is retired.

The opposite direction has its own rules: [V3 to V2 bridge](v3-to-v2.md).

**Area code:** `V2V3`

**Topics**

| Topic | Covers |
|---|---|
| `MSG` | Messages, edits and deletes |
| `REACT` | Reactions |
| `READ` | Read state |
| `DM` | Direct conversations |
| `PUBLIC` | Following public Rooms |
| `AUD` | Audience changes |
| `MENTION` | People added by being mentioned |
| `ARCHIVE` | Archiving and unarchiving |

Design: <figma link> · Runway: <epic link>

### V2V3-MSG-001: Messages sent in V2 appear in V3
`req~V2V3-MSG-001~1`

A message sent in a Connect V2 conversation appears in the matching V3
conversation, from the same person, including attachments.

    Given a conversation exists in both Connect V2 and V3
    When a person sends a message in V2
    Then the message appears in V3 as sent by that person
    And any attachment on it appears too

Rationale:
People switch between versions throughout the day. A message that exists in only one of them looks lost.

Needs: nitro, server

### V2V3-MSG-002: Edits in V2 appear in V3
`req~V2V3-MSG-002~1`

Editing a message in Connect V2 updates the same message in V3.

    Given a message exists in both Connect V2 and V3
    When its author edits it in V2
    Then V3 shows the edited text on the same message

Rationale:
An edit usually fixes something wrong. V3 readers must not keep seeing the version that was corrected.

Needs: nitro, server

### V2V3-MSG-003: Deletes in V2 remove the message in V3
`req~V2V3-MSG-003~1`

Deleting a message in Connect V2 removes it from V3.

    Given a message exists in both Connect V2 and V3
    When it is deleted in V2
    Then it is removed from the V3 conversation

Rationale:
A deleted message is usually one that should never have been sent. It must disappear everywhere.

Needs: nitro, server

### V2V3-REACT-001: Reactions in V2 appear in V3
`req~V2V3-REACT-001~1`

Adding or removing a reaction in Connect V2 does the same in V3. A V2 "like" is a
👍 in V3.

    Given a message exists in both Connect V2 and V3
    When a person likes it in V2
    Then V3 shows a 👍 from that person on the message
    And when they remove the like in V2, the 👍 is removed in V3

Rationale:
Reactions are often the whole reply ("seen it", "agreed"). Losing them loses the answer.

Needs: nitro, server

### V2V3-READ-001: Reading in V2 clears unread in V3
`req~V2V3-READ-001~1`

When a person reads a conversation in Connect V2, it stops showing as unread for
them in V3.

    Given a person has unread messages in a conversation in both versions
    When they read the conversation in V2
    Then V3 no longer shows those messages as unread

Rationale:
Reading something once should be enough. Badges that come back in the other version train people to ignore badges.

Needs: nitro, server

### V2V3-DM-001: A new V2 Direct conversation appears in V3
`req~V2V3-DM-001~1`

Starting a Direct conversation in Connect V2 creates the matching one in V3
for both people.

    Given two people who both use Connect V3
    When one starts a Direct conversation with the other in Connect V2
    Then both see that conversation in Connect V3

Rationale:
A Direct conversation that exists only in V2 is invisible to anyone who has moved to V3.

Needs: nitro, server

### V2V3-PUBLIC-001: Bookmarking a public Room makes you a member in V3
`req~V2V3-PUBLIC-001~1`

In Connect V2 a person follows a public Room by bookmarking it. A bookmark
holder is a member of the matching V3 conversation, and removing the bookmark
removes them.

    Given a public Room exists in both Connect V2 and V3
    When a person bookmarks it in V2
    Then they are a member of the conversation in V3
    And when they remove the bookmark, they leave the conversation in V3

Rationale:
The bookmark is how V2 users say "I follow this conversation". V3 has no bookmarks, so membership carries the same meaning.

Needs: nitro, server

### V2V3-AUD-001: V2 audience changes reach V3
`req~V2V3-AUD-001~1`

When a conversation's audience or individual members change in Connect V2, the
matching V3 conversation reflects the same change.

    Given a conversation exists in both Connect V2 and V3
    When its criteria or individual members change in V2
    Then the matching V3 conversation reflects the same change

Rationale:
Audience membership is defined in V2 until it is retired.

Needs: nitro, server

### V2V3-MENTION-001: A person mentioned in V2 joins the conversation in V3
`req~V2V3-MENTION-001~1`

When a mention in a Connect V2 public Room adds someone to it in V2, they
are also added to the matching V3 conversation.

    Given a public Room exists in both Connect V2 and V3
    And Sam is not a member
    When Dana mentions @Sam in the conversation in V2
    Then Sam is a member of the conversation in both V2 and V3

Rationale:
Otherwise someone who has moved to V3 never sees the message that asked for their attention.

Needs: nitro, server

### V2V3-ARCHIVE-001: Archiving in V2 archives in V3
`req~V2V3-ARCHIVE-001~1`

Archiving or unarchiving a conversation in Connect V2 does the same to the matching
V3 conversation.

    Given a conversation exists in both Connect V2 and V3
    When it is archived in V2
    Then it is archived in V3
    And when it is unarchived in V2, it is unarchived in V3

Rationale:
A conversation that is closed in one version and open in the other splits the conversation.

Needs: nitro, server
