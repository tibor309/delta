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
    @discord.user_command(name="Show user images")
    async def useravatar(self, ctx, member: discord.Member):
        embed = discord.Embed(color=bot_color)
        embed.set_author(name=f'{member.name}#{member.discriminator}', icon_url=user_icon)

        if member.banner != None:
            embed.set_image(url=member.banner)
            embed.set_thumbnail(url=member.avatar)
            
        if member.banner == None:
            embed.set_image(url=member.avatar) # if the memebr doesn't have a banner, display a message instead
            embed.set_footer(text=f"{member.name} doesn't have a banner yet")

        await ctx.respond(embed=embed, ephemeral=True)


    # User perms command
    @discord.user_command(name="Show user perms")
    async def userperms(self, ctx, member: discord.Member):
        perms = ', '.join([str(perm[0]).upper() for perm in member.guild_permissions if perm[1]])
        embed = discord.Embed(color=bot_color, description=f"```{perms}```")
        embed.set_author(name="User permissions", icon_url=user_icon)
        embed.set_footer(text=f"{member.name}#{member.discriminator} • User ID: {member.id}", icon_url=member.avatar)
        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(user_commands(bot))