import discord, random
from discord.ext import commands
import datetime
from config import bot_join_msg, bot_no_perm, bot_time

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print((datetime.datetime.now().strftime(f"{bot_time}")), f"Loaded events")


    # Guild join
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print((datetime.datetime.now().strftime(f"{bot_time}")), f"Joined '{guild.name}' guild (ID: {guild.id})")
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
        print((datetime.datetime.now().strftime(f"{bot_time}")), f"{ctx.author} used the {ctx.command.name} command")

    @commands.Cog.listener()
    async def on_application_command(self, ctx):
        print((datetime.datetime.now().strftime(f"{bot_time}")), f"{ctx.author} used the {ctx.command.name} command")


    # Command error
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, (commands.CommandNotFound, commands.NoPrivateMessage)):
            return
        elif isinstance(error.original, commands.BotMissingPermissions):
            await ctx.respond(random.choice(bot_no_perm))
        raise error


def setup(bot):
    bot.add_cog(events(bot))