# Open questions

Owner: Product and UX. Questions about how Connect *behaves* also exist as
`Status: draft` rules in the [spec](../spec/), so they show up where the
behavior lives; answering one means approving, correcting or rejecting that
draft. Everything else stays here until answered.

## Conflicts to resolve

- Strikethrough: `~text~` (catalog, PowerLife) vs `~~text~~` (proposal). Both supported?
- Conversation search example sorts alphabetically within match groups, but the rule puts recency first. Do rooms rank above People Conversations?
- v3 Apple release: rollout announced Aug 2025; context summary says Dec 2025.
- Layout names: Classic and Cozy (PowerLife) vs Comfortable, Compact, and Cozy (Huddle).
- Phase 2 gate: only Message Search and Mark as Unread/Read, or also Appointment Hashtags and Favorites?

## Copy and timing differences between clients

The same situation behaves or reads differently depending on the client. Confirm
whether each difference is intended, and if not, which version is correct.

- Invalid appointment message: sending an appointment number that doesn't exist shows "Appointment ID does not exist" on Apple but "Appt with ID# does not exist" on Web.
- Update reminder snooze: on iOS, "Remind me later" on the update dialog waits 4 hours before asking again; on Web, closing the update toast waits 24 hours.
- Where Conversation Layout is saved: PowerLife says Classic/Cozy is set per device; Web saves it on the server, separately for Browser and PWA (Safari and Firefox share one setting); Apple's behavior isn't documented.
- Room wording in group conversations: a group conversation on macOS shows the state event "This room has been set to private. Only invited members can read and post messages here." Should group conversations say "conversation" instead of "room"?

## QA catalog rows to retire or rewrite

These contradict confirmed answers or later work. Once the QA catalogs point at
rule IDs, a contradiction like this shows up as a test tagged to a rule it
doesn't match.

CA-MARK-003 (`*` bold, `**` italic), CA-COMP-013 / CA-ROOM-025 (110 MB; "<1MB"), CA-UI-005 / CA-BOOK-032 (light blue offline banner), CA-NEWMSG-024 ("3–10 users"; it's up to 10 others plus you), CA-BOOK-039 / -040 (Mark as Read/Unread by swiping left; it's left to right), CA-BOOK-013 / CW-BOOK-015 (fixed "+3" for 4+ others; it's others minus one), CA-BOOK-031 (iOS swipe shows a "delete button"; it's an x icon), CW-BOOK-006 (PWA three-dot menu "removes the conversation"; it opens options), CA-HEADER-009 (three avatars + "+2" for any larger group; actual is "+" the number not shown), CA-ECHO-005 (old failed-block rule), CA-ROOM-032 (search "blocked by encryption"), CA-BROWSE-010 (Leave Room "pending bridge work").

## Still unknown

- Headings 4–6: which Playbook styles? Are Title 1–3 too large in chat?
- Markdown in push notifications and previews; formatting shortcuts (⌘ + B, ⌘ + I) in the composer.
- Keyboard: Ctrl mapping on Windows/ChromeOS; browser conflicts for ⌘ + N and ⌘ + ,; whether Esc ever discards a draft; telling /room-name from /command.
- Corporate Directory on macOS?
- Rename one of the two New Message Buttons.
- Sliding Sync, what CCL moves server-side, and "system messaging via bots".
- PowerP menu location and contents; inventory of Nitro links to Connect (Phase 2).
- Sign-off criteria for Tim Wenhold and Marc Sule; who Marc Sule is.
- Save Messages on mobile depends on a future Tab Bar: is it planned?
- Design: principles, UI copy examples, patterns to use and avoid, platform conventions, dark mode, accessibility, motion. Responsive Screens specs are behind a Figma login.
- Client support matrix (feature × client × tenant); bug tracking and roadmap links. *(The spec's `Needs` plus each repo's coverage answers the feature × client part.)*
