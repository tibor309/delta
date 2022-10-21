import discord
from discord.ext import commands
import requests
from config import bot_time, err_msg
import datetime
from random import choice

# These commands are in the message popout menu

api = "https://some-random-api.ml"

class message_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @discord.Cog.listener()
    async def on_ready(self):
        print((datetime.datetime.now().strftime(f"[{bot_time}]")), "Loaded message commands")


    # Encode to base64
    @discord.message_command(name="Encode to Base64")
    async def encode_base64(self, ctx, message: discord.Message):
        text = message.content.replace(" ", "+")
        url = f"{api}/base64?encode={text}"
        
        response = requests.get(url, verify=True)
        data = response.json()
        
        try: 
            message = data['base64']
            await ctx.respond(message, ephemeral=True)
        except:
            await ctx.respond(random.choice(err_msg), ephemeral=True)

            
    # Decode from base64
    @discord.message_command(name="Decode from Base64")
    async def decode_base64(self, ctx, message: discord.Message):
        url = f"{api}/base64?decode={message.content}"
        
        response = requests.get(url, verify=True)
        data = response.json()
        
        try: 
            message = data['text']
            await ctx.respond(message, ephemeral=True)
        except:
            await ctx.respond(random.choice(err_msg), ephemeral=True)





def setup(bot):
    bot.add_cog(message_commands(bot))