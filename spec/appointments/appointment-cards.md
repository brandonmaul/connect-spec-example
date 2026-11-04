# Appointment cards

Power's appointment cards: writing an appointment's tag, like `A#12345`, in a message shows that appointment's details under it. Stream Financial has no appointment cards.

**Area code:** `APPT`

**Topics**

| Topic | Covers |
|---|---|
| `TAG` | How appointments are written in a message |
| `CARD` | What an appointment card shows |
| `ACCESS` | Who can see which appointment details |

Design: <figma link> · Runway: <epic link>

### APPT-TAG-001: An appointment tag shows a card
`req~APPT-TAG-001~1`

Writing an appointment's tag, `A#` followed by its number, in a message shows that
appointment's card under the message.

    Given a person writes "Can someone cover A#12345 tomorrow?"
    When the message is sent
    Then everyone in the conversation sees the card for appointment 12345 under it

Rationale:
Talking about a specific appointment is constant at Power. The card saves everyone looking it up in Nitro.

Needs: ccl

### APPT-TAG-002: How an appointment tag is written
`req~APPT-TAG-002~1`

A tag is `A#` or `a#` followed straight away by digits. It can sit against other
text, a space breaks it, and its number is the digits only.

    Given a message contains "blahA#3407abcd" and "A# 99"
    When it is sent
    Then it shows a card for appointment 3407
    And no card for 99

Rationale:
People type tags quickly and sloppily. The rule has to be simple and predictable.

Needs: ccl

### APPT-TAG-003: Each appointment gets one card
`req~APPT-TAG-003~1`

A message shows one card per appointment, in the order each was first mentioned,
however many times it is mentioned.

    Given a message says "A#2 then A#1, and A#2 again"
    When it is sent
    Then it shows a card for 2, then a card for 1

Rationale:
Repeated cards add nothing and push the conversation off the screen.

Needs: ccl

### APPT-TAG-004: A bare link gets no card
`req~APPT-TAG-004~1`

A message that is nothing but a web link gets no appointment card, even if the link
contains something that looks like a tag.

    Given a person pastes only "https://example.com/page#A#123"
    When it is sent
    Then no appointment card is shown

Rationale:
Links are full of `#` signs. A pasted link is not someone talking about an appointment.

Needs: ccl

### APPT-CARD-001: A message of only tags shows only the cards
`req~APPT-CARD-001~1`

If a message contains only appointment tags, it shows just their cards, without the
message bubble. Any other text keeps the bubble.

    Given a person sends "A#1 A#2"
    When it is shown
    Then the conversation shows the two cards and no bubble
    But "A#1 xx A#2" shows the bubble as well

Rationale:
A bubble repeating the tags above the cards is noise. Any other words, though, are part of what the person said.

Needs: ccl, ios, macos, web

### APPT-CARD-002: What an appointment card shows
`req~APPT-CARD-002~1`

A card shows the appointment's date and time in the appointment's own time zone, the
home and its homeowners, phone numbers, products pitched, lead source, assigned rep,
project and a link to it in Nitro.

    Given an appointment in Denver at 3pm
    When a person in Philadelphia views its card
    Then it shows 3pm
    And the homeowners, home, phone numbers and a link to the appointment in Nitro

Rationale:
The card has to answer the usual questions about an appointment without opening Nitro. The time is the customer's, so it is shown in their time zone.

Needs: ios, macos, web

### APPT-CARD-003: A card shows what it has
`req~APPT-CARD-003~1`

A card leaves out details that are blank, and one detail it cannot read never stops
the rest of the card from showing.

    Given an appointment has no rep assigned and an unreadable date
    When its card is shown
    Then the card shows everything else
    And has no empty rep or date fields

Rationale:
A partial card is still useful. A broken one is not.

Needs: ccl

### APPT-CARD-004: An unknown appointment says so on its card
`req~APPT-CARD-004~1`

A tag for an appointment that does not exist shows a "not found" card for it, while
the message's other cards show normally.

    Given a message mentions A#1 and A#99999999, which does not exist
    When it is shown
    Then A#1 shows its card
    And A#99999999 shows as not found

Rationale:
A typo in one number should not hide the details of the others.

Needs: ccl, ios, macos, web

### APPT-ACCESS-001: Nitro permissions decide which details a person sees
`req~APPT-ACCESS-001~1`

Each person sees only the appointment details their Nitro permissions allow, such as
phone numbers and address, or who issued it.

    Given a person without permission to see appointment status details
    When they view an appointment card
    Then it shows no phone numbers or address

Rationale:
Homeowners' contact details are private. Connect must not show more than Nitro would.

Needs: nitro

### APPT-ACCESS-002: Losing permission takes effect straight away
`req~APPT-ACCESS-002~1`

When online, a card always shows the current details, so a removed permission takes
effect at once. Offline, it shows the last details the device saw.

    Given a person loses permission to see phone numbers
    When they next view a card while online
    Then the phone numbers are gone

Rationale:
Access to customer details has to stop when it is taken away, not whenever the device next tidies up.

Needs: ccl

### APPT-ACCESS-003: No appointment cards at Stream Financial
`req~APPT-ACCESS-003~1`

Stream Financial people never see appointment cards, and an appointment-like tag in
their messages causes no error.

    Given a Stream Financial person writes "A#123"
    When the message is shown
    Then it shows as plain text with no card and no error

Rationale:
Stream Financial has no appointments in Nitro.

Needs: ccl
