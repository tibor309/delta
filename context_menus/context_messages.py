import random
import discord
from discord.ext import commands

from config import err_msg


# These commands are in the message popout menu
class message_cmds(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    # React with the funny emoji
    @discord.message_command(name="React with 🤓")
    @discord.commands.default_permissions(administrator=True)
    async def funny_react(self, ctx, message: discord.Message):
        emoji = "🤓"
        
        try: 
            await message.add_reaction(emoji)
            await ctx.respond("did the funny", ephemeral=True)
        except:
            await ctx.respond(random.choice(err_msg), ephemeral=True)



def setup(bot: commands.Bot):
    bot.add_cog(message_cmds(bot))
    