import aiohttp, io
import discord
from discord.ext import commands

class img_cmds(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    # Post cool images of foxes
    @discord.slash_command(name="fox", description="I like foxes :3")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def fox(self, ctx):
        await ctx.defer()
        url = "https://api.tinyfox.dev/img?animal=fox"
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(url) as trigImg:
                imageData = io.BytesIO(await trigImg.read())
                await trigSession.close()
                await ctx.followup.send(file=discord.File(imageData, f'fox.png'))




def setup(bot: commands.Bot) -> None:
    bot.add_cog(img_cmds(bot))