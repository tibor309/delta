import discord
from discord.ext import commands
import random
from messages import *

class sudo(commands.Cog):
  def __init__(self, client):
    self.client = client


  ##### Sudo
  @commands.group(invoke_without_command=True, no_pm=True, pass_context=True)
  @commands.is_owner()
  async def sudo(self, ctx):
    await ctx.reply("```\nsudo - execute a command as an another user\n\nuseage: sudo [command] <command parameters>\nexample: sudo cls 10\n```", mention_author=False)


  @sudo.command(no_pm=True) #kick
  @commands.is_owner()
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    kick_messages = [f"{member.mention} just got kicked by {ctx.message.author}! <a:speeen:862366334930780170>", f"{ctx.message.author} kicked {member.mention}!", f"Looks like {member.mention} just got kicked!"]
    await ctx.send(random.choice(kick_messages), mention_author=True)


  @sudo.command(no_pm=True) #ban
  @commands.is_owner()
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    ban_messages = [f"<:ban:903287524699566150> {member.mention} just got BANNED!", f"{member.mention} got banned by {ctx.message.author}. good.", f"Well, looks like {member.mention} just got banned!", f"<:ban:903287524699566150> {member.mention} got bonked with the ban hammer!"]
    await ctx.send(random.choice(ban_messages), mention_author=True)


  @sudo.command(no_pm=True) #unban
  @commands.is_owner()
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        
    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      unban_messages = [f"Unbanned {user.mention}!", f"{ctx.message.author.mention} unbanned {user.mention}!"]
      await ctx.reply(random.choice(unban_messages), mention_author=True)
      return


  @sudo.command(no_pm=True) #cls
  @commands.is_owner()
  async def cls(self, ctx, amount=20):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)


  @sudo.command(no_pm=True) #nick
  @commands.is_owner()
  async def nick(self, ctx, member: discord.Member = None, *, nick = None):
    if member == None:
      await ctx.reply(random.choice(nick_no_member_messages), mention_author=True)
    elif nick == None:
      await ctx.reply(random.choice(nick_no_nick_messages), mention_author=True)
    await member.edit(nick=nick)
    nick_messages = [f"Changed {member.mention}'s nickname to {nick}", f"{member.mention}'s nickname has been changed to {nick}"]
    await ctx.reply(random.choice(nick_messages), mention_author=False)


  @sudo.command(no_pm=True) #roleadd
  @commands.is_owner()
  async def roleadd(self, ctx, member: discord.Member = None, *, role: discord.Role = None):
    if member == None:
      await ctx.reply(random.choice(role_no_user_messages), mention_author=True)
      return
    elif role == None:
      await ctx.reply(random.choice(role_no_role_mention_messages), mention_author=True)
    await member.add_roles(role)
    role_added_messages = [f"{member.mention} recived the {role} role!", f"{ctx.message.author} gave the {role} role to {member.mention}", f"{member.mention} now has the {role} role!"]
    await ctx.reply(random.choice(role_added_messages), mention_author=False)


  @sudo.command(no_pm=True) #roleremove
  @commands.is_owner()
  async def roleremove(self, ctx, member: discord.Member = None, *, role: discord.Role = None):
    if member == None:
      await ctx.reply(random.choice(role_no_user_messages), mention_author=True)
      return
    elif role == None:
      await ctx.reply(random.choice(role_no_role_mention_messages), mention_author=True)
    await member.remove_roles(role)
    role_removed_messages = [f"{ctx.message.author} revoked the {role} role from {member.mention}", f"{member.mention} just lost their {role} role", f"{member.mention} just lost their {role} perms!"]
    await ctx.reply(random.choice(role_removed_messages), mention_author=False)

  @sudo.command(no_pm=True) #servername
  @commands.is_owner()
  async def servername(self, ctx, *, name=None):
    if name == None:
      await ctx.reply(random.choice(no_server_name_messages), mention_author=True)
    else:
      await ctx.guild.edit(name=name)
      server_name_messages = [f"{ctx.message.author} changed server name to {name}", "Done!", f"Done! Now the server is called {name}."]
      await ctx.reply(random.choice(server_name_messages), mention_author=False)
      return


def setup(client):
  client.add_cog(sudo(client))