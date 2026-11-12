# Settings

A person's own preferences for how Connect looks to them, chosen in the **User Menu**.
Settings for one conversation are covered in [Conversations](../conversations/conversations.md)
and [Notifications](../notifications/notifications.md). How each sort orders names is
covered in [Sorting and naming](../sorting/sorting-and-naming.md).

**Area code:** `SETTING`

**Topics**

| Topic | Covers |
|---|---|
| `SORT` | How the **Conversation List** is sorted |
| `DENSITY` | The **Conversation List** layout (Classic or Cozy) and where it is saved |
| `SYNC` | Settings following the person between devices |
| `MENU` | The **User Menu**, where personal settings are chosen |

Design: [User Options](https://huddle.powerapp.cloud/projects/650) · [Conversation List](https://huddle.powerapp.cloud/projects/495)

### SETTING-SORT-001: The Conversation List can be sorted three ways
`req~SETTING-SORT-001~1`

A person can sort their **Conversation List** by Self-Managed (their own order, arranged
by dragging), Recent Activity, or Alphabetical.

    Given a person opens the User Menu
    When they choose how to sort their Conversation List
    Then they can pick Self-Managed, Recent Activity or Alphabetical

Rationale:
People use Connect differently: some keep a fixed order of what matters to them, some follow what is new, and some look things up by name.

Needs: ccl, browser, pwa, macos, ios

### SETTING-SORT-002: New people start with Self-Managed
`req~SETTING-SORT-002~1`

A person who has never chosen a sort starts with Self-Managed.

    Given a person signs in to Connect for the first time
    When their Conversation List opens
    Then it is sorted Self-Managed

Rationale:
Self-Managed is the default, so a person's list stays where they put it until they choose otherwise.

Needs: ccl, browser, pwa, macos, ios

### SETTING-SORT-003: Alphabetical sorts by conversation name, ignoring case and accents
`req~SETTING-SORT-003~1`

The Alphabetical sort lists conversations by name A–Z. Comparisons ignore capital
letters and accents, so accented letters sort with their plain letter.

    Given conversations named "emma", "Zed", "Émile" and "Ebb"
    When the list is sorted Alphabetical
    Then they are listed as Ebb, Émile, emma, Zed

Rationale:
Same behavior as SORT-LIST-002, which owns it. Kept for the record.
People look for a name where they expect it, and every client must show the same order.

Status: rejected

Needs: ccl, browser, pwa, macos, ios

### SETTING-SORT-004: Reactions do not count as Recent Activity
`req~SETTING-SORT-004~1`

With the Recent Activity sort, a reaction does not move a conversation up the list.

    Given a person sorts by Recent Activity
    And conversation A had the newest message
    When someone reacts to an older message in conversation B
    Then A stays above B

Rationale:
A reaction is not new conversation, and rows jumping for every reaction would make the list hard to follow.

Needs: ccl, browser, pwa, macos, ios

### SETTING-DENSITY-001: The Conversation List has a choice of layouts
`req~SETTING-DENSITY-001~1`

A person can choose Classic or Cozy as the layout of their **Conversation List**. A new
person starts with Classic.

    Given a person's list uses Classic
    When they choose Cozy in the User Menu
    Then their Conversation List shows in the Cozy layout

Rationale:
Open: are the layouts Classic and Cozy, or Comfortable, Compact and Cozy? And which layout does a new person start with?

Status: draft

Needs: ccl, browser, pwa, macos, ios

### SETTING-DENSITY-002: Layout is chosen per device
`req~SETTING-DENSITY-002~1`

The layout is saved separately for each device, so changing it on one device does not
change it on another.

    Given a person uses Cozy on their iPhone
    When they open Connect on their Mac
    Then the Mac still uses the layout they chose there

Rationale:
Open: is the layout saved per device, or on the person's account per client? Web saves it on the account, separately for Browser and PWA; how Apple saves it is not documented.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### SETTING-DENSITY-003: Classic shows avatars and Icon Circles
`req~SETTING-DENSITY-003~1`

In the Classic layout, People Conversations show avatars and Rooms show a colored Icon
Circle.

    Given a person uses the Classic layout
    When they look at their Conversation List
    Then each DM shows the other person's avatar
    And each Room shows a colored Icon Circle

Rationale:
Pictures make conversations quick to recognise when scanning the list.

Needs: browser, pwa, macos, ios

### SETTING-DENSITY-004: Cozy shows Presence and group icons
`req~SETTING-DENSITY-004~1`

In the Cozy layout, a DM shows a **Presence** dot and the other person's name, and a
group conversation shows a group icon.

    Given a person uses the Cozy layout
    When they look at their Conversation List
    Then each DM shows a Presence dot and the person's name
    And each group conversation shows a group icon

Rationale:
Cozy gives up photos for a simpler row while still showing who is online.

Needs: browser, pwa, macos, ios

### SETTING-DENSITY-005: Classic DM rows show territory and job title
`req~SETTING-DENSITY-005~1`

In the Classic layout, a DM row shows the other person's avatar, name, territory and job
title (as "territory · job title"), and a **Presence** dot.

    Given a person uses the Classic layout
    And has a DM with a Foreman in Philadelphia
    When they look at that row
    Then it shows the avatar, the name, "Philadelphia · Foreman" and a Presence dot

Rationale:
Territory and title tell people which coworker a name belongs to, and Presence says whether they are around.

Needs: browser, pwa, macos, ios

### SETTING-DENSITY-006: Browser and PWA keep separate layouts
`req~SETTING-DENSITY-006~1`

On Web, the layout is saved on the person's account separately for the Browser and the
PWA.

    Given a person uses Cozy in the Connect PWA
    When they open the Connect Browser
    Then the Browser uses the layout they chose in the Browser

Rationale:
The PWA and the Browser are used on different screens and in different ways, so each keeps its own choice.

Needs: server, browser, pwa

### SETTING-DENSITY-007: Every browser shares one Browser layout
`req~SETTING-DENSITY-007~1`

The Browser layout is the same in every web browser, for example Safari and Firefox.

    Given a person chose Cozy in the Connect Browser in Firefox
    When they open the Connect Browser in Safari
    Then it also uses Cozy

Rationale:
The layout is saved on the person's account, so it should not depend on which browser they happen to use.

Needs: server, browser

### SETTING-SYNC-001: Sort and Self-Managed order follow the person to every device
`req~SETTING-SYNC-001~1`

The sort a person chooses, and their Self-Managed order, are saved on their account and
apply on all their devices.

    Given a person has Connect on their Mac and iPhone
    When they switch to Alphabetical on the iPhone
    Then the Mac list is sorted Alphabetical too

Rationale:
A list that is in a different order on each device makes people hunt for conversations.

Needs: server, ccl, browser, pwa, macos, ios

### SETTING-SYNC-002: Changing one setting keeps the others
`req~SETTING-SYNC-002~1`

Changing one setting never resets another.

    Given a person has set up a Self-Managed order
    When they switch the sort to Alphabetical
    And later switch back to Self-Managed
    Then their Self-Managed order is still there

Rationale:
Losing a carefully arranged order because of an unrelated change is the kind of thing people do not forgive.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### SETTING-SYNC-003: The list opens in the person's own order
`req~SETTING-SYNC-003~1`

When a person signs in again, their list opens in the order they chose, not in the
default order first.

    Given a person sorts Alphabetical
    When they sign out and sign in again
    Then their list first appears in Alphabetical order

Rationale:
A list that appears in one order and then jumps to another looks broken.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### SETTING-SYNC-004: Self-Managed order is shared with v2
`req~SETTING-SYNC-004~1`

In Nitro Connect, a person's Self-Managed order is bridged to v2, so the list is in the
same order in v2 and v3.

    Given a person rearranges their conversations in v3
    When they open v2
    Then their conversations are in the same order there

Rationale:
People using both versions expect one list, not two.

Needs: nitro, server

### SETTING-MENU-001: The User Menu opens from Self User or Menu Bars
`req~SETTING-MENU-001~1`

On Desktop, the **User Menu** opens from **Self User** in the User Header. On Mobile, it
opens from **Menu Bars** in the Header.

    Given a person is on Desktop
    When they click their own avatar and name at the top of the sidebar
    Then the User Menu opens
    And on Mobile, tapping the hamburger in the Header opens it

Rationale:
Personal settings belong with the person's own name and picture, and on a small screen with the main menu.

Needs: browser, pwa, macos, ios

### SETTING-MENU-002: Layout and sort are chosen in the User Menu
`req~SETTING-MENU-002~1`

The **User Menu** is where a person chooses their **Conversation List** layout and sort.

    Given a person wants their list sorted Alphabetical
    When they open the User Menu
    Then they find the sort and layout choices there

Rationale:
These are the person's own settings, so they live in one personal place.

Needs: browser, pwa, macos, ios

### SETTING-MENU-003: Notifications can be switched on or off in the User Menu
`req~SETTING-MENU-003~1`

The **User Menu** has a toggle that switches Connect notifications on or off for the
person.

    Given a person wants a break from notifications
    When they open the User Menu
    Then they find a notifications toggle there

Rationale:
People need one obvious place to turn notifications off and back on.

Needs: browser, pwa, macos, ios
