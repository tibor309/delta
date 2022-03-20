import discord
from discord.ext import commands
import random
from messages import *

class mod(commands.Cog):
  def __init__(self, client):
    self.client = client


  ##### Kick
  @commands.command(no_pm=True)
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    kick_messages = [f"{member.mention} just got kicked! <a:speeen:862366334930780170>", f"{ctx.message.author} kicked {member.mention}!", f"Looks like {member.mention} just got kicked!"]
    if isinstance(ctx.channel, discord.channel.DMChannel):
      await ctx.send(random.choice(unusable_cmd_in_dms_messages))  
    await member.kick(reason=reason)
    await ctx.message.delete()
    await ctx.send(random.choice(kick_messages)) 


  ##### Ban
  @commands.command(no_pm=True)
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    ban_messages = [f"<:ban:903287524699566150> {member.mention} just got BANNED!", f"{ctx.message.author} banned {member.mention}. good.", f"Well, looks like {member.mention} just got banned!", f"<:ban:903287524699566150> {member.mention} got bonked with the ban hammer!"]
    if isinstance(ctx.channel, discord.channel.DMChannel):
      await ctx.send(random.choice(unusable_cmd_in_dms_messages))  
    await member.ban(reason=reason)
    await ctx.message.delete()
    await ctx.send(random.choice(ban_messages))


  ##### Unban
  @commands.command(no_pm=True)
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member):  
    if isinstance(ctx.channel, discord.channel.DMChannel):
      await ctx.send(random.choice(unusable_cmd_in_dms_messages))  
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry.user
      
    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
    unban_messages = [f"Unbanned {user.mention}!", f"{ctx.message.author} unbanned {user.mention}!", f"You just unbanned {user.mention}. Was it worh it?"]
    await ctx.message.delete()
    await ctx.send(random.choice(unban_messages))
    return


  ##### Cls
  @commands.command(no_pm=True)
  @commands.has_permissions(manage_messages=True)
  async def cls(self, ctx, amount=1000):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)


  ##### Vcmute
  @commands.command(no_pm=True)
  @commands.has_permissions(mute_members=True)
  async def vcmute(self, ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
      await ctx.send(random.choice(unusable_cmd_in_dms_messages))  
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=True)
        await ctx.message.delete()


  ##### Vcunmute
  @commands.command(no_pm=True)
  @commands.has_permissions(mute_members=True)
  async def vcunmute(self, ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
      await ctx.send(random.choice(unusable_cmd_in_dms_messages))  
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=False)
        await ctx.message.delete()


  ##### Lock
  @commands.command(no_pm=True)
  @commands.has_permissions(manage_channels=True)
  async def lock(self, ctx, channel: discord.TextChannel=None):
    if isinstance(ctx.channel, discord.channel.DMChannel):
      await ctx.send(random.choice(unusable_cmd_in_dms_messages))  
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(random.choice(lock_messages), mention_author=True)


  ##### Unlock
  @commands.command(no_pm=True)
  @commands.has_permissions(manage_channels=True)
  async def unlock(self, ctx, channel: discord.TextChannel=None):
    if isinstance(ctx.channel, discord.channel.DMChannel):
      await ctx.send(random.choice(unusable_cmd_in_dms_messages))  
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(random.choice(unlock_messages), mention_author=True)


  ##### Slowmode
  @commands.command(no_pm=True)
  @commands.has_permissions(manage_channels=True)
  async def slowmode(self, ctx, sec: int = None):
    if sec == None:
      await ctx.reply(random.choice(slowmode_no_num_messages), mention_author=True)
    if sec == '0':
      await ctx.reply(random.choice(slowmode_off_messages), mention_author=False)
    await ctx.channel.edit(slowmode_delay=sec)
    slowmode_set_messages = [f"{ctx.message.author} set the slowmode to {sec} sec!", f"Set channel slowmode to {sec} sec", f"Done!"]
    await ctx.reply(random.choice(slowmode_set_messages), mention_author=False)


  ##### Roleadd
  @commands.command(no_pm=True)
  @commands.has_permissions(manage_roles=True)
  async def roleadd(self, ctx, member: discord.Member = None, *, role: discord.Role = None):

    role_added_messages = [f"{member.mention} recived the {role} role!", f"Gave the {role} role to {member.mention}", f"{member.mention} now has the {role} role!"]

    if isinstance(ctx.channel, discord.channel.DMChannel):
      await ctx.send(random.choice(unusable_cmd_in_dms_messages))  
    elif member == None:
      await ctx.reply(random.choice(role_no_user_messages), mention_author=True)
      return
    elif role == None:
      await ctx.reply(random.choice(role_no_give_role_mention_messages), mention_author=True)
    await member.add_roles(role)
    await ctx.reply(random.choice(role_added_messages), mention_author=False)


  ##### Roleremove
  @commands.command(no_pm=True)
  @commands.has_permissions(manage_roles=True)
  async def roleremove(self, ctx, member: discord.Member = None, *, role: discord.Role = None):

    role_removed_messages = [f"Revoked the {role} role from {member.mention}", f"{member.mention} just lost their {role} role", f"{member.mention} just lost their {role} perms!"]

    if isinstance(ctx.channel, discord.channel.DMChannel):
      await ctx.send(random.choice(unusable_cmd_in_dms_messages))  
    elif member == None:
      await ctx.reply(random.choice(role_no_user_messages), mention_author=True)
      return
    elif role == None:
      await ctx.reply(random.choice(role_no_revoke_role_mention_messages), mention_author=True)
    await member.remove_roles(role)
    await ctx.reply(random.choice(role_removed_messages), mention_author=False)
      

  ##### Nick
  @commands.command(no_pm=True)
  @commands.has_permissions(manage_nicknames=True)
  async def nick(self, ctx, member: discord.Member = None, *, nick = None):

    nick_messages = [f"Changed {member.mention}'s nickname to {nick}", f"{member.mention}'s nickname has been changed to {nick}"]

    if isinstance(ctx.channel, discord.channel.DMChannel):
      await ctx.send(random.choice(unusable_cmd_in_dms_messages))  
    elif member == None:
      await ctx.reply(random.choice(nick_no_member_messages), mention_author=True)
    elif nick == None:
      await ctx.reply(random.choice(nick_no_nick_messages), mention_author=True)
    await member.edit(nick=nick)
    await ctx.reply(random.choice(nick_messages), mention_author=False)


  ##### Userinf
  @commands.command(no_pm=True)
  @commands.has_permissions(manage_nicknames=True)
  async def userinf(self, ctx, *, member:discord.Member = None):
    if isinstance(ctx.channel, discord.channel.DMChannel):
      await ctx.send(random.choice(unusable_cmd_in_dms_messages))  
    elif member == None:
      await ctx.reply(random.choice(whois_no_member_mention), mention_author=True)
    embed=discord.Embed(colour=bot_color)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_author(name="User info", icon_url="https://i.imgur.com/Ig8pkwg.png")
    embed.add_field(name="Username", value=f'```{member.name}#{member.discriminator}```', inline=True)
    embed.add_field(name="Nickname", value=f'```{member.nick}```', inline=True)
    embed.add_field(name="Status", value=f'```{member.status}```', inline=True)
    embed.add_field(name="Highest role", value=member.top_role.mention, inline=True)
    embed.add_field(name="User ID", value=f"||{member.id}||", inline=True)
    embed.add_field(name="Nitro user", value=f'```{bool(member.premium_since)}```', inline=True)
    roles = " ".join([role.mention for role in member.roles])
    embed.add_field(name="Roles", value=f"{roles}", inline=False)
    embed.add_field(name="Account created on",value=f'```{member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}```', inline=False)
    embed.add_field(name="Joined on",value=f'```{member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}```', inline=False)
    await ctx.reply(embed=embed, mention_author=False)





  ##### Errors
  @kick.error
  async def kick_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(random.choice(err_kick_messages), mention_author=True)

  @ban.error
  async def ban_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(random.choice(err_ban_messages), mention_author=True)

  @unban.error
  async def unban_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(random.choice(err_unban_messages), mention_author=True)


def setup(client):
  client.add_cog(mod(client))