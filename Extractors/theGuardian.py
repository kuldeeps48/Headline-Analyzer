##########
#
# theGuardian.py
# By Aadarsha Shrestha (aadarsha.shrestha.nepal@gmail.com, aadarsha@tutanota.com)
#
# Returns the headlines from The Guardian of the current day
# API: http://open-platform.theguardian.com
#
# 
# Restrictions:	
#		Up to 12 calls per second
#		Up to 5,000 calls per day
#		Access to article text
#
# Date: 11-03-2017
#
##########

#!/usr/bin/python3
import datetime, os, time, requests
from Extractors.apiKeys import code

source_code = "theGuardian"

# Headline extractor for The Guardian
# Returns headlines list
def extractor(headlines):
    # Assign URL and payload
    cur_date = time.strftime("%Y-%m-%d")
    payload = {'from-date': cur_date,
               'to-date': cur_date,
               'api-key': code['theGuardian'],
               'use-date': 'published',
               'page-size': '200',
               'page': '1'
               }
    base_url = 'http://content.guardianapis.com/search'

    # Get JSON object
    response = requests.get(base_url, params = payload)
    json_data = response.json()

    # Extract headlines from JSON object
    for single_news in json_data['response']['results']:
        headlines.append(single_news['webTitle'])

    return headlines


# Module to be called from extractorRunner.py
# Returns file populated with news headlines
def scrapper():
    # Initialize headlines list
    headlines = []

    extractor(headlines)

    # Compute file path
    today = str(datetime.date.today())

    directory = "./data/" + source_code + "/" + today
    if not os.path.exists(directory):
        os.makedirs(directory)

    file = directory + "/" + today + ".txt"

    # Write in file
    with open(file, "w") as tf:
        for headline in headlines:
            try:
                tf.write(headline + "\n")
            except:
                pass

    return file

# scrapper()