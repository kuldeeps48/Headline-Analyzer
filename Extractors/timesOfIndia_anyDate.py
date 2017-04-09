##########
#
# timesOfIndia.py
# By Aadarsha Shrestha (aadarsha.shrestha.nepal@gmail.com, aadarsha@tutanota.com)
#
# Returns the current day's headlines from Times Of India
# API: (Webpage extraction)
#
#
#
# Date: 19-03-2017
#
##########

# !/usr/bin/python3
import datetime, os, requests
from lxml import html

SOURCE_CODE = "timesOfIndia"

# Headline extractor
# Returns headlines list
def extractor(headlines_list, url):
    # Retrieve web page
    news_page = requests.get(url)

    # Parse results into tree
    html_tree = html.fromstring(news_page.content)

    # First row headlines
    headlines = html_tree.xpath('//a[1]/text()')
    for i in range(2):
        headlines_list.append(headlines[-39 + i])

    # Second row headlines
    headlines = html_tree.xpath('//a[2]/text()')
    for i in range(2):
        headlines_list.append(headlines[i + 2])

    # Headlines of the rest 50 rows
    for i in range(48):
        headlines = html_tree.xpath('//a[' + str(i + 3) + ']/text()')
        for i in range(2):
            headlines_list.append(headlines[i])



# Module to be called from extractorRunner.py
# Returns file populated with news headlines
def scrapper(y, m, d):
    # Initialize headlines list
    headlines = []
    url = 'http://timesofindia.indiatimes.com/' + y + '/' + m + '/' + d + '/archivelist/year-' + y + ',month-' + m + ',starttime-'

    # Compute file path
    store_date = y + '-' + m + '-' + d

    y = int(y)
    m = int(m)
    d = int(d)

    root_date = datetime.date(2001, 1, 1)
    extract_date = datetime.date(y, m, d)
    result = extract_date - root_date
    day_id = 36892 + result.days # sum of ID of 2001-01-01 and num of days
    url = url + str(day_id) + '.cms'

    extractor(headlines, url)

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

#year = '2016'
#month = '07'
#day = '10'
#scrapper(year, month, day)