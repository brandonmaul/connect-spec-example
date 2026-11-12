# The Connect app

Connect as an app on a person's device: installing it, its icon, updates, losing the connection and catching up after sleep, short notices, Help & Diagnostics, opening files, the Crash Screen, and fitting the screen.

**Area code:** `APP`

**Topics**

| Topic | Covers |
|---|---|
| `INSTALL` | Getting Connect onto a device |
| `ICON` | The Connect app icon |
| `UPDATE` | New versions of Connect |
| `OFFLINE` | Losing and regaining the connection |
| `LAYOUT` | How Connect fits the screen |
| `SYNC` | Catching up after the device sleeps or Connect is in the background |
| `NOTICE` | How short on-screen notices (toasts) appear and go away |
| `HELP` | Help & Diagnostics in the User Menu |
| `FILE` | Opening and saving attached files |
| `CRASH` | What a person sees after Connect quits unexpectedly |

Design: [Error Messaging](https://huddle.powerapp.cloud/projects/506) · [Loading](https://huddle.powerapp.cloud/projects/590) · [Nitro Application Portal](https://huddle.powerapp.cloud/projects/788) · [Responsive Breakpoints](https://huddle.powerapp.cloud/projects/555)

### APP-INSTALL-001: The PWA is installed from the browser
`req~APP-INSTALL-001~1`

Connect can be installed from a web browser as the PWA, an app with its own icon
that opens in its own window without the browser's address bar.

    Given a person opens Connect in Chrome on Android
    When they choose "Add to home screen"
    Then Connect has its own icon on their home screen
    And opens in its own window

Rationale:
This is how Android users get Connect as an app, since there is no native Android v3 app.

Needs: pwa

### APP-INSTALL-002: The installed PWA is called Nitro Connect
`req~APP-INSTALL-002~1`

Installed from the browser, the PWA is named "Nitro Connect". Test versions carry
their own names so they can be told apart.

    Given a person installs the PWA
    Then the icon is labelled "Nitro Connect"

Rationale:
People with test versions installed need to know which one they are opening.

Status: draft

Needs: pwa

### APP-INSTALL-003: Power-owned Apple devices get Connect from the company
`req~APP-INSTALL-003~1`

In Nitro Connect only, Power-owned Macs, iPhones and iPads get Nitro Connect
preinstalled or from the company's Self-Service app.

    Given a Power employee receives a company iPhone
    When they look for Connect
    Then Nitro Connect is already installed or is offered in Self-Service

Rationale:
Company devices should not depend on each employee finding and installing the app themselves.

Needs: macos, ios

### APP-INSTALL-004: Personal devices install Connect from My Personal Device Setup
`req~APP-INSTALL-004~1`

In Nitro Connect only, people install Connect on their personal iPhone or Android
phone from My Personal Device Setup in Nitro.

    Given a Power employee wants Connect on their own Android phone
    When they open My Personal Device Setup in Nitro
    Then it walks them through installing Connect on that phone

Rationale:
One place in Nitro gives people the right app for their personal device, without hunting through app stores.

Needs: nitro, pwa, ios

### APP-ICON-001: The installed PWA's icon shows unread conversations
`req~APP-ICON-001~1`

The icon of the installed PWA shows how many conversations have unread messages,
and shows nothing when everything is read.

    Given three conversations have unread messages
    Then the installed PWA icon shows 3
    And when they are all read, the number goes

Rationale:
The icon is the one place people look to know whether Connect needs them.

Status: draft

Needs: pwa

### APP-ICON-002: The browser tab shows unread conversations
`req~APP-ICON-002~1`

In a browser tab, Connect's title shows how many conversations are unread, and its
tab icon has a dot while anything is unread.

    Given three conversations have unread messages
    Then the tab reads "(3) Nitro Connect"
    And its icon shows a dot

Rationale:
People keep Connect in a tab among many others.

Status: draft

Needs: browser

### APP-ICON-003: Unread counts show without notification permission
`req~APP-ICON-003~1`

The app icon and browser tab show unread conversations whether or not the person
allowed notifications.

    Given a person blocked Connect's notifications in their browser
    When conversations are unread
    Then the tab still shows how many

Rationale:
Open: should the browser show an unread count when notifications are not allowed? Today it shows none unless they are.

Status: draft

Needs: browser, pwa

### APP-ICON-004: Shortcuts from the app icon
`req~APP-ICON-004~1`

Pressing and holding the Connect icon, once signed in, offers shortcuts straight to
starting something new.

    Given a person presses and holds the Connect icon on their iPhone
    Then they can choose Take Photo, Attach Photos, Attach File or New Message
    And the installed PWA offers New Message

Rationale:
The most common reason to open Connect is to send something. A shortcut saves steps.

Status: draft

Needs: pwa, ios

### APP-UPDATE-001: Web says when a new version is ready
`req~APP-UPDATE-001~1`

When a new version of Connect is available on Web, a toast says "A new version of
Connect is ready!" with an "Update Now" button.

    Given a new version of Connect has been released
    When a person has Connect open in the Browser or PWA
    Then they see "A new version of Connect is ready!"
    And "Update Now" reloads Connect into the new version

Rationale:
A browser tab can stay open for weeks. Without a prompt, people stay on old versions.

Needs: browser, pwa

### APP-UPDATE-002: Dismissing the Web update toast waits a day
`req~APP-UPDATE-002~1`

Dismissing the new version toast on Web hides it for 24 hours.

    Given a person dismisses the new version toast
    Then it does not come back for 24 hours

Rationale:
Open: Web waits 24 hours after dismissal but iOS "Remind me later" waits 4 hours. Is the difference intended, and if not, which is correct?

Status: draft

Needs: browser, pwa

### APP-UPDATE-003: iOS personal devices are asked to update
`req~APP-UPDATE-003~1`

On a personal iPhone or iPad, when a new version of Connect is available, Connect
asks the person to update with "Update now" and "Remind me later".

    Given a new version of Connect is available
    When a person opens Connect on their personal iPhone
    Then they see a prompt with "Update now" and "Remind me later"

Rationale:
Personal devices are not updated by the company, so the app has to ask.

Needs: ios

### APP-UPDATE-004: "Remind me later" on iOS waits 4 hours
`req~APP-UPDATE-004~1`

Choosing "Remind me later" on the iOS update prompt waits 4 hours before asking
again.

    Given a person chooses "Remind me later" on the update prompt
    Then Connect does not ask again for 4 hours

Rationale:
Open: iOS waits 4 hours but Web waits 24 hours after the update toast is closed. Is the difference intended, and if not, which is correct?

Status: draft

Needs: ios

### APP-UPDATE-005: Company-managed devices get the company's update alert
`req~APP-UPDATE-005~1`

On a company-managed device, a new version of Connect is announced by the company's
device management alert rather than Connect's own prompt.

    Given a new version of Connect is available
    When a person uses Connect on a Power-owned iPhone
    Then the update is offered by the company's device management alert
    And not by the "Update now / Remind me later" prompt

Rationale:
The company installs updates on its own devices, so one alert from device management avoids two competing prompts.

Needs: ios

### APP-UPDATE-006: A failed update says so and offers a way forward
`req~APP-UPDATE-006~1`

When an update fails, Connect shows a fullscreen "Update failed" error with
"Try again" and "Submit a support ticket".

    Given a person starts updating Connect
    When the update fails
    Then they see "Update failed" filling the screen
    And they can choose "Try again" or "Submit a support ticket"

Rationale:
An update that fails silently leaves people stuck on an old version without knowing it, or with no way to get help.

Needs: browser, pwa, macos, ios

### APP-OFFLINE-001: Losing the connection is shown
`req~APP-OFFLINE-001~1`

When the device loses its connection, Connect shows a gray toast saying so until the
connection is back.

    Given a person's laptop loses its Wi-Fi
    Then Connect shows a gray toast "Lost connection. Check your internet connectivity."
    And the toast goes when the connection returns

Rationale:
Without it, people think messages have stopped coming.

Needs: browser, pwa, macos, ios

### APP-OFFLINE-002: Web opens without a connection
`req~APP-OFFLINE-002~1`

Once Connect has been opened in the Browser or PWA, it opens again even without a
connection.

    Given a person used Connect in their browser yesterday
    When they open it today on a plane
    Then Connect opens

Rationale:
People still want to read and write while offline (MSG-SEND-004).

Status: draft

Needs: browser, pwa

### APP-LAYOUT-001: Small Screens show one thing at a time
`req~APP-LAYOUT-001~1`

On Small Screens, Connect shows either the Conversation List or a Conversation View,
not both side by side.

    Given a person uses Connect in a Mobile Browser
    When they open a conversation
    Then the Conversation View fills the screen
    And a back button returns to the Conversation List

Rationale:
Two panels side by side on a narrow screen are both too small to use.

Status: draft

Needs: browser, pwa

### APP-LAYOUT-002: Phones suggest portrait
`req~APP-LAYOUT-002~1`

Turning a phone sideways shows a hint, which can be closed, that Connect works
better in portrait.

    Given a person turns their phone sideways in the Mobile Browser or Mobile PWA
    Then they see "Use Connect in portrait mode for a better experience."

Rationale:
Sideways on a phone, the keyboard leaves almost no room for the conversation.

Status: draft

Needs: browser, pwa

### APP-SYNC-001: Web shows "Syncing..." after background or sleep
`req~APP-SYNC-001~1`

When Connect on Web comes back from the background or the device waking from sleep,
it shows "Syncing..." while it catches up.

    Given a person's laptop slept with Connect open in the Browser
    When they wake it
    Then Connect shows "Syncing..." until it has caught up

Rationale:
People need to know that what they see may not be up to date yet.

Needs: browser, pwa

### APP-SYNC-002: Cached conversations stay usable while Web syncs
`req~APP-SYNC-002~1`

While Web shows "Syncing...", the conversations already on the device stay usable.

    Given Connect on Web shows "Syncing..." after sleep
    When the person opens a conversation
    Then it opens with the messages already on the device

Rationale:
Waiting for a full catch-up before anything works would make every return to Connect feel slow.

Needs: browser, pwa

### APP-SYNC-003: Apple pauses syncing on sleep and resumes on wake
`req~APP-SYNC-003~1`

On Apple, Connect pauses syncing when the device sleeps or Connect goes to the
background, and resumes when it wakes or returns.

    Given Connect is open on a Mac
    When the Mac sleeps
    Then Connect stops syncing
    And when the Mac wakes, Connect resumes syncing and catches up

Rationale:
Syncing while asleep wastes battery and can leave Connect in a broken state on wake.

Needs: ccl, macos, ios

### APP-NOTICE-001: Web toasts stack
`req~APP-NOTICE-001~1`

On Web, several toasts at once stack instead of covering each other.

    Given a toast is showing in the Browser
    When a second toast appears
    Then both are visible, one stacked above the other

Rationale:
A toast hidden under another is a message the person never reads.

Needs: browser, pwa

### APP-NOTICE-002: Dismissing a Web toast closes the gap
`req~APP-NOTICE-002~1`

On Web, when a toast in a stack is dismissed, the remaining toasts move together to
close the gap.

    Given three toasts are stacked in the Browser
    When the person dismisses the middle one
    Then the other two close up with no gap between them

Rationale:
A gap looks like something is missing and wastes space.

Needs: browser, pwa

### APP-NOTICE-003: Web success toasts go away by themselves
`req~APP-NOTICE-003~1`

On Web, a success toast dismisses itself after about 4–5 seconds.

    Given a success toast appears in the Browser
    When about 4–5 seconds pass
    Then it goes away without the person closing it

Rationale:
Success needs no action, so it should not wait to be closed.

Needs: browser, pwa

### APP-HELP-001: Help & Diagnostics on Apple
`req~APP-HELP-001~1`

On Apple, Help & Diagnostics in the User Menu offers Export Log File, Test Crash,
Send Custom Error, Reset Notification Token and Corporate Events tools.

    Given a person opens the User Menu on a Mac
    When they open Help & Diagnostics
    Then they see Export Log File, Test Crash, Send Custom Error, Reset Notification Token and Corporate Events tools

Rationale:
Support needs a person to be able to send logs and reset notifications without reinstalling Connect.

Needs: macos, ios

### APP-HELP-002: Help & Diagnostics on Web
`req~APP-HELP-002~1`

On Web, Help & Diagnostics in the User Menu offers Connect Guides, Export Error Log
and Source Code, plus a test error report on staging only.

    Given a person opens the User Menu in the Browser
    When they open Help & Diagnostics
    Then they see Connect Guides, Export Error Log and Source Code
    And on staging they also see an item that sends a test error report

Rationale:
People need a way to the guides and a way to give support a log; the test error report only makes sense where the team is testing.

Needs: browser, pwa

### APP-HELP-003: The Web error log leaves out message text
`req~APP-HELP-003~1`

An error log exported from Web has message bodies redacted.

    Given a person exports the error log from Help & Diagnostics in the Browser
    When support reads it
    Then no message text appears in it

Rationale:
Logs are passed to support. They must be safe to hand over without exposing private conversations.

Needs: browser, pwa

### APP-HELP-004: The Reset Notification Token toast shows above the User Menu on macOS
`req~APP-HELP-004~1`

On macOS, the toast confirming Reset Notification Token appears above the User Menu.

    Given a person chooses Reset Notification Token in Help & Diagnostics on a Mac
    Then the confirming toast appears above the User Menu, not hidden behind it

Rationale:
A confirmation hidden behind the menu leaves the person unsure whether the reset worked.

Needs: macos

### APP-FILE-001: macOS previews files in a window
`req~APP-FILE-001~1`

On macOS, opening an attached file shows it in a preview window inside Connect.

    Given a message has a PDF attached
    When a person opens it on a Mac
    Then it shows in a preview window

Rationale:
People can look at a file without leaving Connect or choosing an app.

Needs: macos

### APP-FILE-002: macOS saves files to Downloads
`req~APP-FILE-002~1`

On macOS, saving an attached file puts it in the Downloads folder.

    Given a message has a spreadsheet attached
    When a person saves it on a Mac
    Then the file is in their Downloads folder

Rationale:
Downloads is where people expect to find files they saved.

Needs: macos

### APP-CRASH-001: A Crash Screen follows an unexpected quit
`req~APP-CRASH-001~1`

After Connect quits unexpectedly, it shows the Crash Screen, a fullscreen error
"Connect quit unexpectedly" with a "Restart Connect" button.

    Given Connect quit unexpectedly on a Mac
    Then the Crash Screen says "Connect quit unexpectedly"
    And "Restart Connect" starts Connect again

Rationale:
People need to know what happened and have one obvious way to get back to work.

Needs: macos
