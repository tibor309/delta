import discord, os
from discord.ext import commands
from config import bot_prefix, bot_token, bot_time
import datetime

import utils.mobile_status
import server

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=bot_prefix, intents=intents)
bot.remove_command('help')

# Load cogs
for f in os.listdir("./commands"):
	if f.endswith(".py"):
		bot.load_extension("commands." + f[:-3])

for f in os.listdir("./privilaged_commands"):
	if f.endswith(".py"):
		bot.load_extension("privilaged_commands." + f[:-3])

bot.load_extension("utils.events")


@bot.event
async def on_ready():
    print((datetime.datetime.now().strftime(f"{bot_time}")), f"Logged in as {bot.user}")

  
try:
  server.run_server()
  bot.run(bot_token)
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  os.system("python utils/restarter.py")
  os.system('kill 1')