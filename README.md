# Delta
Delta is a multipurpose discord bot with fun and moderation features and some linux like commands. This bot was made for my friends, and for myself to learn programming.
Suggestions are always welcome! You can try to set it up by yourself, or you can just invite it.

<div id="badges", align="center">
  <a href="https://replit.com/@Tibor309/Delta">
    <img src="https://img.shields.io/badge/Replit-F26207.svg?style=for-the-badge&logo=Replit&logoColor=white" alt="Replit Badge"/>
  </a>
  <a href="https://discord.com/api/oauth2/authorize?client_id=475223111323746305&permissions=8&scope=bot%20applications.commands">
    <img src="https://img.shields.io/badge/Discord-5662f6?style=for-the-badge&logo=discord&logoColor=white" alt="Discord invite Badge"/>
  </a>
</div>

## Setup
### Replit
Click on the Replit button above, and clone my repl. Then head over to the secrets tab and add fill it out using the `.env.example` file as template.
After everything set up, just click on the run button to run the bot. You can change more stuff in the config if you want! Optionally you can enable the Flask server to make the bot run 24/7.

### Source
If you prefer it you can host your own copy of this bot! First, install all the required packages with this command. **Make sure you install [py-cord][py-cord] instead of discord.py!**
```
pip3 install -r requirements.txt
```
Then rename the `.env.example` file to `.env` and fill it out with your values. **Never share your token or app secrets with anyone!**
And if you're ready, run the bot with the `python3 main.py` command!

## Config
You can customize the bot in the `config.py` file. You can change the messages, icons, colors, and emojis used by the bot. Just remember to change the emojis if you're planning to make your own fork! If you use replit or similar, uncomment the `keep_alive` lines to make the bot run 24/7!

## Usage
This bot uses the new slash commands and permissions system. That means you can override and restrict the required permissions for commands however you like in discord's integrations menu.

[py-cord]: https://github.com/Pycord-Development/pycord/