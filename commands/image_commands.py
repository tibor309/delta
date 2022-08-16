import discord, datetime
from discord.ext import commands
from discord.commands import SlashCommandGroup
from discord import option
from config import bot_time, bot_color2

api1 = "https://api.popcat.xyz" # Apis for images
api2 = "https://some-random-api.ml"

class image_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        print((datetime.datetime.now().strftime(f"{bot_time}")), "Loaded image commands")


    image = SlashCommandGroup("imagemagick", "Edit images (images can take a while to load)")

    # Add overlays to uploaded images
    @image.command(name="addoverlay", description="Add different overlays to user images")
    @option("overlay", str, description="Select an overlay", choices=["uncover", "ad", "m&m", "pet", "clown", "gun", "wanted", "communism", "drip", "horny license", "triggered", "jail", "glass", "gay"], required=True)
    @option("image", discord.Member, description="Upload an image to edit", required=True)
    async def overlay(self, ctx, overlay: str, member: discord.Member):
        avatar = member.avatar
        
        if overlay == "uncover":
            image = f"{api1}/uncover?image={avatar}"
        elif overlay == "ad":
            image = f"{api1}/ad?image={avatar}"
        elif overlay == "m&m":
            image = f"{api1}/mnm?image={avatar}"
        elif overlay == "pet":
            image = f"{api1}/pet?image={avatar}"
        elif overlay == "clown":
            image = f"{api1}/clown?image={avatar}"
        elif overlay == "gun":
            image = f"{api1}/gun?image={avatar}"
        elif overlay == "wanted":
            image = f"{api1}/wanted?image={avatar}"
        elif overlay == "communism":
            image = f"{api1}/communism?image={avatar}"
        elif overlay == "drip":
            image = f"{api1}/drip?image={avatar}"

        elif overlay == "horny license":
            image = f"{api2}/canvas/horny?avatar={avatar}"
        elif overlay == "triggered":
            image = f"{api2}/canvas/triggered?avatar={avatar}"
        elif overlay == "jail":
            image = f"{api2}/canvas/jail?avatar={avatar}"


        embed = discord.Embed(color=bot_color2)
        embed.set_image(url=image)
        await ctx.respond(embed=embed)


    # Add filters to user images
    @image.command(name="addfilter", description="Add different filters to user images")
    @option("filter", str, description="Select filter", choices=["glass", "gay", "pixelate", "invert", "invertgrayscale"], required=True)
    @option("image", discord.Member, description="Upload an image to edit", required=True)
    async def filter(self, ctx, filter: str, member: discord.Member):
        avatar = member.avatar

        if filter == "glass":
            image = f"{api2}/canvas/glass?avatar={avatar}"
        elif filter == "gay":
            image = f"{api2}/canvas/gay?avatar={avatar}"
        elif filter == "pixelate":
            image = f"{api2}/canvas/pixelate?avatar={avatar}"
        elif filter == "invert":
            image = f"{api2}/canvas/invert?avatar={avatar}"
        elif filter == "invertgrayscale":
            image = f"{api2}/canvas/invertgreyscale?avatar={avatar}"

        
        embed = discord.Embed(color=bot_color2)
        embed.set_image(url=image)
        await ctx.respond(embed=embed)    



def setup(bot):
    bot.add_cog(image_commands(bot))