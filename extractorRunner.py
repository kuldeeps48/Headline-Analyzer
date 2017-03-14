import analyzer
import multiprocessing
from ui.progress import showProgress
import time

from Extractors.googleNews import googleScrapper
from Extractors.redditNews import redditScrapper
from Extractors.redditWorldNews import redditWorldScrapper
from Extractors.theGuardian import scrapper as guardianScrapper
from Extractors.nyTimes import scrapper as nyTimesScrapper

"""Names to use in source_functions when adding remaining scrappers
    These will insure proper calling from MainUI:-

    "times of india", "hindu", "CNN", "telegraph", "bbc"
"""
source_functions = {"google news": googleScrapper, "reddit news": redditScrapper,
                    "reddit world news": redditWorldScrapper,
                    "guardian": guardianScrapper, "new york times": nyTimesScrapper}


def runScrapper(source):  # Button press function
    if source in source_functions:
        e = multiprocessing.Event()
        p = multiprocessing.Process(target=showProgress, args=(e,)).start()
        time.sleep(1)  # To ensure progress dialog is drawn before starting extraction

        print("Starting ", source, " Extraction")
        fileToAnalyze = source_functions[source]()
        print("Finished extraction")
        e.set()  # Done extraction
        # time.sleep(2)  # To ensure progress bar shows done

        e.clear()  # reset flag
        print("Calling Analyzer on file ", fileToAnalyze)
        analyzer.analyze(fileToAnalyze)
        e.set()  # Done analysis
        time.sleep(0.2)

    else:
        # Custom Headline
        analyzer.analyze(source)  # Analyze custom headline file
