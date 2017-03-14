import analyzer
import subprocess

from Extractors.googleNews import googleScrapper
from Extractors.redditNews import redditScrapper
from Extractors.redditWorldNews import redditWorldScrapper
from Extractors.theGuardian import scrapper as guardianScrapper
from Extractors.nyTimes import scrapper as nyTimesScrapper


source_functions = {"google news":googleScrapper, "reddit news":redditScrapper, "reddit world news":redditWorldScrapper,
                    "guardian":guardianScrapper, "new york times":nyTimesScrapper}

def runScrapper(source):  # Button press function
    if source in source_functions:
        subprocess.Popen("python ./ui/progress.py ", shell=True)
        print("Starting ", source," Extraction")

        fileToAnalyze = source_functions[source]()

        print("Finished extraction")
        print("Calling Analyzer on file ", fileToAnalyze)
        analyzer.analyze(fileToAnalyze)

    else: # Custom Headline
        analyzer.analyze(source) # Analyze custom headline file

