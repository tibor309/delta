import discord
from discord.ext import commands
import os
from config import bot_color

bot_prefix = os.environ['PREFIX']
bot_owner = os.environ['OWNER_ID']

class owner(commands.Cog):
  def __init__(self, client):
    self.client = client


#
# I know what you are thinking. Don't worry i'm only gonna use these commands when i have no choice.
# I'm not gonna try to harm any server without a reason. But maybe troll my friends.
#


  ##### Bothelp
  @commands.command(pass_context=True)
  @commands.is_owner()
  async def bothelp(self, ctx):
    
    bot_help = f"`{bot_prefix}sudo [command] <command parameters>` - Execute a command as root\n`{bot_prefix}say [channel] [message]` - Send a message with the bot\n`{bot_prefix}saydm [member] [message]` - Send a private message\n`{bot_prefix}react [emoji] [message_id]` - React to a message\n`{bot_prefix}guildinf` - Get info about the current server\n\n**Settings**\n`{bot_prefix}leaveguild [server_id]` - Leave a server\n`{bot_prefix}ping` - Check ping\n`{bot_prefix}setbot name [name]` - Change bot name"
  
    embed = discord.Embed(description=bot_help, color=bot_color)
    embed.set_author(name="Bot owner commands", icon_url="https://i.imgur.com/PiFG9ng.png")
    embed.set_footer(text=self.client.user, icon_url=self.client.user.avatar_url)
    await ctx.reply(embed=embed, mention_author=False)


  ##### Leaveguild
  @commands.command(pass_context=True)
  @commands.is_owner()
  async def leaveguild(self, ctx, guild_id = None):
    if guild_id == None:
      await ctx.reply("Give a server id!", mention_author=True)
    if ctx.message.author.id == bot_owner:
      await self.client.get_guild(int(guild_id)).leave()
      await ctx.reply(f"I've left the server", mention_author=True)


  ##### Setbot
  @commands.group(invoke_without_command=True)
  @commands.is_owner()
  async def setbot(self, ctx):
    await ctx.reply("Add a parameter!", mention_author=True)
  
  @setbot.command()
  @commands.is_owner() #setbot name
  async def name(self, ctx, name=None):
    if name == None:
      await ctx.reply("Invalid parameter", mention_author=True)
    await self.client.user.edit(username=name)


  ##### Say
  @commands.command(pass_context=True)
  @commands.is_owner()
  async def say(self, ctx, channel: discord.TextChannel=None, *, text=None):
    if channel == None:
      await ctx.reply(f"Mention a channel, or give a channel id!", mention_author=True)
    elif text == None:
      await ctx.reply(f"Give me someting to say", mention_author=True)
    await channel.send(f'{text}')
    await ctx.message.delete()
  
  
  ##### Saydm
  @commands.command(pass_context=True, aliases=['dm'])
  @commands.is_owner()
  async def saydm(self, ctx, member: discord.Member, *, msg):
    try:
      await member.send(msg)
      await ctx.message.delete()
    except:
      await ctx.send(f"{member.name} has their dms closed!")
      await ctx.message.delete()
  
  
  ##### React
  @commands.command(pass_context=True)
  @commands.is_owner()
  async def react(self, ctx, emoji = None, message_id:int = None):
    if emoji == None:
      await ctx.reply("Add an emoji", mention_author=True)
    if message_id == None:
      await ctx.reply("Add a message id", mention_author=True)
    try:
      message = await ctx.fetch_message(message_id)
      await ctx.message.delete()
      await message.add_reaction(emoji)
    except:
      await ctx.send("I can't find that message")
  
  
  ##### Guildinfo
  @commands.command(pass_context=True)
  @commands.is_owner()
  async def guildinf(self, ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
      await ctx.send(f"You can't use this in dms!")
      return
    embed = discord.Embed(title=ctx.guild.name, 
    description=f"**2FA mod requirement:** {ctx.guild.mfa_level}\n**Description**:\n{ctx.guild.description}", color=bot_color)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_author(name="Server info", icon_url="https://i.imgur.com/8WKidRM.png")
    embed.add_field(name="Owner", value=ctx.guild.owner.mention, inline=True)
    embed.add_field(name="Verification LVL", value=f'```{ctx.guild.verification_level}```', inline=True)
    embed.add_field(name="Region", value=f'```{ctx.guild.region}```', inline=True)
    embed.add_field(name="Members", value=f'```{ctx.guild.member_count} Members```', inline=True)
    embed.add_field(name="Server boost", value=f'```LVL {ctx.guild.premium_tier}\n({ctx.guild.premium_subscription_count} boosted)```', inline=True)
    embed.add_field(name="Channels", value=f'```{len(ctx.guild.text_channels)} Text channels\n{len(ctx.guild.voice_channels)} Voice channels```', inline=True)
    embed.add_field(name="Roles", value=f'```{len(ctx.guild.roles)} roles```', inline=True)
    embed.add_field(name="Invites", value=f'```{len(await ctx.guild.invites())} links created```', inline=True)
    embed.add_field(name="Creation date", value=f'```{ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}```', inline=False)
    embed.set_footer(text=f"Server ID: {ctx.guild.id}")
    await ctx.message.delete()
    await ctx.author.send(embed=embed)


######################################################################################################################################


  ##### Sudo help
  @commands.group(invoke_without_command=True, no_pm=True, pass_context=True)
  @commands.is_owner()
  async def sudo(self, ctx):

    sudo_help = f"```\nsudo - execute a command as root\n\nuseage: sudo [command] <command parameters>\nexample: sudo cls 10\navailable commands: kick, ban, unban, cls, nick, roleadd, roledel, servername, userinf\n```"
    
    await ctx.reply(sudo_help, mention_author=False)

    
  #### Kick
  @sudo.command(no_pm=True)
  @commands.is_owner()
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    if reason != None:
      await ctx.send(f"Kicked **{member.name}#{member.discriminator}** by {ctx.message.author}", mention_author=True)
      await member.kick(reason=reason)
    else:
      await ctx.send(f"Kicked **{member.name}#{member.discriminator}** by {ctx.message.author} with reason: {reason}", mention_author=True)
      await member.kick(reason=reason)

      
  #### Ban
  @sudo.command(no_pm=True)
  @commands.is_owner()
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    if reason != None:
      await ctx.send(f"Banned **{member.name}#{member.discriminator}** by {ctx.message.author}", mention_author=True)
      await member.ban(reason=reason)
    else:
      await ctx.send(f"Banned **{member.name}#{member.discriminator}** by {ctx.message.author} with reason: {reason}", mention_author=True)
      await member.ban(reason=reason)

      
  #### Unban
  @sudo.command(no_pm=True)
  @commands.is_owner()
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        
    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.reply(f"{ctx.message.author.mention} unbanned {user.mention}!", mention_author=True)
      return

      
  #### Cls
  @sudo.command(no_pm=True)
  @commands.is_owner()
  async def cls(self, ctx, amount=20):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)

    
  #### Nick
  @sudo.command(no_pm=True)
  @commands.is_owner()
  async def nick(self, ctx, member: discord.Member = None, *, nick = None):
    if member == None:
      await ctx.reply("Mention a member, or give a member id!", mention_author=True)
    elif nick == None:
      await ctx.reply("Add a parameter!", mention_author=True)
    await member.edit(nick=nick)
    await ctx.reply(f"Changed {member.mention}'s nickname to {nick}", mention_author=False)

    
  #### Roleadd
  @sudo.command(no_pm=True)
  @commands.is_owner()
  async def roleadd(self, ctx, member: discord.Member = None, *, role: discord.Role = None):
    if member == None:
      await ctx.reply("Mention a member, or give a member id!", mention_author=True)
      return
    elif role == None:
      await ctx.reply("Mention a role, or give a role id", mention_author=True)
    await member.add_roles(role)
    await ctx.reply(f"{ctx.message.author} gave the **{role}** role to {member.mention}", mention_author=False)

    
  #### Roledel
  @sudo.command(no_pm=True)
  @commands.is_owner()
  async def roledel(self, ctx, member: discord.Member = None, *, role: discord.Role = None):
    if member == None:
      await ctx.reply("Mention a member, or give a member id!", mention_author=True)
      return
    elif role == None:
      await ctx.reply("Mention a role, or give a role id", mention_author=True)
    await member.remove_roles(role)
    await ctx.reply(f"{ctx.message.author} revoked the **{role}** role from {member.mention}", mention_author=False)

    
  #### Servername
  @sudo.command(no_pm=True)
  @commands.is_owner()
  async def servername(self, ctx, *, name=None):
    if name == None:
      await ctx.reply("Add a name!", mention_author=True)
    else:
      await ctx.guild.edit(name=name)
      await ctx.reply(f"{ctx.message.author} changed the server name to **{name}**", mention_author=False)
      return

      
  #### Userinf
  @sudo.command(no_pm=True)
  @commands.is_owner()
  async def userinf(self, ctx, member: discord.Member):
    embed = discord.Embed(color=member.color)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_author(name="User info", icon_url="https://i.imgur.com/Ig8pkwg.png")
    embed.add_field(name="Username", value=f'```{member.name}#{member.discriminator}```', inline=True)
    embed.add_field(name="Nickname", value=f'```{member.nick}```', inline=True)
    embed.add_field(name="Status", value=f'```{member.status}```', inline=True)
    embed.add_field(name="Bot", value=f'```{member.bot}```', inline=True)
    embed.add_field(name="Nitro user", value=f'```{bool(member.premium_since)}```', inline=True)
    embed.add_field(name="Highest role", value=member.top_role.mention, inline=True)
    embed.add_field(name="Account created",value=f'```{member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}```', inline=False)
    embed.add_field(name="Joined on",value=f'```{member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}```', inline=False)
    
    roles = " ".join([role.mention for role in member.roles])
    embed.add_field(name="Roles", value=f"{roles}", inline=False)
    
    if len(member.roles) > 1:
        role_string = ' '.join([r.mention for r in member.roles][1:])
      
        embed.add_field(name="Roles [{}]".format(len(member.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions:", value=perm_string, inline=False)
    
    embed.set_footer(text='User ID: ' + str(member.id))
    await ctx.send(embed=embed)

  

def setup(client):
  client.add_cog(owner(client))