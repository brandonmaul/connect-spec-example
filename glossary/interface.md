# Interface terms

The names for every part of Connect's screens. Rules, designs, tickets and
conversations use these words and no others. A term in **bold** in a rule means
the term defined here.

Owner: UX. To change a term, see [Contributing](../docs/contributing.md).

## Writing with these terms

- Use the capitalized term. If something has no term here, say so and propose
  one; don't invent a name in a rule.
- Never write "New Message Button" on its own. There are two: say
  **New Message Button (compose)** or **New Message Button (jump)**.
- Keep **bold (unread)** and the **Notification Badge** apart. Bold means the
  conversation has something unread. The badge means something notifying
  happened, or the person marked it unread.
- "Bookmark" is the old name for a **Conversation**. Use it only when quoting an
  older handoff.

## User Header

| Term (aliases) | Definition |
|---|---|
| User Header | Top-left of the Desktop sidebar: Self User plus the New Message Button (compose). Mobile uses the Header instead |
| Self User | Signed-in user's avatar and name; opens the User Menu |
| User Menu | User settings (layout, sort, notifications toggle) and Help & Diagnostics. Opened from Self User (Desktop) or Menu Bars (Mobile) |
| New Message Button (compose) | Compose icon that starts a new conversation |

## Header

| Term (aliases) | Definition |
|---|---|
| Header (Mobile), Menu Bars | Mobile top bar: hamburger (Menu Bars) left, compose right |

## Conversation List

| Term (aliases) | Definition |
|---|---|
| Conversation List (Sidebar) | Sections top to bottom: EVENTS, Favorites, ROOMS, PEOPLE; each collapses and a collapsed section totals its badges |
| Conversation (formerly Bookmark) | A row in the list; older handoffs say "bookmark" |
| Rooms | Multi-person channels, public (globe icon) or private (padlock) |
| People Conversations (DMs, group conversations) | 1:1 and group conversations of up to 10 other people plus you |
| Self Message | A conversation with yourself |
| Conversation options menu | Favorites and Mark as Read/Unread. Desktop: hover, then the ellipsis. iOS: swipe a conversation left to right |
| Hide (Close) | Removes a conversation from the list without leaving it; it returns on the next notifying message. Desktop and Android: x button (labeled "Close conversation" on Web); iOS: swipe right to left to reveal an x icon |
| "+" beside ROOMS | Create a Room and Browse Rooms |
| "+" beside PEOPLE | Opens the new message flow, same as the New Message Button (compose) |

## Conversation Header

| Term (aliases) | Definition |
|---|---|
| Conversation Header (Room Header) | Name, topic, member count; right side has search, pin (thumbtack) and notification bell (rooms only). Click opens Room Info |
| Room Info (Room Information View) | Modal with About and Members tabs, room settings, and Leave Room (public rooms only, for now) |
| Member Count, Members List | Member total ("N Members" on Mobile); opens the Members List. In a group conversation, clicking the header opens a Members (N) popover that includes you |
| Pinned Message Drawer | Pinned messages, most recently pinned first |

## Conversation View

| Term (aliases) | Definition |
|---|---|
| Conversation View | Message history, Date Separators, reactions, Message Composer |
| Welcome Screen | "Welcome to Connect" shown when no conversation is open (Desktop) |
| Date Separator | Sticky day label in caps (weekday, date, month, or TODAY / YESTERDAY) |
| Message, Message Composer | One post; the input at the bottom with a "+" attachment menu |

## New Messages

| Term (aliases) | Definition |
|---|---|
| New Message Indicator | Thin "↓ New" line above the first unread message |
| New Message Button (jump) | Blue "↓ New Messages" pill that scrolls to unread |
| Notification Badge (New Message Badge) | Blue badge for notifying activity (number) or Mark as Unread (empty) |

## Reactions

| Term (aliases) | Definition |
|---|---|
| Reaction Bar (Reaction Nav, Message Options) | Quick reactions, emoji picker, and the message actions. Desktop hover; iOS long-press; PWA tap |
| Reaction Button, Add Reaction Button | Emoji pill with count (click toggles yours); smiley-plus opens the picker |

## Rooms

| Term (aliases) | Definition |
|---|---|
| Room Admin | Creator plus anyone promoted: edits name/topic, manages members and filters, pins messages |
| Broadcast Room | Only broadcasters can post; others don't see a composer |
| Required Room | Admin setting (iOS) for rooms members are expected to stay in; behavior not documented |
| Member filters (Audiences) | Rules (Territory, Department, Title) that keep a private room's membership updated |

## People

| Term (aliases) | Definition |
|---|---|
| Presence | Dot on avatars: green = online with Connect open; gray = logged out or asleep; blue = Nitro bot (always online); yellow = seen when testing with the mock client |
| Contact Card | Opens from any avatar; profile details and Direct Message |
| Corporate Directory | People, Departments, Territories tabs; iOS and Web |

## Other

| Term (aliases) | Definition |
|---|---|
| Appointment Card | Card for a verified Appointment Hashtag (A#12345678) |
| Siri intent | "Send a message using Nitro Connect" on macOS and iOS (CCL client) |
| Local Echo | Showing a sent message or reaction before the server confirms it |
| Crash Screen | Fullscreen error after the app quits unexpectedly |
