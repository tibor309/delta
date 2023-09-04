from flask import Flask
from threading import Thread

app = Flask('Delta Discord Bot')

@app.route('/')
def home() -> str:
    return "Bot is online"

def run() -> None:
    app.run(host='0.0.0.0',port=8080)

def keep_alive() -> None:  
    t = Thread(target=run)
    t.start()
