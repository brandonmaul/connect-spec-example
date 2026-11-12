# Device, platform and screen terms

How to say *where* a behavior happens. Layout follows screen size; interaction
follows platform. The screen-size breakpoint is **620px wide**.

Owner: UX. To change a term, see [Contributing](../docs/contributing.md).

## Clients

The four v3 clients. Behavior is written per client, and no client is assumed to
match another.

| Client | What it is | `Needs` target |
|---|---|---|
| Browser | Connect Browser: v3 in a web browser, desktop or mobile | `browser` |
| PWA | Connect PWA: v3 installed from the browser as an app; the Android app | `pwa` |
| macOS | Connect for Mac | `macos` |
| iOS | Connect for iPhone and iPad | `ios` |

"Apple" means macOS and iOS together. "Web" means Browser and PWA together.
Android has no native v3 app, so "Native App" always means the Apple apps.

## Platform and screen

| Term | Means |
|---|---|
| Mobile PWA / Mobile Browser / Mobile Native App | On a phone or iPad; native = iOS. "Mobile" = all three |
| Desktop PWA / Desktop Browser / Desktop Native App | On a computer; native = macOS. "Desktop" = all three |
| Desktop Large Screen / Desktop Small Screen | Any Desktop platform at ≥ 620px / < 620px |
| Small Screens | Desktop Small Screen plus all Mobile |

Don't use Mobile Large/Small Screen, PWA or Browser Small Screen, or Native App
Small/Large Screen. iPad follows the 620px rule (portrait is usually Small
Screens).

If a request says only "mobile" or "the app", ask which of these it means.
