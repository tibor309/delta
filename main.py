import discord, os
from discord.ext import commands
import utils.mobile_status # set mobile status
from config import bot_token, bot_time
import datetime

from keep_alive import keep_alive # this makes the bot "always" run

intents = discord.Intents.all() # make sure to enable all intents on the discord dev portal!
bot = commands.Bot(intents=intents, help_command=None) # set prefix, intents, and remove the default help command

# Load commands
for f in os.listdir("./commands"):
	if f.endswith(".py"):
		bot.load_extension("commands." + f[:-3])

for f in os.listdir("./privilaged_commands"):
	if f.endswith(".py"):
		bot.load_extension("privilaged_commands." + f[:-3])

bot.load_extension("utils.events") # and events


@bot.event
async def on_ready():
    print((datetime.datetime.now().strftime(f"[{bot_time}]")), f"Logged in as {bot.user}")

# Make bot not respond to it's owm messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

keep_alive()
try:
  bot.run(bot_token)
except discord.HTTPException as err:  # If discord blocks the current ip, request a new one then restart the bot.
    if err.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        os.system("python utils/restarter.py")
    else:
        raise err