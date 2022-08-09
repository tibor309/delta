import discord, datetime
from discord.ext import commands
from discord.commands import SlashCommandGroup
from discord import option
from config import bot_time, bot_color2

class image_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        print((datetime.datetime.now().strftime(f"{bot_time}")), "Loaded image commands")


    image = SlashCommandGroup("imagemagick", "Edit images (images can take a while to load)")

    # Add overlays to uploaded images
    @image.command(name="addoverlay", description="Add different overlays to user images")
    @option("overlay", str, description="Select an overlay", choices=["uncover", "ad", "m&m", "pet", "clown", "gun", "wanted", "communism", "drip"], required=True)
    @option("image", discord.Member, description="Upload an image to edit", required=True)
    async def overlay(self, ctx, overlay: str, image: discord.Member):

        if overlay == "uncover":
            api = "https://api.popcat.xyz/uncover"
        elif overlay == "ad":
            api = "https://api.popcat.xyz/ad"
        elif overlay == "m&m":
            api = "https://api.popcat.xyz/mnm"
        elif overlay == "pet":
            api = "https://api.popcat.xyz/pet"
        elif overlay == "clown":
            api = "https://api.popcat.xyz/clown"
        elif overlay == "gun":
            api = "https://api.popcat.xyz/gun"
        elif overlay == "wanted":
            api = "https://api.popcat.xyz/wanted"
        elif overlay == "communism":
            api = "https://api.popcat.xyz/communism"
        elif overlay == "drip":
            api = "https://api.popcat.xyz/drip"
        
        edited = image.avatar
        embed = discord.Embed(color=bot_color2)
        embed.set_image(url=f"{api}?image={edited}")
        await ctx.respond(embed=embed)    



def setup(bot):
    bot.add_cog(image_commands(bot))