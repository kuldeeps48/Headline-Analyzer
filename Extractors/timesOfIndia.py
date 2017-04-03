##########
#
# timesOfIndia.py
# By Aadarsha Shrestha (aadarsha.shrestha.nepal@gmail.com, aadarsha@tutanota.com)
#
# Returns the current day's headlines from Times Of India
# API: (RSS) http://timesofindia.indiatimes.com/rss.cms
#
# NOTE:
#  - url_formatter(), extractor() are to be changed according to need
#  - Do not change the modules: get_json(), scrapper()
#
#
# Date: 19-03-2017
#
##########

# !/usr/bin/python3
import datetime, os, requests
from Extractors.apiKeys import code

SOURCE_CODE = "timesOfIndia"

'''
# Formats the Request
# Returns base URL
def url_formatter():
    cur_date = time.strftime("%Y%m%d")
    api_key = code['']
    url = '' + cur_date + '' + cur_date + '&api-key=' + api_key
    return url
'''

# Fetches JSON data and parses it
# Returns JSON object
def get_json(url):
    response = requests.get(url)
    json_data = response.json()
    return json_data

# Headline extractor
# Returns headlines list
def extractor(headlines):
    # URL for RSS feed
    base_url = []
    base_url.append('http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms?feedtype=json') # National
    base_url.append('http://timesofindia.indiatimes.com/rssfeeds/296589292.cms?feedtype=json') # World
    base_url.append('http://timesofindia.indiatimes.com/rssfeeds/-2128833038.cms?feedtype=json') # Bangalore

    for i in range(3):
        # Fetch JSON data and refine the data
        json_data = get_json(base_url[i])
        news = json_data['channel']['item']

        # Append headline to list
        for single_news in news:
            headlines.append(single_news['title'])


# Module to be called from extractorRunner.py
# Returns file populated with news headlines
def scrapper():
    # Initialize headlines list
    headlines = []

    extractor(headlines)

    # Compute file path
    today = str(datetime.date.today())

    directory = "./data/" + SOURCE_CODE + "/" + today
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