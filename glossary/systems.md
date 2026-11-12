# System and tenant terms

The names for Connect's two generations, its two companies, and the systems
behind them.

Owner: UX, with engineering. To change a term, see
[Contributing](../docs/contributing.md).

## Generations

| Term | Means |
|---|---|
| v2 | Connect built into Nitro (green "Connect" app icon). Power only. The v2 Browser and the v2 iOS and Android apps |
| v3 | Connect built on Matrix and served by connect-server (blue "Nitro Connect" icon). Keeps working when Nitro is down |
| v2 Browser / Connect Browser (v3) | Different products. Always say which |
| The Bridge | Two-way v2↔v3 sync of messages, reactions, attachments, read receipts, room membership. Most employees don't know there are two systems because of it |

## Tenants

| Term | Means |
|---|---|
| Nitro Connect | The Power Home Remodeling deployment of v3 |
| Tempo Connect | The Stream Innovations deployment of v3. A copy of Nitro Connect with mainly visual differences and Stream Tempo routing. Stream never had v2 |

Nitro Connect and Tempo Connect can differ. A rule that applies to only one says
so in its text.

## Systems behind Connect

| Term | Means |
|---|---|
| Nitro | Power's company system. People, roles, titles and territories live here. Hosts v2 |
| Nitro ID | Power's company login. It also passes people and groups from Nitro to v3 |
| Tempo ID | Stream's company login and directory. It does the same job as Nitro ID |
| Connect Client Library (CCL) | Shared library on Matrix's Rust SDK that moves logic into connect-server so clients are thin UI. "Modern app" in tickets = the CCL Apple client |
| Sliding Sync | A stability requirement for connect-apple; not yet defined here |
| PowerP | A Nitro menu whose Connect notifications and links move to connect-server in Phase 2 of the v2 sunset |
