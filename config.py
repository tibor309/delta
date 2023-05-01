import os
from dotenv import load_dotenv
load_dotenv()

# Embed color for messages (#ffffff -> 0xffffff)
bot_color = 0x17c6ff # General color
bot_color2 = 0x2F3136 # Color for image commands

bot_time = "%d/%b/%Y %H:%M:%S" # Time structure for logs

# Set these in your env file!
bot_token = os.getenv("TOKEN")  # NEVER SHARE YOUR TOKEN WITH ANYONE!
err_channel = os.getenv("ERR_CHANNEL") # Channel id for logging

support_link = os.getenv("SUPPORT")
code_link = os.getenv("CODE")

reddit_id = os.getenv("REDDIT_APP_ID")
reddit_secret = os.getenv("REDDIT_APP_SECRET")


# Icons for embeds
user_icon = "https://i.imgur.com/zGVdnZ5.png" # for member specific commnds
guild_icon = "https://i.imgur.com/jW1kIa7.png" # icon for guild specific commands

# Emojis for commands
# The bot needs access to the server to use custom emojs
yes_emoji = "<:ye:935798200621760533>" # emoji for upvote
no_emoji = "<:nah:935798200869208074>" # emoji for downvote 
invite_emoji = "<:love:1027605898593579118>" # emoji for invite button
support_emoji = "<:message:1102166660959457281>" # emoji for support server invite
code_emoji = "<:github:1102166658589655080>" # emoji for source code link 


# Messages
# One message is randomly selected to be sent
no_perm = ["nope", "you don't have perms for this!", "access denied", "You don't have enough perms for this", "skill issue", "https://i.imgur.com/TmudNRr.png", "you don't have perms", "https://tenor.com/view/nuh-uh-beocord-no-lol-gif-24435520", "nuh uh!"]
bot_no_perm = ["I don't have perms!", "i don't have enough perms for this", "i can't help you with that. i don't have perms"]
cmd_dms = ["You can't use this command here.", "No", "You can only use these commands in servers.", "Nope", "you can't use this command in dms!"]
activity_link = ["use the link to join", "join with the link", "here's the link", "heres the invite"]
bot_join_msg = ["Hi everyone!", "Hi", "hi everyone", "hi", "Hello everyone!", "https://tenor.com/view/hi-gif-25925938"]
err_msg = ["something went wrong", "well that didn't work", "uh.. i got an error", "got an error", "something didn't work"]
img_fail = ["I couldn't get the image", "Failed to get the image :("]
on_cooldown = ["You're on cooldown!", "hey slow down", "not yet!"]