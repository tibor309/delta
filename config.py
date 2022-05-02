import os
bot_prefix = os.environ['PREFIX']

bot_color = 0x17c6ff # Embed color #17c6ff > 0x17c6ff
time = ["%Y-%m-%d %H:%M:%S %p UTC"] # Time structure for logs



#####  Help commands
basic_help = "`/avatar [member]` - Steals someones profile pic\n`/activity [activity]` - Start a vc activity\n`/meme <subreddit>` - Get a spicy meme"

music_help = f"`{bot_prefix}back` - Play previous song\n`{bot_prefix}clearq` or `{bot_prefix}cq` - Clear queue\n`{bot_prefix}filter <filter name>` - Add filters to the song\n`{bot_prefix}loop (queue)` - Loop current song or queue\n`{bot_prefix}nowplaying` or `{bot_prefix}np` - View currently playing song\n`{bot_prefix}pause` - Pause player\n`{bot_prefix}play <text/URL>` or `{bot_prefix}p <text/URL>` - Add filters to the song\n`{bot_prefix}loop (queue)` - Loop current song or queue\n`{bot_prefix}queue` or `{bot_prefix}q` - View music queue\n`{bot_prefix}resume` - Resume player\n`{bot_prefix}save` - Save current song\n`{bot_prefix}search [text]` - Search for a song\n`{bot_prefix}skip` - Skip current song\n`{bot_prefix}stop` - Stop player\n`{bot_prefix}progress` or `{bot_prefix}time` - Check song duration\n`{bot_prefix}volume <1-100>` - Change volume\n\nThe available filters are `bassboost`, `8D`, and `nightcore`."

mod_help = f"**Member commands**\n`{bot_prefix}kick [member] (reason)` - Kicks a member from the server\n`{bot_prefix}ban [member] (reason)` - Bans a member from the server\n`{bot_prefix}unban [member]` - Unbans a member\n`{bot_prefix}nick [member] [name]` - Set member nickname\n`{bot_prefix}userinf [member]` - Show info about a mentioned member. Id, status, etc.\n\n**Role commands**\n`{bot_prefix}roleadd [memeber] [role]` - Give a role to a member\n`{bot_prefix}roleremove [memeber] [role]` - Revoke a role from a member\n\n**Channel commands**\n`{bot_prefix}cls (number)` - Delete a number of messages *(Default: 1000)*\n`{bot_prefix}lock (channel)` - Lock chat\n`{bot_prefix}unlock (channel)` - Unlock chat\n`{bot_prefix}slowmode [sec]` - Set slowmode delay"

admin_help = f"**Server commands**\n`{bot_prefix}servername [text]` - Change the server name\n\n**Role commands**\n`{bot_prefix}rolecreate [name]` - Create a role\n`{bot_prefix}roledel [name]` - Delete role\n\n**Channel commands**\n`{bot_prefix}channelcreate <text/voice> [name]` - Create channel\n`{bot_prefix}channeldel [name]` - Delete a channel"



#### No perms
unusable_cmd_in_dms = ["You can't use this command here.", "No", "You can only use these commands in servers."]
no_admin_messages = ["You're not an admin.", "You don't have enough perms!", "You need the manage server perm for this.", "Nope <a:yeeehaaw:733395207222984794>"]
no_mod_messages = ["You need to be a mod first!", "you don't have enough perms! <a:speeen:862366334930780170>", "Get mod from someone.", "Ask for mod <a:dead:886340564851785789>"]


##### Servername
no_server_name = ["You forgot the name!", "what?", "Add a name!"]

##### Rolecreate
rolecreate_no_name = ["Give the new role a name", "you forgot the role name!"]

##### Roledel
roledel_no_role = ["I can't find that role.", "there's no role named like that!", "i still can't find that role"]

##### Channelcreate
channelcreate_no_name = ["Give it a name!", "you forgot the channel name!", "channel name?"]
channelcreate_no_type = ["Thats not a channel type!", "idk what you're talking about", "Theres only 2 types: text, or voice"]

##### Lock
lock_messages = ["Lockdown began!", "Locked! So chat is wild today i see.", "Channel locked!", "Done! No more chat!"]

##### Unlock
unlock_messages = ["Unlocked chat!", "Channel unlocked!", "Chat unlocked!"]

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
