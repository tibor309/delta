import discord, random
import requests
from discord.ext import commands
from discord_together import DiscordTogether
from config import bot_token, bot_color, bot_color2
from config import activity_link, yes_emoji, no_emoji
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
    @discord.option("channel", discord.VoiceChannel, description="Select a channel to start the activity in", required=True)
    @discord.option("activity", description="Select an activity",
        choices=[
        "Watch Together",
        "Poker Night (Requires boost)",
        "Chess In The Park (Requires boost)",
        "Letter League (Requires boost)",
        "Word Snacks",
        "Sketch Heads",
        "SpellCast (Requires boost)",
        "Awkword (Requires boost)",
        "Checkers In The Park (Requires boost)",
        "Blazing 8s (Requires boost)",
        "Land-io (Requires boost)",
        "Putt Party (Requires boost)",
        "Bobble League (Requires boost)",
        "Ask Away"
        ], required=True)

    async def activity(self, ctx: discord.ApplicationContext, channel: discord.VoiceChannel, activity: str):
        await ctx.defer()
        invite_age = 900 # 15 mins age
        invite_uses = 0 # unlimited use

        if activity == "Watch Together":
            selected = 'youtube'
        elif activity == "Poker Night (Requires boost)":
            selected = 'poker'
        elif activity == "Chess In The Park (Requires boost)":
            selected = 'chess'
        elif activity == "Letter League (Requires boost)":
            selected = 'letter-league'
        elif activity == "Word Snacks":
            selected = 'wold-snack'
        elif activity == "Sketch Heads":
            selected = 'sketch-heads'
        elif activity == "SpellCast (Requires boost)":
            selected = 'spellcast'
        elif activity == "Awkword (Requires boost)":
            selected = 'awkword'
        elif activity == "Checkers In The Park (Requires boost)":
            selected = 'checkers'
        elif activity == "Blazing 8s (Requires boost)":
            selected = 'blazing-8s'
        elif activity == "Land-io (Requires boost)":
            selected = 'land-io'
        elif activity == "Putt Party (Requires boost)":
            selected = 'putt-party'
        elif activity == "Bobble League (Requires boost)":
            selected = 'bobble-league'
        elif activity == "Ask Away":
            selected = 'ask-away'

        try:
            link = await self.togetherControl.create_link(channel.id, selected, max_age=invite_age, max_uses=invite_uses) # generate link and send it
            await ctx.followup.send(f"{random.choice(activity_link)}\n{link}")
        except:
            await ctx.followup.send("Failed to create activity", ephemeral=True)


    # Facts command
    @discord.slash_command(name="fact", description="He do speaking facts doe")
    async def facts(self, ctx):
        await ctx.defer()
        api = "https://api.popcat.xyz/fact"
        response = requests.get(api, verify=True)
        data = response.json()
        await ctx.followup.send(data['fact'])


    # Tell a joke
    @discord.slash_command(name="joke", description="for the funny")
    async def joke(self, ctx):
        await ctx.defer()
        api = "https://api.popcat.xyz/joke"
        response = requests.get(api, verify=True)
        data = response.json()
        await ctx.followup.send(data['joke'])


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
        message = await interaction.original_respponse()
        await message.add_reaction(yes_emoji) # yes
        await sleep(1) # wait before react
        await message.add_reaction(no_emoji) # no


    # Get a random color
    @discord.slash_command(name="randomcolor", description="Get a random color")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    async def color(self, ctx):
        await ctx.defer()
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
        response = requests.get(api, verify=True)
        data = response.json()
        embed = discord.Embed(color=bot_color, description=f"🎱 " + data['answer'])
        await ctx.followup.send(f"> {question}", embed=embed)



def setup(bot):
    bot.add_cog(fun_cmds(bot))