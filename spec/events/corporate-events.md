# Corporate events

Power's corporate events: a banner with a list of links, shown above the conversation list while an event is on. Corporate events are not calendar events: there is no RSVP, attendee list or reminder. Stream Financial has no corporate events.

**Area code:** `EVENT`

**Topics**

| Topic | Covers |
|---|---|
| `SHOW` | When an event shows and who sees it |
| `ORDER` | The order of events and of their links |
| `TAP` | What tapping an event's links does |
| `REFRESH` | Keeping events up to date |

Design: <figma link> · Runway: <epic link>

### EVENT-SHOW-001: An event shows as a banner above the conversation list
`req~EVENT-SHOW-001~1`

While a corporate event is on, its banner shows above the conversation list and
opens into its sections of links.

    Given the Power Summit event is on
    When a person opens their conversation list
    Then the Power Summit banner is at the top
    And tapping it shows the event's sections and links

Rationale:
Everything a person needs for an event is one tap from where they already are.

Needs: ios, macos, web

### EVENT-SHOW-002: An event shows exactly between its start and stop times
`req~EVENT-SHOW-002~1`

An event appears at the moment it is set to start showing and disappears at the
moment it is set to stop, judged by Connect's clock, not the device's.

    Given an event is set to stop showing at 10:00
    When it is 10:00
    Then the banner is gone
    Even on a phone whose clock is a few minutes wrong

Rationale:
Organisers time events to the minute. A banner that lingers or appears early points people at the wrong thing.

Needs: ccl, ios, macos, web

### EVENT-SHOW-003: The company decides who sees each event
`req~EVENT-SHOW-003~1`

Who sees an event, and which of its links, is decided in Nitro: attendees, the
people sharing their accommodation, and preview users, with links filtered by territory.

    Given an event is for Philadelphia attendees
    When a person from Atlanta who is not attending opens Connect
    Then they do not see the event

Rationale:
Events are organised per person and territory. Showing everyone everything would bury the links that matter.

Needs: nitro

### EVENT-SHOW-004: Event dates are for display
`req~EVENT-SHOW-004~1`

The dates shown on an event are when it takes place. They do not decide when the
banner shows, which often starts days before.

    Given an event takes place on 12 March and starts showing on 1 March
    When a person opens Connect on 5 March
    Then the banner shows, with the date 12 March

Rationale:
People need the event in front of them before it starts.

Needs: ios, macos, web

### EVENT-SHOW-005: No corporate events at Stream Financial
`req~EVENT-SHOW-005~1`

Stream Financial people never see corporate events, and nothing about their being
unavailable gets in the way.

    Given a Stream Financial person
    When they open Connect
    Then there is no corporate events area
    And no loading spinner or error for it

Rationale:
Stream Financial does not use corporate events. An empty or broken space would look like a fault.

Needs: ccl, ios, macos, web

### EVENT-ORDER-001: The newest event comes first
`req~EVENT-ORDER-001~1`

When several events are showing, the one that started showing most recently is
first. Sections and links keep the order the organisers set.

    Given event A started showing on Monday and event B on Wednesday
    When a person opens Connect
    Then B is listed above A

Rationale:
The newest event is the one people are most likely looking for.

Needs: ccl, ios, macos, web

### EVENT-TAP-001: Event links open where they point
`req~EVENT-TAP-001~1`

Tapping an event's link opens what it points to: a web page in the browser, a
conversation, or a Direct conversation with a person, which is created if it does not
exist yet.

    Given an event has a link to the person running registration
    And I have never messaged them
    When I tap the link
    Then a Direct conversation with them opens, ready to write in

Rationale:
Event links are shortcuts. They should land the person exactly where the organiser meant.

Needs: ccl, ios, macos, web

### EVENT-TAP-002: An event link to a hidden conversation brings it back
`req~EVENT-TAP-002~1`

Tapping an event's link to a conversation the person has hidden opens it and puts it
back in their list.

    Given a person hid the event's Q&A conversation
    When they tap its link in the event
    Then the conversation opens
    And it is back in their conversation list

Rationale:
The person chose to go there, so it should behave like any conversation they are using.

Needs: ccl, ios, macos, web

### EVENT-TAP-003: Links the app cannot open are shown as inactive
`req~EVENT-TAP-003~1`

A link an app cannot open, such as a Nitro page in the iPhone app, is shown as
inactive or left out, never as a link that does nothing.

    Given an event has a link to a Nitro page
    When a person views it in the iPhone app
    Then the link is shown as inactive or not shown

Rationale:
A link that does nothing when tapped looks broken.

Needs: ios, macos, web

### EVENT-REFRESH-001: Events appear straight away on opening
`req~EVENT-REFRESH-001~1`

When Connect opens, the events it last knew about show straight away, and are then
brought up to date.

    Given a person saw the Power Summit banner yesterday
    When they open Connect today without a connection
    Then the banner still shows

Rationale:
During an event people open Connect to find their next session, often on poor venue Wi-Fi.

Needs: ccl, ios, macos, web

### EVENT-REFRESH-002: A failed update never empties the events
`req~EVENT-REFRESH-002~1`

If Connect cannot get the latest events, it keeps showing the ones it has.

    Given the events are showing
    When Connect fails to fetch an update
    Then the events it had are still shown

Rationale:
Losing the event links because of a network blip would strand people at the event.

Needs: ccl, ios, macos, web

### EVENT-REFRESH-003: Changes to an event show within 15 minutes
`req~EVENT-REFRESH-003~1`

Changes organisers make to an event reach people within 15 minutes.

    Given an organiser adds a link to an event
    When 15 minutes have passed
    Then everyone who sees the event sees the new link

Rationale:
Plans change during events, and people need the current links the same morning.

Needs: ccl, ios, macos, web
