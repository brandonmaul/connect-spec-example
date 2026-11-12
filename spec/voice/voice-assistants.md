# Voice assistants

Sending Connect messages by voice, without opening Connect. Today this is the Siri
intent on macOS and iOS. Another voice assistant would add its own rules here, or list
its client in the `Needs` of the rules that already apply.

**Area code:** `VOICE`

**Topics**

| Topic | Covers |
|---|---|
| `SEND` | Sending messages by voice |

### VOICE-SEND-001: Siri sends a message to a Room
`req~VOICE-SEND-001~1`

A person can ask Siri to "Send a message using Nitro Connect" to a Room.

    Given a person says "Send a message using Nitro Connect" and picks the Room "Roofing Crew"
    When Siri asks for the text and the person confirms
    Then the message is sent to "Roofing Crew"

Rationale:
Hands-free sending lets people message a team without stopping what they are doing.

Needs: macos, ios

### VOICE-SEND-002: A message Siri could not send shows in the app
`req~VOICE-SEND-002~1`

If a message sent through Siri fails, it appears in the Conversation in Connect as
failed, with Retry. It is not sent again automatically.

    Given a person sends a message through Siri
    When the send fails
    Then the next time they open Connect, the message is in the Conversation View marked as failed
    And it offers "Retry"

Rationale:
The person believes Siri sent it. Showing the failure where they will look is the only way they find out, and resending without asking could send it twice.

Status: draft

Needs: macos, ios

### VOICE-SEND-003: Siri can start a group conversation
`req~VOICE-SEND-003~1`

A person can ask Siri to send a message to several people who do not yet share a
group conversation, which starts one.

    Given a person asks Siri to send a message using Nitro Connect to Dana and Sam
    When Dana, Sam and the person have no group conversation together
    Then a new group conversation with the three of them is created with the message in it

Rationale:
Open: should Siri create group conversations, or only send to existing ones?

Status: draft

Needs: macos, ios

### VOICE-SEND-004: Siri sends a message to a DM
`req~VOICE-SEND-004~1`

A person can ask Siri to "Send a message using Nitro Connect" to a DM.

    Given a person says "Send a message using Nitro Connect" and picks Dana
    When Siri asks for the text and the person confirms
    Then the message is sent in their DM with Dana

Rationale:
Messaging one colleague is the most common thing people do by voice.

Needs: macos, ios

### VOICE-SEND-005: Siri sends a message to a group conversation
`req~VOICE-SEND-005~1`

A person can ask Siri to "Send a message using Nitro Connect" to a group
conversation.

    Given a person has a group conversation with Dana and Sam
    When they ask Siri to send a message using Nitro Connect to Dana and Sam and confirm the text
    Then the message is sent in that group conversation

Rationale:
Small teams talk in group conversations, so voice has to reach them too.

Needs: macos, ios

### VOICE-SEND-006: Group conversations need each member picked again
`req~VOICE-SEND-006~1`

To send to a group conversation with Siri, the person picks each of its members
again; the group conversation cannot be picked by name.

    Given a person has a group conversation with Dana and Sam
    When they ask Siri to send it a message using Nitro Connect
    Then Siri has them pick Dana and Sam
    And the message is sent in that group conversation

Rationale:
A group conversation's name is its members' names, so Siri finds it by its members.

Needs: macos, ios

### VOICE-SEND-007: Siri asks which Conversation when two match
`req~VOICE-SEND-007~1`

If two Conversations match the name a person gave Siri, Siri asks which one before
sending.

    Given a person has two Rooms named "Roofing Crew"
    When they ask Siri to send a message using Nitro Connect to "Roofing Crew"
    Then Siri asks which "Roofing Crew" before sending

Rationale:
Guessing between two Conversations would message the wrong audience.

Status: draft

Needs: macos, ios
