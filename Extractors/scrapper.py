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
'''
bbc-news
cnn
independent
reuters
the-guardian-uk
the-hindu
the-new-york-times
the-times-of-india
the-wall-street-journal
'''

import json
from urllib.request import urlopen

# Specify URL appended with source and API key
# Source in the format of newsapi.org
# Modify this section later for user selectable sources
source = input("Please enter headline source: ")
url = 'https://newsapi.org/v1/articles?apiKey=30a1f0a5d59b4267a08eadae0ee64508&sortBy=top&source=' + source

# Get the JSON dataset
response = urlopen(url)

# Convert bytes to string, then string to dict
string = response.read().decode('utf-8')
json_obj = json.loads(string)

# Print the title from the json_obj
# Later, redirect to storage
for single_news in json_obj['articles']:
	print(single_news['title'])
