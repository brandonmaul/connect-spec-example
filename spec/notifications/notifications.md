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

### NOTIFY-TAP-003: Clicking a notification brings that conversation forward
`req~NOTIFY-TAP-003~1`

Clicking a Connect notification on a computer opens its conversation in the Connect
tab or window already open, and brings it to the front. If none is open, a new one
opens.

    Given a person has Connect open in a browser tab behind other tabs
    When they click a Connect notification
    Then that tab comes to the front
    And shows the conversation the notification was about

Rationale:
Opening a second copy of Connect, or switching a tab the person cannot see, both leave them looking for the message.

Needs: web

### NOTIFY-TAP-004: Reading a conversation clears its notifications
`req~NOTIFY-TAP-004~1`

When a person reads a conversation, its notifications are removed from the device's
notification list.

    Given a person has three notifications from "Philly Roofing"
    When they read the conversation
    Then those three notifications are gone

Rationale:
Notifications for messages already read are clutter, and make people check twice.

Needs: web

### NOTIFY-TAP-005: No notification for the conversation you are reading
`req~NOTIFY-TAP-005~1`

A person is not notified about a message in the conversation they are looking at.

    Given a person has "Philly Roofing" open and in front of them
    When a message arrives in it
    Then no notification pops up for it

Status: draft

Rationale:
Product to decide. Today the web shows a notification even while the person is reading that very conversation.

Needs: web

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

### NOTIFY-DEVICE-003: Notifications are turned on per browser
`req~NOTIFY-DEVICE-003~1`

In a web browser, a person turns Connect notifications on or off for that browser
only, from Settings. Connect remembers if they turned them off.

    Given a person uses Connect in Chrome and as an installed app
    When they turn notifications off in Chrome
    Then Chrome stops showing Connect notifications
    And the installed app keeps showing them

Rationale:
People choose where they want to be interrupted, device by device.

Needs: web

### NOTIFY-DEVICE-004: Blocked notifications explain how to unblock them
`req~NOTIFY-DEVICE-004~1`

If a person has blocked notifications in their browser and tries to turn them on,
Connect tells them how to unblock them.

    Given a person blocked Connect's notifications in their browser
    When they turn notifications on in Settings
    Then they see "Notifications blocked. Enable them in system or browser settings to continue."
    And the setting stays off

Rationale:
Only the browser can undo a block, so the person has to be told where to go.

Needs: web

### NOTIFY-DEVICE-005: Browsers without notifications point to the app
`req~NOTIFY-DEVICE-005~1`

If a browser cannot show notifications, turning them on tells the person to use the
Connect app instead.

    Given a browser that cannot show notifications
    When a person turns notifications on in Settings
    Then they see "Notifications aren't available in this browser. To receive alerts for new messages, please download the Connect app."

Rationale:
The person can still get notifications, just not in that browser.

Needs: web

### NOTIFY-DEVICE-006: When the web asks to send notifications
`req~NOTIFY-DEVICE-006~1`

Connect asks for permission to send notifications once, at a moment the person
chooses, not every time it opens.

    Given a person has never been asked about Connect notifications in their browser
    When they sign in
    Then they are not asked straight away
    But are offered notifications in a way they can accept or put off

Status: draft

Rationale:
Product to decide. Today the browser asks as soon as the person signs in, and again on every visit until they answer. Browsers start hiding sites that ask too often.

Needs: web
