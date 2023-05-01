import discord
from discord.ext import commands
from config import invite_emoji, support_emoji, code_emoji
from config import support_link, code_link
import os, platform, psutil
import datetime, time


start_time = time.time()

class system_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # Neofetch command
    @discord.slash_command(name="neofetch", description="Some info about the system")
    async def neofetch(self, ctx):
        await ctx.defer()
        
        current_time = time.time()
        difference = int(round(current_time - start_time))
        
        mins, sec = divmod(difference, 60)
        hour, mins = divmod(mins, 60)
        days, hour = divmod(hour, 24)

        uptime = f"{days} days, {hour} hours, {mins} minutes, {sec} seconds"

        host_name = platform.uname()[1]
        ram_usage = int(psutil.virtual_memory().used / (1024**2))
        total_ram = int(psutil.virtual_memory().total / (1024**2))
        terminal = os.ctermid()
      
        cogs = len(self.bot.cogs)
        modules = len(dir())
        ping = round(self.bot.latency * 1000)
        
        name = ctx.author.name
        botname = self.bot.user.name

        neofetch = (f"```ansi\n"
        f"      [2;37m_____[0m      [2;34m[1;34m{name.lower()}[0m[2;34m[0m@[2;34m[2;34m[1;34m{botname.lower()}[0m[2;34m[0m[2;34m[0m\n"
        f"     [2;37m/[0m  [2;37m __)[0m[2;34m\[0m    [2;34m[2;34m[1;34mOS[0m[2;34m[0m[2;34m[0m[2;37m:[0m Fedora Linux 38 (Server Edition)\n"
        f"     [2;37m|  /[0m  [2;34m\ \[0m   [2;34m[1;34mHost[0m[2;34m[0m[2;37m:[0m {host_name}\n"
        f"  [2;34m__[0m[2;37m_|  |[0m[2;37m_[0m[2;37m[2;34m_/ /[0m[2;37m[0m   [1;2m[1;34mUptime[0m[0m[2;37m:[0m {uptime}\n"
        f" [2;34m/[0m [2;37m(_    _)[0m[2;34m_/[0m    [2;34m[1;34mPing[0;34m[0;37m:[0m {ping}ms\n"
        f"[2;34m/ /[0m  [2;37m|  |[0m        [2;34m[2;34m[1;34mPackages[0m[2;34m[0m[2;34m[0m[2;37m:[0m 837 (rpm), {modules} (py), {cogs} (cog)\n"
        f"[2;34m\ \[0m[2;37m__/  |[0m        [2;34m[2;34m[1;34mShell[0m[2;34m[0m[2;34m[0m[2;37m:[0m bash\n"
        f" [2;34m\[0m[2;37m(_____/[0m        [2;34m[1;34mTerminal[0m[2;34m[0m[2;37m:[0m {terminal}\n"
        f"                 [2;34m[1;34mMemory[0m[2;34m[0m[2;37m:[0m {ram_usage}MiB / {total_ram}MiB\n```")
        await ctx.followup.send(neofetch)


    # Uname command
    @discord.slash_command(name="uname", description="Useful links")
    async def uname(self, ctx):
        view = discord.ui.View()
        invite = f"https://discord.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot%20applications.commands"
        
        view.add_item(discord.ui.Button(label="invite me", style=discord.ButtonStyle.link, emoji=invite_emoji, url=invite)) 
        view.add_item(discord.ui.Button(label="support", style=discord.ButtonStyle.link, emoji=support_emoji, url=support_link))
        view.add_item(discord.ui.Button(label="code", style=discord.ButtonStyle.link, emoji=code_emoji, url=code_link))
        
        await ctx.respond("Linux", view=view)


def setup(bot):
    bot.add_cog(system_commands(bot))