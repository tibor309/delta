import discord, random
import requests
from discord.ext import commands
from discord_together import DiscordTogether
from config import bot_token, bot_color2, activity_link, yes_emoji, no_emoji
from asyncio import sleep

class fun_cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        self.togetherControl = await DiscordTogether(bot_token)



    # Activity command
    @discord.slash_command(name="activity", description="Start or join a voice channel activity", guild_only=True)
    @discord.commands.default_permissions(start_embedded_activities=True)
    #@commands.has_permissions(start_embedded_activities=True)
    @discord.option("channel", discord.VoiceChannel, description="Select a channel to start the activity in", required=True)
    @discord.option("activity", description="Select an activity",
        choices=[
        "Watch Together",
        "Poker Night (Boost Lvl 1)",
        "Chess In The Park (Boost Lvl 1)",
        "Letter League (Boost Lvl 1)",
        "Word Snacks",
        "Sketch Heads",
        "SpellCast (Boost Lvl 1)",
        "Awkword (Boost Lvl 1)",
        "Checkers In The Park (Boost Lvl 1)",
        "Blazing 8s (Boost Lvl 1)",
        "Land-io (Boost Lvl 1)",
        "Putt Party (Boost Lvl 1)",
        "Bobble League (Boost Lvl 1)",
        "Ask Away"
        ], required=True)

    async def activity(self, ctx: discord.ApplicationContext, channel: discord.VoiceChannel, activity: str):
        invite_age = 900 # 15 mins age
        invite_uses = 0 # unlimited use

        if activity == "Watch Together":
            selected = 'youtube'
        elif activity == "Poker Night (Boost Lvl 1)":
            selected = 'poker'
        elif activity == "Chess In The Park (Boost Lvl 1)":
            selected = 'chess'
        elif activity == "Letter League (Boost Lvl 1)":
            selected = 'letter-league'
        elif activity == "Word Snacks":
            selected = 'wold-snack'
        elif activity == "Sketch Heads":
            selected = 'sketch-heads'
        elif activity == "SpellCast (Boost Lvl 1)":
            selected = 'spellcast'
        elif activity == "Awkword (Boost Lvl 1)":
            selected = 'awkword'
        elif activity == "Checkers In The Park (Boost Lvl 1)":
            selected = 'checkers'
        elif activity == "Blazing 8s (Boost Lvl 1)":
            selected = 'blazing-8s'
        elif activity == "Land-io (Boost Lvl 1)":
            selected = 'land-io'
        elif activity == "Putt Party (Boost Lvl 1)":
            selected = 'putt-party'
        elif activity == "Bobble League (Boost Lvl 1)":
            selected = 'bobble-league'
        elif activity == "Ask Away":
            selected = 'ask-away'

        try:
            link = await self.togetherControl.create_link(channel.id, selected, max_age=invite_age, max_uses=invite_uses) # generate link and send it
            await ctx.respond(f"{random.choice(activity_link)}\n{link}")
        except:
            await ctx.respond("Failed to create activity", ephemeral=True)


    # Facts command
    @discord.slash_command(name="fact", description="He do speaking facts doe")
    async def facts(self, ctx):
        api = "https://api.popcat.xyz/fact"
        response = requests.get(api, verify=True)
        data = response.json()
        await ctx.respond(data['fact'])


    # Tell a joke
    @discord.slash_command(name="joke", description="for the funny")
    async def joke(self, ctx):
        api = "https://api.popcat.xyz/joke"
        response = requests.get(api, verify=True)
        data = response.json()
        await ctx.respond(data['joke'])


    # Flip command
    @discord.slash_command(name="flipcoin", description="Flip a coin")
    async def flip(self, ctx):
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
        message = await interaction.original_message()
        await message.add_reaction(yes_emoji) # yes
        await sleep(1) # wait before react
        await message.add_reaction(no_emoji) # no


    # Get a random color
    @discord.slash_command(name="randomcolor", description="Get a random color")
    async def color(self, ctx):
        api = "https://api.popcat.xyz/randomcolor"
        response = requests.get(api, verify=True)
        data = response.json()
        hex = data['hex']
        name = data['name']
        icon = data['image']
        color = discord.Color(int(hex, 16))

        def rgb(hex): # convert to rgb
          return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
        
        embed = discord.Embed(color=color , title=name)
        embed.add_field(name="HEX", value=f"```#{hex}```")
        embed.add_field(name="RGB", value=f"```{rgb(hex)}```")
        embed.set_thumbnail(url=icon)
        await ctx.respond(embed=embed)


    # RTD command
    @discord.slash_command(name="rtd", description="Roll the dice")
    async def rtd(self, ctx):
        await ctx.respond(f'🎲 You got, {random.randint(1,6)}!', ephemeral=False)




def setup(bot):
    bot.add_cog(fun_cmds(bot))