import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import sentiwordnet as swn
from nltk.stem import WordNetLemmatizer

from additional import Dict # use the dictionary


def pos_to_senti_tag(tag_from_POS):
    if tag_from_POS in ("NN", "NNS", "NNP", "NNPS", "CC"):
        return "n"  # noun
    if tag_from_POS in ("VB", "VBD", "VBG", "VBN", "VBP", "VBZ"):
        return "v"  # verb
    if tag_from_POS in ("JJ", "JJR", "JJS", "DT"):
        return "a"  # adjective
    if tag_from_POS in ("RB", "RBR", "RBS"):
        return "r"  # adverb


def ignore_word(tag):
    neutral_tags = ["CD", "IN", "(", ")", ",", "--", ".", ":", "LS", "''","TO"]
    return tag in neutral_tags


def cleanHeadlineString(headline):
    headline = headline.replace("'s", "")
    headline = headline.replace(":", "")
    headline = headline.replace("-", " ")
    headline = headline.replace("'", "")
    headline = headline.replace(",", "")
    headline = headline.replace("?", "")
    headline = headline.replace(";", "")
    return headline.lower()


def analyze(file):
    outputFile = file[:-4] + "scores.txt"
    with open(file, mode="r") as data:
        with open(outputFile, "w") as f: # Open once in write more to remove previous data
            pass
        with open(outputFile, "a") as f: # open file once to append data for each headline
            for headline in data:
                if len(headline) > 120: # Skip Huge Headlines
                    continue

                # remove special characters & make it lower case
                headline_to_analyze = cleanHeadlineString(headline)

                # Convert headline sentence to a list of words
                words = word_tokenize(headline_to_analyze)

                # Tag each word in list with POS tagger
                tagged_words = nltk.pos_tag(words)

                # Initialize Lemmatizer
                w_lem = WordNetLemmatizer()

                pos_score = 0
                neg_score = 0
                # obj_score = 0

                for i in tagged_words:
                    senti_tag = pos_tag = i[1]

                    # Check if word creates no opinion, else tag them properly
                    # nltk.help.upenn_tagset()
                    if ignore_word(senti_tag):
                        continue
                    else:
                        senti_tag = pos_to_senti_tag(i[1])

                    # Lemmatize the word according to its tag
                    # make argument 2 accurate
                    try:
                        lem_word = w_lem.lemmatize(i[0], senti_tag)
                    except:
                        lem_word = i[0]

                    # Lookup in additional dictionary
                    if i[0] in Dict:
                        score = float(Dict[i[0]])
                        if score < 0:
                            neg_score += score
                            continue
                        else:
                            pos_score += score
                            continue

                    # print(lem_word," ", senti_tag)
                    # Get the numerical equivalent sentiwordnet score
                    # work on argument 3
                    try:
                        breakdown = swn.senti_synset(lem_word + "." + senti_tag + "." + "01")
                        # print(breakdown)
                    except:
                        # sentiword lookup failed
                        continue

                    pos_score += breakdown.pos_score()
                    neg_score += breakdown.neg_score()
                    # obj_score += breakdown.obj_score()

                # print("P=", pos_score, end="")
                # print("    |    N=", neg_score)
                if neg_score > 0:
                    neg_score = -neg_score

                f.write(headline + ">> " + str(pos_score + neg_score) + "\n")
                # f.write("  >P="+str(pos_score)+"  >N="+str(neg_score)+"\n")

    return outputFile


analyze("./data/timesOfIndia/2017-03-28/2017-03-28.txt")