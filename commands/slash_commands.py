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



    # Help command
    @discord.slash_command(name="help", description="Displays help message", hidden=False, guild_only=False)
    async def help(self, ctx):
        name = ctx.author.name
        version = "GNU bash, version 5.1.16(1)-release (x86_64-redhat-linux-gnu)"
        help_message = f"```ansi\n[{name.lower()}@splash ~]$ help\n{version}\nThese bot commands are defined internally.  Type 'help' to see this list.\n\nA star (*) next to a name means that the command is disabled.\n\nactivity [channel] [activity] - Start a voice chat activity\nmeme [subreddit] - Post a random meme from reddit\nneofetch - Show system info\nflip - Flip a coin\nrtd - Roll a dice\nmv [member] [channel] - Move a member to a voice channel\nrm [number] - Remove a number of messages\nchannel slowmode [seconds] - Set slowmode in current channel\nchannel lock [bool] - Toggle channel lock```"
        await ctx.respond(f'{help_message}', ephemeral=True)
      
      

    # Memes command
    @discord.slash_command(name="meme", description="Post memes from reddit", hidden=False, guild_only=False)
    @option("subreddit", description="Choose a subreddit", choices=["r/memes", "r/dankmemes", "r/shitposting", "r/me_irl", "r/ProgrammerHumor", "r/softwaregore", "r/furrymemes"], required=True)
    async def meme(self, ctx: discord.ApplicationContext, subreddit: str):
        reddit = praw.Reddit(client_id=reddit_id, client_secret=reddit_secret, user_agent='Splash Discord Bot', check_for_async=False)
        post_to_pick = random.randint(1, 50)

        if subreddit == "r/memes":
            memes_submissions = reddit.subreddit('memes').hot()
        elif subreddit == "r/dankmemes":
            memes_submissions = reddit.subreddit('dankmemes').hot()
        elif subreddit == "r/shitposting":
            memes_submissions = reddit.subreddit('shitposting').hot()
        elif subreddit == "r/me_irl":
            memes_submissions = reddit.subreddit('me_irl').hot()
        elif subreddit == "r/ProgrammerHumor":
            memes_submissions = reddit.subreddit('ProgrammerHumor').hot()
        elif subreddit == "r/softwaregore":
            memes_submissions = reddit.subreddit('softwaregore').hot()
        elif subreddit == "r/furrymemes":
            memes_submissions = reddit.subreddit('furrymemes').hot()

        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        embed = discord.Embed(color=bot_color2, title=submission.title)
        embed.set_image(url=submission.url)
        await ctx.respond(embed=embed)



    # Activity command
    @discord.slash_command(name="activity", description="Start or join a voice channel activity", guild_only=True, guild_ids=[380315051879432202])
    @option("channel", discord.VoiceChannel, description="Select a channel to start the activity in", required=True)
    @option("activity", description="Select an activity",
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
        "Putt Party (Boost Lvl 1)"
        ], required=True)

    async def activity(self, ctx: discord.ApplicationContext, channel: discord.VoiceChannel, activity: str):
        if ctx.author.guild_permissions.start_embedded_activities is False:
            await ctx.respond(random.choice(no_perm), ephemeral=True)
        else:
            invite_age = 900
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

            try:
                link = await self.togetherControl.create_link(channel.id, selected, max_age=invite_age, max_uses=invite_uses) # generate link and send it
                await ctx.respond(f"{random.choice(activity_link)}\n{link}")
            except:
                await ctx.respond("Failed to create activity", ephemeral=True)



    # RTD command
    @discord.slash_command(name="rtd", description="Roll the dice")
    async def rtd(self, ctx):
        await ctx.respond(f'🎲 You got, {random.randint(1,6)}!', ephemeral=False)

    # Flip command
    @discord.slash_command(name="flip", description="Flip a coin")
    async def flip(self, ctx):
        coin = ["tails", "heads"]
        await ctx.respond(f'🪙 You flipped, {random.choice(coin)}!', ephemeral=False)


    # Neofetch command
    @discord.slash_command(name="neofetch", description="Some info about the system")
    async def neofetch(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        uptime = str(datetime.timedelta(seconds=difference))

        #cpu_usage = psutil.cpu_percent()
        cpu_name = cpuinfo.get_cpu_info()['brand_raw']
        #ram_usage = round(psutil.virtual_memory().used / (1024.0**3), 1)

        ram_usage = round(psutil.virtual_memory().used / (1024**3), 1)
        total_ram = round(psutil.virtual_memory().total / (1024**3), 1)
      
        disk_usage = round(psutil.disk_usage("/").used / (1024**3), 1)
        total_disk = round(psutil.disk_usage("/").total / (1024**3), 1)
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