import random
import io
from asyncio import sleep
import requests
import aiohttp
import discord
from discord.ext import commands

from config import bot_color
from config import bot_color2
from config import yes_emoji
from config import no_emoji


class fun_cmds(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    # Facts command
    @discord.slash_command(name="fact", description="He do speaking facts doe")
    async def fact(self, ctx):
        await ctx.defer()
        api = "https://api.popcat.xyz/fact"
        response = requests.get(api, verify=True, timeout=15)
        data = response.json()
        await ctx.followup.send(data['fact'])


    # Tell a joke
    @discord.slash_command(name="joke", description="for the funny")
    async def joke(self, ctx):
        await ctx.defer()
        api = "https://api.popcat.xyz/joke"
        response = requests.get(api, verify=True, timeout=15)
        data = response.json()
        await ctx.followup.send(data['joke'])


    # Get a random dadjoke
    @discord.slash_command(name="dadjoke", description="Fetch a random dadjoke")
    async def dadjoke(self, ctx):
        await ctx.defer()
        api = "https://icanhazdadjoke.com/"
        response = requests.get(api, headers={"Accept": "application/json"}, verify=True, timeout=15)
        data = response.json()
        await ctx.followup.send(data['joke'])


    # Flip command
    @discord.slash_command(name="flipcoin", description="Flip a coin")
    async def flipcoin(self, ctx):
        coin = ["tails", "heads"]
        await ctx.respond(f'🪙 You flipped, {random.choice(coin)}!', ephemeral=False)


    # Create polls
    @discord.slash_command(name="poll", description="Create a yes/no poll", guild_only=True)
    @discord.option("question", description="The big question", required=True)
    @discord.option("description", description="And the description of the poll (optional)", required=False)
    async def poll(self, ctx, question: str, description: str):
        if description != None:
            embed=discord.Embed(title=question, description=description, color=bot_color2)
        else:
            embed=discord.Embed(title=question, color=bot_color)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar)
        
        interaction = await ctx.respond(embed=embed)
        message = await interaction.original_response()
        await message.add_reaction(yes_emoji) # yes
        await sleep(1) # wait before react
        await message.add_reaction(no_emoji) # no


    # Get a random color
    @discord.slash_command(name="randomcolor", description="Get a random color")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    async def randomcolor(self, ctx):
        await ctx.defer()
        api = "https://api.popcat.xyz/randomcolor"
        response = requests.get(api, verify=True, timeout=15)
        data = response.json()
        hex = data['hex']
        name = data['name']
        icon = data['image']
        color = discord.Color(int(hex, 16))

        def rgb(hex): # convert to rgb
          return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
        
        embed = discord.Embed(color=color , title=name)
        embed.add_field(name="HEX", value=f"#{hex}")
        embed.add_field(name="RGB", value=f"{rgb(hex)}")
        embed.set_thumbnail(url=icon)
        await ctx.followup.send(embed=embed)


    # RTD command
    @discord.slash_command(name="rtd", description="Roll the dice")
    async def rtd(self, ctx):
        await ctx.respond(f'🎲 You got, {random.randint(1,6)}!', ephemeral=False)


    # 8ball command
    @discord.slash_command(name="8ball", description="Talk to the magic ball")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    @discord.option("question", str, description="Ask something", required=True)
    async def ball(self, ctx, question:str):
        api = "https://api.popcat.xyz/8ball"
        await ctx.defer()
        response = requests.get(api, verify=True, timeout=15)
        data = response.json()
        embed = discord.Embed(color=bot_color, description=f"🎱 " + data['answer'])
        await ctx.followup.send(f"> {question}", embed=embed)


    # Periodic table command
    @discord.slash_command(name="randomelement", description="Show a random element from the periodic table")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    async def randomelement(self, ctx):
        await ctx.defer()
        element = random.randint(1,118)
        api = f"https://api.popcat.xyz/periodic-table?element={element}"
        response = requests.get(api, verify=True, timeout=15)
        data = response.json()

        embed = discord.Embed(color=bot_color, title=data['name'], description=data['summary'])
        embed.add_field(name="Symbol", value=data['symbol'])
        embed.add_field(name="Phase", value=data['phase'])
        embed.add_field(name="Period", value=data['period'])

        embed.add_field(name="Atomic number", value=data['atomic_number'])
        embed.add_field(name="Atomic mass", value=data['atomic_mass'])
        embed.add_field(name="Discovered by", value=data['discovered_by'])
        embed.set_thumbnail(url=data['image'])

        await ctx.followup.send(embed=embed)


    # Give headpet
    @discord.slash_command(name="petpet", description="Create a petpet gif (might take a few seconds)")
    @commands.cooldown(1, 3, commands.BucketType.user) # Cooldown for 3 sec
    @discord.option("member", discord.Member, description="Select someone", required=True)
    async def petpet(self, ctx, member: discord.Member):
        await ctx.defer()
        api = f"https://api.popcat.xyz/pet?image={member.display_avatar}"
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(api) as trigImg:
                imageData = io.BytesIO(await trigImg.read())
                await trigSession.close()
                await ctx.followup.send(file=discord.File(imageData, f'pet.gif'))


    # Send pickup lines
    @discord.slash_command(name="pickuplines", description="Get some pickup lines")
    async def pickuplines(self, ctx):
        await ctx.defer()
        api = "https://api.popcat.xyz/pickuplines"
        response = requests.get(api, verify=True, timeout=15)
        data = response.json()
        await ctx.followup.send(data['pickupline'])


    # Lulcat
    @discord.slash_command(name="lulcat", description="Translate your text into funny lul cat language")
    @commands.cooldown(1, 3, commands.BucketType.user) # Cooldown for 2 sec
    @discord.option("text", str, description="Write something", required=True)
    async def lulcat(self, ctx, text: str):
        await ctx.defer()
        api = f"https://api.popcat.xyz/lulcat?text={text}"
        response = requests.get(api, verify=True, timeout=15)
        data = response.json()
        await ctx.followup.send(data['text'])


    # Encode to binary
    @discord.slash_command(name="encode", description="Encode text to binary")
    @commands.cooldown(1, 3, commands.BucketType.user) # Cooldown for 2 sec
    @discord.option("text", str, description="Write some text", required=True)
    async def encode(self, ctx, text: str):
        await ctx.defer(ephemeral=True)
        api = f"https://api.popcat.xyz/encode?text={text}"
        response = requests.get(api, verify=True, timeout=15)
        data = response.json()
        await ctx.followup.send(f"```{data['binary']}```")


    # Decode from binary
    @discord.slash_command(name="decode", description="Decode binary to text")
    @commands.cooldown(1, 3, commands.BucketType.user) # Cooldown for 2 sec
    @discord.option("binary", str, description="Write some binary numbers", required=True)
    async def decode(self, ctx, binary: str):
        await ctx.defer(ephemeral=True)
        api = f"https://api.popcat.xyz/decode?binary={binary}"
        response = requests.get(api, verify=True, timeout=15)
        data = response.json()
        await ctx.followup.send(f"```{data['text']}```")



def setup(bot: commands.Bot):
    bot.add_cog(fun_cmds(bot))
    