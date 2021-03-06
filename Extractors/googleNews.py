import os
from lxml import html
import requests
import datetime

def googleScrapper():

    today = str(datetime.date.today())

    directory = './data/googleNews/' + today
    if not os.path.exists(directory):
        os.makedirs(directory)

    file = directory + '/' + today + ".txt"

    # Send request to get the web page
    response = requests.get('https://news.google.co.in/')

    # Check if the request succeeded (response code 200)
    if (response.status_code == 200):

        # Parse the html from the webpage
        pagehtml = html.fromstring(response.text)

        # search for news headlines
        news = pagehtml.xpath('//h2[@class="esc-lead-article-title"] \
                          /a/span[@class="titletext"]/text()')

        with open(file, "w") as f:
            try:
                f.write("\n".join(news))
            except UnicodeEncodeError:
                pass

    return file

