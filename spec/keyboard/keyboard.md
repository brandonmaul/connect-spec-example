# Keyboard

Using Connect from the keyboard: shortcut keys, moving around without a mouse, and
what Esc does. The goal is one set of keys across Browser, PWA, macOS, and iOS with a
keyboard, with no clashes with the operating system or browser. Keys that exist today
are agreed; proposed keys are drafts.

**Area code:** `KEYS`

**Topics**

| Topic | Covers |
|---|---|
| `REACH` | Everything in Connect can be used from the keyboard, with the same keys on every client |
| `ACTION` | Keys that start an action |
| `COMPOSE` | Keys in the Message Composer |
| `MOVE` | Moving between fields, results, conversations and messages |
| `CLOSE` | What Esc does |

Design: [Keyboard](https://huddle.powerapp.cloud/projects/1047) · [Start a Message](https://huddle.powerapp.cloud/projects/497)

### KEYS-REACH-001: Interactive parts of Connect can be reached by keyboard
`req~KEYS-REACH-001~1`

Every interactive part of Connect can be reached and used from the keyboard.

    Given a person using Connect with only a keyboard
    When they move through a screen
    Then every button, field and menu on it can be reached and used

Rationale:
People who work from the keyboard, or cannot use a mouse, must be able to do everything in Connect.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-REACH-002: Shortcuts are the same on every client
`req~KEYS-REACH-002~1`

Each shortcut uses the same keys on Browser, PWA, macOS and iOS with a keyboard, and
none clashes with an operating system or browser shortcut.

    Given a person who uses Connect on macOS and in the Browser
    When they use a shortcut they learned on one
    Then it does the same thing on the other

Rationale:
One set of keys means people learn them once. Open: what do they map to with Ctrl on Windows and ChromeOS, and do ⌘ + N and ⌘ + , clash with the browser?

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-ACTION-001: ⌘ + N starts a new message
`req~KEYS-ACTION-001~1`

On macOS, ⌘ + N opens the New Message flow from anywhere in Connect.

    Given a person is anywhere in Connect on macOS
    When they press ⌘ + N
    Then the New Message flow opens

Rationale:
Starting a conversation is one of the most common actions, and ⌘ + N is the standard Mac key for "new".

Needs: macos

### KEYS-ACTION-002: Holding Shift while dropping a file sends it at once
`req~KEYS-ACTION-002~1`

On Desktop, holding Shift while dropping a file into a Conversation sends it
immediately instead of adding it as a draft.

    Given a person has a Conversation open on Desktop
    When they hold Shift and drop a file onto it
    Then the file is sent straight away, without a draft to confirm

Rationale:
People who already know the file is right can skip the extra step.

Needs: browser, pwa, macos

### KEYS-ACTION-003: ⌘ + ⇧ + F searches in the Conversation
`req~KEYS-ACTION-003~1`

In the Conversation View, ⌘ + ⇧ + F opens search in the open Conversation.

    Given a person has a Conversation open
    When they press ⌘ + ⇧ + F
    Then search in that Conversation opens

Rationale:
Searching a Conversation should not need the mouse.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-ACTION-004: ⌘ + F stays the browser's Find
`req~KEYS-ACTION-004~1`

On Web, Connect does not take over ⌘ + F; it still opens the browser's own Find.

    Given a person has a Conversation open in the Browser
    When they press ⌘ + F
    Then the browser's Find opens, not Connect's search

Rationale:
People rely on the browser's Find everywhere; taking it over would clash with what they expect.

Status: draft

Needs: browser, pwa

### KEYS-COMPOSE-001: Enter sends
`req~KEYS-COMPOSE-001~1`

In the Message Composer, Enter sends the Message.

    Given a person has typed a Message in the Message Composer
    When they press Enter
    Then the Message is sent

Rationale:
Sending with Enter is what people expect from a chat app with a keyboard.

Status: draft

Needs: browser, macos, ios

### KEYS-COMPOSE-002: ⇧ + Enter adds a new line
`req~KEYS-COMPOSE-002~1`

In the Message Composer, ⇧ + Enter adds a new line instead of sending.

    Given a person is typing in the Message Composer
    When they press ⇧ + Enter
    Then a new line is added and nothing is sent

Rationale:
People need a way to write more than one line when Enter sends.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-COMPOSE-003: In the PWA, Enter adds a new line
`req~KEYS-COMPOSE-003~1`

In the PWA, Enter in the Message Composer adds a new line; the Message is sent with
the send button.

    Given a person is typing in the Message Composer in the PWA
    When they press Enter
    Then a new line is added and nothing is sent

Rationale:
On a phone keyboard, Enter is where people expect a new line, and an accidental send cannot be taken back.

Status: draft

Needs: pwa

### KEYS-COMPOSE-004: ↑ in an empty Message Composer edits the last sent Message
`req~KEYS-COMPOSE-004~1`

Pressing ↑ in an empty Message Composer starts editing the person's last sent Message.

    Given a person's Message Composer is empty
    When they press ↑
    Then their last sent Message in that Conversation opens for editing

Rationale:
Fixing a typo just sent is common, and should not need the mouse.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-MOVE-001: Enter selects a typeahead result
`req~KEYS-MOVE-001~1`

In a typeahead, Enter selects the highlighted result.

    Given a person has typed "@kel" and Kelly is highlighted in the suggestions
    When they press Enter
    Then Kelly is selected

Rationale:
People should be able to pick a result without leaving the keyboard.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-MOVE-002: Tab and ⇧ + Tab move between fields
`req~KEYS-MOVE-002~1`

Tab moves to the next field and ⇧ + Tab to the previous one, anywhere in Connect.

    Given a person is in a field in Create a Room
    When they press Tab
    Then the next field is focused
    And ⇧ + Tab returns to the previous one

Rationale:
Tab is the standard way to move between fields on every platform.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-MOVE-003: ↑ and ↓ scroll the Conversation View
`req~KEYS-MOVE-003~1`

In the Conversation View, ↑ and ↓ scroll through the Messages.

    Given a person has a Conversation open
    When they press ↓
    Then the Conversation View scrolls down

Rationale:
Reading history should not need the mouse or trackpad.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-MOVE-004: ⌘ + ↓ jumps to the newest Message
`req~KEYS-MOVE-004~1`

In the Conversation View, ⌘ + ↓ jumps to the newest Message.

    Given a person has scrolled up in a Conversation
    When they press ⌘ + ↓
    Then the Conversation View jumps to the newest Message

Rationale:
After reading back, people need a quick way to return to the latest Messages.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-MOVE-005: Tab moves between Conversation List section headers and search
`req~KEYS-MOVE-005~1`

In the Conversation List, Tab moves between the section headers and the Search
conversations field.

    Given focus is on the ROOMS section header
    When the person presses Tab
    Then focus moves to the next section header, or to the Search conversations field

Rationale:
The Conversation List is long; moving section by section gets people where they want faster than one row at a time.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-MOVE-006: Space collapses a Conversation List section
`req~KEYS-MOVE-006~1`

In the Conversation List, Space on a focused section header collapses that section.

    Given focus is on the PEOPLE section header and the section is expanded
    When the person presses Space
    Then the PEOPLE section collapses

Rationale:
Collapsing sections should be possible without the mouse, like everything else in the list.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-MOVE-007: ↑ and ↓ move between Conversations
`req~KEYS-MOVE-007~1`

In the Conversation List, ↑ and ↓ move between Conversations.

    Given focus is on a Conversation in the Conversation List
    When the person presses ↓
    Then focus moves to the next Conversation

Rationale:
Moving through the list from the keyboard lets people switch Conversations without the mouse.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-CLOSE-001: Every interactive part of Connect defines what Esc does
`req~KEYS-CLOSE-001~1`

Every interactive part of Connect has a defined result for Esc.

    Given a person is in any interactive part of Connect
    When they press Esc
    Then the defined result for that part happens, never nothing unexpected

Rationale:
Esc is how people back out from the keyboard; it must always do something they can predict.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-CLOSE-002: Esc closes a modal
`req~KEYS-CLOSE-002~1`

Esc closes the open modal.

    Given Room Info is open
    When the person presses Esc
    Then Room Info closes

Rationale:
Esc is the standard way to dismiss a modal.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-CLOSE-003: Esc closes search
`req~KEYS-CLOSE-003~1`

Esc closes an open search.

    Given search in a Conversation is open
    When the person presses Esc
    Then search closes

Rationale:
People should be able to leave search without reaching for the mouse.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-CLOSE-004: Esc exits editing without saving
`req~KEYS-CLOSE-004~1`

Esc stops editing a Message without saving the changes.

    Given a person is editing one of their Messages
    When they press Esc
    Then editing stops and the Message is unchanged

Rationale:
Esc means "cancel"; it must never save a change the person was backing out of.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-CLOSE-005: Esc goes back in panels
`req~KEYS-CLOSE-005~1`

In a panel, Esc goes back one step.

    Given a person has moved one step into a panel
    When they press Esc
    Then the panel goes back to the previous step

Rationale:
Going back one step at a time lets people retrace their path without losing their place.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-CLOSE-006: Esc deselects in the Conversation List
`req~KEYS-CLOSE-006~1`

In the Conversation List, Esc deselects the selected Conversation.

    Given a Conversation is selected in the Conversation List
    When the person presses Esc
    Then it is no longer selected

Rationale:
People need a keyboard way to clear a selection they did not mean to make.

Status: draft

Needs: browser, pwa, macos, ios

### KEYS-CLOSE-007: Esc does not discard a draft
`req~KEYS-CLOSE-007~1`

Pressing Esc in the Message Composer does not discard the draft.

    Given a person has a draft in the Message Composer
    When they press Esc
    Then the draft is kept

Rationale:
Open: should Esc ever discard a draft?

Status: draft

Needs: browser, pwa, macos, ios
