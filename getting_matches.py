import urllib.request
import os
import schedule
import time
from datetime import date
import datetime

API_KEY = "HERE"

with open("API_Token.txt") as API_Keys:
  API_KEY = API_keys.read()
  
url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key=" + API_KEY + "&format=json&steamid=" + user_id[i] + "&include_appinfo=1&include_played_free_games=1&appids_filter="
try:
  req = urllib.request.Request(url)
  response = urllib.request.urlopen(req)
  urlbyte = response.read()
except:
  time.sleep(10)
