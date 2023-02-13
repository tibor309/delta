import discord
import random
import datetime
from discord.ext import commands
from config import bot_no_perm, bot_color, no_perm, on_cooldown, err_msg, err_channel

class errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    # Command error
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error): # app command error
        if isinstance(error, (commands.CommandNotFound, commands.NoPrivateMessage)): # not an exisiting command or executed in private messages
            return
            
            
        elif isinstance(error, commands.BotMissingPermissions): # bot doesn't have perms
            return await ctx.respond(random.choice(bot_no_perm), ephemeral=True)

        elif isinstance(error, commands.MissingPermissions): # user doesn't have perms
            return await ctx.respond(random.choice(no_perm), ephemeral=True)
            
        elif isinstance(error, commands.CommandOnCooldown): # user on cool down
            return await ctx.respond(random.choice(on_cooldown), ephemeral=True)
        else:
            await ctx.respond(random.choice(err_msg), ephemeral=True)

            # Send error log to channel
            channel = bot.get_channel(err_channel)
            embed = discord.Embed(color=bot_color, title=f"An error occured", description=f"```{error}```")
            embed.set_footer(text=f"{ctx.guild.name} • Guild ID: {ctx.guild.id}" , icon_url=ctx.guild.icon_url)
            embed.timestamp = datetime.datetime.utcnow()
            await channel.send(embed=embed)
            raise error


def setup(bot):
    bot.add_cog(errors(bot))