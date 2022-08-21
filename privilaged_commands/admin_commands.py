import discord
from discord import option
from discord.ext import commands
from discord.utils import get
from config import bot_time
import datetime


allowed_content_types = ['image/jpeg', 'image/png']  # Setting up allowed attachments types

class admin_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @discord.Cog.listener()
    async def on_ready(self):
        print((datetime.datetime.now().strftime(f"[{bot_time}]")), "Loaded admin commands")



    @discord.slash_command(name="add_private_emoji", description="Create role specific emojis", guild_only=True, guild_ids=[380315051879432202])
    @option("name", str, description="Name of the emoji", required=True)
    @option("image", discord.Attachment, description="Image", required=True)
    @option("role", discord.Role, description="Whos gonna be able to use this emoji?", required=True)
    async def add_private_emoji(self, ctx, name: str, image: discord.Attachment, role: discord.Role):
        if image.content_type not in allowed_content_types:
            return await ctx.respond("Invalid attachment type!", ephemeral=True)
    
        image_file = await image.read()  # Reading attachment's content to get bytes
    
        await ctx.guild.create_custom_emoji(name=name, image=image_file, roles=[role])  # Image argument only takes bytes!
        emoji = get(ctx.message.guild.emojis, name=name)
        await ctx.respond(content=f"Private emoji is successfully created! {emoji}")


def setup(bot):
    bot.add_cog(admin_commands(bot))