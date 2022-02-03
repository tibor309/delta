from flask import Flask
from threading import Thread
import logging

app = Flask('Splash')

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def main():
  return "Server is online!"
  print("Server is online")

def run():
    app.run(host="0.0.0.0", port=8080)

def run_server():
    server = Thread(target=run)
    server.start()

def stop():
    server = Thread(target=run)
    server.stop()