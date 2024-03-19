import random
import io
import aiohttp
import requests
import discord
from discord.ext import commands

from config import bot_color2
from config import img_fail


class meme_cmds(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    
    memegen = discord.SlashCommandGroup("memegen", "Generate memes")

    # One panel memes
    @memegen.command(name="one_panel", description="Create a one panel meme")
    @commands.cooldown(1, 3, commands.BucketType.user) # Cooldown for 3 sec
    @discord.option("template", str, description="Choose a template", choices=["oogway", "pikachu", "biden", "facts", "sad cat", "iphone alert", "caution", "sad cat", "change my mind", "lisa", "worthless", "burn"], required=True)
    @discord.option("text", str, description="Meme text", required=True)
    async def memegen_onepanel(self, ctx, template: str, text: str):
        await ctx.defer()

        if template == "oogway":
            api = "https://api.popcat.xyz/oogway"
        elif template == "pikachu":
            api = "https://api.popcat.xyz/pikachu"
        elif template == "biden":
            api = "https://api.popcat.xyz/biden"
        elif template == "facts":
            api = "https://api.popcat.xyz/facts"
        elif template == "sad cat":
            api = "https://api.popcat.xyz/sadcat"
        elif template == "iphone alert":
            api = "https://api.popcat.xyz/alert"
        elif template == "caution":
            api = "https://api.popcat.xyz/caution"
        elif template == "caution":
            api = "https://api.popcat.xyz/sadcat"

        elif template == "change my mind":
            api = "https://frenchnoodles.xyz/api/endpoints/changemymind"
        elif template == "lisa":
            api = "https://frenchnoodles.xyz/api/endpoints/lisastage"
        elif template == "worthless":
            api = "https://frenchnoodles.xyz/api/endpoints/worthless"
        elif template == "burn":
            api = "https://frenchnoodles.xyz/api/endpoints/spongebobburnpaper"

        meme_text = text.replace(" ", "+")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{api}?text={meme_text}") as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "meme.png")
                    
                    embed = discord.Embed(color=bot_color2)
                    embed.set_image(url="attachment://meme.png")
                    await ctx.followup.send(embed=embed, file=file)
                else:
                    await ctx.followup.send(random.choice(img_fail))
                await session.close()


    # Two panel memes
    @memegen.command(name="two_panel", description="Create a meme with two panels")
    @commands.cooldown(1, 3, commands.BucketType.user) # Cooldown for 3 sec
    @discord.option("template", str, description="Select a meme template", choices=["drake", "pooh", "happysad", "npc"], required=True)
    @discord.option("text1", str, description="Top panel text", required=True)
    @discord.option("text2", str, description="Bottom panel text", required=True)
    async def memegen_twopanel(self, ctx, template: str, text1: str, text2:str):
        await ctx.defer()

        if template == "drake":
            api = "https://api.popcat.xyz/drake"
        elif template == "pooh":
            api = "https://api.popcat.xyz/pooh"
        elif template == "happysad":
            api = "https://api.popcat.xyz/happysad"
        elif template == "npc":
            api = "https://vacefron.nl/api/npc"

        panel1 = text1.replace(" ", "+")
        panel2 = text2.replace(" ", "+")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{api}?text1={panel1}&text2={panel2}") as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "meme2.png")
                    
                    embed = discord.Embed(color=bot_color2)
                    embed.set_image(url="attachment://meme2.png")
                    await ctx.followup.send(embed=embed, file=file)
                else:
                    await ctx.followup.send(random.choice(img_fail))
                await session.close()


    # Meme command
    @discord.slash_command(name="meme", description="Get a random meme")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    async def meme(self, ctx):
        api = "https://api.popcat.xyz/meme"
        await ctx.defer()
        response = requests.get(api, verify=True)
        data = response.json()
        embed = discord.Embed(color=bot_color2, title=data['title'], url=data['url'])
        embed.set_image(url=data['image'])
        await ctx.followup.send(embed=embed)


    # Get inside a nokia
    @discord.slash_command(name="nokia", description="Trap someone inside a nokia")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    @discord.option("member", discord.Member, description="Select a member", required=True)
    async def nokia(self, ctx, member: discord.Member):
        await ctx.defer()
        avatar = member.avatar
        url = f"https://api.popcat.xyz/nokia?image={avatar}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "nokia.png")
                    
                    embed = discord.Embed(color=bot_color2)
                    embed.set_image(url="attachment://nokia.png")
                    await ctx.followup.send(embed=embed, file=file)
                else:
                    await ctx.followup.send(random.choice(img_fail))
                await session.close()


    # Jail someone
    @discord.slash_command(name="jail", description="tax time :)")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    @discord.option("member", discord.Member, description="Select a member", required=True)
    async def jail(self, ctx, member: discord.Member):
        await ctx.defer()
        avatar = member.avatar
        url = f"https://api.popcat.xyz/jail?image={avatar}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "jail.png")
                    
                    embed = discord.Embed(color=bot_color2)
                    embed.set_image(url="attachment://jail.png")
                    await ctx.followup.send(embed=embed, file=file)
                else:
                    await ctx.followup.send(random.choice(img_fail))
                await session.close()


    # We got a funny guy overhere!
    @discord.slash_command(name="clown", description="yo we got a funny guy here!")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    @discord.option("member", discord.Member, description="Select a member", required=True)
    async def clown(self, ctx, member: discord.Member):
        await ctx.defer()
        avatar = member.avatar
        url = f"https://api.popcat.xyz/clown?image={avatar}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "clown.png")
                    
                    embed = discord.Embed(color=bot_color2)
                    embed.set_image(url="attachment://clown.png")
                    await ctx.followup.send(embed=embed, file=file)
                else:
                    await ctx.followup.send(random.choice(img_fail))
                await session.close()


    # Gun
    @discord.slash_command(name="gun", description="Add a gun to someone's avatar")
    @commands.cooldown(1, 3, commands.BucketType.user) # Cooldown for 3 sec
    @discord.option("member", discord.Member, description="Select someone", required=True)
    async def gun(self, ctx, member: discord.Member):
        await ctx.defer()

        if member.guild_avatar != None:
            image = member.guild_avatar
        else:
            image = member.avatar

        api = f"https://api.popcat.xyz/gun?image={image}"

        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(api) as trigImg:
                imageData = io.BytesIO(await trigImg.read())
                await trigSession.close()
                await ctx.followup.send(file=discord.File(imageData, f'gun.png'))


    # Drip
    @discord.slash_command(name="drip", description="Wear the drip jacket")
    @commands.cooldown(1, 3, commands.BucketType.user) # Cooldown for 3 sec
    @discord.option("member", discord.Member, description="Select someone", required=True)
    async def drip(self, ctx, member: discord.Member):
        await ctx.defer()

        if member.guild_avatar != None:
            image = member.guild_avatar
        else:
            image = member.avatar

        api = f"https://vacefron.nl/api/drip?user={image}"

        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(api) as trigImg:
                imageData = io.BytesIO(await trigImg.read())
                await trigSession.close()
                await ctx.followup.send(file=discord.File(imageData, f'drip.png'))


    # Stonks
    @discord.slash_command(name="stonks", description="Business is booming! or not")
    @commands.cooldown(1, 3, commands.BucketType.user) # Cooldown for 3 sec
    @discord.option("member", discord.Member, description="Select someone", required=True)
    @discord.option("not_stonks", bool, description="not yippie", requred=False)
    async def stonks(self, ctx, member: discord.Member, not_stonks: bool = False):
        await ctx.defer()

        if member.guild_avatar != None:
            image = member.guild_avatar
        else:
            image = member.avatar

        api = f"https://vacefron.nl/api/stonks?user={image}&notStonks={not_stonks}"

        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(api) as trigImg:
                imageData = io.BytesIO(await trigImg.read())
                await trigSession.close()
                await ctx.followup.send(file=discord.File(imageData, f'gun.png'))



def setup(bot: commands.Bot):
    bot.add_cog(meme_cmds(bot))
    