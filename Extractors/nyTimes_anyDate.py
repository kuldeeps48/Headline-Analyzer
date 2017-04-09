##########
#
# nyTimes.py
# By Aadarsha Shrestha (aadarsha.shrestha.nepal@gmail.com, aadarsha@tutanota.com)
#
# Returns the headlines from New York Times of the current day
# API: https://developer.nytimes.com/article_search_v2.json
#
#
# Date: 10-03-2017
#
##########

#!/usr/bin/python3
import datetime, os, time, requests
import threading

# Since, it returns too large data, the default number of headlines returned = 100
# PAGE_LIMIT = no_of_headlines / 10 - 1
# PAGE_LIMIT = 9
SOURCE_CODE = "nyTimes"
from Extractors.apiKeys import code


# Multhreading class
class booster(threading.Thread):
    def __init__(self, api_key, headlines, num, extract_date):
        threading.Thread.__init__(self)
        self.api_key = api_key
        self.page_no = num
        self.headlines = headlines
        self.extract_date = extract_date
    def run(self):
        threaded_extractor(self.api_key, self.page_no, self.headlines, self.extract_date)

'''
# Formats the Request
def url_formatter(api_key):
    cur_date = time.strftime("%Y%m%d")
    fl = 'headline'
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=' + cur_date + '&end_date=' + cur_date + '&api-key=' + api_key + '&fl=' + fl
    return url
'''


# Fetches JSON data and parses it
# Returns JSON object
def get_json(url):
    response = requests.get(url)
    json_data = response.json()
    return json_data


# Threaded headline extractor
def threaded_extractor(api_key, page_no, headlines, extract_date):
    # Base URL for each thread, Call to url_formatter() removed for optimized time
    fl = 'headline'
    base_url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=' + extract_date + '&end_date=' + extract_date + '&api-key=' + api_key + '&fl=' + fl
    index = page_no * 10

    # Scrapping headlines for each thread
    for i in range(5):
        # Construct URL and get JSON object
        url = base_url + '&page=' + str(page_no)
        json_data = get_json(url)

        # Store headlines in list
        for single_news in json_data['response']['docs']:
            headlines.insert(index, single_news['headline']['main'])
            index += 1
        page_no += 1


# Headline extractor for The New York Times
def extractor(headlines, extract_date):
    # Create and start threads
    threads = []
    thread1 = booster(code['nyTimes1'], headlines, 0, extract_date)
    thread2 = booster(code['nyTimes2'], headlines, 5, extract_date)

    threads.append(thread1)
    threads.append(thread2)

    thread1.start()
    thread2.start()

    # Wait for termination of all threads before proceeding
    for t in threads:
        t.join()


# Module to be called from extractorRunner.py
# Returns file populated with news headlines
def scrapper(y, m, d):
    # Initialize headlines list
    headlines = []

    extract_date = y + m + d
    extractor(headlines, extract_date)

    # Compute file path
    store_date = y + '-' + m + '-' + d # 2017-04-06

    directory = "./data/" + SOURCE_CODE + "/" + store_date
    if not os.path.exists(directory):
        os.makedirs(directory)

    file = directory + "/" + store_date + ".txt"

    # Write in file
    with open(file, "w") as tf:
        for headline in headlines:
            try:
                tf.write(headline + "\n")
            except:
                pass

    return file

# year = '2016'
# month = '07'
# day = '10'
# scrapper(year, month, day)