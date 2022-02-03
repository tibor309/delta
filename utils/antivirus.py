import discord
from discord.ext import commands
import random

class antivirus(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.Cog.listener()
  async def on_ready(self):
    with open('./utils/blacklist.txt', 'r') as links:
      global scam_links
      scam_links = links.read().split()
    print(f'Loaded url blacklist')


  @commands.Cog.listener()
  async def on_message(self, message):
    member = message.author
    dm_message = f'Hi {member.name}! sorry for kicking you, but your account probably got hacked, because you or someone started posting nirto scam links with your account.\ni suggest that you unfriend people that you don\'t talk to regularly, and changing your password and turning on 2fa if it wasn\'t on.\ni hope it helps'

    user_message = [f'Looks like {member.name}#{member.discriminator} got hacked. they started posting fake nitro links. i\'ve already kicked them, but please don\'t click on any links!', f'Hey! {member.name}#{member.discriminator}\'s account probably got hacked, because they started sending nitro scams!\nif they sends any links, don\'t click on them!', f'@here sorry for the ping but {member.name}#{member.discriminator} got hacked!they started sending fake nitro links, so please don\'t click on any links and don\'t fall for it\ni\'ve already kicked them']

    channel_message = f'i tried to dm them, but {member.name} has their dms closed.'

    for scam in scam_links:
      if f'https://{scam}' in message.content.lower():
        await message.delete()
        await message.channel.send(random.choice(user_message))
        try:
          await member.send(dm_message)
        except:
          await message.channel.send(channel_message)
        await member.kick(reason='Posted scam link')
      elif f'http://{scam}' in message.content.lower():
        await message.delete()
        await message.channel.send(random.choice(user_message))
        try:
          await member.send(dm_message)
        except:
          await message.channel.send(channel_message)
        await member.kick(reason='Posted scam link')
    #await self.client.process_commands(message)


def setup(client):
  client.add_cog(antivirus(client))