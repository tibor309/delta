import os
from dotenv import load_dotenv
load_dotenv()

# Embed color for messages
bot_color = 0x17c6ff # General color
bot_color2 = 0x2F3136 # Color for image commands

bot_prefix = "." # Bot prefix (currenty unused)
bot_time = "%d/%b/%Y %H:%M:%S" # Time structure for logs
err_channel = os.getenv("ERR_CHANNEL") # Channel id for logging

# Set these in your env file!
bot_token = os.getenv("TOKEN")  # NEVER SHARE YOUR TOKEN WITH ANYONE!
bot_invite = os.getenv("INVITE")
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


# Messages
# One message is randomly selected to be sent
no_perm = ["nope", "you don't have perms for this!", "access denied", "You don't have enough perms for this", "skill issue"]
bot_no_perm = ["I don't have perms!", "i don't have enough perms for this", "i can't help you with that. i don't have perms"]
cmd_dms = ["You can't use this command here.", "No", "You can only use these commands in servers.", "Nope", "you can't use this command in dms!"]
activity_link = ["use the link to join", "join with the link", "here's the link"]
bot_join_msg = ["Hi everyone!", "Hi", "hi everyone", "hi", "Hello everyone!"]
no_vc = ["Join a vc first!", "Connect to a voice channel!", "connect to a vc!", "vc?"]
no_same_vc = ["You're not in the same vc as me!", "you're not in our voice channel!", "you're not in the same vc as me"]
err_msg = ["something went wrong", "well that didn't work", "uh.. i got an error", "got an error", "wrong"]
img_fail = ["I couldn't get the image", "Failed to get the image :("]
on_cooldown = ["You're on cooldown!", "hey slow down", "not yet!"]