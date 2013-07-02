# import the following
import requests
import json
from urllib2 import	urlopen
from json import load

# for reference http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=214560&key=27B902676079AB5FE078B4FC58E52C9C&steamid=76561198014694823
steam_api_url = "http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=214560"

# steam keys needed to form the url request
steam_api_key = "27B902676079AB5FE078B4FC58E52C9C"
steam_user_id = "76561198014694823"
steam_app_id = "214560"

steam_api_url += "&key=27B902676079AB5FE078B4FC58E52C9C"
steam_api_url += "&key=27B902676079AB5FE078B4FC58E52C9C&steamid=76561198014694823"

steam_response = requests.get(steam_api_url)

print str(steam_api_url)

response = urlopen(steam_api_url)
load_json_obj = load(response)

print load_json_obj

# now I need to figure out how to parse through all the json to find an achievement








