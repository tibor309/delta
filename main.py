import discord, os
from discord.ext import commands
import utils.mobile_status # set mobile status
from config import bot_token, bot_time
#from keep_alive import keep_alive # this makes the bot "always" run

intents = discord.Intents.all() # require all intents
bot = commands.Bot(intents=intents, help_command=None) # set intents, and remove the default help command

# Load commands and events
for f in os.listdir("./commands"):
    if f.endswith(".py"):
        try:
            bot.load_extension("commands." + f[:-3]) # commands
        except Exception as error:
            print((discord.utils.utcnow().strftime(f"[{bot_time}]")), f"ERROR {f} could not be loaded: {error}")
        else:
            print((discord.utils.utcnow().strftime(f"[{bot_time}]")),f"Loaded {f}")

for f in os.listdir("./privilaged_commands"):
    if f.endswith(".py"):
        try:
            bot.load_extension("privilaged_commands." + f[:-3]) # privilaged commands
        except Exception as error:
            print((discord.utils.utcnow().now().strftime(f"[{bot_time}]")), f"ERROR {f} could not be loaded: {error}")
        else:
            print((discord.utils.utcnow().strftime(f"[{bot_time}]")),f"Loaded {f}")

try:
    bot.load_extension("utils.events") # events
except Exception as error:
    print((discord.utils.utcnow().strftime(f"[{bot_time}]")), f"ERROR events.py could not be loaded: {error}")
else:
    print((discord.utils.utcnow().strftime(f"[{bot_time}]")),f"Loaded events.py")

try:
    bot.load_extension("utils.errors") # and errors
except Exception as error:
    print((discord.utils.utcnow().strftime(f"[{bot_time}]")), f"ERROR errors.py could not be loaded: {error}")
else:
    print((discord.utils.utcnow().strftime(f"[{bot_time}]")),f"Loaded errors.py")
## thats all

@bot.event
async def on_connect():
    await bot.sync_commands(delete_existing=True)
    print((discord.utils.utcnow().strftime(f"[{bot_time}]")), "Synced commands")

@bot.event
async def on_ready():
    print((discord.utils.utcnow().strftime(f"[{bot_time}]")), f"Successfully logged in as {bot.user}")


# Make bot not respond to it's owm messages
@bot.listen
async def on_message(message):
    if message.author == bot.user:
        return

#keep_alive() # keep the bot alive (uncomment this too)
try:
  bot.run(bot_token)
except discord.HTTPException as err:
    if err.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
        #os.system("python3 utils/restarter.py") # This auto kills the repl (uncomment if you're using replit to host)
    else:
        raise err