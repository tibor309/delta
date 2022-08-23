from time import sleep
import os
from os import system

print("Restarting repl")
os.system('kill 1') # get a new ip
sleep(7) # wait a few seconds
system("python main.py") # then start the bot