import discord
from discord.ext import commands
from config import bot_invite, invite_emoji
import os, platform, psutil, cpuinfo
import datetime, time


start_time = time.time()

class system_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # Neofetch command
    @discord.slash_command(name="neofetch", description="Some info about the system")
    async def neofetch(self, ctx):
        await ctx.defer()
        invite = discord.ui.Button(label="invite me", emoji=invite_emoji, url=bot_invite)
        view = discord.ui.View()
        view.add_item(invite)
    
        current_time = time.time()
        difference = int(round(current_time - start_time))
        uptime = str(datetime.timedelta(seconds=difference))

        host_name = platform.uname()[1]
        cpu_name = cpuinfo.get_cpu_info()['brand_raw']
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
        terminal = os.ctermid()
       
        name = ctx.author.name
        botname = self.bot.user.name
        
        neofetch = (f"```ansi\n"
        f"[2;34m[1;34m{name.lower()}[0m[2;34m[0m@[2;34m[1;34m{botname.lower()}[0m[2;34m[0m\n-----------------\n"
        f"[2;34m[1;34mOS[0m[2;34m[0m: Fedora Linux 37 (Server Edition) x86_64\n"
        f"[2;34m[1;34mHost[0m[2;34m[0m: {host_name}\n"
        f"[2;34m[1;34mKernel[0m[2;34m[0m: 6.0.8-300.fc37.x86_64\n"
        f"[2;34m[1;34mUptime[0m[2;34m[0m: {uptime} seconds\n"
        f"[2;34m[1;34mPing[0m[2;34m[0m: {ping}ms\n"
        f"[2;34m[1;34mPackages[0m[2;34m[0m: 798 (rpm), {modules} (py), {cogs} (cog)\n"
        f"[2;34m[1;34mShell[0m[2;34m[0m: bash 5.2.9\n"
        f"[2;34m[1;34mResolution[0m[2;34m[0m: 3840x2160\n"
        f"[2;34m[1;34mPython version[0m[2;34m[0m: {python_version}\n"
        f"[2;34m[1;34mPycord version[0m[2;34m[0m: {pycord_version}\n"
        f"[2;34m[1;34mGuilds[0m[2;34m[0m: {guilds} guilds\n"
        f"[2;34m[1;34mTerminal[0m[2;34m[0m: {terminal}\n"
        f"[2;34m[1;34mCPU[0m[2;34m[0m: {cpu_name}\n"
        f"[2;34m[1;34mMemory[0m[2;34m[0m: {ram_usage}GB / {total_ram}GB\n"
        f"[2;34m[1;34mDisk[0m[2;34m[0m: {disk_usage}GB / {total_disk}GB\n\n\n```")
        await ctx.followup.send(neofetch, view=view,ephemeral=False)



def setup(bot):
    bot.add_cog(system_commands(bot))