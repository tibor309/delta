import discord
from discord.ext import commands
import random

guild_id = 380315051879432202

class da_server(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.command(pass_context=True)
  async def thisgood(self, ctx):
    if ctx.guild.id != guild_id:
      return
    await ctx.reply("<:heavy_very_good:904079512814354442> very good")



def setup(client):
  client.add_cog(da_server(client))