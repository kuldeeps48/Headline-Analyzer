import analyzer
import time

from Extractors.googleNews import googleScrapper
from Extractors.redditNews import redditScrapper
from Extractors.redditWorldNews import redditWorldScrapper
from Extractors.theGuardian import scrapper as guardianScrapper
from Extractors.nyTimes import scrapper as nyTimesScrapper
from Extractors.timesOfIndia import scrapper as toiScrapper

"""Names to use in source_functions when adding remaining scrappers
    These will insure proper calling from MainUI:-

    "times of india", "hindu", "CNN", "telegraph", "bbc"
"""
source_functions = {"google news": googleScrapper, "reddit news": redditScrapper,
                    "reddit world news": redditWorldScrapper,
                    "guardian": guardianScrapper, "new york times": nyTimesScrapper,
                    "times of india":toiScrapper}


def runScrapper(source,e):  # Button press function
    if source in source_functions:
        print("Starting ", source, " Extraction")
        fileToAnalyze = source_functions[source]()
        print("Finished extraction")
        e.set()  # Done extraction
        time.sleep(0.4)  # To ensure progress bar shows done
        e.clear()  # reset flag
        print("Calling Analyzer on file ", fileToAnalyze)
        analyzer.analyze(fileToAnalyze)
        time.sleep(0.2)
        e.set()  # Done analysis

    else:
        # Custom Headline
        analyzer.analyze(source)  # Analyze custom headline file
