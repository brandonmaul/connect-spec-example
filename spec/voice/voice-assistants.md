# Voice assistants

Sending Connect messages by voice, without opening Connect. Today this is Siri on
iPhone. Another voice assistant would add its own rules here, or list its device in
the `Needs` of the rules that already apply.

**Area code:** `VOICE`

**Topics**

| Topic | Covers |
|---|---|
| `SEND` | Sending messages by voice |

### VOICE-SEND-001: Send a message to a conversation by name
`req~VOICE-SEND-001~1`

A user can ask Siri to send a Connect message to a conversation by name.

    Given the user says "Send a Connect message to Roofing Crew"
    When Siri asks for the text and the user confirms
    Then the message is sent to "Roofing Crew"
    And if two conversations match the name, Siri asks which one first

Rationale:
Hands-free sending is the point. Guessing between two conversations would message the wrong audience.

Needs: ios

### VOICE-SEND-002: A message Siri could not send shows in the app
`req~VOICE-SEND-002~1`

If a message sent through Siri fails, it appears in the conversation in Connect as
failed, with Retry. It is not sent again automatically.

    Given the user sends a message through Siri
    When the send fails
    Then the next time they open Connect, the message is in the conversation marked as failed
    And it offers "Retry"

Rationale:
The person believes Siri sent it. Showing the failure where they will look is the only way they find out, and resending without asking could send it twice.

Needs: ios

### VOICE-SEND-003: Siri can start a group conversation
`req~VOICE-SEND-003~1`

A user can ask Siri to send a message to several people who do not yet share a
conversation, which starts one.

    Given the user says "Send a Connect message to Dana and Sam"
    When Dana, Sam and the user have no conversation together
    Then a new conversation with the three of them is created with the message in it

Status: draft

Rationale:
Product to decide whether Siri should create conversations at all, or only send to existing ones.

Needs: ios
