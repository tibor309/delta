import aiohttp, io
import discord, datetime
from discord.ext import commands
from discord.commands import SlashCommandGroup
from config import bot_time

api1 = "https://api.popcat.xyz" # Apis for images
api2 = "https://some-random-api.ml"
api3 = "https://api.jeyy.xyz"

class image_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        print((datetime.datetime.now().strftime(f"[{bot_time}]")), "Loaded image commands")


    image = SlashCommandGroup("imagemagick", "Edit images (images can take a while to load)")

    # Add overlays to uploaded images
    @image.command(name="addoverlay", description="Add different overlays to user images")
    @commands.cooldown(1, 3, commands.BucketType.user) # Set cooldown for 3 seconds per user
    @discord.option("overlay", str, description="Select an overlay", choices=["uncover", "ad", "m&m", "pet", "clown", "gun", "wanted", "communism", "drip", "horny license", "triggered", "jail", "kanye"], required=True)
    @discord.option("image", discord.Member, description="Upload an image to edit", required=True)
    async def imagemagik_overlay(self, ctx, overlay: str, user: discord.Member):
        avatar = user.avatar
        
        if overlay == "uncover":
            url = f"{api1}/uncover?image={avatar}"
            ext = "png"
        elif overlay == "ad":
            url = f"{api1}/ad?image={avatar}"
            ext = "png"
        elif overlay == "m&m":
            url = f"{api1}/mnm?image={avatar}"
            ext = "png"
        elif overlay == "pet":
            url = f"{api1}/pet?image={avatar}"
            ext = "gif"
        elif overlay == "clown":
            url = f"{api1}/clown?image={avatar}"
            ext = "png"
        elif overlay == "gun":
            url = f"{api1}/gun?image={avatar}"
            ext = "png"
        elif overlay == "wanted":
            url = f"{api1}/wanted?image={avatar}"
            ext = "png"
        elif overlay == "communism":
            url = f"{api1}/communism?image={avatar}"
            ext = "png"
        elif overlay == "drip":
            url = f"{api1}/drip?image={avatar}"
            ext = "png"

        elif overlay == "horny license":
            url = f"{api2}/canvas/horny?avatar={avatar}"
            ext = "png"
        elif overlay == "triggered":
            url = f"{api2}/canvas/triggered?avatar={avatar}"
            ext = "gif"
        elif overlay == "jail":
            url = f"{api2}/canvas/jail?avatar={avatar}"
            ext = "png"

        elif overlay == "kanye":
            url = f"{api3}/image/kanye?image_url={avatar}"
            ext = "png"


        await ctx.defer()
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(url) as trigImg: # get user's avatar with the image
                imageData = io.BytesIO(await trigImg.read()) # read the image/bytes
                await trigSession.close() # closing the session
                await ctx.followup.send(file=discord.File(imageData, f'image.{ext}')) # sending the file



    # Add filters to user images
    @image.command(name="addfilter", description="Add different filters to user images")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @discord.option("filter", str, description="Select filter", choices=["glass", "gay", "pixelate", "invert", "invertgrayscale", "lines", "glitch", "stereo", "cartoon", "matrix"], required=True)
    @discord.option("image", discord.Member, description="Upload an image to edit", required=True)
    async def imagemagik_filter(self, ctx, filter: str, user: discord.Member):
        avatar = user.avatar

        if filter == "glass":
            url = f"{api2}/canvas/glass?avatar={avatar}"
            ext = "png"
        elif filter == "gay":
            url = f"{api2}/canvas/gay?avatar={avatar}"
            ext = "png"
        elif filter == "pixelate":
            url = f"{api2}/canvas/pixelate?avatar={avatar}"
            ext = "png"
        elif filter == "invert":
            url = f"{api2}/canvas/invert?avatar={avatar}"
            ext = "png"
        elif filter == "invertgrayscale":
            url = f"{api2}/canvas/invertgreyscale?avatar={avatar}"
            ext = "png"

        elif filter == "lines":
            url = f"{api3}/image/lines?image_url={avatar}"
            ext = "png"
        elif filter == "glitch":
            url = f"{api3}/image/glitch?image_url={avatar}&level=3"
            ext = "gif"
        elif filter == "stereo":
            url = f"{api3}/image/stereo?image_url={avatar}"
            ext = "png"
        elif filter == "cartoon":
            url = f"{api3}/image/cartoon?image_url={avatar}"
            ext = "png"
        elif filter == "matrix":
            url = f"{api3}/image/matrix?image_url={avatar}"
            ext = "gif"

        await ctx.defer()
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(url) as trigImg:
                imageData = io.BytesIO(await trigImg.read())
                await trigSession.close()
                await ctx.followup.send(file=discord.File(imageData, f'image0.{ext}'))  



def setup(bot):
    bot.add_cog(image_commands(bot))