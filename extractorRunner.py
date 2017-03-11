import posTagging

from Extractors.googleNews import startScrapping

def runScrapper(source):  # Button press function
    if source == "google news":
        print("Starting Google News Extraction")
        fileToAnalyze = startScrapping()
        print("Finished extraction")
        print("Calling Analyzer on file ", fileToAnalyze)
        posTagging.analyze(fileToAnalyze)

    else:
        pass
