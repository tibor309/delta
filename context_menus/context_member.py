import discord
from discord.ext import commands

from config import bot_color
from config import user_icon


# These commands are in the user popout menu
class user_cmds(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    # View user avatars
    @discord.user_command(name="View profile picture")
    async def useravatar(self, ctx, member: discord.Member):
        embed = discord.Embed(color=bot_color)
        embed.set_author(name=f"{member.name}'s avatar", icon_url=user_icon)
        embed.set_image(url=member.display_avatar)
        await ctx.respond(embed=embed, ephemeral=True)


    # View user banner
    @discord.user_command(name="View banner")
    async def userbanner(self, ctx, member: discord.Member):
        embed = discord.Embed(color=bot_color)
        embed.set_author(name=f"{member.name}'s profile", icon_url=user_icon)

        if member.banner != None:
            embed.set_image(url=member.banner)
            await ctx.respond(embed=embed, ephemeral=True)
        else:
            await ctx.respond(f"{member.display_name} doesn't have a banner yet", ephemeral=True)



def setup(bot: commands.Bot):
    bot.add_cog(user_cmds(bot))
