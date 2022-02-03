print("Booting system")
import discord
from discord.ext import commands
from dislash import InteractionClient
import random
from datetime import datetime
import os

import server ## Server
from messages import * ## Messages
import mobile_status ## Mobile status patch


bot_token = os.environ['TOKEN']
bot_prefix = os.environ['PREFIX']
bot_owner = os.environ['OWNER_ID']


client = commands.Bot(command_prefix=bot_prefix, intents=discord.Intents.all())
inter_client = InteractionClient(client)
client.remove_command('help')

for f in os.listdir("./commands"):
	if f.endswith(".py"):
		client.load_extension("commands." + f[:-3])

for f in os.listdir("./server_commands"):
	if f.endswith(".py"):
		client.load_extension("server_commands." + f[:-3])

for f in os.listdir("./utils"):
	if f.endswith(".py"):
		client.load_extension("utils." + f[:-3])

##### Logs
@client.event
async def on_ready():
  print((datetime.now().strftime('[%Y-%m-%d %H:%M:%S %p UTC]')), f"[CLIENT] {client.user} is online")

@client.event
async def on_command(ctx):
  print((datetime.now().strftime('[%Y-%m-%d %H:%M:%S %p UTC]')), f'[CLIENT] User {ctx.author} used the \'{ctx.command}\' command in the \'{ctx.guild.name}\' server! (server_id: {ctx.guild.id})')
  return

@client.event
async def on_server_join(server):
  print((datetime.now().strftime('[%Y-%m-%d %H:%M:%S %p UTC]')), "[CLIENT] Joined the \'{0}\' server".format(server.name))


##### Errors
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    pass



##############################
##### Bot owner commands #####
##############################

##### Bothelp
@client.command(pass_context=True)
@commands.is_owner()
async def bothelp(ctx):
  embed = discord.Embed(description=bot_help, color=bot_color)
  embed.set_author(name="Bot owner commands", icon_url="https://i.imgur.com/PiFG9ng.png")
  embed.set_footer(text=client.user, icon_url=client.user.avatar_url)
  await ctx.reply(embed=embed, mention_author=False)


##### Leaveguild
@client.command(pass_context=True)
@commands.is_owner()
async def leaveguild(ctx, guild_id = None):
  if guild_id == None:
    await ctx.reply("server id?", mention_author=True)
  if ctx.message.author.id == bot_owner:
    await client.get_guild(int(guild_id)).leave()
    await ctx.reply(f"I've left the server", mention_author=True)


##### Ping
@client.command()
async def ping(ctx):
  embed=discord.Embed(description=f"<:folder2:902564322847383592> Base `{round(client.latency * 1000)}ms`",color=bot_color)
  await ctx.send(embed=embed)


##### Setbot
@client.group(invoke_without_command=True)
@commands.is_owner()
async def setbot(ctx):
  await ctx.reply("Add a parameter!", mention_author=True)


@setbot.command()
@commands.is_owner() #setbot name
async def name(ctx, name=None):
  if name == None:
    await ctx.reply(random.chance(setname_no_name_messages), mention_author=False)
  await client.user.edit(username=name)


##### Say
@client.command(pass_context=True)
@commands.is_owner()
async def say(ctx, channel: discord.TextChannel=None, *, text=None):
  if channel == None:
    await ctx.reply(random.choice(sayid_no_channel_messages), mention_author=True)
  elif text == None:
    await ctx.reply(random.choice(sayid_no_text_messages), mention_author=True)
  await channel.send(f'{text}')
  await ctx.message.delete()


##### Saydm
@client.command(pass_context=True, aliases=['dm'])
@commands.is_owner()
async def saydm(ctx, member: discord.Member, *, msg):
  try:
    await member.send(msg)
    await ctx.message.delete()
  except:
    saydm_closed_messages = [f"{member.name} has their dms closed!", f"I can't send messages to {member.name}, because their dms are closed."]
    await ctx.send(random.chance(saydm_closed_messages))
    await ctx.message.delete()


##### React
@client.command(pass_context=True)
@commands.is_owner()
async def react(ctx, emoji = None, message_id:int = None):
  if emoji == None:
    await ctx.reply("Add an emoji", mention_author=True)
  if message_id == None:
    await ctx.reply("Add a message id", mention_author=True)
  try:
    message = await ctx.fetch_message(message_id)
    await ctx.message.delete()
    await message.add_reaction(emoji)
  except:
    await ctx.send("i can't find that message")


##### Guildinfo
@client.command(pass_context=True, no_pm=True)
@commands.is_owner()
async def guildinf(ctx):
  if isinstance(ctx.channel, discord.channel.DMChannel):
    await ctx.send(random.choice(unusable_cmd_in_dms_messages))   
  embed = discord.Embed(title=ctx.guild.name, 
  description=f"**2FA mod requirement:** {ctx.guild.mfa_level}\n**Description**:\n{ctx.guild.description}", color=bot_color)
  embed.set_thumbnail(url=ctx.guild.icon_url)
  embed.set_author(name="Server info", icon_url="https://i.imgur.com/8WKidRM.png")
  embed.add_field(name="Owner", value=ctx.guild.owner.mention, inline=True)
  embed.add_field(name="Verification LVL", value=f'```{ctx.guild.verification_level}```', inline=True)
  embed.add_field(name="Region", value=f'```{ctx.guild.region}```', inline=True)
  embed.add_field(name="Server ID", value=f'||{ctx.guild.id}||', inline=True)
  embed.add_field(name="Members", value=f'```{len(list(filter(lambda m: not m.bot, ctx.guild.members)))} Members\n{len(list(filter(lambda m: m.client, ctx.guild.members)))} Bots```', inline=True)
  embed.add_field(name="Server boost", value=f'```LVL {ctx.guild.premium_tier}\n({ctx.guild.premium_subscription_count} boosted)```', inline=True)
  embed.add_field(name="Channels", value=f'```{len(ctx.guild.text_channels)} Text channels\n{len(ctx.guild.voice_channels)} Voice channels```', inline=True)
  embed.add_field(name="Roles", value=f'```{len(ctx.guild.roles)} roles```', inline=True)
  embed.add_field(name="Invites", value=f'```{len(await ctx.guild.invites())} links created```', inline=True)
  embed.add_field(name="Creation date", value=f'```{ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}```', inline=False)
  await ctx.message.delete()
  await user.send(embed=embed)


##############################


server.run_server()
client.run(bot_token)