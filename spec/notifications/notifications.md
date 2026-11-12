# Notifications

What makes a conversation bold (unread) or gives it a Notification Badge, which messages notify a person, the counts on the app icon, what a notification says, and what happens when a person acts on one. Mark as Unread is covered in [Conversations](../conversations/conversations.md); when an open conversation is marked read is covered in [Conversation View](../conversations/conversation-view.md).

**Area code:** `NOTIFY`

**Topics**

| Topic | Covers |
|---|---|
| `UNREAD` | What makes a conversation bold, gives it a Notification Badge, or sends a notification |
| `LEVEL` | What each Room notifies a person about |
| `COUNT` | The unread count on the app icon and browser tab |
| `TEXT` | What a notification says |
| `TAP` | Opening Connect from a notification, and clearing notifications |
| `REPLY` | Replying or reacting straight from a notification |
| `DEVICE` | Turning notifications on and off for a device |

Design: [Handoff Repository](https://huddle.powerapp.cloud/projects/489) · [User Options](https://huddle.powerapp.cloud/projects/650)

### NOTIFY-UNREAD-001: A message from someone else makes a conversation bold
`req~NOTIFY-UNREAD-001~1`

A message from another person marks the conversation unread, and its row in the
Conversation List turns bold.

    Given a person has read everything in a conversation
    When someone else sends a message in it
    Then the conversation is unread and its row is bold

Rationale:
Bold tells the person there is something they haven't read, whether or not it notified them.

Needs: ccl, browser, pwa, macos, ios

### NOTIFY-UNREAD-002: A notifying message adds a Notification Badge
`req~NOTIFY-UNREAD-002~1`

A notifying message adds a Notification Badge with a count to the conversation's row
and to the app icon, as well as making it bold.

    Given a person's conversation notifies them about every message
    When someone sends a message in it
    Then the row is bold
    And it shows a Notification Badge with a count
    And the app icon shows a badge

Rationale:
The badge separates what asked for the person's attention from what is merely unread.

Needs: server, ccl, browser, pwa, macos, ios

### NOTIFY-UNREAD-003: A message that doesn't notify only bolds
`req~NOTIFY-UNREAD-003~1`

A message that is not notifying makes the conversation bold but adds no
Notification Badge and sends no notification.

    Given a person's Room notifies them only about mentions of them
    When someone posts in it without mentioning them
    Then the Room's row is bold
    And it has no Notification Badge
    And no notification is sent

Rationale:
The person chose not to be interrupted by this conversation, but should still see that it has something new.

Needs: server, ccl, browser, pwa, macos, ios

### NOTIFY-UNREAD-004: A notifying message sends a notification when Connect is not in focus
`req~NOTIFY-UNREAD-004~1`

When a notifying message arrives while Connect is not in focus, the person gets a
notification.

    Given Connect is not in focus on a person's device
    When a notifying message arrives for them
    Then the device shows a Connect notification

Rationale:
A person who isn't looking at Connect needs to be told when something asks for their attention.

Needs: server, browser, pwa, macos, ios

### NOTIFY-UNREAD-005: Bots never notify
`req~NOTIFY-UNREAD-005~1`

A message from a bot never sends a notification or adds a Notification Badge.

    Given the Nitro App bot posts in a person's conversation
    Then the person gets no notification
    And the conversation has no Notification Badge for it

Rationale:
Automated messages are informational; they shouldn't interrupt people like a coworker would.

Needs: server, browser, pwa, macos, ios

### NOTIFY-LEVEL-001: Each Room has a notification level
`req~NOTIFY-LEVEL-001~1`

For each Room, a person chooses one of four notification levels: All Messages;
Mentions Only (@all and @you); Direct Mentions Only (@you); or No Notifications.

    Given a person is in a busy Room
    When they set it to Direct Mentions Only
    Then they are notified when someone mentions them
    But not when someone mentions @all, or posts without mentioning them

Rationale:
People are in many Rooms that matter to different degrees. One setting for all of them would mean too many notifications or too few.

Needs: server, browser, pwa, macos, ios

### NOTIFY-LEVEL-002: Default notification levels
`req~NOTIFY-LEVEL-002~1`

Until a person changes it, a People Conversation notifies them about every message,
and a Room notifies them about mentions of everyone and of them.

    Given a person has just been added to a Room and to a DM
    When a message without a mention arrives in each
    Then only the DM notifies them

Rationale:
A People Conversation is written to you. Most Rooms are shared by many people, and notifying everyone of everything would bury what matters.

Status: draft

Needs: server

### NOTIFY-LEVEL-003: A person mentioned twice is notified once
`req~NOTIFY-LEVEL-003~1`

If a message mentions the same person more than once, they get one notification.

    Given a message mentions @Sam twice
    When it is sent
    Then Sam gets one notification

Rationale:
Repeating a name is emphasis, not a request to buzz someone twice.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### NOTIFY-LEVEL-004: No Notifications still bolds
`req~NOTIFY-LEVEL-004~1`

In a Room set to No Notifications, new messages make the Room bold but add no
Notification Badge.

    Given a person set a Room to No Notifications
    When someone posts in it, mentioning them
    Then the Room's row is bold
    And it has no Notification Badge

Rationale:
Silencing a Room shouldn't hide that it has new messages.

Needs: server, ccl, browser, pwa, macos, ios

### NOTIFY-LEVEL-005: The notification level is set from the bell on macOS and Web
`req~NOTIFY-LEVEL-005~1`

On macOS, Browser and PWA, a Room's notification level is set from the notification
bell in its Conversation Header.

    Given a person has a Room open on macOS
    When they click the bell in the Conversation Header
    Then they can choose the Room's notification level

Rationale:
The setting belongs next to the Room it changes.

Needs: browser, pwa, macos

### NOTIFY-LEVEL-006: The notification level is set from Room Info on iOS
`req~NOTIFY-LEVEL-006~1`

On iOS, a Room's notification level is set from Room Info.

    Given a person has a Room open on iOS
    When they open Room Info
    Then they can choose the Room's notification level

Rationale:
On a phone the header has no room for the bell, so the setting lives with the Room's other details.

Needs: ios

### NOTIFY-LEVEL-007: Notification levels sync across devices
`req~NOTIFY-LEVEL-007~1`

A Room's notification level, once set, applies on all of the person's devices.

    Given a person sets a Room to Mentions Only on their Mac
    When they open Connect on their iPhone
    Then the Room is set to Mentions Only there too

Rationale:
People expect a Room to behave the same wherever they read it.

Needs: server, ccl, browser, pwa, macos, ios

### NOTIFY-COUNT-001: The macOS Dock icon counts unread messages
`req~NOTIFY-COUNT-001~1`

The badge on the Connect icon in the macOS Dock shows the number of unread messages.

    Given a person has 3 unread messages in one conversation and 2 in another
    Then the Dock icon's badge shows 5

Rationale:
On a computer the Dock tells the person how much is waiting without opening Connect.

Needs: ccl, macos

### NOTIFY-COUNT-002: The iOS app icon counts conversations with unread
`req~NOTIFY-COUNT-002~1`

The badge on the Connect app icon on iOS shows the number of conversations with
unread messages.

    Given a person has 3 unread messages in one conversation and 2 in another
    Then the iOS app icon's badge shows 2

Rationale:
On a phone, the number of conversations waiting is the quickest measure of what needs attention.

Needs: ccl, ios

### NOTIFY-COUNT-003: The Firefox tab counts unread conversations
`req~NOTIFY-COUNT-003~1`

In Firefox, the Connect tab shows the number of unread conversations.

    Given a person uses Connect in Firefox with 2 unread conversations
    Then the Connect tab shows 2

Rationale:
A browser tab is the only place a person sees Connect's state while working in other tabs.

Needs: browser

### NOTIFY-TEXT-001: A notification shows who wrote what, and where
`req~NOTIFY-TEXT-001~1`

A notification's title is the sender's name, followed by the Room's name for a Room.
Its text is the message, up to its first 1,024 characters.

    Given Dana Ruiz writes "Crew is on site" in the Room "Philly Roofing"
    Then the notification's title is "Dana Ruiz in Philly Roofing"
    And its text is "Crew is on site"
    But from a People Conversation, the title is only "Dana Ruiz"

Rationale:
People decide from the notification alone whether to open Connect now.

Status: draft

Needs: server

### NOTIFY-TEXT-002: A message with no text still notifies clearly
`req~NOTIFY-TEXT-002~1`

When a message has no text to show, its notification says who wrote in which Room,
or that the sender is connecting with the person.

    Given Dana sends a message with no text in the Room "Philly Roofing"
    Then the notification says "Dana Ruiz wrote a message in Philly Roofing"
    And from a DM it says "Dana Ruiz is Connecting with you"
    And if even the sender is unknown, it says "Someone is connecting with you..."

Rationale:
An empty notification looks like a fault, and still tells the person nothing.

Status: draft

Needs: server

### NOTIFY-TEXT-003: iOS can hide message previews
`req~NOTIFY-TEXT-003~1`

On iOS, a person can hide message previews in notifications. A hidden-preview
notification says the sender is Connecting with them instead of showing the message.

    Given a person on iOS has hidden notification previews
    When Dana Ruiz sends them a message
    Then the notification says "Dana Ruiz is Connecting with you…"
    And does not show the message

Rationale:
A phone's lock screen can be seen by others, so people need a way to keep message text off it.

Needs: ios

### NOTIFY-TEXT-004: Web notifications say "New Message in Connect"
`req~NOTIFY-TEXT-004~1`

On Browser and PWA, a notification says "New Message in Connect".

    Given a person has notifications on in the Browser
    When a notifying message arrives
    Then the notification says "New Message in Connect"

Rationale:
The notification tells the person there is something to read in Connect.

Needs: browser, pwa

### NOTIFY-TAP-001: Tapping a notification opens at the New Message Indicator
`req~NOTIFY-TAP-001~1`

Tapping a notification opens its conversation scrolled to the New Message Indicator.
Opening it does not by itself mark the conversation read.

    Given a person gets a notification for a message in a busy conversation
    When they tap it
    Then the conversation opens scrolled to the New Message Indicator
    And it stays unread until they reach the bottom

Rationale:
The first unread message is where the person needs to start reading to catch up.

Needs: ccl, browser, pwa, macos, ios

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

Status: draft

Needs: ccl, browser, pwa, macos, ios

### NOTIFY-TAP-003: Clicking a Browser notification finds the right tab
`req~NOTIFY-TAP-003~1`

Clicking a Connect notification in the Browser focuses a tab already showing that
conversation; otherwise the last-focused Connect tab, which then shows the
conversation; otherwise a new tab.

    Given a person has two Connect tabs open, neither showing "Philly Roofing"
    When they click a notification from "Philly Roofing"
    Then the Connect tab they used last comes to the front
    And it shows "Philly Roofing"
    But if no Connect tab is open, a new tab opens on "Philly Roofing"

Rationale:
Opening a second copy of Connect, or switching a tab the person cannot see, both leave them looking for the message.

Needs: browser

### NOTIFY-TAP-004: Reading a conversation clears its notifications in Firefox and the PWA
`req~NOTIFY-TAP-004~1`

In Firefox and in the PWA, when a person reads a conversation, its notification
banners are removed from the device's notification list.

    Given a person has three notifications from "Philly Roofing" in Firefox
    When they read the conversation
    Then those three notifications are gone

Rationale:
Notifications for messages already read are clutter, and make people check twice.

Needs: browser, pwa

### NOTIFY-TAP-005: No notification for the conversation you are reading
`req~NOTIFY-TAP-005~1`

A person is not notified about a message in the conversation they are looking at.

    Given a person has "Philly Roofing" open and in front of them
    When a message arrives in it
    Then no notification pops up for it

Rationale:
Open: should a notification appear for a message in the conversation the person is already looking at?

Status: draft

Needs: browser, pwa

### NOTIFY-TAP-006: A PWA notification opens in the PWA
`req~NOTIFY-TAP-006~1`

Tapping a notification from the PWA opens the conversation in the PWA, not in a
browser tab.

    Given a person uses the PWA on Android
    When they tap a Connect notification
    Then the conversation opens in the PWA

Rationale:
A person who installed the app expects to stay in it.

Needs: pwa

### NOTIFY-TAP-007: Safari keeps notification banners after reading
`req~NOTIFY-TAP-007~1`

In Safari, reading a conversation does not remove its notification banners; the
person clears them.

    Given a person has three notifications from "Philly Roofing" in Safari
    When they read the conversation
    Then the three notifications stay until the person clears them

Rationale:
Safari leaves delivered notifications for the person to clear.

Needs: browser

### NOTIFY-TAP-008: Clearing a notification on one Apple device clears it on the others
`req~NOTIFY-TAP-008~1`

When a person clears a Connect notification on one of their Apple devices, it is
also cleared on their other Apple devices.

    Given a person has the same Connect notification on their Mac and iPhone
    When they clear it on the Mac
    Then it is also gone from the iPhone

Rationale:
A notification already dealt with on one device is clutter on the others.

Needs: server, macos, ios

### NOTIFY-REPLY-001: A reply from a notification is sent once
`req~NOTIFY-REPLY-001~1`

A reply sent from a notification is sent straight away or not at all. It is never
sent later without the person knowing.

    Given a person replies to a notification while their connection is poor
    When the reply cannot be sent within a few seconds
    Then it is not sent in the background later on

Rationale:
A message that turns up hours later, out of context, can do more harm than one that never arrived.

Status: draft

Needs: ccl, macos, ios

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

Status: draft

Needs: ccl, macos, ios

### NOTIFY-REPLY-003: Liking from a notification always adds the reaction
`req~NOTIFY-REPLY-003~1`

Liking a message from its notification always adds the like. It never removes one
already there.

    Given a person already liked a message
    When they choose Like again from its notification
    Then their like stays

Rationale:
From a notification the person cannot see what they already did, so a reaction there can only mean "add".

Status: draft

Needs: ccl, macos, ios

### NOTIFY-REPLY-004: Like from a notification on iOS
`req~NOTIFY-REPLY-004~1`

On iOS, a person can Like a message straight from its notification.

    Given a person on iOS gets a notification for a message
    When they choose Like on the notification
    Then the message gets their like reaction without opening Connect

Rationale:
A quick acknowledgement shouldn't need the app opened.

Needs: ios

### NOTIFY-REPLY-005: Reply from a notification on iOS
`req~NOTIFY-REPLY-005~1`

On iOS, a person can reply to a message straight from its notification.

    Given a person on iOS gets a notification for a message
    When they choose Reply and send "On my way"
    Then "On my way" is sent in that conversation without opening Connect

Rationale:
A short answer shouldn't need the app opened.

Needs: ios

### NOTIFY-DEVICE-001: Turning notifications off or signing out stops them
`req~NOTIFY-DEVICE-001~1`

When a person turns notifications off for Connect on a device, or signs out there,
that device stops getting Connect notifications.

    Given a person signs out of Connect on their old phone
    When someone sends them a message
    Then the old phone shows no notification

Rationale:
Notifications on a device someone has stopped using leak conversations to whoever has it now.

Status: draft

Needs: browser, pwa, macos, ios

### NOTIFY-DEVICE-002: Notifications are in the device's language
`req~NOTIFY-DEVICE-002~1`

Notification text is written in the language the person's device uses.

    Given a person's phone is set to Spanish
    When they get a Connect notification
    Then its wording from Connect is in Spanish

Rationale:
A notification is read in a glance. It must be in the person's own language.

Status: draft

Needs: server, browser, pwa, macos, ios

### NOTIFY-DEVICE-003: Notifications are turned on per browser
`req~NOTIFY-DEVICE-003~1`

On Browser and PWA, a person turns Connect notifications on or off for that browser
only, from the User Menu. Connect remembers if they turned them off.

    Given a person uses Connect in Chrome and as the PWA
    When they turn notifications off in Chrome
    Then Chrome stops showing Connect notifications
    And the PWA keeps showing them

Rationale:
People choose where they want to be interrupted, device by device.

Status: draft

Needs: browser, pwa

### NOTIFY-DEVICE-004: Blocked notifications explain how to unblock them
`req~NOTIFY-DEVICE-004~1`

If a person has blocked notifications in their browser and tries to turn them on,
Connect tells them how to unblock them.

    Given a person blocked Connect's notifications in their browser
    When they turn notifications on in the User Menu
    Then they see "Notifications blocked. Enable them in system or browser settings to continue."
    And the setting stays off

Rationale:
Only the browser can undo a block, so the person has to be told where to go.

Status: draft

Needs: browser, pwa

### NOTIFY-DEVICE-005: Browsers without notifications point to the app
`req~NOTIFY-DEVICE-005~1`

If a browser cannot show notifications, turning them on tells the person to use the
Connect app instead.

    Given a browser that cannot show notifications
    When a person turns notifications on in the User Menu
    Then they see "Notifications aren't available in this browser. To receive alerts for new messages, please download the Connect app."

Rationale:
The person can still get notifications, just not in that browser.

Status: draft

Needs: browser, pwa

### NOTIFY-DEVICE-006: When Browser and PWA ask to send notifications
`req~NOTIFY-DEVICE-006~1`

Connect asks for permission to send notifications once, at a moment the person
chooses, not every time it opens.

    Given a person has never been asked about Connect notifications in their browser
    When they sign in
    Then they are not asked straight away
    But are offered notifications in a way they can accept or put off

Rationale:
Open: when should Connect ask for permission to send notifications? Asking as soon as a person signs in, and on every visit until they answer, annoys people, and browsers start hiding sites that ask too often.

Status: draft

Needs: browser, pwa

### NOTIFY-DEVICE-007: The device's notification permission comes first
`req~NOTIFY-DEVICE-007~1`

If a person has not allowed Connect to notify them on a device, that device shows no
Connect notifications, whatever the Room's notification level.

    Given a person has not allowed notifications for Connect on their phone
    And a Room is set to All Messages
    When someone posts in the Room
    Then the phone shows no notification

Rationale:
The device's own setting is the person's final word on being interrupted.

Needs: browser, pwa, macos, ios

### NOTIFY-DEVICE-008: Focus modes come first on Apple devices
`req~NOTIFY-DEVICE-008~1`

On macOS and iOS, a Focus mode that silences Connect stops its notifications,
whatever the Room's notification level.

    Given a person has a Focus mode on that silences Connect
    And a Room is set to All Messages
    When someone posts in the Room
    Then the device shows no notification

Rationale:
People use Focus to protect their time; Connect must respect it.

Needs: macos, ios
