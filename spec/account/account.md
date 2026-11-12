# Account: signing in and out

How a person signs in to Connect on a device, stays signed in, and signs out. Who is allowed a Connect account at all is covered in [Membership](../membership/connect-access.md).

**Area code:** `ACCOUNT`

**Topics**

| Topic | Covers |
|---|---|
| `SIGNIN` | Signing in |
| `SESSION` | Staying signed in, and being signed out by the company |
| `SIGNOUT` | Signing out |
| `DEVICE` | Using Connect on several devices |
| `PRIVACY` | Keeping personal and sign-in details safe on the device |
| `ENV` | Telling non-production environments apart |

Design: [Loading](https://huddle.powerapp.cloud/projects/590)

### ACCOUNT-SIGNIN-001: People sign in with their company login
`req~ACCOUNT-SIGNIN-001~1`

People sign in to Connect with their company login: Nitro ID in Nitro Connect,
Tempo ID in Tempo Connect. There is no separate Connect password.

    Given a person has a Connect account
    When they open Connect and are not signed in
    Then they are sent to their company login
    And after signing in there, they are in Connect

Rationale:
One login means one place to reset passwords, enforce security and switch access off.

Comment:
v2 is part of Nitro, so signing in to Nitro signs in to v2.

Needs: nitro, nitroid, server, browser, pwa, macos, ios

### ACCOUNT-SIGNIN-002: Sign-in goes straight to the company login when there is only one
`req~ACCOUNT-SIGNIN-002~1`

If the company offers one way to sign in, people go straight to it. If it offers
several, they choose one first.

    Given Power offers only Nitro ID
    When a person chooses "Login with Nitro"
    Then the Nitro ID login opens with no choice to make first

Rationale:
An extra step with only one option is friction for nothing.

Status: draft

Needs: server, browser, pwa, macos, ios

### ACCOUNT-SIGNIN-003: A failed sign-in says why
`req~ACCOUNT-SIGNIN-003~1`

When signing in fails, the person is told which of these happened: wrong details,
account switched off, no connection, or something else went wrong.

    Given a person whose account has been switched off
    When they try to sign in
    Then they are told their account is switched off
    And not that their details are wrong

Rationale:
"Wrong password" sends someone whose account was switched off round in circles resetting a password that is fine. Open: Nitro ID sign-in errors have no agreed design or copy yet; what should each one say?

Status: draft

Needs: ccl, browser, pwa, macos, ios

### ACCOUNT-SIGNIN-004: Signing in returns you to where you were going
`req~ACCOUNT-SIGNIN-004~1`

If a person opens a link to a conversation while signed out, signing in takes them
to that conversation.

    Given a person clicks a link to the "Philly Roofing" room while signed out
    When they sign in
    Then "Philly Roofing" opens

Rationale:
Landing on the Welcome Screen after signing in makes people find the link again.

Status: draft

Needs: browser, pwa

### ACCOUNT-SIGNIN-005: Nitro Connect offers "Login with Nitro"
`req~ACCOUNT-SIGNIN-005~1`

In Nitro Connect, the sign-in screen's button reads "Login with Nitro".

    Given a Power employee opens Nitro Connect while signed out
    Then the sign-in screen shows "Login with Nitro"

Rationale:
People recognise the company login by name, so they know which account to use.

Needs: browser, pwa, macos, ios

### ACCOUNT-SIGNIN-006: Tempo Connect offers "Login with Tempo"
`req~ACCOUNT-SIGNIN-006~1`

In Tempo Connect, the sign-in screen's button reads "Login with Tempo".

    Given a Stream Innovations employee opens Tempo Connect while signed out
    Then the sign-in screen shows "Login with Tempo"

Rationale:
People recognise the company login by name, so they know which account to use.

Needs: macos, ios

### ACCOUNT-SIGNIN-007: Double-clicking the logo opens the server picker
`req~ACCOUNT-SIGNIN-007~1`

On the sign-in screen, double-clicking the Connect logo opens the server picker.

    Given a person is on the sign-in screen
    When they double-click the Connect logo
    Then the server picker opens

Rationale:
Testers and support need to reach other servers, but everyday users should never stumble onto the choice.

Needs: browser, pwa, macos, ios

### ACCOUNT-SESSION-001: People stay signed in
`req~ACCOUNT-SESSION-001~1`

Once signed in, a person stays signed in when they close and reopen Connect, with
their settings as they left them.

    Given a person is signed in and has sorted their Conversation List alphabetically
    When they quit Connect and open it again
    Then they are still signed in
    And their Conversation List is still sorted alphabetically

Rationale:
Signing in every time is the fastest way to make people stop opening an app.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### ACCOUNT-SESSION-002: Ending a session elsewhere signs the device out
`req~ACCOUNT-SESSION-002~1`

When a person's session is ended from outside the app, for example by an
administrator, the device signs out, clears that person's data and returns to
sign-in.

    Given a person is signed in on their phone
    When an administrator ends their session
    Then the next time the phone reaches Connect it shows the sign-in screen
    And none of their conversations remain on the phone

Rationale:
Ending a session must actually end access, including what is already on the device.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### ACCOUNT-SESSION-003: Only an ended session signs a person out
`req~ACCOUNT-SESSION-003~1`

A person is never signed out because a feature is unavailable to them or their
company. Only an ended session or their own sign-out does it.

    Given a person in Tempo Connect, which has no EVENTS section
    When Connect checks for corporate events and is refused
    Then they stay signed in and carry on as normal

Rationale:
Being refused one feature is normal for some companies. Signing everyone there out would make Connect unusable for the whole company.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### ACCOUNT-SIGNOUT-001: Signing out works without a connection
`req~ACCOUNT-SIGNOUT-001~1`

Signing out always signs the person out on the device, even when Connect cannot be
reached.

    Given a person is offline
    When they sign out
    Then they are signed out and see the sign-in screen

Rationale:
The person asked to sign out. Refusing because the network is down leaves their account open on a device they may be handing over.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### ACCOUNT-SIGNOUT-002: Signing out leaves nothing behind
`req~ACCOUNT-SIGNOUT-002~1`

Signing out removes everything of that person's from the device: messages, drafts,
unsent messages, Notification Badges, the Corporate Directory, corporate events and
Appointment Cards.

    Given Dana signs out of a shared iPad
    When Sam signs in on it
    Then Sam sees none of Dana's conversations, drafts, Notification Badges or Appointment Cards

Rationale:
Devices are shared and handed on. The next person must never see the previous person's conversations or customers' details.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### ACCOUNT-DEVICE-001: People can be signed in on several devices
`req~ACCOUNT-DEVICE-001~1`

A person can be signed in on several devices at once, and each one shows the same
conversations.

    Given a person is signed in on their iPhone
    When they also sign in on their Mac
    Then both stay signed in and show the same conversations

Rationale:
People move between phone and computer all day.

Status: draft

Needs: server, ccl, browser, pwa, macos, ios

### ACCOUNT-DEVICE-002: One account at a time in each app
`req~ACCOUNT-DEVICE-002~1`

Each Connect app holds one signed-in account at a time. Switching to another
account means signing out and in again.

    Given a person is signed in on their phone
    When they want to use a different account
    Then they sign out first, and then sign in with the other account

Rationale:
Mixing two accounts' conversations in one place makes it too easy to send something from the wrong one.

Status: draft

Needs: browser, pwa, macos, ios

### ACCOUNT-PRIVACY-001: Diagnostic logs never hold secrets or customer details
`req~ACCOUNT-PRIVACY-001~1`

Logs that Connect keeps for troubleshooting never contain passwords, sign-in
details or homeowner details.

    Given a person exports Connect's log from Help & Diagnostics and sends it to support
    When support reads it
    Then they find no passwords, sign-in details or homeowner names, addresses or phone numbers

Rationale:
Logs are shared with support and vendors. They must be safe to hand over.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### ACCOUNT-ENV-001: Non-production environments show a dark branding bar
`req~ACCOUNT-ENV-001~1`

Connect connected to a non-production environment shows a dark branding bar;
production does not.

    Given a tester signs in to a staging server
    Then Connect shows a dark branding bar
    And Connect signed in to production shows no such bar

Rationale:
People testing must never mistake a test environment for the real one, or the other way round.

Needs: browser, pwa, macos, ios
