##########
#
# theGuardian.py
# By Aadarsha Shrestha (aadarsha.shrestha.nepal@gmail.com, aadarsha@tutanota.com)
#
# Returns the headlines from The Guardian of the current day
# API: http://open-platform.theguardian.com
# 
# NOTE:
#  - url_formatter(), extractor() are to be changed according to need
#  - Do not change the modules: get_json(), scrapper()
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


# Formats the Request
def url_formatter():
    cur_date = time.strftime("%Y-%m-%d")
    api_key = code['theGuardian']
    use_date = 'published'
    url = 'http://content.guardianapis.com/search?from-date=' + cur_date + '&to-date=' + cur_date + '&api-key=' + api_key + '&use-date=' + use_date
    return url


# Fetches JSON data and parses it
# Returns JSON object
def get_json(url):
    response = requests.get(url)
    json_data = response.json()
    return json_data


# Headline extractor for The Guardian
# Returns headlines list
def extractor(headlines):
    base_url = url_formatter()

    # Fetch JSON data and compute the total number of news articles
    json_data = get_json(base_url)

    total = json_data['response']['total']
    page_no = 1

    # Return news headlines
    while True:
        url = base_url + '&page-size=200' + '&page=' + str(page_no)
        json_data = get_json(url)

        for single_news in json_data['response']['results']:
            headlines.append(single_news['webTitle'])

        total -= 200
        page_no += 1
        if total <= 0:
            break
        
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