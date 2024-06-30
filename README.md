# LinKetchup
Concept: A Discord bot for aggregating YouTube links shared in a channel into a single YouTube playlist.

## Background
Many discord servers keep a `#music` channel, where users are encouraged to share links (usually from YouTube) of music.

I always want to keep up with what my friends are listening to, but often miss days or even weeks of songs they share. I created this bot because I wanted an easy way to aggregate all the links that were being shared.

You could use this bot to aggregate YouTube links of any kind, but it is designed towards `#music` type channels and the users of those channels who want to get more out of them.

## Basic Steps
1. User connects their YouTube account to discord bot
    1b. User assigns a playlist to their requests

2. Command: ketchup.collect - Creates a new `playlist ruleset` instance with the following attributes/options:
    - Discord User: YouTube Account: Assigned Playlist
    - days: default 1
        - optional: provide number of days of message history to scrape and add to playlist. Default order oldest to newest, optional order newest to oldest
    - collect_behavior: default 'once'
        - optional: 'daily' (collect links once per day)
    - cleanup_behavior: default 'never'
        - optional: 
            - only save the n most recently shared videos, removing the oldest added once the threshold is reached
            - remove videos from playlist after d days
    - video_types:
        - Vevo/Topic only
        - All

## Bot Attributes
User:
    YouTube Account:
        Assigned Playlist:
        - Collection Behavior
        - Videos

## Bot management
### Users
1. Clear User
2. Clear All Users (admin only)

### YouTube Accounts
1. Change YT account assigned to User
2. Clear YT account assigned to User (leaving YT account entry blank)
3. Clear all account/user connections (admin only)

### Playlists
1. User assignment
    a. Change which playlist assigned to user
    b. playlist unassign from user (leaving user playlist entry blank)
    c. Unassign all playlists (leaving user playlist entry blank) (admin only)

2. Playlist behavior: Change any attributes/options listed under `Basic Steps`

3. Videos
    a. Remove videos from playlist added before d date
    b. Remove videos until the number of videos is v, default starting with the earliest, but can choose to start with latest
    c. Remove v videos, default starting with the latest, but can choose to start with latest
    d. Remove all videos from playlist
     