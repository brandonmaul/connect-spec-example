# The Connect app

Connect as an app on a person's device: installing it from the web, its icon, updates, and what it shows when the connection drops.

**Area code:** `APP`

**Topics**

| Topic | Covers |
|---|---|
| `INSTALL` | Installing Connect from a web browser |
| `ICON` | The Connect app icon |
| `UPDATE` | New versions of Connect |
| `OFFLINE` | Losing and regaining the connection |
| `LAYOUT` | How Connect fits the screen |

Design: <figma link> · Runway: <epic link>

### APP-INSTALL-001: Connect can be installed from the browser
`req~APP-INSTALL-001~1`

Connect can be installed from a web browser as an app with its own icon, which opens
in its own window without the browser's address bar.

    Given a person opens Connect in Chrome on Android
    When they choose "Add to home screen"
    Then Connect has its own icon on their home screen
    And opens in its own window

Rationale:
This is how Android users get Connect as an app.

Needs: web

### APP-INSTALL-002: The installed app is called Nitro Connect
`req~APP-INSTALL-002~1`

Installed from the browser, Connect is named "Nitro Connect". Test versions carry
their own names so they can be told apart.

    Given a person installs Connect from the browser
    Then the icon is labelled "Nitro Connect"

Rationale:
People with test versions installed need to know which one they are opening.

Needs: web

### APP-ICON-001: The installed web app's icon shows unread conversations
`req~APP-ICON-001~1`

The icon of Connect installed from the browser shows how many conversations have
unread messages, and shows nothing when everything is read.

    Given three conversations have unread messages
    Then the installed Connect icon shows 3
    And when they are all read, the number goes

Rationale:
The icon is the one place people look to know whether Connect needs them.

Needs: web

### APP-ICON-002: The browser tab shows unread conversations
`req~APP-ICON-002~1`

In a browser tab, Connect's title shows how many conversations are unread, and its
tab icon has a dot while anything is unread.

    Given three conversations have unread messages
    Then the tab reads "(3) Nitro Connect"
    And its icon shows a dot

Rationale:
People keep Connect in a tab among many others.

Needs: web

### APP-ICON-003: Unread counts show without notification permission
`req~APP-ICON-003~1`

The app icon and browser tab show unread conversations whether or not the person
allowed notifications.

    Given a person blocked Connect's notifications in their browser
    When conversations are unread
    Then the tab still shows how many

Status: draft

Rationale:
Product to decide. Today the browser shows no unread count at all unless notifications are allowed.

Needs: web

### APP-ICON-004: Shortcuts from the app icon
`req~APP-ICON-004~1`

Pressing and holding the Connect icon, once signed in, offers shortcuts straight to
starting something new.

    Given a person presses and holds the Connect icon on their iPhone
    Then they can choose Take Photo, Attach Photos, Attach File or New Message
    And the installed web app offers New Message

Rationale:
The most common reason to open Connect is to send something. A shortcut saves steps.

Needs: ios, web

### APP-UPDATE-001: The web says when a new version is ready
`req~APP-UPDATE-001~1`

When a new version of Connect is available on the web, a notice says "A new version
of Connect is ready!" with an "Update Now" button.

    Given a new version of Connect has been released
    When a person has Connect open in their browser
    Then they see "A new version of Connect is ready!"
    And "Update Now" reloads Connect into the new version

Rationale:
A browser tab can stay open for weeks. Without a prompt, people stay on old versions.

Needs: web

### APP-UPDATE-002: Dismissing the update notice waits a day
`req~APP-UPDATE-002~1`

Dismissing the new version notice hides it for about a day.

    Given a person dismisses the new version notice
    Then it does not come back for about 24 hours

Rationale:
The person may be in the middle of something. Asking again every few minutes would nag.

Needs: web

### APP-OFFLINE-001: Losing the connection is shown
`req~APP-OFFLINE-001~1`

When the device loses its connection, Connect says so until it is back.

    Given a person's laptop loses its Wi-Fi
    Then Connect shows "Lost connection. Check your internet connectivity."
    And the notice goes when the connection returns

Rationale:
Without it, people think messages have stopped coming.

Needs: ios, macos, web

### APP-OFFLINE-002: The web app opens without a connection
`req~APP-OFFLINE-002~1`

Once Connect has been opened in a browser, it opens again even without a connection.

    Given a person used Connect in their browser yesterday
    When they open it today on a plane
    Then Connect opens

Rationale:
People still want to read and write while offline (MSG-SEND-004).

Needs: web

### APP-LAYOUT-001: Narrow windows show one thing at a time
`req~APP-LAYOUT-001~1`

On a narrow screen or window, Connect shows either the conversation list or a
conversation, not both side by side.

    Given a person uses Connect on a phone browser
    When they open a conversation
    Then it fills the screen
    And a back button returns to the list

Rationale:
Two panels side by side on a narrow screen are both too small to use.

Needs: web

### APP-LAYOUT-002: Phones suggest portrait
`req~APP-LAYOUT-002~1`

Turning a phone sideways shows a hint, which can be closed, that Connect works
better in portrait.

    Given a person turns their phone sideways in the Connect web app
    Then they see "Use Connect in portrait mode for a better experience."

Rationale:
Sideways on a phone, the keyboard leaves almost no room for the conversation.

Needs: web
