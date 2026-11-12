# Message formatting: how Markdown looks

How each Markdown element renders, by Playbook kit. Which syntax Connect accepts,
and when formatting applies, are behavior rules in
[Formatting](../spec/messaging/formatting.md).

Owner: UX. To change a style, see [Contributing](../docs/contributing.md).

| Element | Syntax | Renders as |
|---|---|---|
| Italic / bold / both | `*text*` / `**text**` / `***text***` | [Playbook RTE](https://playbook.powerapp.cloud/kits/rich_text_editor/react#default) italic; Title 4 / Body Bold |
| Strikethrough | `~text~` | Playbook RTE strikethrough |
| Lists | `-`, `*`, `+`; `1.` | Playbook RTE lists, small indent |
| Link | `[text](url)` | [Playbook Link](https://playbook.powerapp.cloud/kits/link/react#underline) |
| Headings | `#` to `######` | [Playbook Title](https://playbook.powerapp.cloud/kits/title/react#default-ui); `#`–`###` = Title 1–3 |
| Horizontal rule | `***`, `- - -`, `___` | [Section Separator](https://playbook.powerapp.cloud/kits/section_separator/react#line-separator) |
| Code | `` `code` ``, ```` ``` ```` blocks | [Connect code designs](https://huddle.powerapp.cloud/projects/280/handoffs/948), syntax-colored |
| Line break | Shift + Return | One line; repeats collapse to one |

Body text uses [Playbook Body](https://playbook.powerapp.cloud/kits/body/react#default)
line height.

Open: which Playbook styles do headings 4–6 use, and are Title 1–3 too large in
chat? See [Open questions](../context/open-questions.md).
