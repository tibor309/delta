# Splash
This discord bot was made for me and my friends using discord.py. It currently still in development.

# Setup
Install all dependecies with this command, then config the `.env` files. Thats all.
```
pip install -r requirements.txt
```

## Discord Activities
Discord has released a beta feature that allows users to use slash commands, and create activities. At least one person needs to click on the <strong>blue link</strong>, and not the 'Play' button, in order to start the activity! Once the activity is started, people can join by clicking 'Play'. **All the generated invite links are valid for 10 mins!**
 
The activities feature is only supported on web and updated PC app versions of Discord and is not supported on mobile.
Multiple people clicking the blue link at once can cause a "Activity Ended" error screen, however it's not a common occurence.


![YouTube Together](https://cdn.discordapp.com/attachments/678298437854298122/860210751448547328/msedge_HpqALcJCcD.png)

# Commands
These commands can be used by the server members. The default prefix is `.`!


| Command | Description |
| --- | --- | 
| `/activity <activity>` | Start an activity |
| `/help <command>` | Get info abot commands |
| `/avatar <user>` | Steal someones avatar |

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
| `.whois [member]` | Show data about a meber | MANAGE_NICKNAMES |

## Admin commands
| Command | Description | Required perm |
| --- | --- | --- |
| `.servername [name]` | Change the server name | MANAGE_GULD |