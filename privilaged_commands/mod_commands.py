import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
from config import bot_time
import datetime


class mod_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @discord.Cog.listener()
    async def on_ready(self):
        print((datetime.datetime.now().strftime(f"[{bot_time}]")), "Loaded moderator commands")


    channel = SlashCommandGroup("channel", "Commands for channel moderation", guild_only=True) # create group for channel commands

    # Set custom slowmode command
    @channel.command(name="slowmode", description="Configure slowmode for channel")
    @commands.has_guild_permissions(manage_channels=True)
    @discord.option("sec", int, description="Slowmode delay in seconds", required=True)
    async def channel_slowmode(self, ctx, sec: int):
        await ctx.channel.edit(slowmode_delay=sec)
        await ctx.respond(f"Set channel slowmode to {sec} sec")

    # Lock and unlock chat
    @channel.command(name="lock", description="Lock and unlock chat")
    @commands.has_guild_permissions(manage_channels=True)
    @discord.option("locked", bool, description="True or False", required=True)
    async def channel_lock(self, ctx, locked: bool):
        if locked == True:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
            await ctx.respond("Locked chat")
        if locked == False:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
            await ctx.respond("Unlocked chat")
                

    # Remove messages
    @discord.slash_command(name="rm", description="Remove messages", guild_only=True)
    @commands.has_guild_permissions(manage_messages=True)
    @discord.option("msg", int, description="Number of messages", required=True)
    async def remove_messages(self, ctx, messages: int):
        await ctx.channel.purge(limit=messages)
        await ctx.respond(f"Deleted {messages} messages", ephemeral=True) 

  
    # Move a user to a different voice channel
    @discord.slash_command(name="mv", description="Move a user to a different vc", guild_only=True)
    @commands.has_guild_permissions(move_members=True)
    @discord.option("user", discord.Member, description="Select a user", required=True)
    @discord.option("channel", discord.VoiceChannel, description="Select a channel to move the user to", required=True)
    async def move_members(self, ctx, user: discord.Member, channel: discord.VoiceChannel):
        voice_state = user.voice
            
        if voice_state is None:
            await ctx.respond(f"{user.name} is not in a voice channel", ephemeral=True)
        else:
            await user.move_to(channel)
            await ctx.respond(f"Moved {user.mention} to {channel.mention}", ephemeral=True)





def setup(bot):
    bot.add_cog(mod_commands(bot))