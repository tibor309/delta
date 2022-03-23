import discord
from discord.ext import commands
from dislash import InteractionClient
from datetime import datetime
import os
import asyncio

import keepAlive # Server
from config import time, bot_color # Import config
import mobile_status # Mobile status patch


bot_token = os.environ['TOKEN']
bot_prefix = os.environ['PREFIX']
bot_owner = os.environ['OWNER_ID']


client = commands.Bot(command_prefix=bot_prefix, intents=discord.Intents.all())
inter_client = InteractionClient(client)
client.remove_command('help')


#### Import commands
for f in os.listdir("./commands"):
	if f.endswith(".py"):
		client.load_extension("commands." + f[:-3])

for f in os.listdir("./servers"):
	if f.endswith(".py"):
		client.load_extension("servers." + f[:-3])

for f in os.listdir("./utils"):
	if f.endswith(".py"):
		client.load_extension("utils." + f[:-3])


##### Ready #####
@client.event
async def on_ready():
  print((datetime.now().strftime(f"{time}")), f"[CLIENT] {client.user} is online")


##### Ping
@client.command()
async def ping(ctx):
  embed=discord.Embed(description=f"<:folder2:902564322847383592> **Commands** `{round(client.latency * 1000)}ms`",color=bot_color)
  await asyncio.sleep(0.3)
  await ctx.send(embed=embed)




##############################

keepAlive.run_server()
client.run(bot_token)