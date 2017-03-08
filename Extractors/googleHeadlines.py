import os
from lxml import html
import requests
import datetime

today = str(datetime.date.today())

directory = "..\data\\googleNews\\" + today
if not os.path.exists(directory):
    os.makedirs(directory)

file = directory + "\\" + today + ".txt"

# Send request to get the web page
response = requests.get('https://news.google.co.in/')

# Check if the request succeeded (response code 200)
if (response.status_code == 200):

    # Parse the html from the webpage
    pagehtml = html.fromstring(response.text)

    # search for news headlines
    news = pagehtml.xpath('//h2[@class="esc-lead-article-title"] \
                      /a/span[@class="titletext"]/text()')

    with open(file, "w") as tf:
        tf.write("\n".join(news))


