import discord, random
from discord.ext import commands
import datetime
from config import bot_join_msg, bot_no_perm, no_perm, bot_time

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print((datetime.datetime.now().strftime(f"[{bot_time}]")), f"Loaded events")


    # Guild join
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print((datetime.datetime.now().strftime(f"[{bot_time}]")), f"Joined '{guild.name}' guild (ID: {guild.id})")
        sent = False
        count = 0

        while not sent:
            guild_channel = guild.text_channels[count]
            message_channel = self.bot.get_channel(guild_channel.id)

            message = (random.choice(bot_join_msg))

            try:
                await message_channel.send(message)
                sent = True
            except discord.Forbidden:
                count += 1


    # Commands
    @commands.Cog.listener()
    async def on_command(self, ctx):
        print((datetime.datetime.now().strftime(f"[{bot_time}]")), f"{ctx.author} used the {ctx.command.name} command")

    @commands.Cog.listener()
    async def on_application_command(self, ctx):
        print((datetime.datetime.now().strftime(f"[{bot_time}]")), f"{ctx.author} used the {ctx.command.name} command")


    # Command error
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error): # app command error
        if isinstance(error, (commands.CommandNotFound, commands.NoPrivateMessage)):
            return

        elif isinstance(error, commands.CommandOnCooldown): # user doesn't have perms
            return await ctx.respond(error, ephemeral=True)
            
        elif isinstance(error, commands.BotMissingPermissions): # bot doesn't have perms
            return await ctx.respond(random.choice(bot_no_perm), ephemeral=True)

        elif isinstance(error, commands.MissingPermissions): # user doesn't have perms
            return await ctx.respond(random.choice(no_perm), ephemeral=True)
        raise error


def setup(bot):
    bot.add_cog(events(bot))