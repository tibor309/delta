import discord
from discord.ext import commands
from config import bot_time
import platform, psutil, cpuinfo
import datetime, time


start_time = time.time()

class system_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        print((datetime.datetime.now().strftime(f"[{bot_time}]")), "Loaded system commands")




    # Neofetch command
    @discord.slash_command(name="neofetch", description="Some info about the system")
    async def neofetch(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        uptime = str(datetime.timedelta(seconds=difference))

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
        
        neofetch = f"```ansi\n[{name.lower()}@{botname.lower()} ~]$ neofetch --no_ascii\n[2;34m{name.lower()}[0m@[2;34m{botname.lower()}[0m\n-------------\n[1;2m[1;37mOS[0m[0m: Fedora Linux 36 (Workstation Edition)\n[1;2m[1;37mKernel[0m[0m: 5.18.17-200.fc36.x86_64\n[1;2m[1;37mUptime[0m[0m: {uptime} seconds\n[1;2m[1;37mPing[0m[0m: {ping}ms\n[1;2m[1;37mPackages[0m[0m: {modules} (py), {cogs} (cog)\n[1;2m[1;37mPython[0m[0m: {python_version}\n[1;2m[1;37mPycord[0m[0m: {pycord_version}\n[1;2m[1;37mShell[0m[0m: bash 5.1.16\n[1;2m[1;37mGuilds[0m[0m: {guilds} guilds\n[1;2m[1;37mResolution[0m[0m: 3840x2160\n[2;37m[1;37mDE[0m[2;37m[0m: GNOME 42.4\n[1;2m[1;37mWM[0m[0m: Mutter\n[1;2m[1;37mWM Theme[0m[0m: Adwaita\n[1;2m[1;37mTheme[0m[0m: Adwaita [GTK2/3]\n[1;2m[1;37mIcons[0m[0m: Adwaita [GTK2/3]\n[1;2m[1;37mTerminal[0m[0m: gnome-terminal\n[1;2m[1;37mCPU[0m[0m: {cpu_name}\n[1;2m[1;37mMemory[0m[0m: {ram_usage}GB / {total_ram}GB\n[1;2m[1;37mDisk[0m[0m: {disk_usage}GB / {total_disk}GB\n\n\n```"
        await ctx.respond(neofetch, ephemeral=False)



def setup(bot):
    bot.add_cog(system_commands(bot))