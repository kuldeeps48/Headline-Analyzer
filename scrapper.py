##########
#
# scrapper.py
# By Aadarsha Shrestha (aadarsha.shrestha.nepal@gmail.com)
#
# The scrapper can scrape news headlines from multiple news sources.
# Powered by newsapi.org
#
# Date: 05-03-2017
# Last Modified Date: 05-07-2017
#
##########

import json
from urllib.request import urlopen

# Specify URL appended with source and API key
# Modify this section later for more sources
url = 'https://newsapi.org/v1/articles?apiKey=30a1f0a5d59b4267a08eadae0ee64508&source=the-hindu&sortBy=top'

# Get the JSON dataset
response = urlopen(url)

# Convert bytes to string, then string to dict
string = response.read().decode('utf-8')
json_obj = json.loads(string)

# Print the title from the json_obj
# Later, redirect to storage
for set in json_obj['articles']:
	print(set['title'])
