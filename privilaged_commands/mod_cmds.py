import discord
from discord.ext import commands
from config import bot_color, user_icon
from asyncio import sleep

class mod_cmds(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

            
    # Remove messages
    @discord.slash_command(name="rm", description="Delete messages", guild_only=True)
    @discord.commands.default_permissions(manage_messages=True)
    @discord.option("msg", int, description="Number of messages", required=True)
    async def remove_messages(self, ctx, messages: int):
        await ctx.defer()
        await ctx.channel.purge(limit=messages, reason=f"Deleted messages by @{ctx.author.name}")
        await sleep(1)
        await ctx.followup.send(f"Deleted {messages} messages", ephemeral=True) 


    # Kick user
    @discord.slash_command(name="kick", description="Kick an user", guild_only=True)
    @discord.commands.default_permissions(kick_members=True)
    @discord.option("user", discord.Member, description="Select a user", required=True)
    @discord.option("reason", str, description="Give a reason (optional)", required=False)
    async def ban(self, ctx, user: discord.Member, reason: str = "*no reason given*"):
        if user == ctx.author:
            return await ctx.respond(f"You can't kick yourself", ephemeral=True)
            
        try:
            embed = discord.Embed(color=bot_color, title=f"{user.name} has been kicked!", description=f"**Reason:**\n{reason}")
            embed.set_author(name="User kicked", icon_url=user_icon)
            embed.set_thumbnail(url=user.avatar)
            await user.kick(reason=f"{reason} - Kicked by @{ctx.author.name}")
            await ctx.respond(embed=embed)
        except:
            await ctx.respond(f"Failed to kick {user.mention}", ephemeral=True)


    # Ban user
    @discord.slash_command(name="ban", description="Ban a user", guild_only=True)
    @discord.commands.default_permissions(ban_members=True)
    @discord.option("user", discord.Member, description="Select a user", required=True)
    @discord.option("reason", str, description="Give a reason (optional)", required=False)
    async def ban(self, ctx, user: discord.Member, reason: str = "*no reason given*"):
        if user == ctx.author:
            return await ctx.respond(f"You can't ban yourself", ephemeral=True)          
            
        try:
            embed = discord.Embed(color=bot_color, title=f"{user.name} has been banned!", description=f"**Reason:**\n{reason}")
            embed.set_author(name="User banned", icon_url=user_icon)
            embed.set_thumbnail(url=user.avatar)
            await ctx.guild.ban(user, reason=f"{reason} - Banned by @{ctx.author.name}")
            await ctx.respond(embed=embed)
        except:
            await ctx.respond(f"Failed to ban {user.mention}", ephemeral=True)

        

def setup(bot: commands.Bot) -> None:
    bot.add_cog(mod_cmds(bot))