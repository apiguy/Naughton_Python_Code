# todo 
# make it so the user can enter in an achievement name - DONE!
# make it so a user can enter in the steam user ID - DONE!
# make it so the user can switch games - 
# make it into a module so that others can use it - 

# Steam achievement tracker
# christopher naughton

import requests
import json
import urllib2
from urllib2 import	urlopen
from json import load

# get information from the user: 
print "*****************************************************************************"
print "If you need help finding your steam Id please visit http://steamidfinder.com/"
print "*****************************************************************************"
print ""
steam_user_id = raw_input("Please enter your Steam User Id: ")
steam_app_id = raw_input("Please enter the application Id for the game you want to track: ")
steam_achi_name = raw_input("Please enter the name of the achievement you want to track: ")



# for reference http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=214560&key=27B902676079AB5FE078B4FC58E52C9C&steamid=76561198014694823
# begin create steam API URL
steam_api_url = "http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=214560"

# supply values: api key, user_id, and app_id
steam_api_key = "27B902676079AB5FE078B4FC58E52C9C"
# steam_user_id = "76561198014694823"
# steam_app_id = "214560"
steam_user_id = steam_user_id
steam_app_id = steam_app_id

# add items to the URL
steam_api_url += "&key=27B902676079AB5FE078B4FC58E52C9C"
steam_api_url += "&key=27B902676079AB5FE078B4FC58E52C9C&steamid=76561198014694823"

# take the url information that was supplied and open it
steam_response = urllib2.urlopen(steam_api_url)

# read the json information that is returned from the URL call 
parse_json = json.loads(steam_response.read())

# drill down into the json data	
achievements = parse_json['playerstats']['achievements']

# setup so you can read through the specific details
for info in achievements:
    # if the achievement is a match for the following:
    if info['apiname'] == steam_achi_name and info['achieved']:
        print "Looks like you can buy a new game!"
        break
else:
    print "Keep working on your backlog!"
		

	
	
	
	
	
	
	
	
	
	
	
