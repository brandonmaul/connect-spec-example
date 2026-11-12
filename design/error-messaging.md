# Error messaging

Which pattern each kind of error uses, with example copy. Source of truth:
[Error Messaging Guide](https://huddle.powerapp.cloud/projects/506) in Huddle.

Owner: UX. To change a pattern, see [Contributing](../docs/contributing.md).

| Type | Pattern | Example copy |
|---|---|---|
| Download | Blue info toast, optional Refresh | "Content download failed. Check connection & try again." |
| Save | Red toast | "Unable to save your action. Try again later." |
| Send / upload | Red toast with Retry | "There was an issue sending your message. Try again." |
| Connectivity | Gray toast | "Lost connection. Check your internet connectivity." |
| Fullscreen | Illustration, title, explanation, button, link | "Connect quit unexpectedly" (Restart Connect); "Update failed" (Try again / Submit a support ticket) |
| Warning | Dialog: question title, consequence, named buttons | "Make room private?" "Private rooms cannot be changed back to public." (Yes, Make Private / No, Go back) |

NitroID errors aren't designed yet. Confirm error type and copy with UX before
building.

Where a specific error's copy is part of how Connect behaves (for example a failed
send), the rule in the [spec](../spec/) quotes it.
