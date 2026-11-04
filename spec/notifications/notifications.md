# Notifications

Which messages notify a person, and what happens when they act on a notification. Unread badges in the conversation list are covered in [Conversations](../conversations/conversations.md).

**Area code:** `NOTIFY`

**Topics**

| Topic | Covers |
|---|---|
| `LEVEL` | What each conversation notifies a person about |
| `TEXT` | What a notification says |
| `TAP` | Opening Connect from a notification |
| `REPLY` | Replying or reacting straight from a notification |
| `DEVICE` | Turning notifications on and off for a device |

Design: <figma link> · Runway: <epic link>

### NOTIFY-LEVEL-001: Each conversation has a notification level
`req~NOTIFY-LEVEL-001~1`

For each conversation, a person chooses to be notified about every message, about
mentions of everyone and of them, only about mentions of them, or about nothing.

    Given a person is in a busy conversation
    When they set it to "Only mentions of me"
    Then they are notified when someone mentions them
    But not when someone mentions everyone, or posts without mentioning them

Rationale:
People are in many conversations that matter to different degrees. One setting for all of them would mean too many notifications or too few.

Needs: server, ios, macos, web

### NOTIFY-LEVEL-002: Direct and Group conversations notify on every message
`req~NOTIFY-LEVEL-002~1`

Until a person changes it, a Direct or Group conversation notifies them about every
message, and a Room notifies them about mentions of everyone and of them.

    Given a person has just been added to a Room and to a Direct conversation
    When a message without a mention arrives in each
    Then only the Direct conversation notifies them

Rationale:
A Direct or Group conversation is written to you. Most Rooms are shared by many people, and notifying everyone of everything would bury what matters.

Needs: server

### NOTIFY-LEVEL-003: A person mentioned twice is notified once
`req~NOTIFY-LEVEL-003~1`

If a message mentions the same person more than once, they get one notification.

    Given a message mentions @Sam twice
    When it is sent
    Then Sam gets one notification

Rationale:
Repeating a name is emphasis, not a request to buzz someone twice.

Needs: ccl

### NOTIFY-TEXT-001: A notification shows who wrote what, and where
`req~NOTIFY-TEXT-001~1`

A notification's title is the sender's name, followed by the Room's name for a Room.
Its text is the message, up to its first 1,024 characters.

    Given Dana Ruiz writes "Crew is on site" in the Room "Philly Roofing"
    Then the notification's title is "Dana Ruiz in Philly Roofing"
    And its text is "Crew is on site"
    But from a Direct or Group conversation, the title is only "Dana Ruiz"

Rationale:
People decide from the notification alone whether to open Connect now.

Needs: server

### NOTIFY-TEXT-002: A message with no text still notifies clearly
`req~NOTIFY-TEXT-002~1`

When a message has no text to show, its notification says who wrote in which Room,
or that the sender is connecting with the person.

    Given Dana sends a message with no text in the Room "Philly Roofing"
    Then the notification says "Dana Ruiz wrote a message in Philly Roofing"
    And from a Direct conversation it says "Dana Ruiz is Connecting with you"
    And if even the sender is unknown, it says "Someone is connecting with you..."

Rationale:
An empty notification looks like a fault, and still tells the person nothing.

Needs: server

### NOTIFY-TAP-001: Tapping a notification shows that message
`req~NOTIFY-TAP-001~1`

Tapping a notification opens the conversation at that message, then moves on to the
newest messages. Seeing it there does not by itself mark the conversation read.

    Given a person gets a notification for a message in a busy conversation
    When they tap it
    Then the conversation opens with that message in view
    And then moves on towards the newest messages

Rationale:
The notification was about that message, so that is what the person expects to see first.

Needs: ccl

### NOTIFY-TAP-002: A notification for a deleted message opens the conversation
`req~NOTIFY-TAP-002~1`

If the message a notification was about no longer exists, tapping it opens the
conversation at its newest messages.

    Given a person got a notification for a message
    And that message has since been deleted
    When they tap the notification
    Then the conversation opens at its newest messages

Rationale:
Showing an error for something the person cannot fix is worse than showing them the conversation.

Needs: ccl

### NOTIFY-REPLY-001: A reply from a notification is sent once
`req~NOTIFY-REPLY-001~1`

A reply sent from a notification is sent straight away or not at all. It is never
sent later without the person knowing.

    Given a person replies to a notification while their connection is poor
    When the reply cannot be sent within a few seconds
    Then it is not sent in the background later on

Rationale:
A message that turns up hours later, out of context, can do more harm than one that never arrived.

Needs: ccl

### NOTIFY-REPLY-002: A reply that fails from a notification shows in the conversation
`req~NOTIFY-REPLY-002~1`

If a reply from a notification fails, it appears in the conversation as failed,
with Retry, unless the person was not allowed to post there or was signed out.

    Given a person replies to a notification
    When the reply fails
    Then the next time they open that conversation, the reply is there marked as failed
    And it offers "Retry"

Rationale:
The person thinks they replied. They must be able to find out it did not go, and send it when they choose.

Needs: ccl

### NOTIFY-REPLY-003: Reacting from a notification always adds the reaction
`req~NOTIFY-REPLY-003~1`

Reacting to a message from its notification always adds the reaction. It never
removes one already there.

    Given a person already reacted 👍 to a message
    When they react 👍 again from its notification
    Then their 👍 stays

Rationale:
From a notification the person cannot see what they already did, so a reaction there can only mean "add".

Needs: ccl

### NOTIFY-DEVICE-001: Turning notifications off or signing out stops them
`req~NOTIFY-DEVICE-001~1`

When a person turns notifications off for Connect on a device, or signs out there,
that device stops getting Connect notifications.

    Given a person signs out of Connect on their old phone
    When someone sends them a message
    Then the old phone shows no notification

Rationale:
Notifications on a device someone has stopped using leak conversations to whoever has it now.

Needs: ios, macos, web

### NOTIFY-DEVICE-002: Notifications are in the device's language
`req~NOTIFY-DEVICE-002~1`

Notification text is written in the language the person's device uses.

    Given a person's phone is set to Spanish
    When they get a Connect notification
    Then its wording from Connect is in Spanish

Rationale:
A notification is read in a glance. It must be in the person's own language.

Needs: server, ios, macos, web
