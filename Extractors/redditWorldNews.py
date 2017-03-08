import os
import praw
import prawcore
import datetime

reddit = praw.Reddit(client_id = 'rDXE3HaRccdKYw',
                     client_secret = 'ZbYtPc8f3vLfFWqdF_NVsi98ZY4',
                     user_agent = 'Headline Extractor (by /u/aPerson_)')

today = str(datetime.date.today())

directory = "..\data\\redditWorldNews\\" + today
if not os.path.exists(directory):
    os.makedirs(directory)

file = directory + "\\" + today + ".txt"

if reddit.read_only:
    with open(file, "w") as file:
        try:
            for submission in reddit.subreddit('worldnews').hot():
                try:
                    file.write(submission.title + "\n")
                except UnicodeEncodeError:
                    continue
        except prawcore.exceptions.RequestException:
            print("Wait for some time and request again. Max tries exceeded")