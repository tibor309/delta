import time
import discord
from discord.ext import commands

from config import invite_emoji
from config import code_emoji
from config import code_link


start_time = time.time()

class system_commands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    # Neofetch command
    @discord.slash_command(name="neofetch", description="Show system info")
    async def neofetch(self, ctx) -> None:
        await ctx.defer()
        
        current_time = time.time()
        difference = int(round(current_time - start_time))
        
        mins, sec = divmod(difference, 60)
        hour, mins = divmod(mins, 60)
        days, hour = divmod(hour, 24)

        uptime = f"{days} days, {hour} hours, {mins} minutes, {sec} seconds"
      
        cogs = len(self.bot.cogs)
        modules = len(dir())
        ping = round(self.bot.latency * 1000)
        
        name = ctx.author.name
        botname = self.bot.user.name
        users = len(self.bot.users)
        guilds = len(self.bot.guilds)

        view = discord.ui.View()
        invite = f"https://discord.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot%20applications.commands"
        view.add_item(discord.ui.Button(label="code", style=discord.ButtonStyle.link, emoji=code_emoji, url=code_link))
        view.add_item(discord.ui.Button(label="invite me", style=discord.ButtonStyle.link, emoji=invite_emoji, url=invite))

        neofetch = (f"```ansi\n"
        f"      [2;37m_____[0m      [2;34m[1;34m{name.lower()}[0m[2;34m[0m[2;37m@[0m[2;34m[1;34m[0m[2;34m[0m[1;2m[1;34m{botname.lower()}[0m[0m\n"
        f"     [2;37m/   __)[0m[2;34m\[0m    [1;2m[1;34mOS[0m[0m[1;2m[1;37m:[0m[0m [2;37mFedora Linux 38 (Server Edition)[0m\n"
        f"     [2;37m|  /[0m  [2;34m\ \[0m   [1;2m[1;34m[0m[0m[1;2m[1;34m[1;34mUptime[0m[1;34m[0m[0m[1;2m[1;37m:[0m[0m [2;37m{uptime}[0m\n"
        f"  [2;34m__[0m[2;37m_|  |_[0m[2;34m_/ /[0m   [1;2m[1;34mPackages[0m[0m[1;2m[1;37m:[0m[0m [2;37m{modules} (python), {cogs} (cog)[0m\n"
        f" [2;34m/[0m [2;37m(_    _)[0m[2;34m_/[0m    [1;2m[1;34mUsers[0m[0m[1;2m[1;37m:[0m[0m [2;37m{users} ({guilds} servers)[0m\n"
        f"[2;34m/ /[0m  [2;37m|  |[0m        [1;2m[1;34mPing[0m[0m[1;2m[1;37m:[0m[0m [2;37m{ping} ms[0m\n"
        f"[2;34m\ \[0m[2;37m__/  |[0m\n"
        f" [2;34m\[0m[2;37m(_____/[0m\n```")
        
        await ctx.followup.send(neofetch, view=view, ephemeral=True)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(system_commands(bot))