import discord
from discord.ext import commands
from discord import option
import praw, random
from discord_together import DiscordTogether
from config import bot_token, bot_color2, bot_time, reddit_id, reddit_secret, no_perm, activity_link
import platform, psutil, cpuinfo
import datetime, time


start_time = time.time()

class Slash_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        self.togetherControl = await DiscordTogether(bot_token)
        print((datetime.datetime.now().strftime(f"{bot_time}")), "Loaded slash commands")



    # Memes command
    @discord.slash_command(name="meme", description="Post memes from reddit", hidden=False, guild_only=False)
    @option("subreddit", description="Choose a subreddit", choices=["r/memes", "r/dankmemes", "r/shitposting", "r/me_irl", "r/ProgrammerHumor", "r/softwaregore", "r/furrymemes"], required=True)
    async def meme(self, ctx: discord.ApplicationContext, subreddit: str):
        reddit = praw.Reddit(client_id=reddit_id, client_secret=reddit_secret, user_agent='Splash Discord Bot', check_for_async=False)
        post_to_pick = random.randint(1, 100)

        if subreddit == "r/memes":
            memes_submissions = reddit.subreddit('memes').hot()
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(color=bot_color2, title=submission.title, url=submission.url)
            embed.set_image(url=submission.url)
            await ctx.respond(embed=embed)

        elif subreddit == "r/dankmemes":
            memes_submissions = reddit.subreddit('dankmemes').hot()
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(color=bot_color2, title=submission.title, url=submission.url)
            embed.set_image(url=submission.url)
            await ctx.respond(embed=embed)

        elif subreddit == "r/shitposting":
            memes_submissions = reddit.subreddit('shitposting').hot()
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(color=bot_color2, title=submission.title, url=submission.url)
            embed.set_image(url=submission.url)
            await ctx.respond(embed=embed)

        elif subreddit == "r/me_irl":
            memes_submissions = reddit.subreddit('me_irl').hot()
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(color=bot_color2, title=submission.title, url=submission.url)
            embed.set_image(url=submission.url)
            await ctx.respond(embed=embed)

        elif subreddit == "r/ProgrammerHumor":
            memes_submissions = reddit.subreddit('ProgrammerHumor').hot()
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(color=bot_color2, title=submission.title, url=submission.url)
            embed.set_image(url=submission.url)
            await ctx.respond(embed=embed)

        elif subreddit == "r/softwaregore":
            memes_submissions = reddit.subreddit('softwaregore').hot()
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(color=bot_color2, title=submission.title, url=submission.url)
            embed.set_image(url=submission.url)
            await ctx.respond(embed=embed)

        elif subreddit == "r/furrymemes":
            memes_submissions = reddit.subreddit('furrymemes').hot()
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(color=bot_color2, title=submission.title, url=submission.url)
            embed.set_image(url=submission.url)
            await ctx.respond(embed=embed)



    # Activity command
    @discord.slash_command(name="activity", description="Start or join a voice channel activity", hidden=False, guild_only=True)
    @commands.guild_only()
    @option("channel", discord.VoiceChannel, description="Select a channel to start the activity in", required=True)
    @option("activity", description="Select an activity",
        choices=[
        "Watch Together",
        "Poker Night (Boost Lvl 1)",
        "Chess In The Park (Boost Lvl 1)",
        #"Betrayal.io",
        #"Fishington.io",
        "Letter League (Boost Lvl 1)",
        "Word Snacks",
        "Sketch Heads",
        "SpellCast (Boost Lvl 1)",
        "Awkword (Boost Lvl 1)",
        "Checkers In The Park (Boost Lvl 1)",
        "Blazing 8s (Boost Lvl 1)",
        "Land-io (Boost Lvl 1)",
        "Putt Party (Boost Lvl 1)"
        ], required=True)

    async def activity(self, ctx: discord.ApplicationContext, channel: discord.VoiceChannel, activity: str):
        if ctx.author.guild_permissions.start_embedded_activities is False:
            await ctx.respond(random.choice(no_perm), ephemeral=True)
        else:

            if activity == "Watch Together":
                try:
                    link = await self.togetherControl.create_link(channel.id, 'youtube', max_age=900)
                    await ctx.respond(f"{random.choice(activity_link)}\n{link}")
                except:
                    await ctx.respond("Failed to create activity", ephemeral=True)

            elif activity == "Poker Night (Boost Lvl 1)":
                try:
                    link = await self.togetherControl.create_link(channel.id, 'poker', max_age=900)
                    await ctx.respond(f"{random.choice(activity_link)}\n{link}")
                except:
                    await ctx.respond("Failed to create activity", ephemeral=True)
            
            elif activity == "Chess In The Park (Boost Lvl 1)":
                try:
                    link = await self.togetherControl.create_link(channel.id, 'chess', max_age=900)
                    await ctx.respond(f"{random.choice(activity_link)}\n{link}")
                except:
                    await ctx.respond("Failed to create activity", ephemeral=True)

            elif activity == "Betrayal.io":
                try:
                    link = await self.togetherControl.create_link(channel.id, 'betrayal', max_age=900)
                    await ctx.respond(f"{random.choice(activity_link)}\n{link}")
                except:
                    await ctx.respond("Failed to create activity", ephemeral=True)

            elif activity == "Fishington.io":
                try:
                    link = await self.togetherControl.create_link(channel.id, 'fishing', max_age=900)
                    await ctx.respond(f"{random.choice(activity_link)}\n{link}")
                except:
                    await ctx.respond("Failed to create activity", ephemeral=True)

            elif activity == "Letter League (Boost Lvl 1)":
                try:
                    link = await self.togetherControl.create_link(channel.id, 'letter-league', max_age=900)
                    await ctx.respond(f"{random.choice(activity_link)}\n{link}")
                except:
                    await ctx.respond("Failed to create activity", ephemeral=True)

            elif activity == "Word Snacks":
                try:
                    link = await self.togetherControl.create_link(channel.id, 'word-snack', max_age=900)
                    await ctx.respond(f"{random.choice(activity_link)}\n{link}")
                except:
                    await ctx.respond("Failed to create activity", ephemeral=True)

            elif activity == "Sketch Heads":
                try:
                    link = await self.togetherControl.create_link(channel.id, 'sketch-heads', max_age=900)
                    await ctx.respond(f"{random.choice(activity_link)}\n{link}")
                except:
                    await ctx.respond("Failed to create activity", ephemeral=True)

            elif activity == "SpellCast (Boost Lvl 1)":
                try:
                    link = await self.togetherControl.create_link(channel.id, 'spellcast', max_age=900)
                    await ctx.respond(f"{random.choice(activity_link)}\n{link}")
                except:
                    await ctx.respond("Failed to create activity", ephemeral=True)

            elif activity == "Awkword (Boost Lvl 1)":
                try:
                    link = await self.togetherControl.create_link(channel.id, 'awkword', max_age=900)
                    await ctx.respond(f"{random.choice(activity_link)}\n{link}")
                except:
                    await ctx.respond("Failed to create activity", ephemeral=True)

            elif activity == "Checkers In The Park (Boost Lvl 1)":
                try:
                    link = await self.togetherControl.create_link(channel.id, 'checkers', max_age=900)
                    await ctx.respond(f"{random.choice(activity_link)}\n{link}")
                except:
                    await ctx.respond("Failed to create activity", ephemeral=True)

            elif activity == "Blazing 8s (Boost Lvl 1)":
                try:
                    link = await self.togetherControl.create_link(channel.id, 'blazing-8s', max_age=900)
                    await ctx.respond(f"{random.choice(activity_link)}\n{link}")
                except:
                    await ctx.respond("Failed to create activity", ephemeral=True)

            elif activity == "Land-io (Boost Lvl 1)":
                try:
                    link = await self.togetherControl.create_link(channel.id, 'land-io', max_age=900)
                    await ctx.respond(f"{random.choice(activity_link)}\n{link}")
                except:
                    await ctx.respond("Failed to create activity", ephemeral=True)

            elif activity == "Putt Party (Boost Lvl 1)":
                try:
                    link = await self.togetherControl.create_link(channel.id, 'putt-party', max_age=900)
                    await ctx.respond(f"{random.choice(activity_link)}\n{link}")
                except:
                    await ctx.respond("Failed to create activity", ephemeral=True)


    # RTD command
    @discord.slash_command(name="rtd", description="Roll the dice", ephemeral=False)
    async def rtd(self, ctx):
        await ctx.respond(f'🎲 You got, {random.randint(1,6)}!')

    # Flip command
    @discord.slash_command(name="flip", description="Flip a coin")
    async def flip(self, ctx):
        coin = ["tails", "heads"]
        await ctx.respond(f'🪙 You flipped, {random.choice(coin)}!', ephemeral=False)


    # Neofetch command
    @discord.slash_command(name="neofetch", description="Some info about the system", ephemeral=True)
    async def neofetch(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        uptime = str(datetime.timedelta(seconds=difference))

        #cpu_usage = psutil.cpu_percent()
        cpu_name = cpuinfo.get_cpu_info()['brand_raw']
        ram_usage = round(psutil.virtual_memory().used / (1024.0**3), 1)
        total_ram = round(psutil.virtual_memory().total / (1024.0**3), 1)
        disk_usage = round(psutil.disk_usage("/").used / (1024.0**3), 1)
        total_disk = round(psutil.disk_usage("/").total / (1024.0**3), 1)
        cogs = len(self.bot.cogs)
        python_version = platform.python_version()
        pycord_version = discord.__version__
        modules = len(dir())
        ping = round(self.bot.latency * 1000)
        guilds = len(self.bot.guilds)
       
        name = ctx.author.name
        neofetch = f"```ansi\n[{name.lower()}@splash ~]$ neofetch --no_ascii\n[2;34m{name.lower()}[0m@[2;34msplash[0m\n-------------\n[1;2m[1;37mOS[0m[0m: Fedora Linux 36 (Workstation Edition)\n[1;2m[1;37mKernel[0m[0m: 5.17.8-300.fc36.x86_64\n[1;2m[1;37mUptime[0m[0m: {uptime} seconds\n[1;2m[1;37mPing[0m[0m: {ping}ms\n[1;2m[1;37mPackages[0m[0m: {modules} (py), {cogs} (cog)\n[1;2m[1;37mPython[0m[0m: {python_version}\n[1;2m[1;37mPycord[0m[0m: {pycord_version}\n[1;2m[1;37mShell[0m[0m: bash 5.1.16\n[1;2m[1;37mGuilds[0m[0m: {guilds} guilds\n[1;2m[1;37mResolution[0m[0m: 3840x2160\n[2;37m[1;37mDE[0m[2;37m[0m: GNOME 42.1\n[1;2m[1;37mWM[0m[0m: Mutter\n[1;2m[1;37mWM Theme[0m[0m: Adwaita\n[1;2m[1;37mTheme[0m[0m: Adwaita [GTK2/3]\n[1;2m[1;37mIcons[0m[0m: Adwaita [GTK2/3]\n[1;2m[1;37mTerminal[0m[0m: gnome-terminal\n[1;2m[1;37mCPU[0m[0m: {cpu_name}\n[1;2m[1;37mMemory[0m[0m: {ram_usage}GB / {total_ram}GB\n[1;2m[1;37mDisk[0m[0m: {disk_usage}GB / {total_disk}GB\n\n\n```"
        await ctx.respond(neofetch, ephemeral=False)




def setup(bot):
    bot.add_cog(Slash_commands(bot))