import discord, random
import requests
from discord.ext import commands
from discord_together import DiscordTogether
from config import bot_token, bot_color, bot_color2, bot_time, activity_link, yes_emoji, no_emoji, cpu_folder_icon
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


    @discord.slash_command(name="guildinfo", description="hack the mainframe", guild_only=True)
    async def serverinfo(self, ctx):
        await ctx.defer(ephemeral=True)
        guild = ctx.guild
        member_count = len([m for m in guild.members if not m.bot])
        bot_count = len([b for b in guild.members if b.bot])
        category_count = len(guild.categories)
        text_count = len(guild.text_channels)
        voice_count = len(guild.voice_channels)
        forum_count = len(guild.forum_channels)
        stage_count = len(guild.stage_channels)
        guild_date = guild.created_at.strftime("%A, %#d %B %Y %H:%M")
        file_limit = guild.filesize_limit / 1048576 # covert byte to megabyte
        afk_timeout = guild.afk_timeout / 60

        if guild.mfa_level == 0:
            mfa_level = "None"
        elif guild.mfa_level == 1:
            mfa_level = "Low"
        elif guild.mfa_level == 2:
            mfa_level = "Medium"
        elif guild.mfa_level == 3:
            mfa_level = "High"
        elif guild.mfa_level == 4:
            mfa_level = "Very High"

        if guild.afk_channel == None:
            afk_channel = "`Not set`"
        else:
            afk_channel = guild.afk_channel.mention
        
        embed = discord.Embed(description=guild.description, color=bot_color)
        embed.set_author(name="Guild info", icon_url=cpu_folder_icon)
        embed.add_field(name="Guild Name", value=f"```{guild.name}```", inline=False)
        embed.add_field(name="Owner", value=f"```{guild.owner}```", inline=True)
        embed.add_field(name="Region", value=f"```{guild.preferred_locale}```", inline=True)
        embed.add_field(name="Verification lvl", value=f"```{mfa_level}```", inline=True)
        embed.add_field(name="Server Boosts", value=f"```{guild.premium_subscription_count} boosts\n{len(guild.premium_subscribers)} boosted```", inline=True)
        embed.add_field(name="AFK Channel", value=f"```{afk_timeout} Minutes timeout```\n{afk_channel}", inline=True)
        embed.add_field(name="Roles", value=f"```{len(guild.roles)} roles```", inline=True)
        embed.add_field(name="Channels", value=f"```{category_count} categories\n{text_count} text\n{voice_count} voice\n{forum_count} forum\n{stage_count} stage```", inline=True)
        embed.add_field(name="Limits", value=f"```{file_limit}MB files\n{guild.sticker_limit} stickers\n{guild.emoji_limit} emojis\n{guild.max_members} users```", inline=True)
        embed.add_field(name="Emojis", value=f"```{len(guild.emojis)} emojis\n{len(guild.stickers)} stickers```")
        embed.add_field(name="Users", value=f"```{member_count} users\n{bot_count} bots```", inline=True)
        embed.add_field(name="Created at", value=f"```{guild_date}```", inline=True)

        if guild.icon != None:
            embed.set_thumbnail(url=guild.icon)
        elif guild.banner != None:
            embed.set_image(url=guild.banner)
            
        embed.set_footer(text=f"Guild ID: {guild.id}")
        await ctx.followup.send(embed=embed)



def setup(bot):
    bot.add_cog(slash_commands(bot))