##########
#
# nyTimes.py
# By Aadarsha Shrestha (aadarsha.shrestha.nepal@gmail.com, aadarsha@tutanota.com)
#
# Returns the headlines from New York Times of the current day
# API: https://developer.nytimes.com/article_search_v2.json
#
# NOTE:
#  - url_formatter(), extractor() are to be changed according to need
#  - Do not change the modules: get_json(), scrapper()
#
# Date: 10-03-2017
#
##########

#!/usr/bin/python3
import datetime, os, time, requests

# Since, it returns too large data, the default number of headlines returned = 100
# PAGE_LIMIT = no_of_headlines / 10 - 1
PAGE_LIMIT = 9


source_code = "nyTimes"


# Formats the Request
def url_formatter():
    cur_date = time.strftime("%Y%m%d")
    api_key = '57502be1c0864fe9a3486459a49634bd'
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=' + cur_date + '&end_date=' + cur_date + '&api-key=' + api_key
    return url


# Fetches JSON data and parses it
# Returns JSON object
def get_json(url):
    response = requests.get(url)
    json_data = response.json()
    return json_data


# Headline extractor for The Guardian
# Returns headlines list
def extractor(url, json_data):
    headlines = []
    total = json_data['response']['meta']['hits']
    page_no = 0
    
    # Go through each 10 headlines
    while True:
        url = url + '&page=' + str(page_no)
        json_data = get_json(url)
        
        for single_news in json_data['response']['docs']:
            headlines.append(single_news['headline']['main'])

    
        total -= 10
        page_no += 1
        if page_no > PAGE_LIMIT:
            break
        
    return headlines


# Module to be called from extractorRunner.py
# Returns file populated with news headlines
def scrapper():
    url = url_formatter()

    # Fetch JSON data and compute the total number of news articles
    json_data = get_json(url)
    
    headlines = extractor(url, json_data)
    
    # Compute file path
    today = str(datetime.date.today())
    
    directory = "./data/" + source_code + "/" + today
    if not os.path.exists(directory):
        os.makedirs(directory)

    file = directory + "/" + today + ".txt"
    
    # Write in file
    with open(file, "w") as tf:
        for headline in headlines:
            tf.write(headline + "\n")

    return file