import discord
from discord.ext import commands
from datetime import datetime
from config import bot_time


class Bot_Owner_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @discord.Cog.listener()
    async def on_ready(self):
        print((datetime.now().strftime(f"{bot_time}")), "Loaded bot owner commands")


    # Status commands
    @commands.group(invoke_without_command=True, pass_context=True)
    @commands.is_owner()
    async def status(self, ctx):

        sudo_help = f"```\nstatus - change bot status\n\nuseage: status [status]\nexample: status idle\navailable statuses: online, invis, dnd, idle\n```"
        await ctx.reply(sudo_help, mention_author=False)

    @status.command(pass_context=True)
    @commands.is_owner()
    async def online(self, ctx):
        await self.bot.change_presence(status=discord.Status.online)
        await ctx.reply("Changed status to online")

    @status.command(pass_context=True)
    @commands.is_owner()
    async def invis(self, ctx):
        await self.bot.change_presence(status=discord.Status.invisible)
        await ctx.reply("Changed status to invisible")

    @status.command(pass_context=True)
    @commands.is_owner()
    async def dnd(self, ctx):
        await self.bot.change_presence(status=discord.Status.do_not_disturb)
        await ctx.reply("Changed status to do not disturb")

    @status.command(pass_context=True)
    @commands.is_owner()
    async def idle(self, ctx):
        await self.bot.change_presence(status=discord.Status.idle)
        await ctx.reply("Changed status to idle")


    # Activity
    @commands.group(invoke_without_command=True, pass_context=True)
    @commands.is_owner()
    async def activity(self, ctx):

        sudo_help = f"```\nactivity - change bot activity\n\nuseage: activity [activity] <command args>\nexample: activity watching Some servers\navailable activities: watching, playing, listening, streaming\n```"
        await ctx.reply(sudo_help, mention_author=False)

    @activity.command(pass_context=True)
    @commands.is_owner()
    async def watching(self, ctx, *,watching=None):
        if watching == None:
            await ctx.reply("What do you want me to watch?")
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=watching))
        await ctx.reply(f"Set watching status to '{watching}'")

    @activity.command(pass_context=True)
    @commands.is_owner()
    async def playing(self, ctx, *,playing=None):
        if playing == None:
            await ctx.reply("What do you want me to play?")
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=playing))
        await ctx.reply(f"Set playing status to '{playing}'")

    @activity.command(pass_context=True)
    @commands.is_owner()
    async def listening(self, ctx, *,listening=None):
        if listening == None:
            await ctx.reply("What do you want me to play?")
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=listening))
        await ctx.reply(f"Set listening status to '{listening}'")

    @activity.command(pass_context=True)
    @commands.is_owner()
    async def streaming(self, ctx, twitch_url=None, *,stream=None):
        if twitch_url == None:
            await ctx.reply("Add a twitch url")
        if stream == None:
            await ctx.reply("What shoud be the steam called?")
        await self.bot.change_presence(activity=discord.Streaming(name=stream, url=twitch_url))
        await ctx.reply(f"Set streaming status to '{stream}'")


def setup(bot):
    bot.add_cog(Bot_Owner_commands(bot))