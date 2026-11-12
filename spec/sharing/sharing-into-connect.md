# Sharing into Connect

Sending photos, files and links to Connect from another app, through the device's
share menu: the Share Extension in Apple apps on macOS and iOS, and Google Photos on
Android (the PWA).

**Area code:** `SHARE`

**Topics**

| Topic | Covers |
|---|---|
| `SHEET` | Connect in other apps' share menus |
| `PICK` | Choosing where shared content goes |
| `LINK` | Sharing links and places |
| `FILE` | Sharing photos and files |
| `FAIL` | When sharing goes wrong |

Design: [Attachments](https://huddle.powerapp.cloud/projects/570)

### SHARE-SHEET-001: Connect is in Apple apps' share menus
`req~SHARE-SHEET-001~1`

On macOS and iOS, Connect appears in other apps' share menus.

    Given a person selects three photos in their Photos app on iOS
    When they tap Share
    Then Connect is one of the choices

Rationale:
Most things people want to send start in another app.

Needs: macos, ios

### SHARE-SHEET-002: Connect is called Connect in the share menu
`req~SHARE-SHEET-002~1`

In the share menu, Connect is listed under its own name.

    Given a person opens the share menu on their iPhone
    Then Connect is listed as "Connect"

Rationale:
People look for the app's name. Anything else and they will not find it. Open: is it
listed as "Connect" or "Nitro Connect"?

Status: draft

Needs: pwa, macos, ios

### SHARE-SHEET-003: Connect is in Google Photos' share menu on Android
`req~SHARE-SHEET-003~1`

On Android, Connect appears in Google Photos' share menu.

    Given a person selects a photo in Google Photos on Android
    When they tap Share
    Then Connect is one of the choices

Rationale:
Photos of jobs are the thing people most often send from their phone.

Needs: pwa

### SHARE-SHEET-004: On macOS, Connect is enabled in the share menu once
`req~SHARE-SHEET-004~1`

On macOS, a person enables Connect in the share menu once, and it is there from then
on.

    Given a person has never shared to Connect on their Mac
    When they enable Connect in the share menu
    Then Connect is in the share menu every time after

Rationale:
macOS only lists share options the person has turned on, so it has to be done once.

Needs: macos

### SHARE-PICK-001: Sharing opens a new message with the content in it
`req~SHARE-PICK-001~1`

Sharing to Connect opens Connect's New Message flow with the shared content already
attached, and asks the person to choose a Conversation.

    Given a person shares a PDF to Connect
    Then Connect opens on New Message
    And the PDF is already attached
    And it says "Select a conversation to continue"

Rationale:
The person has already chosen what to send. All that is left is where.

Status: draft

Needs: pwa, macos, ios

### SHARE-PICK-002: The person reviews and sends from the Conversation
`req~SHARE-PICK-002~1`

Once a Conversation is chosen, the shared content moves into that Conversation's
Message Composer, where the person can add a message and send it.

    Given a person shared two photos and chose Dana
    Then their DM with Dana opens
    And the two photos are in the Message Composer, ready to send
    And nothing is sent until the person sends it

Rationale:
Sending without seeing the Conversation risks putting something in the wrong place, and leaves no chance to say what it is.

Status: draft

Needs: pwa, macos, ios

### SHARE-PICK-003: Sharing to someone new starts a Conversation
`req~SHARE-PICK-003~1`

If the person shares to someone they have no Conversation with yet, a DM or group
conversation is started with them.

    Given a person shares a photo and picks Sam, whom they have never messaged
    Then a DM with Sam opens with the photo ready to send

Rationale:
Sharing is often how a Conversation starts.

Status: draft

Needs: pwa, macos, ios

### SHARE-LINK-001: A shared web page arrives as its link
`req~SHARE-LINK-001~1`

Sharing a web page puts its link in the message.

    Given a person shares a page from their browser
    Then the message contains that page's link

Rationale:
The link is what lets others open the same page.

Status: draft

Needs: macos, ios

### SHARE-LINK-002: A shared place arrives as a map link
`req~SHARE-LINK-002~1`

Sharing a place from a maps app puts a map link with the place's name in the
message.

    Given a person shares a job site from Apple Maps
    Then the message contains a map link with the job site's name

Rationale:
Crews share locations all the time. A link opens the place in anyone's maps app.

Status: draft

Needs: ios

### SHARE-LINK-003: Sharing files with a link keeps both
`req~SHARE-LINK-003~1`

When files and a link are shared together, the files are attached and the link is
put in the message.

    Given a person shares a photo and a link together
    Then the photo is attached
    And the link is in the message

Rationale:
Open: when files and a link are shared together, should both be kept, or only the
files?

Status: draft

Needs: pwa, macos, ios

### SHARE-FILE-001: Shared files keep their names
`req~SHARE-FILE-001~1`

Shared files arrive with their original names.

    Given a person shares "Roof estimate.pdf"
    Then it arrives as "Roof estimate.pdf"

Rationale:
The name is often how people know which file is which.

Status: draft

Needs: pwa, macos, ios

### SHARE-FILE-002: Shared files keep their order
`req~SHARE-FILE-002~1`

Shared files are attached in the order the person selected them.

    Given a person selects photos 1, 2 and 3, in that order, and shares them
    Then they are attached as 1, 2, 3

Rationale:
Photos of a job are often a sequence: before, during, after.

Status: draft

Needs: pwa, macos, ios

### SHARE-FILE-003: At most 6 images are shared at once from Apple apps
`req~SHARE-FILE-003~1`

On macOS and iOS, Connect's share menu option is not for more than 6 images at
once.

    Given a person selects 7 photos in their Photos app on iOS
    When they open the share menu
    Then Connect does not take all 7 from the share menu

Rationale:
Sharing is for a few items quickly; larger sets are added from the Message Composer.

Needs: macos, ios

### SHARE-FAIL-001: A failed share says so and can be closed
`req~SHARE-FAIL-001~1`

If something goes wrong while sharing to Connect, the person is told, and can close
the share screen and go back to what they were doing.

    Given sharing a file to Connect fails
    Then the person sees that it did not work
    And they can close the share screen

Rationale:
A share screen that cannot be closed traps the person in the other app.

Status: draft

Needs: pwa, macos, ios

### SHARE-FAIL-002: Nothing is shared halfway
`req~SHARE-FAIL-002~1`

If one of several shared items cannot be loaded, the person is told, and nothing is
sent until they decide.

    Given a person shares five photos and one cannot be read
    Then they are told
    And nothing is sent

Rationale:
Sending part of a set without saying so leaves others with a misleading picture.

Status: draft

Needs: pwa, macos, ios
