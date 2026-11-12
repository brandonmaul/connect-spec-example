# Appointment cards

Power's Appointment Hashtags: writing an appointment's number after `A#`, like
`A#45200838`, in a message shows that appointment's Appointment Card.

**Area code:** `APPT`

**Topics**

| Topic | Covers |
|---|---|
| `TAG` | How Appointment Hashtags are written in a message |
| `CARD` | What an Appointment Card shows |
| `ACCESS` | Who can see which appointment details |
| `LINK` | What an Appointment Card's details open |

Design: [Nitro Hashtags](https://huddle.powerapp.cloud/projects/535)

### APPT-TAG-001: An Appointment Hashtag shows an Appointment Card
`req~APPT-TAG-001~1`

Writing an Appointment Hashtag in a message shows that appointment's Appointment
Card to everyone in the Conversation.

    Given a person writes "Can someone cover A#45200838 tomorrow?"
    When the message is sent
    Then everyone in the Conversation sees the Appointment Card for appointment 45200838

Rationale:
Talking about a specific appointment is constant at Power. The card saves everyone looking it up in Nitro.

Needs: ccl, browser, pwa, macos, ios

### APPT-TAG-002: How an Appointment Hashtag is written
`req~APPT-TAG-002~1`

An Appointment Hashtag is `A#` or `a#` followed by the appointment number with no
space.

    Given a message contains "a#45200838" and "A# 99"
    When it is sent
    Then it shows an Appointment Card for appointment 45200838
    And no Appointment Card for 99

Rationale:
People type tags quickly. The rule has to be simple and predictable.

Needs: ccl, browser, pwa, macos, ios

### APPT-TAG-003: Each appointment gets one card
`req~APPT-TAG-003~1`

A message shows one Appointment Card per appointment, in the order each was first
mentioned, however many times it is mentioned.

    Given a message says "A#2 then A#1, and A#2 again"
    When it is sent
    Then it shows a card for 2, then a card for 1

Rationale:
Repeated cards add nothing and push the Conversation View off the screen.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### APPT-TAG-004: A bare link gets no card
`req~APPT-TAG-004~1`

A message that is nothing but a web link gets no Appointment Card, even if the link
contains something that looks like an Appointment Hashtag.

    Given a person pastes only "https://example.com/page#A#123"
    When it is sent
    Then no Appointment Card is shown

Rationale:
Links are full of `#` signs. A pasted link is not someone talking about an appointment.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### APPT-TAG-005: An Appointment Hashtag can sit against other text
`req~APPT-TAG-005~1`

An Appointment Hashtag is recognised even when other text touches it, and its number
is the digits only.

    Given a message contains "blahA#3407abcd"
    When it is sent
    Then it shows an Appointment Card for appointment 3407

Rationale:
People type tags quickly and sloppily, often without spaces around them.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### APPT-CARD-001: A message of only Appointment Hashtags shows only the cards
`req~APPT-CARD-001~1`

If a message contains only Appointment Hashtags, it shows just their Appointment
Cards, without the message bubble. Any other text keeps the bubble.

    Given a person sends "A#1 A#2"
    When it is shown
    Then the Conversation View shows the two cards and no bubble
    But "A#1 xx A#2" shows the bubble as well

Rationale:
A bubble repeating the tags above the cards is noise. Any other words, though, are part of what the person said.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### APPT-CARD-002: What an Appointment Card shows
`req~APPT-CARD-002~1`

An Appointment Card shows the homeowner and their contact info, the address, the
products and lead source, the Remodeling Consultant and the appointment's status,
as far as the viewer's permissions allow.

    Given a viewer allowed to see every detail of appointment 45200838
    When they view its Appointment Card
    Then it shows the homeowner and contact info, address, products, source, Remodeling Consultant and status

Rationale:
The card has to answer the usual questions about an appointment without opening Nitro.

Needs: nitro, browser, pwa, macos, ios

### APPT-CARD-003: A card shows what it has
`req~APPT-CARD-003~1`

An Appointment Card leaves out details that are blank, and one detail it cannot read
never stops the rest of the card from showing.

    Given an appointment has no Remodeling Consultant assigned and an unreadable date
    When its card is shown
    Then the card shows everything else
    And has no empty Remodeling Consultant or date fields

Rationale:
A partial card is still useful. A broken one is not.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### APPT-CARD-004: An appointment that does not exist says so on Apple
`req~APPT-CARD-004~1`

On Apple, an Appointment Hashtag for an appointment that does not exist shows
"Appointment ID does not exist", while the message's other Appointment Cards show
normally.

    Given a message mentions A#1 and A#99999999, which does not exist
    When it is shown on macOS or iOS
    Then A#1 shows its Appointment Card
    And A#99999999 shows "Appointment ID does not exist"

Rationale:
A typo in one number should not hide the details of the others. Open: Apple says
"Appointment ID does not exist" and Web says "Appt with ID# does not exist"; is the
difference intended, and if not, which copy is correct?

Status: draft

Needs: ccl, macos, ios

### APPT-CARD-005: An Appointment Card shows the appointment's own time
`req~APPT-CARD-005~1`

An Appointment Card shows the appointment's date and time in the appointment's own
time zone.

    Given an appointment in Denver at 3pm
    When a person in Philadelphia views its Appointment Card
    Then it shows 3pm

Rationale:
The time is the customer's, so it is shown in their time zone.

Status: draft

Needs: browser, pwa, macos, ios

### APPT-CARD-006: An Appointment Card refreshes when the Conversation reopens
`req~APPT-CARD-006~1`

An Appointment Card refreshes its details each time its Conversation is reopened.

    Given an appointment's status changed in Nitro
    When a person reopens the Conversation that mentions it
    Then the Appointment Card shows the new status

Rationale:
Appointments change all day; a card should not show yesterday's status.

Needs: browser, pwa, macos, ios

### APPT-CARD-007: An appointment that does not exist says so on Web
`req~APPT-CARD-007~1`

On Web, an Appointment Hashtag for an appointment that does not exist shows "Appt
with ID# does not exist".

    Given a message mentions A#99999999, which does not exist
    When it is shown in Connect Browser
    Then it shows "Appt with ID# does not exist"

Rationale:
Open: Apple says "Appointment ID does not exist" and Web says "Appt with ID# does not
exist"; is the difference intended, and if not, which copy is correct?

Status: draft

Needs: browser, pwa

### APPT-ACCESS-001: Nitro permissions decide which details a person sees
`req~APPT-ACCESS-001~1`

Everyone sees an Appointment Card, but each person sees only the appointment details
their Nitro permissions allow.

    Given a person without permission to see homeowner contact info
    When they view an Appointment Card
    Then it shows no phone numbers or address

Rationale:
Homeowners' contact details are private. Connect must not show more than Nitro would.

Needs: nitro

### APPT-ACCESS-002: Losing permission takes effect straight away
`req~APPT-ACCESS-002~1`

When online, an Appointment Card always shows the current details, so a removed
permission takes effect at once. Offline, it shows the last details the device saw.

    Given a person loses permission to see phone numbers
    When they next view a card while online
    Then the phone numbers are gone

Rationale:
Access to customer details has to stop when it is taken away, not whenever the device next tidies up.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### APPT-ACCESS-003: No Appointment Cards in Tempo Connect
`req~APPT-ACCESS-003~1`

Tempo Connect never shows Appointment Cards, and an Appointment Hashtag in a message
causes no error.

    Given a person using Tempo Connect writes "A#123"
    When the message is shown
    Then it shows as plain text with no card and no error

Rationale:
Stream has no appointments in Nitro.

Status: draft

Needs: ccl, macos, ios

### APPT-LINK-001: A phone number on a card opens the phone app
`req~APPT-LINK-001~1`

Tapping a phone number on an Appointment Card opens the phone app.

    Given an Appointment Card shows the homeowner's phone number
    When a person taps it
    Then the phone app opens ready to call that number

Rationale:
People look at the card to call the homeowner.

Needs: browser, pwa, macos, ios

### APPT-LINK-002: An address on a card opens the maps app
`req~APPT-LINK-002~1`

Tapping the address on an Appointment Card opens the maps app.

    Given an Appointment Card shows the home's address
    When a person taps it
    Then the maps app opens at that address

Rationale:
Crews use the card to get to the home.

Needs: browser, pwa, macos, ios

### APPT-LINK-003: On Web, the appointment number and Home ID open the Homes File
`req~APPT-LINK-003~1`

On Web, the appointment number and the Home ID on an Appointment Card open the
home's Homes File in Nitro.

    Given an Appointment Card in Connect Browser
    When a person clicks its Home ID
    Then the home's Homes File opens in Nitro

Rationale:
The Homes File holds everything else about the home.

Needs: browser, pwa

### APPT-LINK-004: On Web, the project number opens the Project page
`req~APPT-LINK-004~1`

On Web, the project number on an Appointment Card opens the Project page in Nitro.

    Given an Appointment Card in Connect Browser shows a project number
    When a person clicks it
    Then the Project page opens in Nitro

Rationale:
The Project page is where the work on the home is tracked.

Needs: browser, pwa
