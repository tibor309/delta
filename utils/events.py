import random
import discord
from discord.ext import commands

from config import bot_join_msg
from config import bot_time


class events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    # Guild join
    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        print((discord.utils.utcnow().strftime(f"[{bot_time}]")), f"Joined {guild.name} guild (ID: {guild.id})")
        sent = False
        count = 0

        while not sent:
            guild_channel = guild.text_channels[count]
            message_channel = self.bot.get_channel(guild_channel.id)
            message = (random.choice(bot_join_msg))

            try:
                await message_channel.send(message) # send random message after joining server
                sent = True
            except discord.Forbidden:
                count += 1


    # Commands
    @commands.Cog.listener()
    async def on_application_command(self, ctx):
        print((discord.utils.utcnow().strftime(f"[{bot_time}]")), f"User @{ctx.author.name} (ID:{ctx.author.id}) used the '{ctx.command.qualified_name}' command")
        


def setup(bot: commands.Bot):
    bot.add_cog(events(bot))
    