# Settings

A person's own preferences for how Connect looks to them. Settings for one conversation are covered in [Conversations](../conversations/conversations.md) and [Notifications](../notifications/notifications.md).

**Area code:** `SETTING`

**Topics**

| Topic | Covers |
|---|---|
| `SORT` | How the conversation list is sorted |
| `DENSITY` | How tall the rows of the conversation list are |
| `SYNC` | Settings following the person between devices |

Design: <figma link> · Runway: <epic link>

### SETTING-SORT-001: The conversation list can be sorted three ways
`req~SETTING-SORT-001~1`

A person can sort their conversation list by most recent activity, alphabetically,
or in their own custom order.

    Given a person opens their settings
    When they choose how to sort their conversation list
    Then they can pick Most recent, Alphabetical or Custom

Rationale:
People use Connect differently: some follow what is new, some look things up by name, and some keep a fixed order of what matters to them.

Needs: ccl, ios, macos, web

### SETTING-SORT-002: New people start with Most recent
`req~SETTING-SORT-002~1`

A person who has never chosen a sort starts with Most recent.

    Given a person signs in to Connect for the first time
    When their conversation list opens
    Then it is sorted by most recent activity

Rationale:
Most recent is what most chat apps do, and what a new person expects.

Needs: ccl

### SETTING-SORT-003: Alphabetical follows the person's language
`req~SETTING-SORT-003~1`

Alphabetical order ignores capital letters and follows the rules of the person's
language, so accented letters sort with their plain letter.

    Given conversations named "emma", "Zed", "Émile" and "Ebb"
    When the list is sorted alphabetically
    Then they are listed as Ebb, Émile, emma, Zed

Rationale:
People look for a name where their language puts it, the same as everywhere else on their device.

Needs: ccl

### SETTING-DENSITY-001: Rows can be compact or roomy
`req~SETTING-DENSITY-001~1`

A person can choose Classic, compact rows, or Cozy, taller rows, for their
conversation list. A new person starts with Classic.

    Given a person's list uses Classic rows
    When they choose Cozy
    Then each row in their list gets taller

Rationale:
Some people want to see as many conversations as possible, others want them easier to read and tap.

Needs: ccl, ios, macos, web

### SETTING-DENSITY-002: Row size is chosen per kind of device
`req~SETTING-DENSITY-002~1`

Row size is saved separately for phone, tablet, Mac and web, so changing it on one
kind of device does not change it on another.

    Given a person uses Cozy on their iPhone
    When they open Connect on their Mac
    Then the Mac still uses the row size they chose there

Rationale:
What is comfortable on a small phone screen is not what is comfortable on a large monitor.

Needs: ccl

### SETTING-SYNC-001: Sort and custom order follow the person to every device
`req~SETTING-SYNC-001~1`

The sort and custom order a person chooses apply on all their devices, and change
live on any device they have open.

    Given a person has Connect open on their Mac and iPhone
    When they switch to Alphabetical on the iPhone
    Then the Mac list re-sorts alphabetically without a refresh

Rationale:
A list that is in a different order on each device makes people hunt for conversations.

Needs: ccl, server

### SETTING-SYNC-002: Changing one setting keeps the others
`req~SETTING-SYNC-002~1`

Changing one setting never resets another.

    Given a person has set up a custom order
    When they switch the sort to Alphabetical
    And later switch back to Custom
    Then their custom order is still there

Rationale:
Losing a carefully arranged order because of an unrelated change is the kind of thing people do not forgive.

Needs: ccl

### SETTING-SYNC-003: The list opens in the person's own order
`req~SETTING-SYNC-003~1`

When a person signs in again, their list opens in the order they chose, not in the
default order first.

    Given a person sorts alphabetically
    When they sign out and sign in again
    Then their list first appears in alphabetical order

Rationale:
A list that appears in one order and then jumps to another looks broken.

Needs: ccl

### SETTING-SYNC-004: Custom order is shared with Connect V2
`req~SETTING-SYNC-004~1`

A person's custom conversation order is the same in Connect V2 and V3.

    Given a person rearranges their conversations in Connect V3
    When they open Connect V2
    Then their conversations are in the same order there

Rationale:
People using both versions expect one list, not two.

Needs: server, nitro
