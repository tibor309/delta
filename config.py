import os
#from dotenv import load_dotenv
#load_dotenv()


bot_color = 0x17c6ff
bot_color2 = 0x1e1e1e

bot_prefix = "."bot_token = os.environ['TOKEN']


reddit_id = os.environ["REDDIT_APP_ID"]
reddit_secret = os.environ["REDDIT_APP_SECRET"]

bot_time = ["%Y-%m-%d %H:%M:%S %p UTC"] # Time structure for logs

# Icons
user_icon = "https://i.imgur.com/zGVdnZ5.png"
settings_icon1 = "https://i.imgur.com/jbJFUeG.png"
settings_icon2 = "https://i.imgur.com/QEKptpH.png"
settings_folder_icon = "https://i.imgur.com/PiFG9ng.png"
folder_icon = "https://i.imgur.com/E90UgPB.png"

# Emojis
err_emoji = "<:err:935798200869208074>"
success_emoji = "<:approved:935798200621760533>"


# Messages
no_perm = ["nope", "you don't have perms for this!", "access denied", "You don't have enough perms for this"]
bot_no_perm = ["I don't have perms!", "i don't have enough perms for this", "i can't help you with that. i don't have perms"]
cmd_dms = ["You can't use this command here.", "No", "You can only use these commands in servers.", "Nope", "you can't use this command in dms!"]
activity_link = ["use the link to join", "join with the link", "here's the link"]
bot_join_msg = ["Hi everyone!", "Hai", "hi everyone", "hi", "Hello everyone!"]