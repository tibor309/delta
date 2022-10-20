import discord
from discord.ext import commands
from config import bot_color, user_icon, bot_time
import datetime

# These commands are in the user popout menu


class user_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @discord.Cog.listener()
    async def on_ready(self):
        print((datetime.datetime.now().strftime(f"[{bot_time}]")), "Loaded user commands")


    # User avatar command
    @discord.user_command(name="Show user photos")
    async def useravatar(self, ctx, member: discord.Member):
        embed = discord.Embed(color=bot_color)
        embed.set_author(name=f'{member.name}#{member.discriminator}', icon_url=user_icon)

        if member.banner is not None:
            embed.set_image(url=member.banner)
            embed.set_thumbnail(url=member.avatar)
            
        if member.banner is None:
            embed.set_image(url=member.avatar) # if the memebr doesn't have a banner, display a message instead
            embed.set_footer(text=f"{member.name} doesn't have a banner yet")

        await ctx.respond(embed=embed, ephemeral=False)


    # User info command
    @discord.user_command(name="Show user profile", guild_only=True)
    async def userinfo(self, ctx, member: discord.Member):
        await ctx.defer(ephemeral=True)
        roles = " ".join([role.mention for role in member.roles if role != ctx.guild.default_role])
        perms = ', '.join([str(perm[0]).upper() for perm in member.guild_permissions if perm[1]])
    
        embed = discord.Embed(color=bot_color, timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=member.avatar)
        embed.set_author(name="User info", icon_url="https://i.imgur.com/zGVdnZ5.png")
        embed.add_field(name="Username", value=f'```{member.name}#{member.discriminator}```', inline=True)
        embed.add_field(name="Nickname", value=f'```{member.nick}```', inline=True)
    
        embed.add_field(name="Activity", value=member.activity, inline=False)
        
        embed.add_field(name="Bot", value=f'```{member.bot}```', inline=True)
        embed.add_field(name="Nitro booster", value=f'```{bool(member.premium_since)}```', inline=True)
        embed.add_field(name="Highest role", value=member.top_role.mention, inline=True)
        
        embed.add_field(name="Status", value=f'```Desktop: {member.desktop_status}\nWeb: {member.web_status}\nMobile: {member.mobile_status}```', inline=True)
        
        embed.add_field(name="Account created", value=f'```{member.created_at.strftime("%A, %#d %B %Y %H:%M")}```', inline=False)
        embed.add_field(name="Joined on", value=f'```{member.joined_at.strftime("%A, %#d %B %Y %H:%M")}```', inline=False)
        
        embed.add_field(name="Roles", value=f"{roles}", inline=False)
        embed.add_field(name="Guild permissions", value=f"```{perms}```", inline=False)
    
        if member.banner != None:
            embed.set_image(url=member.banner)
        
        embed.set_footer(text=f"User ID: {member.id}")
        await ctx.followup.send(embed=embed)



def setup(bot):
    bot.add_cog(user_commands(bot))