import discord, random
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option
from config import cmd_dms, no_perm, bot_time
import datetime


class Mod_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @discord.Cog.listener()
    async def on_ready(self):
        print((datetime.datetime.now().strftime(f"{bot_time}")), "Loaded moderator commands")


    channel = SlashCommandGroup("channel", "Commands for channel moderation")


    @channel.command(name="slowmode", description="Configure slowmode for channel")
    @commands.guild_only()
    #@commands.has_permissions(manage_channels=True)
    #@commands.bot_has_permissions(manage_channels=True)
    async def slowmode(self, ctx, sec: Option(int, "Slowmode delay in seconds", required=True)):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.respond(random.choice(cmd_dms), ephemeral=True)
            return
        else:
            if ctx.author.guild_permissions.manage_channels is False:
                await ctx.respond(random.choice(no_perm), ephemeral=True)
            else: 
                if sec == "0":
                    await ctx.channel.edit(slowmode_delay=sec)
                    await ctx.respond("Turned off slowmode", ephemeral=False)
                else:
                    await ctx.channel.edit(slowmode_delay=sec)
                await ctx.respond(f"Set channel slowmode to {sec} sec", ephemeral=False)


    @channel.command(name="lock", description="Lock and unlock chat")
    @commands.guild_only()
    async def lock(self, ctx, locked: Option(bool, "True or false", required=True)):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.respond(random.choice(cmd_dms), ephemeral=True)
            return
        else:
            if ctx.author.guild_permissions.manage_channels is False:
                await ctx.respond(random.choice(no_perm), ephemeral=True)
            else:
                if locked == True:
                    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
                    await ctx.respond("Locked chat")

                if locked == False:
                    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
                    await ctx.respond("Unlocked chat")
                



    @discord.slash_command(name="rm", description="Remove messages")
    @commands.guild_only()
    async def rm(self, ctx, messages: Option(int, "Number of messages", required=True)):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.respond(random.choice(cmd_dms), ephemeral=True)
            return
        else:
            if ctx.author.guild_permissions.manage_messages is False:
                await ctx.respond(random.choice(no_perm), ephemeral=True)
                return
            else:
                await ctx.channel.purge(limit=messages)
                await ctx.respond(f"Deleted {messages} messages", ephemeral=True)



def setup(bot):
    bot.add_cog(Mod_commands(bot))