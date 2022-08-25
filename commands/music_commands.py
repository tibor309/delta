import discord, datetime
from discord.ext import commands
from youtube_dl import YoutubeDL
from config import bot_time

class music_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        #all the music related stuff
        self.is_playing = False
        self.is_paused = False
        self._current_song = None

        # 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {'format':'bestaudio', 'noplaylist':'True', 'quiet': 'True', 'no_warnings': 'True', 'default_search': 'ytdlsearch'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = None
        
    #searching the item on youtube
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try: 
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception: 
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title'], 'duration': info['duration']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            #get the first url
            m_url = self.music_queue[0][0]['source']

            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    # infinite loop checking 
    async def play_music(self, ctx):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            
            #try to connect to voice channel if you are not already connected
            if self.vc == None or not self.vc.is_connected():
                self.vc = await self.music_queue[0][1].connect()

                #in case we fail to connect
                if self.vc == None:
                    await ctx.respond("Could not connect to the voice channel", ephemeral=True)
                    return
            else:
                await self.vc.move_to(self.music_queue[0][1])
            
            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

            
    # convert time
    @staticmethod
    def parse_duration(duration: int):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        duration = []
        if days > 0:
            duration.append('{}d'.format(days))
        if hours > 0:
            duration.append('{}h'.format(hours))
        if minutes > 0:
            duration.append('{}m'.format(minutes))
        if seconds > 0:
            duration.append('{}s'.format(seconds))

        return ', '.join(duration)



    @discord.Cog.listener()
    async def on_ready(self):
        print((datetime.datetime.now().strftime(f"[{bot_time}]")), "Loaded music commands")

    
    music = discord.SlashCommandGroup("ffmpeg", "Music playback", guild_only=True) # create command group
    
    @music.command(name="play", description="Play a selected song from youtube (it may be inaccurate)")
    @discord.option("args", str, description="Search for a song, or imput a yt url", required=True)
    async def play(self, ctx, args: str):
        discord.opus.load_opus("./libopus.so.0.8.0")
        query = " ".join(args)

        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            #you need to be connected so that the bot knows where to go
            await ctx.respond("Connect to a voice channel!", ephemeral=True)
        elif self.is_paused:
            self.vc.resume()
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.respond("Failed to download the song! Incorrect format, try another keyword. This could be due to playlist or a livestream format.", ephemeral=True)
            else:
                self.music_queue.append([song, voice_channel])

                title = song.get('title')
                duration = self.parse_duration(int(song.get('duration')))
                await ctx.respond(f"Added `{title}` `[{duration}]` to the queue")
                
                if self.is_playing == False:
                    await self.play_music(ctx)

    
    @music.command(name="pause", description="Pause the currenty playing song")
    async def pause(self, ctx):
        if self.is_playing:
            self.is_playing = False
            self.is_paused = True
            self.vc.pause()
            await ctx.respond("Paused player")
        elif self.is_paused:
            self.is_paused = False
            self.is_playing = True
            self.vc.resume()
            await ctx.respond("Resumed player")

            
    @music.command(name = "resume", description="Resume player")
    async def resume(self, ctx):
        if self.is_paused:
            self.is_paused = False
            self.is_playing = True
            self.vc.resume()
            await ctx.respond("Resumed player")
        else:
            await ctx.respond("Player is already playing", ephemeral=True)

    
    @music.command(name="skip", description="Skips current song")
    async def skip(self, ctx):
        if self.vc != None and self.vc:
            self.vc.stop()
            #try to play next in the queue if it exists
            await self.play_music(ctx)
            await ctx.respond("Skipped current song")
        else:
            await ctx.respond("Theres nothing to skip", ephemeral=True)


    @music.command(name="queue", description="Displays the current songs in queue")
    async def queue(self, ctx):
        name = ctx.author.name
        botname = self.bot.user.name
        retval = ""
        
        for i in range(0, len(self.music_queue)):
            retval += f"{i + 1}. {self.music_queue[i][0]['title']}\n"

        if retval != "":
            await ctx.respond(f"```[{name.lower()}@{botname.lower()} ~]$ ffmpeg -queue\nTotal songs: {len(self.music_queue)} songs\n{retval}```", ephemeral=True)
        else:
            await ctx.respond("There are no more songs in queue")

    
    @music.command(name="clearq", description="Stop player and clears queue")
    async def qclear(self, ctx):
        if self.vc != None and self.is_playing:
            self.vc.stop()
        self.music_queue = []
        await ctx.respond("Cleared music queue")

    
    @music.command(name="stop", description="Stop playback, and leave vc")
    async def stop(self, ctx):
        discord.opus.load_opus("./libopus.so.0.8.0")
        self.vc.stop()
        self.is_playing = False
        self.is_paused = False
        await self.vc.disconnect()
        await ctx.respond("Stopped player, and left vc")


def setup(bot):
    bot.add_cog(music_commands(bot))