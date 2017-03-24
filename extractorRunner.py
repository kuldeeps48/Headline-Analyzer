import analyzer
import time

from Extractors.googleNews import googleScrapper
from Extractors.redditNews import redditScrapper
from Extractors.redditWorldNews import redditWorldScrapper
from Extractors.theGuardian import scrapper as guardianScrapper
from Extractors.nyTimes import scrapper as nyTimesScrapper
from Extractors.timesOfIndia import scrapper as toiScrapper
from Extractors.cnn import scrapper as cnnScrapper
from Extractors.telegraph import scrapper as telegraphScrapper
from Extractors.theHindu import scrapper as hinduScrapper

"""Names to use in source_functions when adding remaining scrappers
    These will insure proper calling from MainUI:-

     "bbc"
"""
source_functions = {"google news": googleScrapper, "reddit news": redditScrapper,
                    "reddit world news": redditWorldScrapper,
                    "guardian": guardianScrapper, "new york times": nyTimesScrapper,
                    "times of india": toiScrapper, "cnn": cnnScrapper, "telegraph": telegraphScrapper,
                    "the hindu": hinduScrapper}


def runScrapper(source, e, queue):  # Button press function
    if source in source_functions:
        print("Started ", source, " Extraction")
        fileToAnalyze = source_functions[source]()
        print("Finished extraction")
        e.set()  # Done extraction
        time.sleep(0.4)  # To ensure progress bar shows done
        e.clear()  # reset flag
        print("Calling Analyzer on file ", fileToAnalyze)
        output_file = analyzer.analyze(fileToAnalyze)
        time.sleep(0.2)
        e.set()  # Done analysis
        queue.put(output_file)
        print("Done Analysis")

    else:
        # Custom Headline
        output_file = analyzer.analyze(source)  # Analyze custom headline file
        e.set()  # Done analysis
        queue.put(output_file)
