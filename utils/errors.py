import discord
import random
from discord.ext import commands
from config import bot_no_perm, bot_color, no_perm, on_cooldown, err_msg, err_channel

class errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    # Command error
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error): # app command error
        if isinstance(error, (commands.CommandNotFound, commands.NoPrivateMessage)): # not an exisiting command or executed in private messages
            pass
            
            
        elif isinstance(error, commands.BotMissingPermissions): # bot doesn't have perms
            return await ctx.respond(random.choice(bot_no_perm), ephemeral=True)

        elif isinstance(error, commands.MissingPermissions): # user doesn't have perms
            return await ctx.respond(random.choice(no_perm), ephemeral=True)
            
        elif isinstance(error, commands.CommandOnCooldown): # user on cool down
            return await ctx.respond(random.choice(on_cooldown), ephemeral=True)
        else:
            await ctx.respond(random.choice(err_msg), ephemeral=True)

        # Send error log to channel
        try:
            channel = await self.bot.fetch_channel(err_channel)
            embed = discord.Embed(color=bot_color, title=f"An error occured", description=f"**Command:** {ctx.command.name}\n**Guild ID:** ||{ctx.guild.id}||\n```{error}```")
    
            if ctx.guild.icon != None:
                embed.set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon)
            else:
                embed.set_footer(text=f"{ctx.guild.name}")
                    
            embed.timestamp = discord.utils.utcnow()
            await channel.send(embed=embed)
        except:
            print("Failed to send error log")
        raise error
                


def setup(bot):
    bot.add_cog(errors(bot))