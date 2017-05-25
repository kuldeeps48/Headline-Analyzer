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
from Extractors.bbc import scrapper as bbcScrapper

from Extractors.theGuardian_anyDate import scrapper as guardianScrapperDate
from Extractors.nyTimes_anyDate import scrapper as nyTimesScrapperDate
from Extractors.timesOfIndia_anyDate import scrapper as toiScrapperDate

source_functions = {"google news": googleScrapper, "reddit news": redditScrapper,
                    "reddit world news": redditWorldScrapper,
                    "guardian": guardianScrapper, "new york times": nyTimesScrapper,
                    "times of india": toiScrapper, "cnn": cnnScrapper, "telegraph": telegraphScrapper,
                    "the hindu": hinduScrapper, "bbc": bbcScrapper}


def runScrapper(source, e, queue):
    if source in source_functions:
        print("Started ", source, " Extraction")
        fileToAnalyze = source_functions[source]()
        print("Finished extraction")
        # Set sync flag to done
        e.set()
        # To ensure progress bar shows done
        time.sleep(0.4)
        # Reset sync done flag before calling analyzer
        e.clear()
        print("Calling Analyzer on file ", fileToAnalyze)
        output_file = analyzer.analyze(fileToAnalyze)
        # Done analysis, set flag
        e.set()
        # Store the file name where the analyzer stored it's scores
        queue.put(output_file)
        print("Done Analysis")
    else:
        # Custom Headline
        output_file = analyzer.analyze(source)
        e.set()  # Done analysis
        queue.put(output_file)


def runScrapperDate(source, e, queue, year, month, day):
    name_functions = {"guardian": guardianScrapperDate, "new-york-times": nyTimesScrapperDate, "times-of-india": toiScrapperDate}

    if source in name_functions:
        print("Started ", source, " Extraction")
        fileToAnalyze = name_functions[source](str(year), str(month), str(day))
        print("Calling Analyzer on file ", fileToAnalyze)
        output_file = analyzer.analyze(fileToAnalyze)
        e.set()
        queue.put(output_file)
        print("Done Analysis")
    else:
        e.set()
        pass
