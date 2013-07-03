# Steam achievement tracker
# christopher naughton

import requests
import json
import urllib2
from urllib2 import	urlopen
from json import load

# for reference http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=214560&key=27B902676079AB5FE078B4FC58E52C9C&steamid=76561198014694823
# begin create steam API URL
steam_api_url = "http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=214560"

# supply values: api key, user_id, and app_id
steam_api_key = "27B902676079AB5FE078B4FC58E52C9C"
steam_user_id = "76561198014694823"
steam_app_id = "214560"

# add items to the URL
steam_api_url += "&key=27B902676079AB5FE078B4FC58E52C9C"
steam_api_url += "&key=27B902676079AB5FE078B4FC58E52C9C&steamid=76561198014694823"

# take the url information that was supplied and open it
steam_response = urllib2.urlopen(steam_api_url)

# read the json information that is returned from the URL call 
parse_json = json.loads(steam_response.read())

# drill down into the json data	
info = parse_json['playerstats']['achievements']

# setup so you can read through the specific details
for i in range(0, len(info)):
	#print info[i]['apiname'],info[i]['achieved']
	
	# if the achievement is as follows 
	if info[i]['apiname'] == 'trickster' and info[i]['achieved'] == 1:
		print "Looks like you can buy a new game!"
	# else if it is not a match just print white space
	else:
	   		info[i]['apiname'] != 'trickster' and info[i]['achieved'] == 0
			print " "
		
# TODO: 
# make it so the user can enter in user_id, achievement name and setting
# do a better job dealing with the else print 
# can this be made into a useful module?
	
	
	
	
	
	
	
	
	
	
	