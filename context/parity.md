# v3 compared with v2, and client parity

Owner: Product. A snapshot (last reviewed 2026-10-28). Once each code repo
reports its rule coverage, the client table below is generated from the spec
instead of kept by hand: a feature is "Built" on a client when every rule for it
that lists that client is proven by a passing test.

## What v3 adds over v2

Uptime independent of Nitro; Conversation Sort and Layout; collapsible sections;
Apple Focus integration; attachment drafts; Markdown; search by coworker name;
Share Extension; native Apple apps; room bridging
([BT release notes](https://huddle.powerapp.cloud/projects/591)).

## connect-web is behind connect-apple

This blocks the Connect Browser launch, not the v2 sunset.

| Feature | connect-apple | connect-web | Blocks Browser launch |
|---|---|---|---|
| Message Search | Built | Missing | Yes |
| Mark as Unread/Read | Built | Missing | Yes |
| Appointment Hashtags | Built | Built | — |
| Favorite Conversations | Built | Built | — |
| Pin Messages | Built | Missing | No |
| Link previews | Built | Missing | No |
