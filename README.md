# `Δ` Delta

Delta is a discord bot with fun and interesting features. This bot was made for my friends, and for myself to learn programming. You can use it to get cute pictures of foxes, create memes, and some more stuff. You can host it yourself, or you can just invite it.

<div id="badges", align="center">
  <a href="https://repl.it/github/tibor309/delta">
    <img src="https://img.shields.io/badge/Replit-403f5f.svg?style=for-the-badge&logo=Replit&logoColor=white&labelColor=595885&label=Run on" alt="replit_badge"/>
  </a>
  <a href="https://glitch.com/edit/#!/import/github/tibor309/delta">
    <img src="https://img.shields.io/badge/Glitch-403f5f.svg?style=for-the-badge&logo=Glitch&logoColor=white&labelColor=595885&label=Remix on" alt="glitch_badge"/>
  </a>
  <a href="https://hub.docker.com/r/tibor309/delta">
    <img src="https://img.shields.io/badge/Docker-403f5f.svg?style=for-the-badge&logo=Docker&logoColor=white&labelColor=595885&label=Pull from" alt="docker_badge"/>
  </a>
  <a href="https://discord.com/api/oauth2/authorize?client_id=475223111323746305&permissions=8&scope=bot%20applications.commands">
    <img src="https://img.shields.io/badge/Discord-403f5f?style=for-the-badge&logo=discord&logoColor=white&labelColor=595885&label=Invite to" alt="discord_badge"/>
  </a>
</div>

## Setup
### Replit and Glitch
Clone the repo, and then head over to the secrets tab and add fill it out using the `.env.example` file as template. Then install all the packages using the same command below. Make sure the package manager won't install discord.py or other discord libraries! You can customize the bot in the config file.

### Source
First, install all the required packages with the command below. At least python 3.10 is required for the bot to run!

```bash
pip3 install -r requirements.txt
```

Then rename the `.env.example` file to `.env` and fill it out with your values. If you're ready, run the bot with this command:

```bash
python3 main.py
```

### Docker
You can also run the bot with docker if you prefer that, but you won't be able to change some settings easily.

```bash
docker run -d -it -e TOKEN=your-bot-token -e ERR_CHANNEL=channel-id tibor309/delta:latest
```

## Config
You can customize the bot in the `config.py` file. You can change the messages, icons, colors, and emojis used by the bot.

> Icons were provided by [fontawesome](https://fontawesome.com/)! <3