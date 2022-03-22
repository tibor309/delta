from flask import Flask
from threading import Thread
import logging

app = Flask('Splash')

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def main():
  return "Oh you found me! This page was made, so i can check when my discord bot is down. For more info check out my github page!"
  print("Server is online")

def run():
    app.run(host="0.0.0.0", port=8080)

def run_server():
    keepAlive = Thread(target=run)
    keepAlive.start()

def stop():
    keepAlive = Thread(target=run)
    keepAlive.stop()