import discord , os
from discord.ext import commands
from config import bot_prefix, bot_token, bot_time
import datetime

#import utils.mobile_status
import server

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=bot_prefix, intents=intents)
bot.remove_command('help')

# Load cogs
bot.load_extension("commands.slash_commands")
bot.load_extension("commands.user_commands")

bot.load_extension("privilaged_commands.mod_slash_commands")
bot.load_extension("privilaged_commands.bot_owner_commands")

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