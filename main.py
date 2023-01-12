#auth-64448-test
import os
os.system("pip install -r requirements.txt")
import discord
from discord.ext import commands
import time
import json
import sys

def clear():
  os.system("clear||cls")

def delete_dpy_and_install_dpy_self():
  """for replit users"""
  os.system("pip uninstall discord.py -y")
  os.system("pip uninstall discord.py-self -y")
  os.system("pip uninstall discord -y")
  os.system("pip install discord.py-self==1.9.2")


if "discord.py" in sys.modules:
  delete_dpy_and_install_dpy_self()

clear()

def title(tatte: any):
  os.system(f"title {tatte}")

title("Discord RPC - [Auth#3301]")

with open("config.json") as f:
  config = json.load(f)

li = config["large_image"]
si = config["small_image"]
lt = config["large_text"]
st = config["small_text"]
app_id = config["application_id"]
token = config["token"]
details = config["details"]
stp = str(config["status"]).lower()
hst = config["has_start_time"]
name,state = config["name"], config["state"]
if stp == "online":
  status = discord.Status.online
elif stp == "idle":
  status = discord.Status.idle
elif stp == "dnd":
  status = discord.Status.dnd
else:
  print("No Status were found in configuration, using default idle.")
  status = discord.Status.idle

client = commands.Bot(command_prefix="rpc-by-auth", help_command=None, self_bot=True)


@client.event
async def on_ready():
  print(f"{client.user} Connected, Starting RPC!, Made By Auth#3301")
  await client.change_presence(status=status, activity=discord.Activity(type=discord.ActivityType.playing, application_id=app_id, name=name, details=details, assets={'large_image': li, 'large_text': lt,"small_image": si, "small_text": st},timestamps={"start": None if not hst else time.time()}, state=state))
  time.sleep(3)
  print("RPC Started!")
  
  


client.run(token)
