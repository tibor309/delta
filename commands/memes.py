import discord
import aiohttp, io
from discord.ext import commands
from discord.commands import SlashCommandGroup
import praw, random
from config import bot_color2, reddit_id, reddit_secret, img_fail

class meme_cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    
    # Post memes from reddit
    @discord.slash_command(name="meme", description="Post memes from reddit")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    @discord.option("subreddit", description="Choose a subreddit", choices=["r/memes", "r/dankmemes", "r/shitposting", "r/me_irl", "r/ProgrammerHumor", "r/softwaregore", "r/furrymemes"], required=True)
    async def meme(self, ctx: discord.ApplicationContext, subreddit: str):
        await ctx.defer()
        reddit = praw.Reddit(client_id=reddit_id, client_secret=reddit_secret, user_agent='Delta', check_for_async=False)
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
        await ctx.followup.send(embed=embed)

    
    memegen = SlashCommandGroup("memegen", "Create your own memes") # Create memes

    # One panel memes
    @memegen.command(name="--onepanel", description="good memes")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    @discord.option("template", str, description="Choose a template", choices=["oogway", "pikachu", "biden", "facts", "sad cat", "iphone alert", "caution"], required=True)
    @discord.option("title", str, description="An interesting title", required=True)
    @discord.option("text", str, description="Meme text", required=True)
    async def memegen_onepanel(self, ctx, template: str, title: str, text: str):
        await ctx.defer()
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
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{api}?text={meme}") as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "meme.png")
                    
                    embed = discord.Embed(color=bot_color2, title=title)
                    embed.set_image(url="attachment://meme.png")
                    await ctx.followup.send(embed=embed, file=file)
                else:
                    await ctx.followup.send(random.choice(img_fail))
                await session.close()


    # Two panel memes
    @memegen.command(name="--twopanel", description="very good memes")
    @commands.cooldown(1, 2, commands.BucketType.user) # Cooldown for 2 sec
    @discord.option("template", str, description="Choose a template", choices=["drake", "pooh"], required=True)
    @discord.option("title", str, description="A very interesting title", required=True)
    @discord.option("text1", str, description="Top panel text", required=True)
    @discord.option("text2", str, description="Bottom panel text", required=True)
    async def memegen_twopanel(self, ctx, template: str, title: str, text1: str, text2:str):
        await ctx.defer()

        if template == "drake":
            api = "https://api.popcat.xyz/drake"
        elif template == "pooh":
            api = "https://api.popcat.xyz/pooh"

        panel1 = text1.replace(" ", "+")
        panel2 = text2.replace(" ", "+")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{api}?text1={panel1}&text2={panel2}") as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "meme2.png")
                    
                    embed = discord.Embed(color=bot_color2, title=title)
                    embed.set_image(url="attachment://meme2.png")
                    await ctx.followup.send(embed=embed, file=file)
                else:
                    await ctx.followup.send(random.choice(img_fail))
                await session.close()




def setup(bot):
    bot.add_cog(meme_cmds(bot))