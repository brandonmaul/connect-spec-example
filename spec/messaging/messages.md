# Messages

Sending and reading messages.

**Area code:** `MSG`

**Topics**

| Topic | Covers |
|---|---|
| `SEND` | Sending a message, and what happens when it fails |
| `COMPOSE` | Typing, pasting and dropping into the composer |
| `FAIL` | Messages that could not be sent |
| `EDIT` | Editing a message |
| `DELETE` | Deleting a message |
| `REACT` | Reactions |
| `MENTION` | Mentioning people in a message |
| `ATTACH` | Photos, files and GIFs |
| `DRAFT` | Unsent text kept for later |
| `READ` | Unread and read state, and where a conversation opens |
| `RETAIN` | How long messages are kept |

Design: <figma link> · Runway: <epic link>

### MSG-SEND-001: Sent messages appear immediately
`req~MSG-SEND-001~1`

A sent message shows at the bottom of the timeline at once, marked pending, and
keeps its position when the server confirms it.

    Given a user is in a conversation
    When they send "hello"
    Then "hello" appears at the bottom marked as pending
    And when the server confirms it the pending mark goes away
    And it stays in the same position

Rationale:
Waiting on the network before showing the message makes the app feel broken.

Needs: ios, macos, web

### MSG-SEND-002: Failed sends can be retried
`req~MSG-SEND-002~1`

A message that cannot be sent stays visible as failed, with Retry and Delete.

    Given a user sends a message while the server is unreachable
    When the send fails
    Then the message stays in the timeline marked as failed
    And it offers "Retry" and "Delete"

Rationale:
A failed message must be visible and recoverable, or the user believes it was delivered.

Needs: ios, macos, web

### MSG-SEND-003: Empty messages are not sent
`req~MSG-SEND-003~1`

A message that is empty or only whitespace is never sent. An attachment with no
text is not empty.

    Given a user has typed only spaces
    When they try to send
    Then nothing is sent

Rationale:
Prevents accidental blank messages.

Needs: ccl

### MSG-SEND-004: Messages sent offline go when the connection returns
`req~MSG-SEND-004~1`

A message sent without a connection waits on the device and is sent when the
connection returns, even if Connect was closed in between.

    Given a person sends a message on a plane
    When they land, and open Connect after restarting their phone
    Then the message is sent

Rationale:
People write when they have a moment, not when they have signal.

Needs: ccl

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

Needs: ccl

### MSG-SEND-006: Only broadcasters post in a broadcast conversation
`req~MSG-SEND-006~1`

In a broadcast conversation only its broadcasters can post. For everyone else the
composer is off.

    Given a person who is not a broadcaster in the "Company News" broadcast conversation
    When they open it
    Then the composer is off
    And they can read but not post

Rationale:
Broadcast conversations are for announcements to large audiences. Offering a composer that cannot send would only frustrate people.

Needs: ccl, server

### MSG-SEND-007: No sending to a conversation you have left
`req~MSG-SEND-007~1`

A person cannot send a message to a conversation they have left or been removed
from.

    Given a person was removed from a conversation
    When they try to send a message to it
    Then they are told they cannot post there

Rationale:
Being out of a conversation must mean being out of it.

Needs: ccl

### MSG-SEND-008: The composer waits until Connect knows you can post
`req~MSG-SEND-008~1`

When a conversation opens, the composer stays off until Connect knows whether the
person can post there.

    Given a person opens a conversation
    When Connect has not yet confirmed they can post there
    Then the composer is off
    And it turns on once Connect confirms they can

Rationale:
A composer that lets someone type and then refuses to send is worse than one that waits a moment.

Needs: ccl, ios, macos, web

### MSG-COMPOSE-001: Enter sends on a computer
`req~MSG-COMPOSE-001~1`

On a computer, Enter sends the message and Shift+Enter starts a new line. On a
phone or narrow window, Enter starts a new line.

    Given a person is typing in Connect on their laptop
    When they press Enter
    Then the message is sent
    But on their phone, Enter adds a new line

Rationale:
That is what people expect from chat on a keyboard. On a phone the send button is right there, and an accidental send is easy.

Needs: web

### MSG-COMPOSE-002: Pasting a picture or file attaches it
`req~MSG-COMPOSE-002~1`

Pasting a picture or file into the composer attaches it, ready to send with a
message.

    Given a person copies a screenshot
    When they paste it into the composer
    Then the screenshot is attached
    And they can write a message before sending

Rationale:
Copy and paste is the quickest way to share a screenshot on a computer.

Needs: web

### MSG-COMPOSE-003: Dropping files attaches them
`req~MSG-COMPOSE-003~1`

Dragging files onto a conversation attaches them, ready to send with a message.
Holding Shift while dropping sends them straight away.

    Given a person drags two photos onto a conversation
    Then it shows "Drag and drop files here"
    And dropping them attaches both
    But dropping them while holding Shift sends them immediately

Rationale:
Usually people want to say what they are sending. Sometimes the files speak for themselves.

Needs: web

### MSG-COMPOSE-004: Leaving with unsent attachments asks first
`req~MSG-COMPOSE-004~1`

Closing or reloading Connect in a browser while attachments are waiting to be sent
asks the person to confirm.

    Given a person attached a file but has not sent it
    When they close the browser tab
    Then the browser asks whether they really want to leave

Rationale:
Closing a tab by accident should not quietly throw away files someone picked.

Needs: web

### MSG-FAIL-001: Messages queued behind a failed one show as failed
`req~MSG-FAIL-001~1`

When a message fails to send, the unsent messages after it in that conversation
show as failed too, instead of waiting forever.

    Given a person sends messages 1, 2 and 3
    When message 1 fails
    Then 1, 2 and 3 all show as failed

Rationale:
A message that spins forever is worse than one that clearly failed.

Needs: ccl

### MSG-FAIL-002: Each failed message is retried on its own
`req~MSG-FAIL-002~1`

Each failed message has its own Retry and Delete. Retrying one never resends the
others.

    Given messages 1, 2 and 3 have failed
    When the person retries only message 2
    Then only message 2 is sent
    And 1 and 3 stay as failed

Rationale:
The person may no longer want to send all of them. Each one is their choice.

Needs: ccl

### MSG-FAIL-003: A retried message is sent as a new message
`req~MSG-FAIL-003~1`

A retried message is sent as the newest message in the conversation, with the time
it was actually sent.

    Given a message failed at 9:00
    When the person retries it at 9:30
    Then it appears after everything sent before 9:30, timed 9:30

Rationale:
The conversation has moved on. Slotting it back at 9:00 would hide it where nobody looks.

Needs: ccl

### MSG-FAIL-004: Failed messages are shown at the end
`req~MSG-FAIL-004~1`

Failed messages are shown after all delivered messages, oldest first.

    Given a person has two failed messages
    When others keep posting
    Then the failed messages stay at the end of the conversation, below the new messages

Rationale:
Failed messages need the person's attention, so they stay where the person is looking.

Needs: ccl

### MSG-FAIL-005: The conversation list flags failed messages
`req~MSG-FAIL-005~1`

A conversation with a failed message is marked in the conversation list until the
message is retried or deleted.

    Given a person has a failed message in "Philly Roofing"
    When they go back to the conversation list
    Then "Philly Roofing" is marked as having a failed message

Rationale:
A person who has moved on from a conversation would otherwise never know their message did not go.

Needs: ccl, ios, macos, web

### MSG-FAIL-006: A failed send is announced wherever the person is
`req~MSG-FAIL-006~1`

When a message fails to send, the person is told even if they are no longer in that
conversation.

    Given a person sends a message and goes to another conversation
    When the message fails
    Then they see a notice that it was not sent

Rationale:
The person thinks they are done. They have to be told they are not.

Needs: ccl, ios, macos, web

### MSG-FAIL-007: Failed messages survive a restart
`req~MSG-FAIL-007~1`

Failed messages are still there, with Retry and Delete, after Connect or the device
is restarted.

    Given a person has a failed message
    When they restart their phone and open Connect
    Then the message is still shown as failed with Retry and Delete

Rationale:
What the person wrote is theirs. A restart must not throw it away.

Needs: ccl

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

Needs: ccl, ios, macos, web

### MSG-FAIL-009: Only failed messages offer Retry
`req~MSG-FAIL-009~1`

Retry is offered only for messages that failed to send. A failed edit, reaction or
delete is not retried; the person does it again.

    Given a person's edit fails to save
    Then the message keeps its old text
    And the person can edit it again

Rationale:
An edit, reaction or delete is quick to redo, and holding failed ones for later adds clutter for little gain.

Needs: ccl

### MSG-EDIT-001: Edited messages are marked as edited
`req~MSG-EDIT-001~1`

An edited message shows its latest text and is marked as edited.

    Given Bob edits his message
    When others look at it
    Then they see the new text, marked "(edited)"

Rationale:
People act on what messages say. They need to know when one changed.

Needs: ccl, ios, macos, web

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

Needs: ccl

### MSG-EDIT-003: Only sent messages can be edited
`req~MSG-EDIT-003~1`

A message can only be edited once it has been sent, not while it is still sending.

    Given a person's message is still sending
    When they look for Edit
    Then they cannot edit it yet

Rationale:
Editing something that has not arrived yet would leave people seeing two different versions.

Needs: ccl

### MSG-EDIT-004: Editing notifies only people newly mentioned
`req~MSG-EDIT-004~1`

An edit notifies only the people it newly mentions, not those the message already
mentioned.

    Given a message mentioned Alice
    When its author edits it to also mention Bob
    Then Bob is notified
    And Alice is not notified again

Rationale:
Alice already knows. Bob was just asked for.

Needs: ccl

### MSG-EDIT-005: Only the sender can edit, at any time
`req~MSG-EDIT-005~1`

Only the person who sent a message can edit it, and there is no time limit.

    Given Bob sent a message a year ago
    Then Bob can still edit it
    But Dana, even as an admin, cannot

Rationale:
A message is the sender's words. Nobody else should be able to change them.

Needs: server, ccl

### MSG-DELETE-001: Deleted messages disappear
`req~MSG-DELETE-001~1`

A deleted message disappears from the conversation for everyone, without a "message
deleted" placeholder.

    Given Bob deletes his message
    When anyone looks at the conversation
    Then the message is gone, with nothing in its place

Rationale:
A deleted message is usually one that should not have been sent. A placeholder still draws attention to it.

Needs: ccl

### MSG-DELETE-002: Deleting works offline
`req~MSG-DELETE-002~1`

Deleting a message without a connection takes effect when the connection returns.

    Given a person deletes a message while offline
    When they are back online
    Then the message is deleted for everyone

Rationale:
Someone who deletes a message wants it gone, and should not have to remember to do it again.

Needs: ccl

### MSG-REACT-001: Reactions are tapped on and off
`req~MSG-REACT-001~1`

Tapping a reaction adds it, and tapping it again removes it. Reactions are shown
grouped by emoji, with a count, who reacted, and whether you did.

    Given two people reacted 👍 to a message
    When a third person taps 👍
    Then it shows 👍 3, including them
    And tapping it again takes theirs away

Rationale:
Reactions are quick replies. They have to be quick to undo too.

Needs: ccl, ios, macos, web

### MSG-REACT-002: Reacting does not mark a conversation read
`req~MSG-REACT-002~1`

Reacting to a message does not mark the conversation as read.

    Given a conversation has unread messages
    When the person reacts to an older message in it
    Then the conversation is still unread

Rationale:
Reacting to one message is not reading the rest.

Needs: ccl

### MSG-MENTION-001: Only the people picked are mentioned
`req~MSG-MENTION-001~1`

A message mentions the people the sender picked from the suggestions, and only
those people are notified.

    Given a person types "@Han Solo" and picks Han Solo
    When they send it
    Then Han Solo is notified

Rationale:
Guessing mentions from text would notify the wrong people, or miss the right ones.

Needs: ccl, ios, macos, web

### MSG-MENTION-002: A broken mention never stops a message
`req~MSG-MENTION-002~1`

If something is wrong with a mention in a message, the message is still sent.

    Given a message with a mention that cannot be read
    When it is sent
    Then it is sent with the rest of its text

Rationale:
One bad mention must never cost someone their whole message.

Needs: ccl

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

Needs: ccl, ios, macos, web

### MSG-ATTACH-002: A failed upload is retried without picking the file again
`req~MSG-ATTACH-002~1`

A failed upload stays in the conversation with Retry, which sends the same file
without picking it again, even after a restart.

    Given a person's upload fails
    When they tap Retry the next day
    Then the same file uploads

Rationale:
Finding the file again is a chore, and on a phone it may no longer be at hand.

Needs: ccl

### MSG-ATTACH-003: A cancelled upload disappears straight away
`req~MSG-ATTACH-003~1`

Cancelling an upload removes it from the conversation at once.

    Given a photo is uploading
    When the person cancels it
    Then it is gone from the conversation immediately

Rationale:
Cancel means "I didn't mean that". It should feel instant.

Needs: ccl

### MSG-ATTACH-004: A caption belongs to its photo or file
`req~MSG-ATTACH-004~1`

A caption is part of the same message as its photo or file, never a separate
message.

    Given a person sends a photo with the caption "Front of the house"
    Then the conversation shows one message: the photo with its caption

Rationale:
Split apart, a caption can end up next to the wrong photo.

Needs: ccl

### MSG-ATTACH-005: GIFs show where they came from
`req~MSG-ATTACH-005~1`

A GIF is shown with a link to the page it came from.

    Given a person sends a GIF
    When others see it
    Then it shows with a link to its page on Giphy

Rationale:
The GIF service asks for this, and it lets people find the original.

Needs: ccl

### MSG-ATTACH-006: Files up to 150 MB, of any type
`req~MSG-ATTACH-006~1`

A person can attach a file of any type up to 150 MB. Larger or empty files are
refused before uploading, and the person is told why.

    Given a person attaches a 200 MB video
    Then it is refused before it starts uploading
    And they are told it is over the 150 MB limit

Rationale:
Telling people before a long upload saves them waiting for a failure.

Needs: server, ios, macos, web

### MSG-DRAFT-001: Unsent text is kept for each conversation
`req~MSG-DRAFT-001~1`

Text a person has typed but not sent is kept for that conversation and is still there
when they come back, even after a restart.

    Given a person types half a message in "Philly Roofing" and switches to another conversation
    When they come back to "Philly Roofing"
    Then their half-written message is still in the composer

Rationale:
Interruptions are constant. Losing what you were writing is maddening.

Needs: ccl, ios, macos, web

### MSG-DRAFT-002: Drafts stay on the device
`req~MSG-DRAFT-002~1`

Unsent text is kept only on the device it was typed on. It is never sent to Connect
or shown on the person's other devices.

    Given a person has a draft on their phone
    When they open the same conversation on their Mac
    Then the draft is not there

Rationale:
Something a person has not sent is not shared yet, not even with Connect.

Needs: ccl

### MSG-DRAFT-003: Sending or clearing the text removes the draft
`req~MSG-DRAFT-003~1`

Sending the message, or clearing the text, removes the draft, so nothing blank or
already sent comes back.

    Given a person has a draft
    When they delete all its text and leave the conversation
    Then there is no draft when they come back

Rationale:
A draft that comes back after it was sent or deleted looks like a message that was never sent.

Needs: ccl, ios, macos, web

### MSG-READ-001: Unread starts after the last message the user read
`req~MSG-READ-001~1`

The first unread message is the oldest message after the last one the user read.
When everything is read, there is none.

    Given a user has read up to message 40 of 50
    When the conversation is opened
    Then message 41 is the first unread message

Rationale:
It decides where a conversation opens, so every device must agree on it.

Needs: ccl

### MSG-READ-002: Reading clears unread everywhere
`req~MSG-READ-002~1`

Reading up to the newest message clears the unread count and marker on every
device the user is signed in on.

    Given a user has 3 unread messages and two signed-in devices
    When they read to the newest message on one device
    Then the other device shows no unread count or marker

Rationale:
An unread badge that survives reading is the most reported annoyance in a chat product.

Needs: ccl, server

### MSG-READ-003: Opens at the unread marker
`req~MSG-READ-003~1`

A conversation with unread messages opens with the unread marker in view. A fully
read conversation opens at the newest message.

    Given a conversation has unread messages
    When the user opens it
    Then the unread marker is visible
    But if everything is read, it opens at the newest message

Rationale:
Opening at the newest message hides what was missed; opening on an old marker makes users scroll for nothing.

Needs: ios, macos, web

### MSG-READ-004: Being added to a conversation does not make it unread
`req~MSG-READ-004~1`

Being added to a conversation does not, by itself, make it show as unread. Only
messages do.

    Given a person is added to a conversation that has no messages they have not seen
    When they look at their conversation list
    Then the conversation does not show as unread
    And it adds nothing to the unread count on the app icon

Rationale:
People are added to conversations automatically all the time (Audiences). If each one looked unread, badges would mean nothing.

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

Needs: ios, macos, web

### MSG-READ-006: Only reading marks a conversation read
`req~MSG-READ-006~1`

A conversation becomes read only when the person reads it or marks it read.
Reacting, editing, deleting or scrolling do not.

    Given a conversation is unread
    When the person edits an old message in it
    Then it is still unread

Rationale:
Unread means "there is something you have not seen". Other actions do not change that.

Needs: ccl

### MSG-READ-007: Posting does not clear the unread count
`req~MSG-READ-007~1`

Sending a message in a conversation does not clear its unread count. Only reading
does.

    Given a conversation shows 58 unread
    When the person replies without reading them
    Then it still shows 58 unread

Rationale:
Replying to the latest message does not mean the person saw the 57 before it.

Needs: ccl

### MSG-READ-008: People can mark a conversation read or unread
`req~MSG-READ-008~1`

From the conversation list, a person can mark a conversation read, which clears its
count at once, or unread, which keeps it unread until they read it.

    Given a person has read a conversation
    When they mark it unread
    Then it shows as unread
    Until they open and read it again

Rationale:
Marking unread is how people leave themselves a reminder to come back.

Needs: ccl, ios, macos, web

### MSG-READ-009: Messages are read only while Connect is in front
`req~MSG-READ-009~1`

Messages only count as read while Connect is the window the person is using.

    Given Connect is open but another window is in front
    When new messages arrive in the open conversation
    Then they stay unread
    Until the person clicks back into Connect

Rationale:
A message on a screen nobody is looking at has not been read.

Needs: web

### MSG-RETAIN-001: Messages are kept for six months
`req~MSG-RETAIN-001~1`

Messages older than six months are removed from Connect, in both versions.

    Given a message was sent more than six months ago
    When a week has passed
    Then the message is no longer in Connect

Status: draft

Rationale:
Product to decide how long messages are kept. Whatever the period, both versions must keep the same history, or the same conversation shows different messages in each.

Needs: nitro, server
