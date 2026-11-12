# Message formatting

Markdown formatting in messages: which syntax Connect formats, when formatting is
applied, and what typing leaves alone. How each formatted element looks is in
[the message formatting design](../../design/message-formatting.md). Line breaks and
repeated new lines are in [Messages](messages.md).

**Area code:** `FORMAT`

**Topics**

| Topic | Covers |
|---|---|
| `SYNTAX` | The Markdown Connect formats, and what it does not |
| `RENDER` | When formatting is applied, and where it shows |
| `INPUT` | What typing does, and does not do, to text |

Design: [Message](https://huddle.powerapp.cloud/projects/280) · [Message Composer](https://huddle.powerapp.cloud/projects/511)

### FORMAT-SYNTAX-001: Single asterisks make italic
`req~FORMAT-SYNTAX-001~1`

Text wrapped in single asterisks is shown in italic.

    Given a person sends "this is *really* urgent"
    Then "really" shows in italic, without the asterisks

Rationale:
Markdown is what people already type in chat to add emphasis.

Needs: browser, pwa, macos, ios

### FORMAT-SYNTAX-002: Double asterisks make bold
`req~FORMAT-SYNTAX-002~1`

Text wrapped in double asterisks is shown in bold.

    Given a person sends "the meeting is **cancelled**"
    Then "cancelled" shows in bold, without the asterisks

Rationale:
Markdown is what people already type in chat to add emphasis.

Needs: browser, pwa, macos, ios

### FORMAT-SYNTAX-003: Triple asterisks make bold italic
`req~FORMAT-SYNTAX-003~1`

Text wrapped in triple asterisks is shown in bold italic.

    Given a person sends "***do not reply***"
    Then "do not reply" shows in bold italic, without the asterisks

Rationale:
Follows from italic and bold together, as in standard Markdown.

Needs: browser, pwa, macos, ios

### FORMAT-SYNTAX-004: Tildes make strikethrough
`req~FORMAT-SYNTAX-004~1`

Text wrapped in single tildes is shown with strikethrough.

    Given a person sends "meet at ~2pm~ 3pm"
    Then "2pm" shows struck through, without the tildes

Rationale:
Open: is strikethrough written `~text~`, `~~text~~`, or are both supported?

Status: draft

Needs: browser, pwa, macos, ios

### FORMAT-SYNTAX-005: Bulleted lists
`req~FORMAT-SYNTAX-005~1`

Lines starting with `-`, `*` or `+` and a space are shown as a bulleted list.

    Given a person sends three lines starting "- Shingles", "- Gutters" and "- Siding"
    Then they show as a bulleted list of three items

Rationale:
Lists make steps and options easy to scan.

Needs: browser, pwa, macos, ios

### FORMAT-SYNTAX-006: Numbered lists
`req~FORMAT-SYNTAX-006~1`

Lines starting with a number and a period, such as `1.`, are shown as a numbered
list.

    Given a person sends lines starting "1. Measure" and "2. Order"
    Then they show as a numbered list

Rationale:
Numbered steps show the order things happen in.

Needs: browser, pwa, macos, ios

### FORMAT-SYNTAX-007: Links with their own text
`req~FORMAT-SYNTAX-007~1`

`[text](url)` is shown as a link labelled with the text.

    Given a person sends "See [the schedule](https://example.com/schedule)"
    Then "the schedule" shows as a link to that address

Rationale:
A short label reads better than a long address.

Needs: browser, pwa, macos, ios

### FORMAT-SYNTAX-008: Hashes make headings
`req~FORMAT-SYNTAX-008~1`

A line starting with one to six `#` and a space is shown as a heading, from level 1
(`#`) to level 6 (`######`).

    Given a person sends a line "## Install day"
    Then "Install day" shows as a level 2 heading, without the hashes

Rationale:
Headings break long announcements into sections people can scan.

Needs: browser, pwa, macos, ios

### FORMAT-SYNTAX-009: Headings 4 to 6 have their own styles
`req~FORMAT-SYNTAX-009~1`

Headings at levels 4, 5 and 6 each have a heading style of their own.

    Given a person sends a line "#### Notes"
    Then "Notes" shows in the level 4 heading style

Rationale:
Open: which styles do headings 4–6 use, and are the level 1–3 styles too large in chat?

Status: draft

Needs: browser, pwa, macos, ios

### FORMAT-SYNTAX-010: Horizontal rules
`req~FORMAT-SYNTAX-010~1`

A line of `***`, `- - -` or `___` on its own is shown as a horizontal rule.

    Given a person sends "Part one", a line "___", and "Part two"
    Then a horizontal rule separates "Part one" from "Part two"

Rationale:
A rule separates sections of a long message.

Needs: browser, pwa, macos, ios

### FORMAT-SYNTAX-011: Inline code
`req~FORMAT-SYNTAX-011~1`

Text wrapped in single backticks is shown as code.

    Given a person sends "run `build --check` first"
    Then "build --check" shows as code, without the backticks

Rationale:
Code must be copied exactly, so it is set apart from the words around it.

Needs: browser, pwa, macos, ios

### FORMAT-SYNTAX-012: Code blocks are syntax-colored
`req~FORMAT-SYNTAX-012~1`

Text between lines of three backticks is shown as a code block, with its syntax
colored.

    Given a person sends a few lines of code between two lines of three backticks
    Then they show as a code block with syntax coloring

Rationale:
Longer code is easier to read in its own block, with coloring that shows its structure.

Needs: browser, pwa, macos, ios

### FORMAT-SYNTAX-013: Underline-style headings are not formatted
`req~FORMAT-SYNTAX-013~1`

A line of `=` or `-` under text does not turn that text into a heading.

    Given a person sends "Totals" with a line "======" under it
    Then "Totals" does not show as a heading

Rationale:
Only one way of writing headings is supported, so people are not surprised by text turning into a heading.

Needs: browser, pwa, macos, ios

### FORMAT-SYNTAX-014: Image syntax is not formatted
`req~FORMAT-SYNTAX-014~1`

Markdown image syntax does not show an image in the message.

    Given a person sends "![roof](https://example.com/roof.jpg)"
    Then no image is shown in the message

Rationale:
Images are shared as attachments, so the people in the conversation see exactly the file that was sent.

Needs: browser, pwa, macos, ios

### FORMAT-SYNTAX-015: Quotes with `>`
`req~FORMAT-SYNTAX-015~1`

A line starting with `>` and a space is shown as a quote.

    Given a person sends "> We start Monday" and "Confirmed"
    Then "We start Monday" shows as a quote above "Confirmed"

Rationale:
Open: quoting is a nice-to-have; is it wanted?

Status: draft

Needs: browser, pwa, macos, ios

### FORMAT-SYNTAX-016: Backslash escapes formatting
`req~FORMAT-SYNTAX-016~1`

A backslash before a formatting character shows the character as typed instead of
formatting the text.

    Given a person sends "\*not italic\*"
    Then it shows "*not italic*" with the asterisks and no italic

Rationale:
Open: escaping is a nice-to-have; is it wanted?

Status: draft

Needs: browser, pwa, macos, ios

### FORMAT-RENDER-001: Formatting applies on send
`req~FORMAT-RENDER-001~1`

Formatting is applied when a message is sent. While typing, the Message Composer
shows the Markdown as typed.

    Given a person types "**cancelled**" in the Message Composer
    Then the Message Composer shows "**cancelled**" with its asterisks
    And once sent, the message shows "cancelled" in bold

Rationale:
People see exactly what they typed until they decide to send it.

Needs: browser, pwa, macos, ios

### FORMAT-RENDER-002: Editing shows the original syntax
`req~FORMAT-RENDER-002~1`

Editing a formatted message shows its original Markdown, not the formatted text.

    Given a person sent "the meeting is **cancelled**"
    When they edit it
    Then the Message Composer shows "the meeting is **cancelled**" with its asterisks

Rationale:
The person edits what they wrote, so they can change the formatting as well as the words.

Needs: browser, pwa, macos, ios

### FORMAT-RENDER-003: Older apps show the raw punctuation
`req~FORMAT-RENDER-003~1`

An older Connect app that does not format Markdown shows a formatted message as it
was typed, with its punctuation.

    Given a person sends "the meeting is **cancelled**"
    When someone reads it in an older app that does not format Markdown
    Then they see "the meeting is **cancelled**" with the asterisks

Rationale:
The words still get through on every app, even one that cannot format them.

Needs: browser, pwa, macos, ios

### FORMAT-RENDER-004: Formatting in notifications and previews
`req~FORMAT-RENDER-004~1`

Notifications and message previews show a formatted message's text without its
Markdown punctuation.

    Given a person sends "the meeting is **cancelled**"
    When someone gets a notification for it
    Then the notification reads "the meeting is cancelled"

Rationale:
Open: how does Markdown render in notifications and previews?

Status: draft

Needs: browser, pwa, macos, ios

### FORMAT-INPUT-001: Hyphens are never auto-replaced
`req~FORMAT-INPUT-001~1`

Connect never replaces hyphens typed in a message with dashes.

    Given a person types "2--3 days"
    When they send it
    Then the message shows "2--3 days" exactly as typed

Rationale:
Hyphens are often part of code, IDs and Markdown, so changing them would break what people meant.

Needs: browser, pwa, macos, ios

### FORMAT-INPUT-002: Option and Hyphen type dashes on a Mac
`req~FORMAT-INPUT-002~1`

On a Mac keyboard, Option+Hyphen types an en dash (–) and Option+Shift+Hyphen types
an em dash (—).

    Given a person is typing in Connect on their Mac
    When they press Option+Shift+Hyphen
    Then an em dash (—) is typed

Rationale:
With no auto-replacement, people who want a dash type it directly.

Needs: browser, pwa, macos

### FORMAT-INPUT-003: Keyboard shortcuts for bold and italic
`req~FORMAT-INPUT-003~1`

In the Message Composer, ⌘ + B makes the selected text bold and ⌘ + I makes it
italic.

    Given a person selects "cancelled" in the Message Composer
    When they press ⌘ + B
    Then "cancelled" is wrapped in double asterisks

Rationale:
Open: should the Message Composer offer formatting shortcuts such as ⌘ + B and ⌘ + I?

Status: draft

Needs: browser, pwa, macos, ios
