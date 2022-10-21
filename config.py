import os
from dotenv import load_dotenv
load_dotenv()

bot_color = 0x17c6ff
bot_color2 = 0x2F3136
bot_token = os.getenv("TOKEN")

reddit_id = os.getenv("REDDIT_APP_ID")
reddit_secret = os.getenv("REDDIT_APP_SECRET")

bot_time = "%d/%b/%Y %H:%M:%S" # Time structure for logs (i should implement a proper logger later)


# Icons
user_icon = "https://i.imgur.com/zGVdnZ5.png"
settings_icon1 = "https://i.imgur.com/jbJFUeG.png"
settings_icon2 = "https://i.imgur.com/QEKptpH.png"
settings_folder_icon = "https://i.imgur.com/PiFG9ng.png"
folder_icon = "https://i.imgur.com/E90UgPB.png"
cpu_folder_icon = "https://i.imgur.com/jW1kIa7.png"

# Emojis
yes_emoji = "<:ye:935798200621760533>"
no_emoji = "<:nah:935798200869208074>"


# Messages
no_perm = ["nope", "you don't have perms for this!", "access denied", "You don't have enough perms for this", "skill issue"]
bot_no_perm = ["I don't have perms!", "i don't have enough perms for this", "i can't help you with that. i don't have perms"]
cmd_dms = ["You can't use this command here.", "No", "You can only use these commands in servers.", "Nope", "you can't use this command in dms!"]
activity_link = ["use the link to join", "join with the link", "here's the link"]
bot_join_msg = ["Hi everyone!", "Hi", "hi everyone", "hi", "Hello everyone!"]
no_vc = ["Join a vc first!", "Connect to a voice channel!", "connect to a vc!", "vc?"]
no_same_vc = ["You're not in the same vc as me!", "you're not in our voice channel!", "you're not in the same vc as me"]
err_msg = ["something went wrong", "well that didn't work", "uh i got an error"]