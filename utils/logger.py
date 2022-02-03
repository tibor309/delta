import discord
from discord.ext import commands
from datetime import datetime

class logger(commands.Cog):
  def __init__(self, client):
    self.client = client


  ##### Logs
  @commands.Cog.listener()
  async def on_command(self, ctx):
    print((datetime.now().strftime('[%Y-%m-%d %H:%M:%S %p UTC]')), f'[CLIENT] User {ctx.author} used the \'{ctx.command}\' command in the \'{ctx.guild.name}\' server! (server_id: {ctx.guild.id})')
    return

  @commands.Cog.listener()
  async def on_server_join(self, server):
    print((datetime.now().strftime('[%Y-%m-%d %H:%M:%S %p UTC]')), "[CLIENT] Joined the \'{0}\' server".format(server.name))


  ##### Errors
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
      pass



def setup(client):
  client.add_cog(logger(client))