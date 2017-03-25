##########
#
# bbc.py
# By Aadarsha Shrestha (aadarsha.shrestha.nepal@gmail.com, aadarsha@tutanota.com)
#
# Returns the current day's headlines from BBC
# API: (RSS) http://www.bbc.com/news/10628494
#
# NOTE:
#  - Update URLs only
#
#
# Date: 25-03-2017
#
##########

# !/usr/bin/python3
import datetime, os, feedparser
SOURCE_CODE = "bbc"


# Headline extractor
# Returns headlines list
def extractor(headlines):
    # URL for RSS feed
    base_url = []
    base_url.append('http://feeds.bbci.co.uk/news/rss.xml?edition=int')  # International
    base_url.append('http://feeds.bbci.co.uk/news/world/asia/rss.xml')  # Asia

    for i in range(2):
        # Parse RSS feed
        feed = feedparser.parse(base_url[i])

        # Append headline to list
        for single_news in feed['entries']:
            headlines.append(single_news["title"])
            # headlines.append(unidecode.unidecode(single_news["title"]))


# Module to be called from extractorRunner.py
# Returns file populated with news headlines
def scrapper():
    # Initialize headlines list
    headlines = []

    extractor(headlines)

    # Compute file path
    today = str(datetime.date.today())

    directory = "./data/" + SOURCE_CODE + '/' + today
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