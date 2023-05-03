import discord
from discord.ext import commands
import requests
from config import err_msg
import random

# These commands are in the message popout menu

api = "https://some-random-api.ml"

class message_cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # Encode to base64
    @discord.message_command(name="Encode to Base64")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    async def encode_base64(self, ctx, message: discord.Message):
        await ctx.defer()
        text = message.content.replace(" ", "+")
        url = f"{api}/base64?encode={text}"
        
        response = requests.get(url, verify=True)
        data = response.json()
        
        try: 
            message = data['base64']
            await ctx.followup.send(message, ephemeral=True)
        except:
            await ctx.followup.send(random.choice(err_msg), ephemeral=True)

            
    # Decode from base64
    @discord.message_command(name="Decode from Base64")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    async def decode_base64(self, ctx, message: discord.Message):
        await ctx.defer()
        url = f"{api}/base64?decode={message.content}"
        
        response = requests.get(url, verify=True)
        data = response.json()
        
        try: 
            message = data['text']
            await ctx.followup.send(message, ephemeral=True)
        except:
            await ctx.followup.send(random.choice(err_msg), ephemeral=True)


    # React with the funny emoji
    @discord.message_command(name="React with \"🤓\"")
    @discord.commands.default_permissions(administrator=True)
    async def funny_react(self, ctx, message: discord.Message):
        emoji = "🤓"
        
        try: 
            await message.add_reaction(emoji)
            await ctx.respond("did the funny", ephemeral=True)
        except:
            await ctx.respond(random.choice(err_msg), ephemeral=True)



def setup(bot):
    bot.add_cog(message_cmds(bot))