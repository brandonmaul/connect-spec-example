# Corporate events

Power's corporate events: the EVENTS section at the top of the Conversation List,
whose items open links and Conversations for an event. Corporate events are not
calendar events: there is no RSVP, attendee list or reminder. Corporate events are
in Nitro Connect only; Tempo Connect has none.

**Area code:** `EVENT`

**Topics**

| Topic | Covers |
|---|---|
| `SHOW` | When an event shows and who sees it |
| `ORDER` | The order of events and of their items |
| `TAP` | What an event's items open |
| `REFRESH` | Keeping events up to date |

Design: [Events](https://huddle.powerapp.cloud/projects/601)

### EVENT-SHOW-001: Events show in the EVENTS section of the Conversation List
`req~EVENT-SHOW-001~1`

Corporate events show in the EVENTS section, the first section of the Conversation
List, above Favorites, ROOMS and PEOPLE.

    Given the Power Summit event is showing
    When a person opens their Conversation List
    Then the EVENTS section is at the top
    And it lists the Power Summit's items

Rationale:
Everything a person needs for an event is one tap from where they already are.

Needs: browser, pwa, macos, ios

### EVENT-SHOW-002: An event shows exactly between its start and stop times
`req~EVENT-SHOW-002~1`

An event appears at the moment it is set to start showing and disappears at the
moment it is set to stop, judged by Connect's clock, not the device's.

    Given an event is set to stop showing at 10:00
    When it is 10:00
    Then the event is gone from the EVENTS section
    Even on a phone whose clock is a few minutes wrong

Rationale:
Organisers time events to the minute. An event that lingers or appears early points people at the wrong thing.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### EVENT-SHOW-003: The company decides who sees each event
`req~EVENT-SHOW-003~1`

Who sees an event, and which of its items, is decided in Nitro: attendees, the
people sharing their accommodation, and preview users, with items filtered by
territory.

    Given an event is for Philadelphia attendees
    When a person from Atlanta who is not attending opens Connect
    Then they do not see the event

Rationale:
Events are organised per person and territory. Showing everyone everything would bury the items that matter.

Status: draft

Needs: nitro

### EVENT-SHOW-004: Event dates are for display
`req~EVENT-SHOW-004~1`

The dates shown on an event are when it takes place. They do not decide when the
event shows in the EVENTS section, which often starts days before.

    Given an event takes place on 12 March and starts showing on 1 March
    When a person opens Connect on 5 March
    Then the event shows in the EVENTS section, with the date 12 March

Rationale:
People need the event in front of them before it starts.

Status: draft

Needs: browser, pwa, macos, ios

### EVENT-SHOW-005: No corporate events in Tempo Connect
`req~EVENT-SHOW-005~1`

Tempo Connect has no EVENTS section.

    Given a person using Tempo Connect
    When they open their Conversation List
    Then there is no EVENTS section

Rationale:
Corporate events are a Power program; Stream does not use them.

Needs: macos, ios

### EVENT-SHOW-006: The EVENTS section is expanded at login
`req~EVENT-SHOW-006~1`

When a person logs in, the EVENTS section starts expanded.

    Given a person collapsed the EVENTS section
    When they log out and log in again
    Then the EVENTS section is expanded

Rationale:
A fresh login is when people most need to see what events are on.

Needs: browser, pwa, macos, ios

### EVENT-SHOW-007: An event is removed after its show-until date
`req~EVENT-SHOW-007~1`

An event is removed from the EVENTS section after its show-until date.

    Given an event's show-until date is 12 March
    When a person opens Connect on 13 March
    Then the event is not in the EVENTS section

Rationale:
Past events crowd out the Conversations people need.

Needs: nitro, browser, pwa, macos, ios

### EVENT-SHOW-008: Events come from Nitro
`req~EVENT-SHOW-008~1`

In Nitro Connect only, the EVENTS section shows the corporate events set up in Nitro.

    Given organisers set up the Power Summit event in Nitro
    When a person who should see it opens Connect
    Then the Power Summit is in their EVENTS section

Rationale:
Events are organised in Nitro, so Connect shows what Nitro holds rather than keeping its own copy.

Needs: nitro, browser, pwa, macos, ios

### EVENT-ORDER-001: The newest event comes first
`req~EVENT-ORDER-001~1`

When several events are showing, the one that started showing most recently is
first. An event's items keep the order the organisers set.

    Given event A started showing on Monday and event B on Wednesday
    When a person opens Connect
    Then B is listed above A

Rationale:
The newest event is the one people are most likely looking for.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### EVENT-TAP-001: Event items open a link, the Self Message, a DM or a Room
`req~EVENT-TAP-001~1`

An item in the EVENTS section opens what it points to: a link, the person's own Self
Message, a DM, or a Room.

    Given an event has an item for the event's Q&A Room
    When a person taps it
    Then the Q&A Room opens

Rationale:
Event items are shortcuts. They should land the person exactly where the organiser meant.

Needs: browser, pwa, macos, ios

### EVENT-TAP-002: An event item for a hidden Conversation brings it back
`req~EVENT-TAP-002~1`

Opening an event's item for a Conversation the person has hidden opens it and puts
it back in their Conversation List.

    Given a person hid the event's Q&A Room
    When they tap its item in the EVENTS section
    Then the Room opens
    And it is back in their Conversation List

Rationale:
The person chose to go there, so it should behave like any Conversation they are using.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### EVENT-TAP-003: Items the app cannot open are shown as inactive
`req~EVENT-TAP-003~1`

An item a client cannot open, such as a Nitro page on iOS, is shown as inactive or
left out, never as an item that does nothing.

    Given an event has an item linking to a Nitro page
    When a person views it on iOS
    Then the item is shown as inactive or not shown

Rationale:
An item that does nothing when tapped looks broken.

Status: draft

Needs: browser, pwa, macos, ios

### EVENT-TAP-004: An event item for a new DM starts it
`req~EVENT-TAP-004~1`

An event's item for a DM with someone the person has never messaged starts that DM.

    Given an event has an item for the person running registration
    And I have never messaged them
    When I tap the item
    Then a DM with them opens, ready to write in

Rationale:
Event items should work the first time, without the person having to find the right colleague.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### EVENT-REFRESH-001: Events appear straight away on opening
`req~EVENT-REFRESH-001~1`

When Connect opens, the events it last knew about show straight away, and are then
brought up to date.

    Given a person saw the Power Summit event yesterday
    When they open Connect today without a connection
    Then the Power Summit still shows in the EVENTS section

Rationale:
During an event people open Connect to find their next session, often on poor venue Wi-Fi.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### EVENT-REFRESH-002: A failed update never empties the events
`req~EVENT-REFRESH-002~1`

If Connect cannot get the latest events, it keeps showing the ones it has.

    Given the EVENTS section shows events
    When Connect fails to fetch an update
    Then the events it had are still shown

Rationale:
Losing the event items because of a network blip would strand people at the event.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### EVENT-REFRESH-003: Events refresh every 15 minutes
`req~EVENT-REFRESH-003~1`

The EVENTS section refreshes every 15 minutes, so changes organisers make reach
people within 15 minutes.

    Given an organiser adds an item to an event
    When 15 minutes have passed
    Then everyone who sees the event sees the new item

Rationale:
Plans change during events, and people need the current items the same morning.

Needs: ccl, browser, pwa, macos, ios

### EVENT-REFRESH-004: Expanding the EVENTS section refreshes it
`req~EVENT-REFRESH-004~1`

Expanding the EVENTS section refreshes its events.

    Given an organiser added an item to an event a minute ago
    When a person expands the EVENTS section
    Then the new item is shown

Rationale:
A person who opens the section is looking for the latest items now, not in 15 minutes.

Needs: browser, pwa, macos, ios
