import discord, os
from discord.ext import commands
from config import bot_prefix, bot_token, bot_time
import datetime


# Set intents
# Make sure to enabale these on the discord dev portal!
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=bot_prefix, intents=intents)
bot.remove_command('help')

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
    print((datetime.datetime.now().strftime(f"{bot_time}")), f"Logged in as {bot.user}")

# Make bot not respond to it's owm messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

  
try:
  bot.run(bot_token)
except discord.HTTPException as err:  # If discord blocks the current ip, request a new one then restart the bot.
    if err.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        os.system("python utils/restarter.py")
        os.system('kill 1')
    else:
        raise err