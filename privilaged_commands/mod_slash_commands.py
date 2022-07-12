import discord, random
from discord import option
from discord.ext import commands
from discord.commands import SlashCommandGroup
from config import cmd_dms, no_perm, bot_time
import datetime


class Mod_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @discord.Cog.listener()
    async def on_ready(self):
        print((datetime.datetime.now().strftime(f"{bot_time}")), "Loaded moderator commands")


    channel = SlashCommandGroup("channel", "Commands for channel moderation") # create group for channel commands

    # Set custom slowmode command
    @channel.command(name="slowmode", description="Configure slowmode for channel", guild_only=True)
    @option("sec", int, description="Slowmode delay in seconds", required=True)
    async def slowmode(self, ctx, sec: int, required=True)):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.respond(random.choice(cmd_dms), ephemeral=True)
            return
        else:
            if ctx.author.guild_permissions.manage_channels is False:
                await ctx.respond(random.choice(no_perm), ephemeral=True)
            else: 
                await ctx.channel.edit(slowmode_delay=sec)
                await ctx.respond(f"Set channel slowmode to {sec} sec", ephemeral=False)

    # Lock and unlock chat
    @channel.command(name="lock", description="Lock and unlock chat", guild_only=True)
    @option("locked", bool, description="True or False", required=True)
    async def lock(self, ctx, locked: bool):
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
                

    # Remove messages
    @discord.slash_command(name="rm", description="Remove messages", guild_only=True)
    @option("messages", int, description="Number of messages", required=True)
    async def rm(self, ctx, messages: int):
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

  
    # Move a user to a different voice channel
    @discord.slash_command(name="mv", description="Move a user to a different vc", guild_only=True)
    @option("member", discord.Member, description="Select a user", required=True)
    @option("channel", discord.VoiceChannel, description="Select a channel to move a member to", required=True)
    async def mv(self, ctx, member: discord.Member, channel: discord.VoiceChannel):
        voice_state = member.voice
        
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.respond(random.choice(cmd_dms), ephemeral=True)
            return
        else:
            if ctx.author.guild_permissions.move_members is False:
                await ctx.respond(random.choice(no_perm), ephemeral=True)
                return
            else:
                if voice_state is None:
                    await ctx.respond(f"{member.name} is not in a voice channel", ephemeral=True)
                else:
                    await member.move_to(channel)
                    await ctx.respond(f"Moved {member.mention} to {channel.mention}", ephemeral=True)





def setup(bot):
    bot.add_cog(Mod_commands(bot))