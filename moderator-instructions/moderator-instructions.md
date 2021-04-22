# Moderator Instructions

These are instructions for common moderation actions.

For general moderation guidelines, see the ["Moderator Guidelines" topic](https://forum.arduino.cc/t/moderation-guidelines/54905).

---

### [Delete spam](#delete-spam)

<a name="delete-spam"></a>

Note that this does not apply to legitimate advertisements of products/services that may be of interest to the Arduino community, which are allowed as long as they are posted to the "Products and Services" board.

- Open the topic.
- Open the user's forum profile page in a new tag/window (right click on user name > Open Link in New Tab or ctrl + click user name).
- If it's a spam topic, click the "Remove Topic" button. If it's a spam reply, click the "More..." button on the reply, then "Remove".
- Click the "OK" button.
- Switch to the tab/window with the user's profile page.
- Check whether the user has any other posts. If so, remove those also, following the instructions above.
- Click "Ban user". A ban is used instead of deleting the account because it prevents recreation of the account and can be undone in the event of a mistake.
- In the case of spam, you can leave the "Reason:" and "Notes:" sections blank in order to make the task of deleting spam less time consuming.
- Expiration: Never
- Restriction: Full Ban
- Triggers: Ban on Email Address, Ban on Username (note the checkboxes are ABOVE the descriptions)
- Click the "Add" button.

---

### [Move to correct language board](#move-to-correct-language-board)

<a name="move-to-correct-language-board"></a>

The Arduino Forum has dedicated boards for several common non-English languages. When a topic written in one of these languages is created in one of the English language boards of the forum, it should be moved to the appropriate board. Topics written in a language for which there is not a dedicated board may be left in the appropriate English language board.

- Copy the text of the post.
- Paste it into Google Translate: https://translate.google.com. This is not be necessary if you are sure of the language and sub-board you want to move it to.
- On the topic, click the "Move Topic" button.
- Select the appropriate language board. Google Translate will automatically detect the language (note that it's easy for someone unfamiliar with the language to mistake Portuguese for Spanish).
- If the language board has sub-boards, select the appropriate one, using the Google translation if necessary.
- Uncheck "Change the topic's subject."
- Uncheck "Post a redirection topic."
- Click the "Move Topic" button.

---

### [Deal with cross-post](#cross-post)

<a name="cross-post"></a>

A cross-post is when a user posts on the same subject to the forum multiple times. This is harmful because it can lead to wasting the time of people trying to help by unknowingly duplicating the efforts that were made previously in reply to another instance of the cross-post.

- Open the cross-posting user's forum profile page by clicking on their user name.
- Click "Show Posts".
- Open all cross-posts.
- Pick one cross-post to keep. If only one cross-post has valuable replies, keep that one. The cross-post that is in the appropriate forum board has preference.

If a cross-post has no replies, you can delete it. If it's a topic, click the "Remove Topic" button. If it's a reply, click the "More..." button on the reply, then "Remove".

If multiple cross-posts have valuable replies, they must be merged into a single topic:

- If one of the cross-posts with valuable replies is a thread hijack, split it and the replies into a separate topic.
- Click the "Merge Topics" button. Note that the forum software will order the posts of the merged topic according to chronological order, so it doesn't make a difference which topic is merged to the other.
- The forum's merge system is very inconvenient and partly broken. You can't select a different board because this just results in an error. There is a list of topics in the same board, but this doesn't help if the merge target is in another board, or was not recently created. Defying all common sense, you need to click the "?" button on the left of the topic on the list to select it as the merge topic. The seemingly useful "ID of target topic:" input field doesn't work. So a bit of a hack is required to easily merge to any topic:
- Right click on any of the "?" buttons on the topic list. It doesn't matter which topic you choose.
- Click "Copy Link Location".
- Paste the copied link to the browser's URL bar.
- Open the topic you want to merge to in a separate tab/window.
- Copy the topic ID. This is the number after "topic=" from the topic's URL, leaving off the part after the ".".
- Switch back to the merge page.
- Replace the topic ID in the URL after "to=" with the topic ID of the target topic.
- Press Enter to load the URL.
- Uncheck "Change the subject of all the messages". Merged threads may be a bit confusing to read so having the original subjects may provide a useful clue to the original sequence of the separate discussions.
- Click the "Merge Topics" button.

Issue a warning to allow all moderators to track the history of the user's violations:

- At the bottom of the cross-posting user's post, click "More...".
- Click "Issue Warning".
- Set "Warning Level" to 20%. This will cause a "Watched" icon to appear (to moderators only) on all the user's posts, as well as a note on their forum profile page.
- Reason for Warning: "Cross-posting"
- Check the "Previous Warnings" section at the bottom of the page to see whether the user has cross-posted previously.
- Click the "Issue Warning" button.

If this is the first time the user has cross-posted, just leave a reply to notify them it is against the rules and warn them that further cross posting will result in a ban:

> I've deleted/merged your other cross-post(s).
>
> Cross-posting is against the rules of the forum. The reason is that duplicate posts can waste the time of the people trying to help. Someone might spend 15 minutes (or more) writing a detailed answer on this topic, without knowing that someone else already did the same in the other topic.
>
> Repeated cross-posting will result in a suspension from the forum.
>
> In the future, please take some time to pick the forum board that best suits the topic of your question and then only post once to that forum board. This is basic forum etiquette, as explained in the sticky "[How to use this forum - please read.](https://forum.arduino.cc/t/how-to-use-this-forum-please-read/145337)" post you will find at the top of every forum board. It contains a lot of other useful information. Please read it.
>
> Thanks in advance for your cooperation.

If the user has previously been warned not to cross-post, they should receive a ban:

- Click "More..." at the bottom of the user's post.
- Click "Ban user".
- Reason: "Cross-posting".
- If this is the first or second ban, click the radio button ABOVE "Ban will expire after". If it is the third ban, click the radio button ABOVE "Never".
- For the first ban, set "day(s)" to 3 (note the input field is ABOVE "day(s)"). For the second ban, set "day(s)" to 7.
- Triggers: Ban on Email Address, Ban on Username (note the checkboxes are ABOVE the descriptions)
- On the topic, leave a reply to explain that the user has received a ban:

> Due to continuing to cross-post after having been warned not to, OP has received a 3 day ban.

OR

> Due to continuing to cross-post after having been warned not to, OP has received a 7 day ban.

OR

> Due to continuing to cross-post after having been warned not to, OP has received a permanent ban.

---

### [Split hijacked topic](#hijack)

<a name="hijack"></a>

A topic hijack is when a user makes a reply that is not relevant to the topic. This can either result in a confusing thread where there are multiple parallel discussions, or else one of the people needing help being forgotten about. Note that a relevant reply to an old topic is NOT considered a hijack.

- On the hijack reply, click "More...".
- Click "Split Topic".
- Enter an appropriate subject for the new topic in the "Subject For New Topic" field.

If there have been no replies to the hijack reply, or all replies have been to the hijack reply (none to the original post), then we can just do a simple split:

- Click the radio button ABOVE "Split topic after and including this post."
- Click the "Split Topic" button.

If there have been replies to both the hijack reply and the original post, then we must do a selective split:

- Click the radio button ABOVE "Select posts to split."
- Click the "Split Topic" button.
- Click the arrow button on all replies you want to split to a new topic.
- Click the "Split Topic" button.

On the new topic, leave a reply to warn the user not to hijack topics:

> Please don't hijack topics! I've had to split your post out to its own topic.
>
> This is basic forum etiquette, as explained in the sticky "[How to use this forum - please read.](https://forum.arduino.cc/t/how-to-use-this-forum-please-read/145337)" post you will find at the top of every forum board. It contains a lot of other useful information. Please read it.
>
> Thanks in advance for your cooperation.

---

### [Resolve report](#resolve-report)

<a name="resolve-report"></a>

Forum users may assist the moderators by reporting inappropriate posts. A list of open reports are shown in the [Moderate > Reported Posts area](https://forum.arduino.cc/review). If you delete the offending topic or post to resolve the report, it will be automatically closed. Otherwise, please click the "Close" button on the report after you have resolved it (or determined that no action is required) so it will be removed from the list of open reports. If you are unsure of how to resolve the report, feel free to leave it for another moderator to deal with.

---

### [Unlock topic](#unlock)

<a name="unlock"></a>

If 120 days have passed since the last reply to a topic, it is locked and non-moderators are unable to reply. Forum members are allowed to request topics be unlocked via the "Report to moderator" functionality. When this happens, a moderator should comment on the locked topic:

> Commenting to unlock topic at the request of a forum member.

The reply is required because clicking the "Unlock Topic" button will not unlock the topic in this case. This reply will unlock the topic for another 120 days.