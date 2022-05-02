import discord
from discord.ext import commands
from discord_together import DiscordTogether
from dislash import *
from config import bot_color, basic_help, mod_help, admin_help, music_help, unusable_cmd_in_dms, no_mod_messages, no_admin_messages, activity_messages
import random
import os
import praw

bot_token = os.environ['TOKEN']
bot_prefix = os.environ['PREFIX']
reddit_id = os.environ['REDDIT_CLIENT_ID']
reddit_secret = os.environ['REDDIT_CLIENT_SECRET']

class user(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    self.togetherControl = await DiscordTogether(bot_token)



  ##### Help
  @slash_command(
    description="Help commands",
    options=[
      Option("command", description="Select a category", type=OptionType.STRING, required=False,
        choices=[
          OptionChoice("Moderator commands", "mod"),
          OptionChoice("Admin commands", "admin"),
          OptionChoice("Music commands", "music"),
        ],
      )
    ]
  )

  async def help(self, inter: SlashInteraction, command: str = None):
    if command == None:
      embed = discord.Embed(description=basic_help, color=bot_color)
      embed.set_author(name="General commands", icon_url="https://i.imgur.com/E90UgPB.png")
      embed.set_footer(text=f'{self.bot.user}  •  For more help, use optional commands.', icon_url=self.bot.user.avatar_url)
      await inter.reply(embed=embed)

    elif command == "mod":
      if isinstance(inter.channel, discord.channel.DMChannel):
        await inter.reply(random.choice(unusable_cmd_in_dms))  
      elif not inter.author.guild_permissions.manage_permissions:
        await inter.reply(random.choice(no_mod_messages))
      else:
        embed = discord.Embed(description=mod_help, color=bot_color)
        embed.set_author(name="Moderator commands", icon_url="https://i.imgur.com/jbJFUeG.png")
        embed.set_footer(text=self.bot.user, icon_url=self.bot.user.avatar_url)
        await inter.reply(embed=embed)

    elif command == "admin":
      if isinstance(inter.channel, discord.channel.DMChannel):
        await inter.respond(random.choice(unusable_cmd_in_dms))  
      if not inter.author.guild_permissions.manage_guild:
        await inter.respond(random.choice(no_admin_messages))
      else:
        embed = discord.Embed(description=admin_help, color=bot_color)
        embed.set_author(name="Admin commands", icon_url="https://i.imgur.com/QEKptpH.png")
        embed.set_footer(text=f'{self.bot.user}', icon_url=self.bot.user.avatar_url)
        await inter.reply(embed=embed)

    elif command == "music":
      embed = discord.Embed(description=music_help, color=bot_color)
      embed.set_author(name="Music commands", icon_url="https://i.imgur.com/5ALtDZZ.png")
      embed.set_footer(text=self.bot.user, icon_url=self.bot.user.avatar_url)
      await inter.reply(embed=embed)


  ##### Activity
  @slash_command(
    description="Create a vc activity",
    options=[
      Option("activity", description="Select an activity", type=OptionType.STRING, required=True,
        choices=[
          OptionChoice("Poker Night", "poker"),
          OptionChoice("Chess In The Park", "chess"),
          OptionChoice("Checkers In The Park", "checkers"),
          OptionChoice("Sketch Heads", "sketch-heads"),
          OptionChoice("World Snacks", "word-snack"),
          OptionChoice("Letter League", "letter-league"),
          OptionChoice("SpellCast", "spellcast"),
          OptionChoice("Watch Together", "youtube"),
          OptionChoice("Betrayal.io", "betrayal"),
          OptionChoice("Fishington.io", "fishing"),
          OptionChoice("Awkword", "awkword")
        ],
      )
    ]
  )

  async def activity(self, inter: SlashInteraction, activity: str):
    try:
      link = await self.togetherControl.create_link(inter.author.voice.channel.id, '' + activity, max_age=900)
      await inter.reply(f"{link}")
    except:
      await inter.reply(random.choice(activity_messages))



  ##### Avatar
  @slash_command(
    description="Grab someones avatar",
    options=[
      Option("member", "So we have a winner!", type=OptionType.USER, required=True)
    ]
  )
  async def avatar(self, inter, member=None):
    embed = discord.Embed(color=bot_color)
    embed.set_image(url=member.avatar_url)
    await inter.reply(embed=embed)

  ##ContextMenu
  @user_command(name="Grab avatar")
  async def grab_avatar(self, inter: ContextMenuInteraction):
    embed = discord.Embed(color=bot_color)
    embed.set_image(url=inter.user.avatar_url)
    await inter.reply(embed=embed)



  ##### Meme
  @slash_command(
    description="Post a spicy meme from reddit",
    options=[
      Option("subreddit", description="Choose a subreddit", type=OptionType.STRING, required=False,
        choices=[
          OptionChoice("r/memes", "memes"),
          OptionChoice("r/dankmemes", "dank"),
          OptionChoice("r/shitposting", "pooppost"),
          OptionChoice("r/me_irl", "irl"),
          OptionChoice("r/ProgrammerHumor", "program"),
          OptionChoice("r/softwaregore", "software"),
          OptionChoice("r/furrymemes", "owo"),
        ],
      )
    ]
  )

  async def meme(self, inter: SlashInteraction, subreddit:str = None):
    reddit = praw.Reddit(client_id=reddit_id,
    client_secret=reddit_secret,
    user_agent='Splash Discord Bot', check_for_async=False)

    if subreddit == None:
      memes_submissions = reddit.subreddit('memes').hot()
      post_to_pick = random.randint(1, 100)
      for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
      await inter.reply(f'{submission.title}\n{submission.url}')

    elif subreddit == "memes":
      memes_submissions = reddit.subreddit('memes').hot()
      post_to_pick = random.randint(1, 100)
      for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
      await inter.reply(f'{submission.title}\n{submission.url}')
      
    elif subreddit == "dank":
      memes_submissions = reddit.subreddit('dankmemes').hot()
      post_to_pick = random.randint(1, 100)
      for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
      await inter.reply(f'{submission.title}\n{submission.url}')
      
    elif subreddit == "pooppost":
      memes_submissions = reddit.subreddit('shitposting').hot()
      post_to_pick = random.randint(1, 100)
      for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
      await inter.reply(f'{submission.title}\n{submission.url}')
      
    elif subreddit == "software":
      memes_submissions = reddit.subreddit('softwaregore').hot()
      post_to_pick = random.randint(1, 100)
      for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
      await inter.reply(f'{submission.title}\n{submission.url}')
      
    elif subreddit == "program":
      memes_submissions = reddit.subreddit('ProgrammerHumor').hot()
      post_to_pick = random.randint(1, 100)
      for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
      await inter.reply(f'{submission.title}\n{submission.url}')
      
    elif subreddit == "irl":
      memes_submissions = reddit.subreddit('me_irl').hot()
      post_to_pick = random.randint(1, 100)
      for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
      await inter.reply(f'{submission.title}\n{submission.url}')
      
    elif subreddit == "owo":
      memes_submissions = reddit.subreddit('furrymemes').hot()
      post_to_pick = random.randint(1, 100)
      for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.over_18 and not x.stickied)
      await inter.reply(f'{submission.title}\n{submission.url}')


  ##### Embed
  



def setup(bot):
    bot.add_cog(user(bot))