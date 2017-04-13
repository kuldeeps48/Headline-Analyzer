##########
#
# nyTimes.py
# By Aadarsha Shrestha (aadarsha.shrestha.nepal@gmail.com, aadarsha@tutanota.com)
#
# Returns the headlines from New York Times of the current day
# API: https://developer.nytimes.com/article_search_v2.json
#
# Date: 10-03-2017
#
##########

# !/usr/bin/python3
import datetime, os, time, requests
import threading

# Since, it returns too large data, the default number of headlines returned = 100
# PAGE_LIMIT = no_of_headlines / 10 - 1
# PAGE_LIMIT = 9
SOURCE_CODE = "nyTimes"
from Extractors.apiKeys import code


# Multhreading class
class booster(threading.Thread):
    def __init__(self, headlines, payload):
        threading.Thread.__init__(self)
        self.payload = payload
        self.headlines = headlines

    def run(self):
        threaded_extractor(self.headlines, self.payload)


# Threaded headline extractor
def threaded_extractor(headlines, payload):
    # Assign base URL
    base_url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'

    # Initialize index of headlines
    # Value at each threaded_extractor is different
    index = int(payload['page']) * 10

    # Scrapping headlines for each thread
    for i in range(5):
        # Get JSON object
        response = requests.get(base_url, params=payload)
        json_data = response.json()

        # Store headlines in list
        for single_news in json_data['response']['docs']:
            headlines.insert(index, single_news['headline']['main'])
            index += 1
        payload['page'] = int(payload['page']) + 1


# Headline extractor for The New York Times
def extractor(headlines):
    # Create and start threads
    threads = []

    # Assign payload
    cur_date = time.strftime("%Y%m%d")
    payload1 = {'begin_date': cur_date,
                'end_date': cur_date,
                'api-key': code['nyTimes1'],
                'fl': 'headline',
                'page': '0'
                }

    payload2 = {'begin_date': cur_date,
                'end_date': cur_date,
                'api-key': code['nyTimes2'],
                'fl': 'headline',
                'page': '5'
                }

    thread1 = booster(headlines, payload1)
    thread2 = booster(headlines, payload2)

    threads.append(thread1)
    threads.append(thread2)

    thread1.start()
    thread2.start()

    # Wait for termination of all threads before proceeding
    for t in threads:
        t.join()


# Module to be called from extractorRunner.py
# Returns file populated with news headlines
def scrapper():
    # Initialize headlines
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
            except UnicodeEncodeError:
                continue
    return file


# scrapper()