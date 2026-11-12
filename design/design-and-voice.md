# Design and voice

How Connect looks and sounds on every client. These are design conventions, not
behavior rules: they say how to build and word things, and the
[spec](../spec/) says what must happen.

Owner: UX. To change a convention, see [Contributing](../docs/contributing.md).

## Playbook and handoffs

Connect uses Playbook on every client (React on Web, Playbook Swift on Apple),
delivered as [Huddle](https://huddle.powerapp.cloud/project_collections/14)
handoffs.

**Handoffs** are per client or "all clients", with UI Specs, Spacing, States,
Notes, Playbook Kits, Prototype, sometimes a Codesandbox. "Rebels" = Web
version, "Rogue" = Apple version.

- Never build blurred areas.
- If a kit isn't in PB Swift (Fixed Confirmation Toast, Loading Inline,
  Typeahead, Detail), match it natively unless told to wait.
- Check the [design projects in Huddle](../context/projects.md#design-projects-in-huddle)
  for an existing handoff before designing anything new.

Sources of truth in Huddle:
[Conversation Modals](https://huddle.powerapp.cloud/projects/549),
[Error Messaging Guide](https://huddle.powerapp.cloud/projects/506),
[Message and Terminology Guides](https://huddle.powerapp.cloud/projects/507),
[Handoff Repository](https://huddle.powerapp.cloud/projects/489).

## Message layout

Playbook Message kit or a 1:1 match.

- Avatar xs (28 × 28).
- Name Title 4 (line height 17), timestamp after it.
- Body line height 21.
- 8px after the avatar and between name and time; 16px between messages; 4px
  above reactions.
- Your own messages are tinted primary at 10% (macOS).

## Look

Calm light surfaces; blue reserved for unread and attention; rounded avatars,
pills, and Icon Circles; name and time on one line, body below, reactions under.

## Voice

- **UI labels** are plain and literal (Rooms, Mark as Unread).
- **Errors** say what happened, then what to do. See
  [Error messaging](error-messaging.md).
- **Warnings** ask a question, and buttons name the action, never a bare OK.
- **Announcements** (PowerLife) are warm and playful, lead with why it matters,
  then give short steps per device.

## Standing requirements for new UI

- New interactive UI must be keyboard reachable and define its Esc behavior
  (see [Keyboard](../spec/keyboard/keyboard.md)).
- Any new surface showing message text must say how Markdown renders there (see
  [Message formatting](message-formatting.md)).
- Lists and searches follow [Sorting and naming](../spec/sorting/sorting-and-naming.md);
  state the sort and tiebreaker in acceptance criteria.
