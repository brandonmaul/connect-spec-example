# Messages

Writing, sending, changing and reacting to messages, and what happens when a send
fails. How Markdown formatting works is in [Message formatting](formatting.md).

**Area code:** `MSG`

**Topics**

| Topic | Covers |
|---|---|
| `SEND` | Sending a message, and what happens when it fails |
| `COMPOSE` | Typing, pasting and dropping into the Message Composer |
| `FAIL` | Messages that could not be sent |
| `ACTION` | The actions offered on a message |
| `EDIT` | Editing a message |
| `DELETE` | Deleting a message |
| `REACT` | Reactions |
| `MENTION` | Mentioning people in a message |
| `ATTACH` | Photos, files and GIFs |
| `DRAFT` | Unsent text and attachments kept for later |
| `READ` | Unread and read state, and where a conversation opens |
| `RETAIN` | How long messages are kept |

Design: [Message](https://huddle.powerapp.cloud/projects/280) · [Message Composer](https://huddle.powerapp.cloud/projects/511) · [Reactions](https://huddle.powerapp.cloud/projects/490) · [Attachments](https://huddle.powerapp.cloud/projects/570) · [GIF Picker](https://huddle.powerapp.cloud/projects/528) · [Loading](https://huddle.powerapp.cloud/projects/590) · [Error Messaging](https://huddle.powerapp.cloud/projects/506)

### MSG-SEND-001: Sent messages appear at once as pending
`req~MSG-SEND-001~1`

A sent message shows at the bottom of the Conversation View at once (Local Echo),
faded, with a spinner in place of its timestamp, until the server confirms it.

    Given a person is in a conversation
    When they send "hello"
    Then "hello" appears at the bottom, faded, with a spinner where the timestamp goes
    And when the server confirms it, it shows normally with its timestamp

Rationale:
Waiting on the network before showing the message makes the app feel broken.

Needs: ccl, browser, pwa, macos, ios

### MSG-SEND-002: On Apple, a failed message turns red with Retry and Delete
`req~MSG-SEND-002~1`

On Apple, a message that cannot be sent stays in the Conversation View, turns red,
and offers Retry and Delete.

    Given a person sends a message on their iPhone while the server is unreachable
    When the send fails
    Then the message stays in the Conversation View in red
    And it offers "Retry" and "Delete"

Rationale:
A failed message must be visible and recoverable, or the person believes it was delivered.

Needs: ccl, macos, ios

### MSG-SEND-003: Empty messages are not sent
`req~MSG-SEND-003~1`

A message that is empty or only whitespace is never sent. An attachment with no
text is not empty.

    Given a person has typed only spaces
    When they try to send
    Then nothing is sent

Rationale:
Prevents accidental blank messages.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-SEND-004: On Apple, an unconfirmed message fails after about 30 seconds
`req~MSG-SEND-004~1`

On Apple, a message the server has not confirmed after about 30 seconds becomes
failed. It is not held to send later.

    Given a person sends a message on a plane with no connection
    When about 30 seconds pass without the server confirming it
    Then the message shows as failed, with Retry and Delete

Rationale:
A message that stays pending forever leaves the person unsure whether it went. Failing it lets them decide what to do.

Needs: ccl, macos, ios

### MSG-SEND-005: Text goes ahead of an upload
`req~MSG-SEND-005~1`

A text message sent while a photo or file is still uploading is delivered straight
away, ahead of the attachment.

    Given a person starts uploading a large video
    When they send "video coming" while it uploads
    Then "video coming" arrives first
    And the video arrives when its upload finishes

Rationale:
A short message should never wait behind a large upload.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-SEND-006: Only broadcasters post in a Broadcast Room
`req~MSG-SEND-006~1`

In a Broadcast Room only its broadcasters can post. Everyone else does not see a
Message Composer.

    Given a person who is not a broadcaster in the "Company News" Broadcast Room
    When they open it
    Then there is no Message Composer
    And they can read but not post

Rationale:
Broadcast Rooms are for announcements to large audiences. Offering a composer that cannot send would only frustrate people.

Needs: server, ccl, browser, pwa, macos, ios

### MSG-SEND-007: No sending to a conversation you have left
`req~MSG-SEND-007~1`

A person cannot send a message to a conversation they have left or been removed
from.

    Given a person was removed from a conversation
    When they try to send a message to it
    Then they are told they cannot post there

Rationale:
Being out of a conversation must mean being out of it.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-SEND-008: The Message Composer waits until Connect knows you can post
`req~MSG-SEND-008~1`

When a conversation opens, the Message Composer stays off until Connect knows
whether the person can post there.

    Given a person opens a conversation
    When Connect has not yet confirmed they can post there
    Then the Message Composer is off
    And it turns on once Connect confirms they can

Rationale:
A composer that lets someone type and then refuses to send is worse than one that waits a moment.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-SEND-009: A pending message has no actions
`req~MSG-SEND-009~1`

While a message is pending, its actions (react, Copy, Edit, Delete, pin) are
blocked.

    Given a person's message is still pending
    When they open its Reaction Bar
    Then none of its actions can be used
    Until the server confirms the message

Rationale:
Acting on a message the server has not accepted yet could leave people seeing different versions of it.

Needs: ccl, browser, pwa, macos, ios

### MSG-SEND-010: A confirmed message keeps its place
`req~MSG-SEND-010~1`

When the server confirms a pending message, it stays in the same position in the
Conversation View.

    Given a person's message is pending at the bottom of the conversation
    When the server confirms it
    Then it does not move

Rationale:
A message that jumps on confirmation makes people think something went wrong.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-COMPOSE-001: In the Browser, Enter sends
`req~MSG-COMPOSE-001~1`

In the Browser, Enter sends the message and Shift+Enter starts a new line.

    Given a person is typing in Connect Browser
    When they press Enter
    Then the message is sent
    But Shift+Enter adds a new line instead

Rationale:
That is what people expect from chat on a keyboard.

Needs: browser

### MSG-COMPOSE-002: Pasting a picture or file attaches it
`req~MSG-COMPOSE-002~1`

Pasting a picture or file into the Message Composer adds it as an attachment draft.
This works on every client except the PWA.

    Given a person copies a screenshot
    When they paste it into the Message Composer
    Then the screenshot is added as an attachment draft, not yet sent

Rationale:
Copy and paste is the quickest way to share a screenshot.

Needs: browser, macos, ios

### MSG-COMPOSE-003: Dropping files attaches them
`req~MSG-COMPOSE-003~1`

On Desktop, dragging files onto a conversation adds each one as an attachment
draft.

    Given a person on their laptop drags two photos onto a conversation
    When they drop them
    Then both are added as attachment drafts, not yet sent

Rationale:
Usually people want to look over what they are sending before it goes.

Needs: browser, pwa, macos

### MSG-COMPOSE-004: Leaving with unsent attachments asks first
`req~MSG-COMPOSE-004~1`

Closing or reloading Connect on Web while attachments are waiting to be sent asks
the person to confirm.

    Given a person attached a file but has not sent it
    When they close the browser tab
    Then the browser asks whether they really want to leave

Rationale:
Closing a tab by accident should not quietly throw away files someone picked.

Status: draft

Needs: browser, pwa

### MSG-COMPOSE-005: On macOS, Return sends
`req~MSG-COMPOSE-005~1`

On macOS, Return sends the message. Shift+Return or Option+Return starts a new
line.

    Given a person is typing in Connect for Mac
    When they press Return
    Then the message is sent
    But Shift+Return or Option+Return adds a new line instead

Rationale:
That is what people expect from chat on a keyboard, and Option+Return matches other Mac apps.

Needs: macos

### MSG-COMPOSE-006: On iOS, Return adds a new line
`req~MSG-COMPOSE-006~1`

On iOS, Return in the Message Composer starts a new line, as does Shift+Return.

    Given a person is typing on their iPhone
    When they press Return
    Then a new line is added and nothing is sent

Rationale:
On a phone the send button is right there, and an accidental send is easy.

Needs: ios

### MSG-COMPOSE-007: In the PWA, Enter adds a new line
`req~MSG-COMPOSE-007~1`

In the PWA, Enter starts a new line. The message is sent with the send button.

    Given a person is typing in Connect PWA on their Android phone
    When they press Enter
    Then a new line is added
    And the message is sent only when they tap the send button

Rationale:
On a phone the send button is right there, and an accidental send is easy.

Needs: pwa

### MSG-COMPOSE-008: Repeated new lines collapse to one
`req~MSG-COMPOSE-008~1`

Several new lines in a row in a sent message show as a single line break.

    Given a person types "Done", presses Shift+Return three times, and types "Thanks"
    When they send it
    Then the message shows "Done" and "Thanks" on two lines with no blank lines between

Rationale:
Keeps messages compact so the conversation stays readable.

Needs: browser, pwa, macos, ios

### MSG-COMPOSE-010: On Web, images can be dragged in from websites
`req~MSG-COMPOSE-010~1`

On Web, an image dragged from a website onto a conversation is added as an
attachment draft, like a file.

    Given a person drags an image from a web page onto a conversation in Connect Browser
    When they drop it
    Then the image is added as an attachment draft

Rationale:
Sharing something seen on the web should not mean saving it to disk first.

Needs: browser, pwa

### MSG-COMPOSE-011: Dragging files shows where to drop them
`req~MSG-COMPOSE-011~1`

While files are dragged over a conversation, it shows "Drag and drop files here".

    Given a person drags a file over a conversation
    Then it shows "Drag and drop files here"

Rationale:
People need to see that dropping here will work before they let go.

Status: draft

Needs: browser, pwa

### MSG-FAIL-001: Messages queued behind a failed one show as failed
`req~MSG-FAIL-001~1`

When a message fails to send, the unsent messages after it in that conversation
show as failed too, instead of waiting forever.

    Given a person sends messages 1, 2 and 3
    When message 1 fails
    Then 1, 2 and 3 all show as failed

Rationale:
A message that spins forever is worse than one that clearly failed.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-FAIL-002: On Apple, each failed message is handled on its own
`req~MSG-FAIL-002~1`

On Apple, each failed message has its own Retry and Delete. Retrying one never
resends the others.

    Given messages 1, 2 and 3 have failed
    When the person retries only message 2
    Then only message 2 is sent
    And 1 and 3 stay as failed

Rationale:
The person may no longer want to send all of them. Each one is their choice.

Needs: ccl, macos, ios

### MSG-FAIL-003: On Apple, a retried message moves to the newest position
`req~MSG-FAIL-003~1`

On Apple, a retried message is sent as the newest message in the conversation.

    Given a message failed at 9:00
    When the person retries it at 9:30
    Then it appears after everything sent before 9:30

Rationale:
The conversation has moved on. Slotting it back at 9:00 would hide it where nobody looks.

Needs: ccl, macos, ios

### MSG-FAIL-004: Failed messages are shown at the end
`req~MSG-FAIL-004~1`

Failed messages are shown after all delivered messages, oldest first.

    Given a person has two failed messages
    When others keep posting
    Then the failed messages stay at the end of the conversation, below the new messages

Rationale:
Failed messages need the person's attention, so they stay where the person is looking.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-FAIL-005: The Conversation List flags a failed send
`req~MSG-FAIL-005~1`

A conversation with a failed message shows an error indicator on its row in the
Conversation List.

    Given a person has a failed message in "Philly Roofing"
    When they look at the Conversation List
    Then the "Philly Roofing" row shows an error indicator

Rationale:
A person who has moved on from a conversation would otherwise never know their message did not go.

Needs: ccl, browser, pwa, macos, ios

### MSG-FAIL-006: A failed send is announced wherever the person is
`req~MSG-FAIL-006~1`

When a message fails to send, the person is told even if they are no longer in that
conversation.

    Given a person sends a message and goes to another conversation
    When the message fails
    Then they see a notice that it was not sent

Rationale:
The person thinks they are done. They have to be told they are not. Open: is this notice the red send-failure toast with Retry, "There was an issue sending your message. Try again."?

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-FAIL-007: On Apple, failed messages survive a restart
`req~MSG-FAIL-007~1`

On Apple, failed messages are still there, with Retry and Delete, after Connect or
the device is restarted.

    Given a person has a failed message
    When they restart their phone and open Connect
    Then the message is still shown as failed with Retry and Delete

Rationale:
What the person wrote is theirs. A restart must not throw it away.

Status: draft

Needs: ccl, macos, ios

### MSG-FAIL-008: A failed send says why
`req~MSG-FAIL-008~1`

A failed message says why it failed: no connection, not allowed to post there, too
large, signed out, or possibly sent already.

    Given a message's sending timed out and may have reached Connect
    When it shows as failed
    Then it says it may already have been sent
    So the person can check before retrying

Rationale:
The right next step depends on the reason. Retrying an "already sent" message could send it twice.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-FAIL-009: Only failed messages offer Retry
`req~MSG-FAIL-009~1`

Retry is offered only for messages that failed to send. A failed edit, reaction or
delete is not retried; the person does it again.

    Given a person's edit fails to save
    Then the message keeps its old text
    And the person can edit it again

Rationale:
An edit, reaction or delete is quick to redo, and holding failed ones for later adds clutter for little gain.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-FAIL-010: In the Browser, a failed message offers Retry and Delete inline
`req~MSG-FAIL-010~1`

In the Browser, a failed message shows "There was a problem sending your message"
with Retry and Delete right on the message.

    Given a person sends a message in Connect Browser while offline
    When the send fails
    Then the message shows "There was a problem sending your message"
    And Retry and Delete are shown inline on it

Rationale:
A failed message must be visible and recoverable, or the person believes it was delivered.

Needs: browser

### MSG-FAIL-011: In the PWA, a failed message offers Retry and Delete in a menu
`req~MSG-FAIL-011~1`

In the PWA, a failed message shows "There was a problem sending your message", and
Retry and Delete are in a menu on the message.

    Given a person sends a message in Connect PWA while offline
    When the send fails
    Then the message shows "There was a problem sending your message"
    And opening its menu offers Retry and Delete

Rationale:
A failed message must be visible and recoverable, and a menu keeps the small screen uncluttered.

Needs: pwa

### MSG-FAIL-012: A failed image or GIF can be retried
`req~MSG-FAIL-012~1`

An image or GIF that fails to send offers Retry, like a text message.

    Given a person's GIF fails to send
    When they choose Retry
    Then the same GIF is sent again

Rationale:
Picking the image or GIF again is a chore, and the person already chose it once.

Needs: browser, pwa, macos, ios

### MSG-FAIL-013: On Web, failed messages clear on refresh or sign-out
`req~MSG-FAIL-013~1`

On Web, failed messages are cleared when the page is refreshed or the person signs
out.

    Given a person has a failed message in Connect Browser
    When they refresh the page
    Then the failed message is gone

Rationale:
A refresh or sign-out starts the Web app over from what the server has, and a failed message never reached the server.

Needs: browser, pwa

### MSG-ACTION-001: On Desktop, hovering a message shows its actions
`req~MSG-ACTION-001~1`

On Desktop, hovering over a message shows its Reaction Bar: quick reactions, the
emoji picker, and the message actions.

    Given a person is reading a conversation on their Mac
    When they hover over a message
    Then its Reaction Bar appears

Rationale:
On a computer the mouse is already there, so actions appear without an extra click.

Needs: browser, macos

### MSG-ACTION-002: On iOS, long-pressing a message shows its actions
`req~MSG-ACTION-002~1`

On iOS, long-pressing a message shows its Reaction Bar.

    Given a person is reading a conversation on their iPhone
    When they long-press a message
    Then its Reaction Bar appears

Rationale:
Long-press is how iOS apps offer actions on an item without getting in the way of scrolling.

Needs: ios

### MSG-ACTION-003: In the PWA, tapping a message shows its actions
`req~MSG-ACTION-003~1`

In the PWA, tapping a message shows its Reaction Bar.

    Given a person is reading a conversation in Connect PWA
    When they tap a message
    Then its Reaction Bar appears

Rationale:
A touch screen has no hover, so a tap opens the actions.

Needs: pwa

### MSG-ACTION-004: Any message can be copied
`req~MSG-ACTION-004~1`

Every message offers Copy, which copies its text.

    Given a person opens the Reaction Bar on someone else's message
    When they choose Copy
    Then the message text is copied

Rationale:
People often need to reuse what someone wrote, in Connect or elsewhere.

Needs: browser, pwa, macos, ios

### MSG-ACTION-005: Only Room Admins can pin messages
`req~MSG-ACTION-005~1`

In a room, only Room Admins are offered Pin on a message.

    Given Dana is a Room Admin of "Philly Roofing" and Bob is a member
    When each opens the Reaction Bar on a message
    Then Dana is offered Pin
    But Bob is not

Rationale:
Pinned messages speak for the room, so pinning is limited to the people who run it.

Needs: server, macos, ios

### MSG-EDIT-001: Edited messages show "(edited)"
`req~MSG-EDIT-001~1`

An edited message shows its latest text, followed by "(edited)".

    Given Bob edits his message
    When others look at it
    Then they see the new text, marked "(edited)"

Rationale:
People act on what messages say. They need to know when one changed.

Needs: ccl, browser, pwa, macos, ios

### MSG-EDIT-002: Edits are noted where they happened
`req~MSG-EDIT-002~1`

When someone edits a message, a line at that point in the conversation says so.
Edits in a row are noted on one line.

    Given Brandon Maul edits three earlier messages one after another
    When others look at the conversation
    Then at that point it says "Brandon Maul edited 3 messages."
    And if Brandon and Jessy both edited, it says "Brandon & Jessy edited messages."

Rationale:
An edit to an old message is easy to miss. The note tells people to look.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-EDIT-003: A pending message cannot be edited
`req~MSG-EDIT-003~1`

A message can only be edited once the server has confirmed it, not while it is
pending.

    Given a person's message is still pending
    When they look for Edit
    Then they cannot edit it yet

Rationale:
Editing something that has not arrived yet would leave people seeing two different versions.

Needs: ccl, browser, pwa, macos, ios

### MSG-EDIT-004: An edit cannot add new @mentions
`req~MSG-EDIT-004~1`

Editing a message cannot add an @mention that was not in the message when it was
sent.

    Given a message mentioned Alice
    When its author edits it and tries to mention Bob
    Then Bob cannot be added as an @mention

Rationale:
A mention notifies someone. Adding one quietly to an old message would ask for attention without anyone seeing the request.

Needs: ccl, browser, pwa, macos, ios

### MSG-EDIT-005: Only the sender can edit
`req~MSG-EDIT-005~1`

Only the person who sent a message is offered Edit on it.

    Given Bob sent a message
    Then Bob can edit it
    But Dana, even as a Room Admin, cannot

Rationale:
A message is the sender's words. Nobody else should be able to change them.

Needs: server, ccl, browser, pwa, macos, ios

### MSG-EDIT-006: Messages can be edited at any time
`req~MSG-EDIT-006~1`

There is no time limit on editing your own message.

    Given Bob sent a message a year ago
    Then Bob can still edit it

Rationale:
A correction is useful whenever the mistake is noticed.

Status: draft

Needs: server, ccl, browser, pwa, macos, ios

### MSG-EDIT-007: On Web, image-only messages can only be deleted
`req~MSG-EDIT-007~1`

On Web, a message that is only an image can be deleted but not edited.

    Given a person sent a message that is only a photo, in Connect Browser
    When they open its actions
    Then Delete is offered
    But Edit is not

Rationale:
An image-only message has no text to edit; to change it, the person deletes it and sends another.

Needs: browser, pwa

### MSG-DELETE-001: Deleted messages disappear
`req~MSG-DELETE-001~1`

A deleted message disappears from the conversation for everyone, without a "message
deleted" placeholder.

    Given Bob deletes his message
    When anyone looks at the conversation
    Then the message is gone, with nothing in its place

Rationale:
A deleted message is usually one that should not have been sent. A placeholder still draws attention to it.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-DELETE-002: Deleting works offline
`req~MSG-DELETE-002~1`

Deleting a message without a connection takes effect when the connection returns.

    Given a person deletes a message while offline
    When they are back online
    Then the message is deleted for everyone

Rationale:
Someone who deletes a message wants it gone, and should not have to remember to do it again.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-DELETE-003: Only the sender can delete
`req~MSG-DELETE-003~1`

Only the person who sent a message is offered Delete on it.

    Given Bob sent a message
    Then Bob can delete it
    But Dana cannot

Rationale:
A message is the sender's words. Only they decide to take it back.

Needs: server, ccl, browser, pwa, macos, ios

### MSG-REACT-001: Reactions are tapped on and off
`req~MSG-REACT-001~1`

Reactions show as Reaction Buttons, one per emoji, with a count. Clicking a
Reaction Button adds your reaction, and clicking it again removes it.

    Given two people reacted 👍 to a message
    When a third person clicks the 👍 Reaction Button
    Then it shows 👍 3, including them
    And clicking it again takes theirs away

Rationale:
Reactions are quick replies. They have to be quick to undo too.

Needs: ccl, browser, pwa, macos, ios

### MSG-REACT-002: Reacting does not mark a conversation read
`req~MSG-REACT-002~1`

Reacting to a message does not mark the conversation as read.

    Given a conversation has unread messages
    When the person reacts to an older message in it
    Then the conversation is still unread

Rationale:
Reacting to one message is not reading the rest.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-REACT-003: Five quick reactions, plus any emoji
`req~MSG-REACT-003~1`

The Reaction Bar offers five quick reactions (like, dislike, happy, love, laugh),
and the Add Reaction Button opens an emoji picker for any other emoji.

    Given a person opens the Reaction Bar on a message
    Then it offers like, dislike, happy, love and laugh
    And the Add Reaction Button opens the emoji picker

Rationale:
The common reactions are one tap away, and anything else is still possible.

Needs: browser, pwa, macos, ios

### MSG-REACT-004: People can see who reacted
`req~MSG-REACT-004~1`

A reaction shows the names of up to 3 people who reacted with it; when more reacted,
the full list is shown in a modal.

    Given five people reacted 👍 to a message
    When a person checks who reacted
    Then up to 3 names are shown
    And the full list of five is available in a modal

Rationale:
Who reacted often matters as much as how many did.

Needs: browser, pwa, macos, ios

### MSG-REACT-005: A pending reaction shows a spinner
`req~MSG-REACT-005~1`

A reaction that the server has not yet confirmed shows a single spinner.

    Given a person adds a 👍 reaction
    When the server has not confirmed it yet
    Then the reaction shows one spinner
    And the spinner goes away once it is confirmed

Rationale:
The person sees their reaction land at once, and can tell it has not gone through yet.

Needs: ccl, browser, pwa, macos, ios

### MSG-REACT-006: A failed reaction is reverted
`req~MSG-REACT-006~1`

A reaction that fails is undone and the person sees "There was an issue with your
reaction. Try again."

    Given a person adds a 👍 reaction while the server is unreachable
    When the reaction fails
    Then the 👍 is removed
    And they see "There was an issue with your reaction. Try again."

Rationale:
A reaction that looks added but never reached anyone is misleading. Undoing it and saying so lets the person try again.

Needs: ccl, browser, pwa, macos, ios

### MSG-MENTION-001: Only the people picked are mentioned
`req~MSG-MENTION-001~1`

A message mentions the people the sender picked from the suggestions, and only
those people are notified.

    Given a person types "@Han Solo" and picks Han Solo
    When they send it
    Then Han Solo is notified

Rationale:
Guessing mentions from text would notify the wrong people, or miss the right ones.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-MENTION-002: A broken mention never stops a message
`req~MSG-MENTION-002~1`

If something is wrong with a mention in a message, the message is still sent.

    Given a message with a mention that cannot be read
    When it is sent
    Then it is sent with the rest of its text

Rationale:
One bad mention must never cost someone their whole message.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-MENTION-003: An @mention acts as one unit
`req~MSG-MENTION-003~1`

In the Message Composer, an @mention behaves as a single unit rather than as
separate letters.

    Given a person has added "@Han Solo" to a message
    When they press Delete just after it
    Then the whole mention is removed, not just the last letter

Rationale:
A half-deleted mention would no longer point at anyone, and would look like a typo.

Needs: browser, pwa, macos, ios

### MSG-MENTION-004: Mentions of others are highlighted yellow
`req~MSG-MENTION-004~1`

An @mention of someone other than you shows blue text on a yellow highlight.

    Given a message mentions Han Solo
    When Leia reads it
    Then "@Han Solo" shows in blue text on a yellow highlight

Rationale:
Mentions stand out from the rest of the message so people can see who was asked.

Needs: browser, pwa, macos, ios

### MSG-MENTION-005: Mentions of you and @all are highlighted blue
`req~MSG-MENTION-005~1`

An @mention of you, and @all, shows with a blue highlight.

    Given a message mentions Han Solo and @all
    When Han Solo reads it
    Then "@Han Solo" and "@all" show with a blue highlight

Rationale:
Blue is reserved for what needs your attention, so a mention of you stands out from mentions of others.

Needs: browser, pwa, macos, ios

### MSG-ATTACH-001: Uploads show their progress
`req~MSG-ATTACH-001~1`

While a photo or file uploads, the person sees its name and progress, and can
cancel it.

    Given a person attaches a 50 MB video
    When it is uploading
    Then they see its name and how far it has got
    And they can cancel it

Rationale:
Large uploads take time. Without progress, people assume it is stuck and send it again.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-ATTACH-002: A failed upload is retried without picking the file again
`req~MSG-ATTACH-002~1`

A failed upload stays in the conversation with Retry, which sends the same file
without picking it again, even after a restart.

    Given a person's upload fails
    When they tap Retry the next day
    Then the same file uploads

Rationale:
Finding the file again is a chore, and on a phone it may no longer be at hand.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-ATTACH-003: A cancelled upload disappears straight away
`req~MSG-ATTACH-003~1`

Cancelling an upload removes it from the conversation at once.

    Given a photo is uploading
    When the person cancels it
    Then it is gone from the conversation immediately

Rationale:
Cancel means "I didn't mean that". It should feel instant.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-ATTACH-004: A caption belongs to its photo or file
`req~MSG-ATTACH-004~1`

A caption is part of the same message as its photo or file, never a separate
message.

    Given a person sends a photo with the caption "Front of the house"
    Then the conversation shows one message: the photo with its caption

Rationale:
Split apart, a caption can end up next to the wrong photo. Open: each attachment sends as its own message; does text typed with an attachment go in the same message or as a separate one?

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-ATTACH-005: GIFs show GIPHY attribution
`req~MSG-ATTACH-005~1`

A GIF from the GIF picker is shown with GIPHY attribution.

    Given a person sends a GIF from the GIF picker
    When others see it
    Then it shows with GIPHY attribution

Rationale:
The GIF service requires attribution, and it tells people where the GIF came from.

Needs: ccl, browser, pwa, macos, ios

### MSG-ATTACH-006: Files from 1 byte to 150 MB
`req~MSG-ATTACH-006~1`

A person can attach a file from 1 byte up to 150 MB, on every client.

    Given a person attaches a 149 MB video
    Then it can be sent
    But a 200 MB video cannot

Rationale:
One limit everywhere means a file that sends from one device sends from all of them.

Needs: server, browser, pwa, macos, ios

### MSG-ATTACH-007: Adding a file creates a draft
`req~MSG-ATTACH-007~1`

Adding a file to a conversation creates an attachment draft. It is sent only when
the person sends it.

    Given a person picks a PDF from the "+" attachment menu
    Then the PDF waits in the Message Composer as a draft
    And it is sent only when they send

Rationale:
People can check what they picked, or remove it, before anyone sees it.

Needs: browser, pwa, macos, ios

### MSG-ATTACH-008: Each attachment is its own message
`req~MSG-ATTACH-008~1`

When several attachments are sent together, each one arrives as its own message.

    Given a person has three photos as attachment drafts
    When they send
    Then the conversation shows three messages, one photo each

Rationale:
Each file can then be reacted to, replied about or deleted on its own.

Needs: ccl, browser, pwa, macos, ios

### MSG-ATTACH-009: The file types Connect accepts
`req~MSG-ATTACH-009~1`

Connect accepts these file types: aac, aiff, m4a, mp3, wav, wma; csv, docx, key,
numbers, pages, pdf, pptx, rtf, txt, xlsx; bmp, gif, heic, jpg, jp2, png, svg, tiff,
webp; zip; avi, mov, mp4, mpeg, mpg, wmv.

    Given a person attaches a .numbers spreadsheet
    Then it can be sent
    But a file of a type not on the list cannot

Rationale:
The list covers the audio, documents, images, archives and video people share for work, and every client accepts the same set.

Needs: server, browser, pwa, macos, ios

### MSG-ATTACH-010: Files that cannot be sent are refused before uploading
`req~MSG-ATTACH-010~1`

A file that is too large or empty is refused before it starts uploading, and the
person is told why.

    Given a person attaches a 200 MB video
    Then it is refused before it starts uploading
    And they are told it is over the 150 MB limit

Rationale:
Telling people before a long upload saves them waiting for a failure.

Status: draft

Needs: browser, pwa, macos, ios

### MSG-ATTACH-011: The GIF picker offers All GIFs and Power GIFs
`req~MSG-ATTACH-011~1`

The GIF picker has two choices: All GIFs, which are G-rated only, and Power GIFs.

    Given a person opens the GIF picker
    Then they can choose between All GIFs and Power GIFs
    And All GIFs shows only G-rated GIFs

Rationale:
Connect is a workplace tool, so general GIFs are kept G-rated, and Power's own GIFs are easy to find.

Needs: browser, pwa, macos, ios

### MSG-ATTACH-012: Picking a GIF sends it
`req~MSG-ATTACH-012~1`

Picking a GIF in the GIF picker sends it immediately, without a draft.

    Given a person opens the GIF picker
    When they pick a GIF
    Then it is sent at once

Rationale:
A GIF is a quick reaction. Asking to confirm it would slow it down.

Needs: browser, pwa, macos, ios

### MSG-ATTACH-013: On Web, GIFs stop playing after 5 seconds
`req~MSG-ATTACH-013~1`

On Web, a GIF plays for up to 5 seconds, then stops and shows "Hover to continue
playing".

    Given a GIF is shown in a conversation in Connect Browser
    When it has played for 5 seconds
    Then it stops and shows "Hover to continue playing"
    And hovering over it plays it again

Rationale:
Endless motion distracts from reading the conversation.

Needs: browser, pwa

### MSG-ATTACH-014: On Web, GIF thumbnails are at most 360px or 312px
`req~MSG-ATTACH-014~1`

On Web, a GIF thumbnail is at most 360px on screens 620px wide or more, and at most
312px on narrower screens.

    Given a large GIF in a conversation on Web
    Then it shows no larger than 360px on a Desktop Large Screen
    And no larger than 312px on Small Screens

Rationale:
A GIF should not take over the conversation, and narrower screens have less room.

Needs: browser, pwa

### MSG-ATTACH-015: On Web, GIF thumbnails are at least 60px
`req~MSG-ATTACH-015~1`

On Web, a GIF thumbnail is never shown smaller than 60px.

    Given a very small GIF in a conversation on Web
    Then it shows at least 60px

Rationale:
Below that size a GIF is too small to make out.

Needs: browser, pwa

### MSG-DRAFT-001: Drafts are kept when switching conversations
`req~MSG-DRAFT-001~1`

Unsent text, @mentions and attachments are kept for each conversation and are still
there when the person switches away and back.

    Given a person types half a message in "Philly Roofing", mentions Alex, and attaches a photo
    When they switch to another conversation and back
    Then the text, the mention and the photo are still in the Message Composer

Rationale:
Interruptions are constant. Losing what you were writing is maddening.

Needs: ccl, browser, pwa, macos, ios

### MSG-DRAFT-002: Drafts stay on the device
`req~MSG-DRAFT-002~1`

Unsent text is kept only on the device it was typed on. It is never sent to Connect
or shown on the person's other devices.

    Given a person has a draft on their phone
    When they open the same conversation on their Mac
    Then the draft is not there

Rationale:
Something a person has not sent is not shared yet, not even with Connect.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-DRAFT-003: Sending or clearing the text removes the draft
`req~MSG-DRAFT-003~1`

Sending the message, or clearing the text, removes the draft, so nothing blank or
already sent comes back.

    Given a person has a draft
    When they delete all its text and leave the conversation
    Then there is no draft when they come back

Rationale:
A draft that comes back after it was sent or deleted looks like a message that was never sent.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-DRAFT-004: Drafts survive a restart
`req~MSG-DRAFT-004~1`

A draft is still there after Connect or the device is restarted.

    Given a person has a half-written message in "Philly Roofing"
    When they restart their phone and open "Philly Roofing"
    Then their half-written message is still in the Message Composer

Rationale:
A restart should not cost someone what they were writing.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-READ-001: Unread starts after the last message the person read
`req~MSG-READ-001~1`

The first unread message is the oldest message after the last one the person read.
When everything is read, there is none.

    Given a person has read up to message 40 of 50
    When the conversation is opened
    Then message 41 is the first unread message

Rationale:
It decides where a conversation opens, so every device must agree on it.

Status: draft

Needs: ccl, browser, pwa, macos, ios

### MSG-READ-002: Reading clears unread everywhere
`req~MSG-READ-002~1`

Reading up to the newest message clears bold (unread), the Notification Badge and
the New Message Indicator on every device the person is signed in on.

    Given a person has 3 unread messages and two signed-in devices
    When they read to the newest message on one device
    Then the other device shows the conversation as read

Rationale:
An unread badge that survives reading is the most reported annoyance in a chat product.

Status: draft

Needs: server, ccl, browser, pwa, macos, ios

### MSG-READ-003: Opens at the New Message Indicator
`req~MSG-READ-003~1`

Opening a conversation with unread messages scrolls to the New Message Indicator.

    Given a conversation has unread messages
    When the person opens it
    Then it scrolls to the New Message Indicator

Rationale:
Opening at the newest message hides what was missed.

Needs: browser, pwa, macos, ios

### MSG-READ-004: Being added to a conversation does not make it unread
`req~MSG-READ-004~1`

Being added to a conversation does not, by itself, make it show as unread. Only
messages do.

    Given a person is added to a conversation that has no messages they have not seen
    When they look at their Conversation List
    Then the conversation is not bold (unread)
    And it adds nothing to the app icon badge

Rationale:
People are added to Rooms automatically all the time by Member filters. If each one looked unread, badges would mean nothing.

Status: draft

Needs: server

### MSG-READ-005: Loading older messages keeps your place
`req~MSG-READ-005~1`

When older messages load as a person scrolls up, the message they were looking at
stays where it was on screen.

    Given a person is scrolling up through a conversation
    When older messages load above what they are reading
    Then the message they were reading does not move

Rationale:
A jump loses the person's place. After a few they stop scrolling back at all.

Status: draft

Needs: browser, pwa, macos, ios

### MSG-READ-006: Only reading marks a conversation read
`req~MSG-READ-006~1`

A conversation becomes read only when the person reaches its newest message, taps
the Message Composer or the message area, sends a message, or uses Mark as Read.

    Given a conversation is unread and the person is scrolled up in it
    When they scroll around without reaching the newest message
    Then it is still unread
    But tapping the Message Composer marks it read at once

Rationale:
Unread means "there is something you have not seen". Only actions that show the person is looking at the conversation change that.

Needs: ccl, browser, pwa, macos, ios

### MSG-READ-007: Sending a message marks the conversation read
`req~MSG-READ-007~1`

Sending a message in a conversation marks it read at once.

    Given a conversation has unread messages
    When the person sends a reply in it
    Then the conversation is marked read

Rationale:
Someone replying is in the conversation and looking at it.

Needs: ccl, browser, pwa, macos, ios

### MSG-READ-008: People can mark a conversation read or unread
`req~MSG-READ-008~1`

From the Conversation options menu, a person can mark a conversation read, which
clears it at once, or unread, which shows it bold with an empty Notification Badge
until a notifying message adds a count.

    Given a person has read a conversation
    When they mark it unread
    Then it shows bold with an empty Notification Badge
    Until they read it, or a notifying message adds a count

Rationale:
Marking unread is how people leave themselves a reminder to come back.

Needs: ccl, browser, pwa, macos, ios

### MSG-READ-009: Messages stay unread while Connect is not in focus
`req~MSG-READ-009~1`

Messages only count as read while Connect is in focus. New messages that arrive
while it is not stay unread until it is.

    Given Connect is open but another window is in front
    When new messages arrive in the open conversation
    Then they stay unread
    Until the person brings Connect back into focus

Rationale:
A message on a screen nobody is looking at has not been read.

Needs: browser, pwa, macos, ios

### MSG-READ-010: A fully read conversation opens at the newest message
`req~MSG-READ-010~1`

Opening a conversation with nothing unread shows its newest message.

    Given a person has read everything in a conversation
    When they open it
    Then it opens at the newest message

Rationale:
With nothing missed, the latest message is where the person picks up.

Status: draft

Needs: browser, pwa, macos, ios

### MSG-RETAIN-001: Messages are kept for six months
`req~MSG-RETAIN-001~1`

Messages older than six months are removed from Connect, in both v2 and v3.

    Given a message was sent more than six months ago
    When a week has passed
    Then the message is no longer in Connect

Rationale:
Product to decide how long messages are kept. Whatever the period, v2 and v3 must keep the same history, or the same conversation shows different messages in each.

Status: draft

Needs: nitro, server
