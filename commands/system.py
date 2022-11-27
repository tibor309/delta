import discord
from discord.ui import Button, View
from discord.ext import commands
import platform, psutil, cpuinfo
import datetime, time


start_time = time.time()

class system_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # Neofetch command
    @discord.slash_command(name="neofetch", description="Some info about the system")
    async def neofetch(self, ctx):
        await ctx.defer()
        invite = Button(label="invite me", emoji="<:love:1027605898593579118>", url="https://sh-ort.app/ym99l")
        view = View()
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
       
        name = ctx.author.name
        botname = self.bot.user.name
        
        neofetch = (f"```ansi\n"
        f"[2;34m{name.lower()}[0m@[2;34m{botname.lower()}[0m\n-------------\n"
        f"[1;2m[1;37mOS[0m[0m: Fedora Linux 37 (Server Edition) x86_64\n"
        f"[1;2m[1;37mHost[0m[0m: {host_name}\n"
        f"[1;2m[1;37mKernel[0m[0m: 6.0.8-300.fc37.x86_64\n"
        f"[1;2m[1;37mUptime[0m[0m: {uptime} seconds\n"
        f"[1;2m[1;37mPing[0m[0m: {ping}ms\n"
        f"[1;2m[1;37mPackages[0m[0m: 798 (rpm), {modules} (py), {cogs} (cog)\n"
        f"[1;2m[1;37mShell[0m[0m: bash 5.2.9\n"
        f"[1;2m[1;37mResolution[0m[0m: 3840x2160\n"
        f"[1;2m[1;37mPython version[0m[0m: {python_version}\n"
        f"[1;2m[1;37mPycord version[0m[0m: {pycord_version}\n"
        f"[1;2m[1;37mGuilds[0m[0m: {guilds} guilds\n"
        f"[1;2m[1;37mTerminal[0m[0m: pid1\n"
        f"[1;2m[1;37mCPU[0m[0m: {cpu_name}\n"
        f"[1;2m[1;37mMemory[0m[0m: {ram_usage}GB / {total_ram}GB\n"
        f"[1;2m[1;37mDisk[0m[0m: {disk_usage}GB / {total_disk}GB\n\n\n```")
        await ctx.followup.send(neofetch, view=view,ephemeral=False)



def setup(bot):
    bot.add_cog(system_commands(bot))