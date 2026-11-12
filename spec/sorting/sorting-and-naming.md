# Sorting and naming

How every list and search in Connect is ordered, and how the order of names in a
group conversation's name is decided. Other areas point here instead of stating
their own sort. For product owners writing acceptance criteria: state the sort and
the tiebreaker by pointing to a rule here.

**Area code:** `SORT`

**Topics**

| Topic | Covers |
|---|---|
| `ORDER` | Rules every list and search follows: a fixed order, a final tiebreaker, the same order on every client, and how text is compared |
| `MATCH` | How search results are ranked against what the person typed |
| `LIST` | The order of named lists: the Corporate Directory, the Conversation List sorted Alphabetical, and the Members List |
| `NAME` | The order of names in a group conversation's name |

Design: [Conversation List](https://huddle.powerapp.cloud/projects/495) · [Corporate Directory](https://huddle.powerapp.cloud/projects/501) · [Message Composer](https://huddle.powerapp.cloud/projects/511)

### SORT-ORDER-001: Every list sorts the same way every time
`req~SORT-ORDER-001~1`

Every list and search in Connect has a fixed order, so the same items always come
out in the same order.

    Given a person searches for "sales" twice with nothing changed in between
    When the results appear the second time
    Then they are in exactly the same order as the first time

Rationale:
People learn where things are in a list; an order that shuffles on its own makes them hunt and distrust what they see.

Needs: server, browser, pwa, macos, ios

### SORT-ORDER-002: The unique ID breaks the last tie
`req~SORT-ORDER-002~1`

When two items are equal on every other part of a sort, their unique ID decides
which comes first.

    Given two Rooms are both named "Philly Sales"
    And they are equal on every other part of the sort
    When a list shows both
    Then they always appear in the same order, decided by each Room's unique ID

Rationale:
Names are not unique, so without a final tiebreaker two equal items could swap places between loads.

Needs: server, browser, pwa, macos, ios

### SORT-ORDER-003: All clients show the same order
`req~SORT-ORDER-003~1`

Lists and searches are ordered by one shared service, so Browser, PWA, macOS and
iOS show the same items in the same order.

    Given a person searches for "sales" on macOS and on the PWA
    When the results appear on both
    Then both show the same results in the same order

Rationale:
People move between devices; a list that orders differently on each one looks broken and makes them doubt which is right.

Needs: server, browser, pwa, macos, ios

### SORT-ORDER-004: Sorting and matching ignore capital letters
`req~SORT-ORDER-004~1`

Comparisons for sorting and search ignore whether letters are capital or small.

    Given a Room named "philly sales" and a Room named "Pittsburgh Sales"
    When a list is sorted A–Z
    Then "philly sales" comes before "Pittsburgh Sales"
    And searching for "PHILLY" finds "philly sales"

Rationale:
People do not think of "Philly" and "philly" as different words, and should not have to type the right capitals to find something.

Needs: server, browser, pwa, macos, ios

### SORT-ORDER-005: Sorting and matching ignore accents
`req~SORT-ORDER-005~1`

Comparisons for sorting and search ignore accents, so an accented letter sorts and
matches as its plain letter, using US English order.

    Given people named "Émile Roy" and "Emma Ruiz"
    When a person searches for "emile"
    Then "Émile Roy" is found
    And sorted A–Z, "Émile" comes before "Emma"

Rationale:
People type names without accents, and expect an accented name to be where its plain letters would put it.

Needs: server, browser, pwa, macos, ios

### SORT-MATCH-001: Best match ranks exact, then starts-with, then contains
`req~SORT-MATCH-001~1`

Search results are ranked by best match: exact matches first, then results that
start with what was typed, then results that only contain it.

    Given Rooms named "Sales", "Sales Philly" and "Philly Sales"
    When a person searches for "sales"
    Then "Sales" is first, "Sales Philly" second and "Philly Sales" third

Rationale:
The closer a result is to what the person typed, the more likely it is the one they want.

Needs: server, browser, pwa, macos, ios

### SORT-MATCH-002: Recency only breaks ties in search
`req~SORT-MATCH-002~1`

Recent activity never moves a result ahead of a better match; it only orders results
that match equally well.

    Given a Room "Philly Sales" active today and a Room "Sales Team" inactive for a year
    When a person searches for "sales"
    Then "Sales Team" comes first, because it starts with "sales"
    And "Philly Sales" comes after it, despite being more recent

Rationale:
A recently active result that matches poorly should not bury the one the person actually typed.

Needs: server, browser, pwa, macos, ios

### SORT-MATCH-003: The New Message Recent section is ordered by recency
`req~SORT-MATCH-003~1`

In the Recent section of the New Message flow, recency is the main order, not only a
tiebreaker.

    Given a person messaged Kelly an hour ago and Rex yesterday
    When they open the New Message flow
    Then Kelly appears above Rex in Recent

Rationale:
Recent exists to get a person back to whoever they talked to last; ranking it any other way defeats its purpose.

Needs: server, browser, pwa, macos, ios

### SORT-MATCH-004: Conversation and room search order
`req~SORT-MATCH-004~1`

Conversation and room search results are ordered by best match, then most recent
activity, then name A–Z.

    Given Rooms "Sales East" and "Sales West" both start with "sales"
    And "Sales West" had activity more recently
    When a person searches for "sales"
    Then "Sales West" appears before "Sales East"

Rationale:
Among equally good matches, the conversation the person used most recently is the likeliest one they are looking for; A–Z keeps the rest predictable.

Needs: server, browser, pwa, macos, ios

### SORT-MATCH-005: Before typing, @mention suggestions start with the last person to post
`req~SORT-MATCH-005~1`

When a person starts an @mention and has not typed a name yet, the suggestions start
with the last person to post in the Conversation.

    Given Ruby posted the most recent Message in a Room
    When a person types "@" in that Room's Message Composer
    Then Ruby is the first suggestion

Rationale:
The person most likely to be mentioned is the one who just spoke.

Needs: server, browser, pwa, macos, ios

### SORT-MATCH-006: User and member search order after typing
`req~SORT-MATCH-006~1`

Once a person types a name, user and member search results, including @mention
suggestions, are ordered by best match, then A–Z.

    Given members named "Alex Cruz" and "Alexis Bell"
    When a person types "@alex"
    Then both are suggested in best-match order
    And people who match equally well are listed A–Z

Rationale:
Once a name is being typed, how well it matches is the best guide to who is meant; A–Z keeps equal matches predictable.

Needs: server, browser, pwa, macos, ios

### SORT-MATCH-007: Rooms and People Conversations rank together in conversation search
`req~SORT-MATCH-007~1`

In conversation search, Rooms and People Conversations are ranked together by the
same order, with neither kind placed above the other.

    Given a Room "Kelly's Team" and a group conversation with Kelly
    When a person searches for "kelly"
    Then both are ranked by the conversation search order alone

Rationale:
Open: the conversation search example sorts alphabetically within match groups, but the rule puts recency before A–Z. Which is right, and do Rooms rank above People Conversations?

Status: draft

Needs: server, browser, pwa, macos, ios

### SORT-LIST-001: The Corporate Directory sorts people by last name
`req~SORT-LIST-001~1`

People in the Corporate Directory are sorted by last name, then first name, and shown
last name first.

    Given people named "Alex Cruz", "Bea Cruz" and "Sam Adams"
    When a person opens the People tab of the Corporate Directory
    Then they are listed as "Adams, Sam", "Cruz, Alex", "Cruz, Bea"

Rationale:
A company directory is looked up by surname, as people expect from a printed directory.

Needs: server, browser, pwa, ios

### SORT-LIST-002: Alphabetical sorts the Conversation List by conversation name
`req~SORT-LIST-002~1`

When the Conversation List is sorted Alphabetical, Conversations are ordered by their
name, A–Z.

    Given a person's Conversation List is sorted Alphabetical
    And they have Rooms named "Zeta Crew", "alpha team" and "Beta"
    When they look at ROOMS
    Then the Rooms are listed "alpha team", "Beta", "Zeta Crew"

Rationale:
Alphabetical lets people find a conversation by name without scanning the whole list.

Needs: server, browser, pwa, macos, ios

### SORT-LIST-003: The Members List is sorted by display name
`req~SORT-LIST-003~1`

The Members List is ordered A–Z by each member's display name.

    Given a Room with members Ruby, Kelly and Mitch
    When a person opens the Members List
    Then the members are listed Kelly, Mitch, Ruby

Rationale:
People look for a member by the name they see; A–Z by that name puts them where expected.

Needs: server, browser, pwa, macos, ios

### SORT-NAME-001: Group conversation names list people in the order they were added
`req~SORT-NAME-001~1`

A group conversation's name lists its members in the order they were added.

    Given a group conversation started with Kelly, then Rex added, then Ruby added
    When the person views its name
    Then the names appear in the order Kelly, Rex, Ruby

Rationale:
Add order keeps the name stable as people join, so a familiar conversation does not change its name and become hard to recognize.

Needs: server, browser, pwa, macos, ios

### SORT-NAME-002: A re-added member goes last in a group conversation's name
`req~SORT-NAME-002~1`

A member who leaves a group conversation and is added again moves to the end of its
name.

    Given a group conversation named "Kelly, Rex, & Ruby"
    When Kelly is removed and later added again
    Then the name becomes "Rex, Ruby, & Kelly"

Rationale:
Being added again is a new addition, so it follows add order like any other.

Needs: server, browser, pwa, macos, ios

### SORT-NAME-003: A renamed member keeps their place in a group conversation's name
`req~SORT-NAME-003~1`

When a member's name changes, they keep their position in the group conversation's
name.

    Given a group conversation named "Kelly, Rex, & Ruby"
    When Rex's name changes to Rexford
    Then the name becomes "Kelly, Rexford, & Ruby"

Rationale:
A name change is not a new addition, so it should not reshuffle the conversation's name.

Needs: server, browser, pwa, macos, ios
