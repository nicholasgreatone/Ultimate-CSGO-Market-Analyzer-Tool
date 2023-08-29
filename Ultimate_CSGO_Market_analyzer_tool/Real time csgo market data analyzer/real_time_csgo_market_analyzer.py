import json
import requests
import time

api_key = 'your key goes here :) '  # API key for Steam

# Read skin names from the text file
with open('skins_list.txt', 'r') as skins_file:
  skin_names = [line.strip() for line in skins_file]

# Dictionary to store skin data
skins_data = {}

for skin_name in skin_names:
  AppID = 730
  money_type = 1
  median_history_days = 15
  region ="US"
  url = f'http://steamcommunity.com/market/priceoverview/?appid={AppID}&currency={money_type}&market_hash_name={skin_name}'

  
  #url =f'http://steamcommunity.com/market/pricehistory/?country={region}&currency={money_type}&appid={AppID}&market_hash_name={skin_name}'

  
  # Send an HTTP GET request to the specified URL and get the JSON response
  find_market_data = requests.get(url)
  response = find_market_data.json()
  print (response)

  # Add the skin data to the dictionary
  skins_data[skin_name] = response

  # Add a 5-second delay before the next API request
  time.sleep(5)

# Define the filename for storing the JSON data
stored_values = 'skins_values.json'

# Open the file in write mode ('w') to save JSON data
with open(stored_values, 'w') as file_object:
  # Use the json.dump() function to write the JSON response into the file
  json.dump(skins_data, file_object, indent=2)
