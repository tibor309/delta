import os
bot_prefix = os.environ['PREFIX']

bot_color = 0x17c6ff # Embed color
time = ["[%Y-%m-%d %H:%M:%S %p UTC]"] # Time structure for logs



#####  Help commands
basic_help = "`/avatar [member]` - Steals someones profile pic\n`/activity [activity]` - Start a vc activity\n`/meme <subreddit>` - Get a spicy meme"

music_help = f"`{bot_prefix}24h` - Toggle 24/7 mode\n`{bot_prefix}autoplay` - Toggle autoplay\n`{bot_prefix}clearqueue` or `{bot_prefix}cq` - Clear queue\n`{bot_prefix}filters` - Apply a sound filter\n`{bot_prefix}grab` or `{bot_prefix}save` - Save current song or playlist in dms\n`{bot_prefix}join` - Join voice channel\n`{bot_prefix}leave` - Disconnect from vc\n`{bot_prefix}loop` - Toggle music loop\n`{bot_prefix}nowplaying` or `{bot_prefix}np` - Show current song\n`{bot_prefix}pause` - Pause player\n`{bot_prefix}resume` - Resume player\n`{bot_prefix}play <url or text>` - Play a song\n`{bot_prefix}queue` or `{bot_prefix}q` - Show queue\n`{bot_prefix}remove [number]` - Remove a song from queue\n`{bot_prefix}search [text]` - Search for a song\n`{bot_prefix}seek [number]<s/m/h>` - Seek the current song\n`{bot_prefix}shuffle` - Shuffle queue\n`{bot_prefix}skip` - Skip the current song\n`{bot_prefix}skipto [number]` - Skip to a song in queue\n`{bot_prefix}stop` - Stop player\n`{bot_prefix}vol <0-100>` - Change volume\n\n**Playlist commands**\n`{bot_prefix}create [text]` - Create a playlist\n`{bot_prefix}delete [playlist name]` - Delete a playlist\n`{bot_prefix}info [playlist name]` -  Show songs in your playlist\n`{bot_prefix}list` - Shows your playlists\n`{bot_prefix}load [playlist name]` - Load songs from your playlist into queue\n`{bot_prefix}removetrack [playlist name] [number]` - Remove a song from your playlist\n`{bot_prefix}savecurrent [playlist name]` - Save current song in your playlist\n`{bot_prefix}savequeue [playlist name]` - Save current queue to your playlist\n\n**Supported platforms**\nYouTube, Spotify, Soundcloud, Deezer, Vimeo, Twitch, Bandcamp, *simple url*"

mod_help = f"**Member commands**\n`{bot_prefix}kick [member] (reason)` - Kicks a member from the server\n`{bot_prefix}ban [member] (reason)` - Bans a member from the server\n`{bot_prefix}unban [member]` - Unbans a member\n`{bot_prefix}nick [member] [name]` - Set member nickname\n`{bot_prefix}userinf [member]` - Show info about a mentioned member. Id, status, etc.\n\n**Role commands**\n`{bot_prefix}roleadd [memeber] [role]` - Give a role to a member\n`{bot_prefix}roleremove [memeber] [role]` - Revoke a role from a member\n\n**Channel commands**\n`{bot_prefix}cls (number)` - Delete a number of messages *(Default: 1000)*\n`{bot_prefix}lock (channel)` - Lock chat\n`{bot_prefix}unlock (channel)` - Unlock chat\n`{bot_prefix}slowmode [sec]` - Set slowmode delay"

admin_help = f"**Server commands**\n`{bot_prefix}servername [text]` - Change the server name\n\n**Role commands**\n`{bot_prefix}rolecreate [name]` - Create a role\n`{bot_prefix}roledel [name]` - Delete role\n\n**Channel commands**\n`{bot_prefix}channelcreate <text/voice> [name]` - Create channel\n`{bot_prefix}channeldel [name]` - Delete a channel"



#### No perms
unusable_cmd_in_dms = ["You can't use this command here.", "No", "You can only use these commands in servers."]
no_admin_messages = ["You're not an admin.", "You don't have enough perms!", "You need the manage server perm for this.", "Nope <a:yeeehaaw:733395207222984794>"]
no_mod_messages = ["You need to be a mod first!", "you don't have enough perms! <a:speeen:862366334930780170>", "Get mod from someone.", "Ask for mod <a:dead:886340564851785789>"]


##### Servername
no_server_name = ["You forgot the name!", "what?", "Add a name!"]

##### Rolecreate
rolecreate_no_name_messages = ["Give the new role a name", "you forgot the role name!"]

##### Roledel
roledel_no_role_messages = ["I can't find that role.", "there's no role named like that!", "i still can't find that role"]

##### Channelcreate
channelcreate_no_name = ["Give it a name!", "you forgot the channel name!", "channel name?"]
channelcreate_no_type = ["Thats not a channel type!", "idk what you're talking about", "Theres only 2 types: text, or voice"]

##### Lock
lock_messages = ["Lockdown began!", "Locked! So chat is wild today i see.", "Channel locked!", "Done! No more chat!"]

##### Unlock
unlock_messages = ["Unlocked chat!", "Unlocked. Chat is now free! <:heavy_very_good:904079512814354442>", "Channel unlocked!", "Chat unlocked!"]

##### Slowmode
slowmode_no_num = ["Give me a number.", "delay?"]
slowmode_off = ["Slowmode turned off!", "Turned off slowmode"]

##### Roleadd & Roleremove
role_no_user = ["Mention a user!", "you forgot the user!"]
role_give_no_role_mention = ["Which role do you want to give?", "mention a role too", "You forgot the role."]
role_revoke_no_role_mention = ["Which role do you want to revoke?", "mention a role too", "You forgot the role."]

##### Nick
nick_no_member = ["Mention a member!", "who's nickname do you want to change?"]
nick_no_name = ["to what?", "i think you don't know how to use this command.", "You forgot the nickname"]

##### Userinf
userinf_no_member_mention = ["Mention a member!", "Who is the target?", "You forgot to mention a member again."]

##### Activity
activity_messages = ["You should join a vc first!", "Join a voice channel!", "Join a vc first!", "Join a vc, so i can know where to generate the invite link!"]



















#####  Error messages
err_kick = ["Mention a user!", "you forgot the user!"]
err_ban = ["Mention a user!", "Tell me who do you want to ban"]
err_unban= ["Who do you want to unban?", "who?"]
