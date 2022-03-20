# :ocean: Splash
This discord bot was made for me and my friends using discord.py. Splash is an advanced discord bot with moderation, general and funfunctionalities.

## Setup
Install all dependecies with the command below. Rename the `.env.example` file to simply `.env`, and edit it. Thats all.
```
pip install -r requirements.txt
```

## Memes
If you want to see some memes, you can use the `/meme` command to post one directly from reddit!

## Discord activities
Discord has released a beta feature that allows users to create vc activities. At least one person needs to click on the <strong>blue link</strong>, in order to start the activity! Once the activity is started, people can join by clicking <kbd>Join</kbd>. All the generated invite links are valid for 15 mins!
 
The activities feature is only supported on web and updated PC app versions of Discord and is not supported on mobile.
Multiple people clicking the blue link at once can cause a "Activity Ended" error screen, however it's not a common occurence.

![YouTube Together](https://cdn.discordapp.com/attachments/678298437854298122/860210751448547328/msedge_HpqALcJCcD.png)

To start activities use the `/activity` command and optional commands. If the invite link is expired, people can still join from the vc.

# Commands
These commands can be used by the server members. The default prefix is `.`!

<details>
<summary>
  Show
</summary>

## General commands

| Command | Description |
| --- | --- | 
| `/activity <activity>` | Start an activity |
| `/help <command>` | Get info about commands |
| `/avatar <user>` | Steal someones avatar |
| `/meme <subreddit>` | Send memes |

## Moderator commands

| Command | Description | Required perm |
| --- | --- | --- |
| `.kick [member] (reason)` | Kick a member from the server | KICK_MEMBERS |
| `.ban [member] (reason)` | Ban a member | BAN_MEMBERS |
| `.unban [member]` | Unban a member | BAN_MEMBERS |
| `.roleadd [memeber] [role]` | Give a role to a member | MANAGE_ROLES |
| `.roleremove [memeber] [role]` | Remove a role from a member | MANAGE_ROLES |
| `.cls (number)` | Purge a number of messages (Default: 1000) | MANAGE_MESSAGES |
| `.lock (channel)` | Lock a channel | MANAGE_CHANNELS |
| `.unlock (channel)` | Unock a channel | MANAGE_CHANNELS |
| `.nick [member] [nickname]` | Change a member's nickname | MANAGE_NICKNAMES |
| `.userinf [member]` | Shows stuff about a member | MANAGE_NICKNAMES |
| `.vcmute` | Mutes everyone in the current vc | MUTE_MEMBERS |
| `.vcunmute` | Unmutes everyone in the current vc | MUTE_MEMBERS |
| `.slowmode` | Set channel slowmode | MANAGE_CHANNELS |

## Admin commands

| Command | Description | Required perm |
| --- | --- | --- |
| `.servername [name]` | Change the server name | MANAGE_GULD |
| `.rolecreate [permission id] [name]` | Create a role | MANAGE_ROLES |
| `.roledel [role name]` | Delete a role | MANAGE_ROLES |
| `.channelcreate <text/voice> [name]` | Create a channel| MANAGE_CHANNELS |
| `.channeldel [channel name]` | Delete a channel | MANAGE_ROLES |

To generate a permission id, use [this](https://discordapi.com/permissions.html) website!

</details>