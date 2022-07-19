import discord, datetime
from discord.ext import commands
from discord.commands import SlashCommandGroup
from discord import option
import praw, random
from config import bot_time, bot_color2, reddit_id, reddit_secret

class meme_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        print((datetime.datetime.now().strftime(f"{bot_time}")), "Loaded meme commands")


    
    # Post memes from reddit
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


        
    # Create memes
    memegen = SlashCommandGroup("memegen", "Create your own memes")

    # One panel memes
    @memegen.command(name="--onepanel", description="good memes")
    @option("template", str, description="Choose a template", choices=["oogway", "pikachu", "biden", "facts", "sad cat", "iphone alert", "caution"], required=True)
    @option("title", str, description="An interesting title", required=True)
    @option("text", str, description="Meme text", required=True)
    async def one_panel(self, ctx, template: str, title: str, text: str):
        global api

        if template == "oogway":
            api = "https://api.popcat.xyz/oogway"
        elif template == "pikachu":
            api = "https://api.popcat.xyz/pikachu"
        elif template == "biden":
            api = "https://api.popcat.xyz/biden"
        elif template == "facts":
            api = "https://api.popcat.xyz/facts"
        elif template == "sad cat":
            api = "https://api.popcat.xyz/sadcat"
        elif template == "iphone alert":
            api = "https://api.popcat.xyz/alert"
        elif template == "caution":
            api = "https://api.popcat.xyz/caution"

        meme = text.replace(" ", "+")
        embed = discord.Embed(color=bot_color2, title=title)
        embed.set_image(url=f"{api}?text={meme}")
        await ctx.respond(embed=embed)


    # Two panel memes
    @memegen.command(name="--twopanel", description="very good memes")
    @option("template", str, description="Choose a template", choices=["drake", "pooh"], required=True)
    @option("title", str, description="A very interesting title", required=True)
    @option("text1", str, description="Top panel text", required=True)
    @option("text2", str, description="Bottom panel text", required=True)
    async def two_panel(self, ctx, template: str, title: str, text1: str, text2:str):

        if template == "drake":
            api = "https://api.popcat.xyz/drake"
        elif template == "pooh":
            api = "https://api.popcat.xyz/pooh"

        panel1 = text1.replace(" ", "+")
        panel2 = text2.replace(" ", "+")
        embed = discord.Embed(color=bot_color2, title=title)
        embed.set_image(url=f"{api}?text1={panel1}&text2={panel2}")
        await ctx.respond(embed=embed)

    


def setup(bot):
    bot.add_cog(meme_commands(bot))