import discord, random
import requests
from discord.ext import commands
from discord_together import DiscordTogether
from config import bot_token, bot_time, activity_link
import datetime, time


start_time = time.time()

class slash_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        self.togetherControl = await DiscordTogether(bot_token)
        print((datetime.datetime.now().strftime(f"[{bot_time}]")), "Loaded slash commands")



    # Activity command
    @discord.slash_command(name="activity", description="Start or join a voice channel activity", guild_only=True)
    @commands.has_permissions(start_embedded_activities=True)
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


    # Flip command
    @discord.slash_command(name="flipcoin", description="Flip a coin")
    async def flip(self, ctx):
        coin = ["tails", "heads"]
        await ctx.respond(f'🪙 You flipped, {random.choice(coin)}!', ephemeral=False)



def setup(bot):
    bot.add_cog(slash_commands(bot))