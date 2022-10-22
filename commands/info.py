import discord
from discord.ext import commands
from datetime import datetime
import time
from config import bot_color, cpu_folder_icon, user_icon

class info_cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        

    @discord.slash_command(name="guildinfo", description="hack the mainframe", guild_only=True)
    async def serverinfo(self, ctx):
        await ctx.defer(ephemeral=True)
        guild = ctx.guild
        user_count = len([m for m in guild.members if not m.bot])
        bot_count = len([b for b in guild.members if b.bot])
        category_count = len(guild.categories)
        text_count = len(guild.text_channels)
        voice_count = len(guild.voice_channels)
        forum_count = len(guild.forum_channels)
        stage_count = len(guild.stage_channels)
        guild_date = int(guild.created_at.timestamp())
        file_limit = guild.filesize_limit / 1048576 # covert byte to megabyte
        afk_timeout = guild.afk_timeout / 60

        if guild.mfa_level == 0:
            mfa_level = "None"
        elif guild.mfa_level == 1:
            mfa_level = "Low"
        elif guild.mfa_level == 2:
            mfa_level = "Medium"
        elif guild.mfa_level == 3:
            mfa_level = "High"
        elif guild.mfa_level == 4:
            mfa_level = "Very High"

        if guild.afk_channel == None:
            afk_channel = "`Not set`"
        else:
            afk_channel = guild.afk_channel.mention
        
        embed = discord.Embed(description=guild.description, color=bot_color)
        embed.set_author(name="Guild info", icon_url=cpu_folder_icon)
        embed.add_field(name="Guild Name", value=f"```{guild.name}```", inline=False)
        embed.add_field(name="Owner", value=f"```{guild.owner}```", inline=True)
        embed.add_field(name="Region", value=f"```{guild.preferred_locale}```", inline=True)
        embed.add_field(name="Verification lvl", value=f"```{mfa_level}```", inline=True)
        embed.add_field(name="Server Boosts", value=f"```{guild.premium_subscription_count} boosts\n{len(guild.premium_subscribers)} boosted```", inline=True)
        embed.add_field(name="AFK Channel", value=f"{afk_channel}\n```{afk_timeout} Minutes timeout```", inline=True)
        embed.add_field(name="Roles", value=f"```{len(guild.roles)} roles```", inline=True)
        embed.add_field(name="Channels", value=f"```{category_count} categories\n{text_count} text\n{voice_count} voice\n{forum_count} forum\n{stage_count} stage```", inline=True)
        embed.add_field(name="Limits", value=f"```{file_limit}MB files\n{guild.sticker_limit} stickers\n{guild.emoji_limit} emojis\n{guild.max_members} users```", inline=True)
        embed.add_field(name="Emojis", value=f"```{len(guild.emojis)} emojis\n{len(guild.stickers)} stickers```")
        embed.add_field(name="Users", value=f"```{user_count} users\n{bot_count} bots```", inline=True)
        embed.add_field(name="Created", value=f"<t:{guild_date}:R>", inline=True)

        if guild.icon != None:
            embed.set_thumbnail(url=guild.icon)
        elif guild.banner != None:
            embed.set_image(url=guild.banner)
            
        embed.set_footer(text=f"Guild ID: {guild.id}")
        await ctx.followup.send(embed=embed, ephemeral=True)


    # User info command
    @discord.slash_command(name="userinfo", description="Show a more detailed profile", guild_only=True)
    @discord.option("user", discord.Member, description="Select a user", required=True)
    async def userinfo(self, ctx, user: discord.user):
        await ctx.defer(ephemeral=True)
        roles = " ".join([role.mention for role in user.roles if role != ctx.guild.default_role])
        creation_time = int(user.created_at.timestamp())
        join_time = int(user.joined_at.timestamp())
    
        embed = discord.Embed(color=bot_color)
        embed.set_thumbnail(url=user.avatar)
        embed.set_author(name="User info", icon_url=user_icon)
        embed.add_field(name="Username", value=f'```{user.name}#{user.discriminator}```', inline=True)
        embed.add_field(name="Nickname", value=f'```{user.nick}```', inline=True)

        if user.activity != None:
            embed.add_field(name="Activity", value=user.activity, inline=False)
            
        embed.add_field(name="Bot", value=f'```{user.bot}```', inline=True)
        embed.add_field(name="Nitro booster", value=f'```{bool(user.premium_since)}```', inline=True)
        embed.add_field(name="Highest role", value=user.top_role.mention, inline=True)
        
        embed.add_field(name="Status", value=f'```Desktop: {user.desktop_status}\nWeb: {user.web_status}\nMobile: {user.mobile_status}```', inline=False)
        
        embed.add_field(name="Account created", value=f"<t:{creation_time}:R>", inline=True)
        embed.add_field(name="Joined", value=f"<t:{join_time}:R>", inline=True)

        if roles != "":
            embed.add_field(name="Roles", value=f"{roles}", inline=False)  
    
        if user.banner != None:
            embed.set_image(url=user.banner)
        
        embed.set_footer(text=f"User ID: {user.id}")
        await ctx.followup.send(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(info_cmds(bot))