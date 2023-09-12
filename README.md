# Delta
Delta is a multipurpose discord bot with fun and moderation features and some linux like commands. This bot was made for my friends, and for myself to learn programming.
Suggestions are always welcome! You can try to set it up by yourself, or you can just invite it.

<div id="badges", align="center">
  <a href="https://repl.it/github/tibor309/delta">
    <img src="https://img.shields.io/badge/Replit-F26207.svg?style=for-the-badge&logo=Replit&logoColor=white&label=Run on" alt="Replit Badge"/>
  </a>
  <a href="https://glitch.com/edit/#!/import/github/tibor309/delta">
    <img src="https://img.shields.io/badge/Glitch-3333FF.svg?style=for-the-badge&logo=Glitch&logoColor=white&label=Remix on" alt="Glitch Badge"/>
  </a>
  <a href="https://discord.com/api/oauth2/authorize?client_id=475223111323746305&permissions=8&scope=bot%20applications.commands">
    <img src="https://img.shields.io/badge/Discord-5662f6?style=for-the-badge&logo=discord&logoColor=white&label=Invite to" alt="Discord invite Badge"/>
  </a>
</div>

## Setup
### Replit and Glitch
Clone the repo, and then head over to the secrets tab and add fill it out using the `.env.example` file as template. You can change more stuff in the config file. And optionally you can enable the Flask server to make the bot run 24/7.

### Source
First, install all the required packages with this command. **Make sure to install [py-cord][py-cord] instead of discord.py!**
```
pip3 install -r requirements.txt
```
Then rename the `.env.example` file to `.env` and fill it out with your values. If you're ready, run the bot with the `python3 main.py` command!

### Docker
You can run the bot with docker if you prefer that, but you might not be able to change some settings. Pull the image, create a container with the command below, and you're good to go! **The docker image might be not up to date with the source!**
```
docker run -d -it -e TOKEN=your-bot-token -e ERR_CHANNEL=channel-id tibor309/delta
```

## Config
You can customize the bot in the `config.py` file. You can change the messages, icons, colors, and emojis used by the bot. Just remember to change out the emojis to your own if you're planning to make host it yourself instead! If you use replit or similar, uncomment the `keep_alive` lines to make the bot run 24/7!

## Usage
This bot uses the new slash commands and permissions system. That means you can override and restrict the required permissions for commands however you like in discord's integrations menu.

[py-cord]: https://github.com/Pycord-Development/pycord/