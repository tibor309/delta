import discord
from discord.ext import commands
from typing import Union


class mod_cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    # Set custom slowmode command
    @discord.slash_command(name="dirmd", description="Configure slowmode for channel", guild_only=True)
    @discord.commands.default_permissions(manage_channels=True)
    #@commands.has_permissions(manage_channels=True)
    @discord.option("sec", int, description="Slowmode delay in seconds", required=True)
    @discord.option("channel", discord.TextChannel, description="Select a channel if you want too", required=False)
    async def channel_slowmode(self, ctx, sec: int, channel: discord.TextChannel = None):
        try:
            channel = channel if channel else ctx.channel
            await channel.edit(slowmode_delay=sec)
            await ctx.respond(f"Set slowmode for {channel.mention} to {sec} sec")
        except:
            await ctx.respond("I don't have access to that channel", ephemeral=True)

    # Lock and unlock chat
    @discord.slash_command(name="lockdir", description="Lock and unlock chat", guild_only=True)
    @discord.commands.default_permissions(manage_messages=True, manage_channels=True)
    #@commands.has_permissions(manage_channels=True)
    @discord.option("locked", bool, description="Change channel lock", required=True)
    @discord.option("channel", discord.TextChannel, description="Select a channel if you want too", required=False)
    async def channel_lock(self, ctx, locked: bool, channel: discord.TextChannel = None):
        try:
            channel = channel if channel else ctx.channel
                
            if locked == True:
                await channel.set_permissions(ctx.guild.default_role, send_messages=False)
                await ctx.respond(f"Locked {channel.mention} >:3")
            elif locked == False:
                await channel.set_permissions(ctx.guild.default_role, send_messages=True)
                await ctx.respond(f"Unlocked {channel.mention}")
        except:
            await ctx.respond("I don't have access to that channel", ephemeral=True)

            
    # Remove messages
    @discord.slash_command(name="rm", description="Delete messages", guild_only=True)
    @discord.commands.default_permissions(manage_messages=True)
    #@commands.has_permissions(manage_messages=True)
    @discord.option("msg", int, description="Number of messages", required=True)
    async def remove_messages(self, ctx, messages: int):
        await ctx.channel.purge(limit=messages)
        await ctx.respond(f"Deleted {messages} messages", ephemeral=True) 


    # Create channel
    @discord.slash_command(name="mkdir", description="Create a channel", guild_only=True)
    @discord.commands.default_permissions(manage_channels=True)
    #@commands.has_permissions(manage_channels=True)
    @discord.option("name", str, description="name of the channel", required=True)
    @discord.option("type", str, description="type of the channel", required=True, choices=["text", "voice"])
    async def create_channel(self, ctx, name: str, type: str):
        if type == "text":
            await ctx.guild.create_text_channel(name=name, reason=f"created text channel by {ctx.author.name}#{ctx.author.discriminator}")
            return await ctx.respond("Created new text channel")
        elif type == "voice":
            await ctx.guild.create_voice_channel(name=name, reason=f"created voice channel by {ctx.author.name}#{ctx.author.discriminator}")
            return await ctx.respond("Created new voice channel")
        

    # Delete channel
    @discord.slash_command(name="rmdir", description="Delete a channel", guild_only=True)
    @discord.commands.default_permissions(manage_channels=True)
    #@commands.has_permissions(manage_channels=True)
    @discord.option("channel", Union[discord.TextChannel, discord.VoiceChannel], description="Select a channel", required=True)
    async def delete_channel(self, ctx, channel: Union[discord.TextChannel, discord.VoiceChannel]):
        await ctx.respond(f"Deleted #{channel.name}")
        await channel.delete(reason=f"deleted channel by {ctx.author.name}#{ctx.author.discriminator}")

            
    # Move a user to a different voice channel
    @discord.slash_command(name="mv", description="Move a user to a different vc", guild_only=True)
    @discord.commands.default_permissions(move_members=True)
    #@commands.has_guild_permissions(move_members=True)
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
    bot.add_cog(mod_cmds(bot))