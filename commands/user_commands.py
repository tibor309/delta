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
        print((datetime.datetime.now().strftime(f"{bot_time}")), "Loaded user commands")


    # User avatar command
    @discord.user_command(name="Show user avatar and banner", guild_only=True)
    @commands.guild_only()
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
    @discord.user_command(name="Show user info")
    async def userinfo(self, ctx, member: discord.Member):
        embed = discord.Embed(color=bot_color)
        embed.set_thumbnail(url=member.avatar)
        embed.set_author(name="User info", icon_url=user_icon)
        embed.add_field(name="Username", value=f'```{member.name}#{member.discriminator}```', inline=True)
        embed.add_field(name="Nickname", value=f'```{member.nick}```', inline=True)
        embed.add_field(name="Status", value=f'```{member.status}```', inline=True)
        embed.add_field(name="Bot", value=f'```{member.bot}```', inline=True)
        embed.add_field(name="Nitro user", value=f'```{bool(member.premium_since)}```', inline=True)
        embed.add_field(name="Highest role", value=member.top_role.mention, inline=True)
        embed.add_field(name="Account created",value=f'```{member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}```', inline=False)
        embed.add_field(name="Joined on",value=f'```{member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}```', inline=False)
        
        roles = " ".join([role.mention for role in member.roles])
        embed.add_field(name="Roles", value=f"{roles}", inline=False)
        
        embed.set_footer(text='User ID: ' + str(member.id))
        await ctx.respond(embed=embed, ephemeral=True)



def setup(bot):
    bot.add_cog(user_commands(bot))