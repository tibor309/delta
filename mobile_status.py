"""
USE THIS AT YOUR OWN RISK. THIS IS UNDOCUMENTED, I'LL NOT BE RESPONSIBLE FOR WHAT HAPPENS WITH YOUR BOT(S).

You can import this into your main file since these are top-level statements or just copy-paste the whole thing.

What this does is patches the identify payload, the `$browser` field to be exact.
Since it's hardcoded to `discord.py`, we're gonna monkey-patch it.
You can change it to either `Discord Android` or `Discord iOS`—I'm not aware of any other options,
but those 2 seem to trigger the mobile indicator.

w/ Hikari: https://github.com/norinorin/nokari/blob/master/nokari/utils/monkey_patch.py
"""

import ast
import inspect
import re

import discord


# s: https://medium.com/@chipiga86/python-monkey-patching-like-a-boss-87d7ddb8098e
def source(o):
    s = inspect.getsource(o).split("\n")
    indent = len(s[0]) - len(s[0].lstrip())
    return "\n".join(i[indent:] for i in s)


source_ = source(discord.gateway.DiscordWebSocket.identify)
patched = re.sub(
    r'([\'"]\$browser[\'"]:\s?[\'"]).+([\'"])',  # hh this regex
    r"\1Discord iOS\2",  # s: https://luna.gitlab.io/discord-unofficial-docs/mobile_indicator.html
    source_
)

loc = {}
exec(compile(ast.parse(patched), "<string>", "exec"), discord.gateway.__dict__, loc)

discord.gateway.DiscordWebSocket.identify = loc["identify"]