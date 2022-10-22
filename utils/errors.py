import discord
from discord.ext import commands
from config import bot_no_perm, no_perm, on_cooldown

class errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    # Command error
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error): # app command error
        if isinstance(error, (commands.CommandNotFound, commands.NoPrivateMessage)):
            return

        if isinstance(error, commands.MissingPermissions): # user doesn't have perms
            return await ctx.respond(random.choice(no_perm), ephemeral=True)
            
        elif isinstance(error, commands.BotMissingPermissions): # bot doesn't have perms
            return await ctx.respond(random.choice(bot_no_perm), ephemeral=True)

        elif isinstance(error, commands.MissingPermissions): # user doesn't have perms
            return await ctx.respond(random.choice(no_perm), ephemeral=True)
            
        elif isinstance(error, commands.CommandOnCooldown): # user on cool down
            return await ctx.respond(random.choice(on_cooldown), ephemeral=True)
        raise error


def setup(bot):
    bot.add_cog(errors(bot))