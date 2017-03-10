##########
#
# scrapper.py
# By Aadarsha Shrestha (aadarsha.shrestha.nepal@gmail.com)
#
# Returns the headlines from The Guardian of the current day
# API: http://open-platform.theguardian.com
# Restrictions:	
#		Up to 12 calls per second
#		Up to 5,000 calls per day
#		Access to article text
# Date: 10-03-2017
# Last Modified Date: 10-03-2017
#
##########

import datetime, os, time, requests, json

today = str(datetime.date.today())

directory = "..\data\\theGuardian\\" + today
if not os.path.exists(directory):
    os.makedirs(directory)

file = directory + "\\" + today + ".txt"


# Formats the Request
def guardian_url_formatter():
    cur_date = time.strftime("%Y-%m-%d")
    api_key = '77ed6500-5bea-4fbc-9709-27b6fc6d2d60'
    use_date = 'published'
    url = 'http://content.guardianapis.com/search?from-date=' + cur_date + '&to-date=' + cur_date + '&api-key=' + api_key + '&use-date=' + use_date
    return url


# Fetches JSON data and parses it
def get_json(url):
    # Make request
    response = requests.get(url)

    json_data = response.json()
    return json_data


###########

url = guardian_url_formatter()

# Fetch JSON data and compute the total number of news articles
json_data = get_json(url)
total = json_data['response']['total']
page_no = 1

headlines = []
counter = 0

# Return news headlines
while True:
    url = url + '&page-size=200' + '&page=' + str(page_no)
    json_data = get_json(url)

    for single_news in json_data['response']['results']:
        headlines.append(single_news['webTitle'])
        counter += 1

    total -= 200
    page_no += 1
    if total <= 0:
        break

with open(file, "w") as tf:
    for headline in headlines:
        tf.write(headline)
