import os
from dotenv import load_dotenv
load_dotenv()


# Embed color for messages (#ffffff -> 0xffffff)
bot_color = 0x17c6ff # General color
bot_color2 = 0x2F3136 # Color for image commands

bot_time = "%d/%b/%Y %H:%M:%S" # Time structure for logs
code_link = "https://github.com/tibor309/delta" # Source code link

# Environment variables
# Set these in your env file!
bot_token = os.getenv("TOKEN") # Your bot token -- NEVER SHARE YOUR TOKEN WITH ANYONE!
err_channel = os.getenv("ERR_CHANNEL") # Channel for logging errors (optional)


# Icons for embeds
user_icon = "https://i.imgur.com/AMn8jzp.png" # for member specific commnds
guild_icon = "https://i.imgur.com/y5N1QY3.png" # icon for guild specific commands

# Reaction images
no_perms_meme = "https://i.imgur.com/cnwdsLo.png"
hi_mods = "https://tenor.com/view/hi-gif-25925938"

# Emojis for commands
# You can use custom emojis, but the bot needs access to the server to use them!
yes_emoji = "✅" # emoji for upvote
no_emoji = "🇽" # emoji for downvote 
invite_emoji = "💙" # emoji for invite button
code_emoji = "🧪" # emoji for source code link 



# Messages
# One message is randomly selected to be sent
no_perm = ["nope", "you don't have perms for this!", "access denied", "You don't have enough perms for this", "skill issue", no_perms_meme, "you don't have perms", "https://tenor.com/view/nuh-uh-beocord-no-lol-gif-24435520", "nuh uh!"]
bot_no_perm = ["I don't have perms!", "i don't have enough perms for this", "i can't help you with that. i don't have perms"]
cmd_dms = ["You can't use this command here.", "No", "You can only use these commands in servers.", "Nope", "you can't use this command in dms!"]
bot_join_msg = ["Hi everyone!", "Hi", "hi everyone", "hi", "Hello everyone!", hi_mods]
err_msg = ["something went wrong", "well that didn't work", "uh.. i got an error", "got an error", "something didn't work"]
img_fail = ["I couldn't get the image", "Failed to get the image :(", "i couldn't download the image"]
on_cooldown = ["You're on cooldown!", "hey slow down", "not yet!"]