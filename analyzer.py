import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import sentiwordnet as swn
from nltk.stem import WordNetLemmatizer

from additional import Dict # use the dictionary

""" TODO:
1) Work on argument 3 of sentiwordnet
3) improve tokens, [WP, POS, PRP$, MD]
2) imporove lemmatiztion
4) imporve tagging
5) add quote detection
6) use additional dictionary
WP - WH-pronoun
"""


def pos_to_senti_tag(tag_from_POS):
    if tag_from_POS in ("NN", "NNS", "NNP", "NNPS", "CC"):
        return "n"  # noun
    if tag_from_POS in ("VB", "VBD", "VBG", "VBN", "VBP", "VBZ"):
        return "v"  # verb
    if tag_from_POS in ("JJ", "JJR", "JJS", "DT"):
        return "a"  # adjective
    if tag_from_POS in ("RB", "RBR", "RBS"):
        return "r"  # adverb

    return "unknown"


def ignore_word(tag):
    neutral_tags = ["CD", "IN", "(", ")", ",", "--", ".", ":", "LS", "''","TO"]
    return tag in neutral_tags


def analyze(file):
    with open(file, mode="r") as data:
        with open('data\output1.txt', "w") as f: # To remove previous data
            pass
        for headline in data:
            print(headline)

            # Convert headline sentence to a list of words
            words = word_tokenize(headline)

            # Tag each word in list with POS tagger
            tagged_words = nltk.pos_tag(words)

            # Initialize Lemmatizer
            w_lem = WordNetLemmatizer()

            pos_score = 0
            neg_score = 0
            obj_score = 0

            for i in tagged_words:
                senti_tag = pos_tag = i[1]

                # modifier scores before analysis since sentiwordnet fails to recognize them properly
                if str.lower(i[0]) in Dict:
                    score = float(Dict[str.lower(i[0])])
                    if score < 0:
                        neg_score += score
                    else:
                        pos_score += score
                    continue

                # Check if word creates no opinion, else tag them properly
                # nltk.help.upenn_tagset()
                if ignore_word(senti_tag):
                    continue
                else:
                    senti_tag = pos_to_senti_tag(i[1])

                if senti_tag == "unknown":
                    continue

                # Lemmatize the word according to its tag
                # make argument 2 accurate
                try:
                    lem_word = w_lem.lemmatize(i[0], senti_tag)
                except:
                    continue

                # print(lem_word," ", senti_tag)
                # Get the numerical equivalent sentiwordnet score
                # work on argument 3
                try:
                    breakdown = swn.senti_synset(lem_word + "." + senti_tag + "." + "01")
                    # print(breakdown)
                except nltk.corpus.reader.wordnet.WordNetError:
                    # print(lem_word," ",senti_tag)
                    continue
                except:
                    continue

                pos_score += breakdown.pos_score()
                neg_score += breakdown.neg_score()
                obj_score += breakdown.obj_score()

            print("P=", pos_score, end="")
            print("    |    N=", neg_score)
            with open('data\output1.txt',"a") as f:
                f.write(headline)
                f.write("  >P="+str(pos_score)+"  >N="+str(neg_score)+"\n")
            print("\n\n")




