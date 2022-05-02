from flask import Flask
from threading import Thread
import logging

app = Flask('Splash')

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def main():
  return "<h2>Oh you found me!</h2><p>This page was made, so i can check when my discord bot is down. For more info check out my <a href=\"https://github.com/Tibor309\">github</a> page!</p>"
  print("Server is online")

def run():
    app.run(host="0.0.0.0", port=8080)

def run_server():
    server = Thread(target=run)
    server.start()

def stop():
    server = Thread(target=run)
    server.stop()