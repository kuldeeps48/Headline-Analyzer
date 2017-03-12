import analyzer
import subprocess

from Extractors.googleNews import googleScrapper
from Extractors.redditNews import redditScrapper
from Extractors.redditWorldNews import redditWorldScrapper
from Extractors.theGuardian import guardianScrapper


source_functions = {"google news":googleScrapper(), "reddit news":redditScrapper(), "reddit world news":redditWorldScrapper(),
                    "guardian":guardianScrapper()}

def runScrapper(source):  # Button press function
    if source in source_functions:
        subprocess.Popen("python ./ui/progress.py")
        print("Starting ", source  ," Extraction")
        fileToAnalyze = source_functions[source]
        if source in ("reddit news", "reddit world news"):
            fileToAnalyze = fileToAnalyze.name
        print("Finished extraction")
        print("Calling Analyzer on file ", fileToAnalyze)
        analyzer.analyze(fileToAnalyze)

    else:
        pass
