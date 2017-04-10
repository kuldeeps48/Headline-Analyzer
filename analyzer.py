import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import sentiwordnet as swn
from nltk.stem import WordNetLemmatizer

from additional import Dict  # use our own dictionary also


class BidirectionalIterator(object):  # Custom 2 direction iterator to read word combinations from headlines
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def next(self):
        try:
            self.index += 1
            result = self.collection[self.index]
        except IndexError:
            raise StopIteration
        return result

    def prev(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.collection[self.index]

    def curr(self):
        return self.collection[self.index]

    def __iter__(self):
        return self


# Function which changes POS tagger tags to SentiWordNet tags
def pos_to_senti_tag(tag_from_POS):
    if tag_from_POS in ("NN", "NNS", "NNP", "NNPS", "CC"):
        return "n"  # noun
    if tag_from_POS in ("VB", "VBD", "VBG", "VBN", "VBP", "VBZ"):
        return "v"  # verb
    if tag_from_POS in ("JJ", "JJR", "JJS", "DT"):
        return "a"  # adjective
    if tag_from_POS in ("RB", "RBR", "RBS"):
        return "r"  # adverb


# Words which has these tags and not useful
def ignore_word(tag):
    neutral_tags = ["CD", "IN", "(", ")", ",", "--", ".", ":", "LS", "''", "TO"]
    return tag in neutral_tags


# Remove special characters from headline and return it in lower case form
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
    # Set file name where we will store our headlines + scores
    outputFile = file[:-4] + "scores.txt"

    with open(file, mode="r") as data:
        # Open our output ile once in write more to remove previous data
        with open(outputFile, "w") as f:
            pass
        # Again open, but in append mode to store headlines + scores
        with open(outputFile, "a") as f:
            for headline in data:
                if len(headline) > 120 or len(headline) < 15:  # Skip small and large strings
                    continue

                # remove special characters & make it lower case
                headline_to_analyze = cleanHeadlineString(headline)

                # Convert headline sentence to a list of words
                words = word_tokenize(headline_to_analyze)

                pos_score = 0
                neg_score = 0

                # Two words combo lookup
                two_combo_lookup = BidirectionalIterator(list(words))  # passing a copy of list
                while True:
                    try:
                        a = two_combo_lookup.curr()
                        a_index = two_combo_lookup.index  # Store index to remove the word
                        b = two_combo_lookup.next()
                        b_index = two_combo_lookup.index
                        combo = a + " " + b
                        if combo in Dict:
                            words[a_index] = ""  # Make word blank, remove later so that indexes don't screw up
                            words[b_index] = ""
                            score = float(Dict[combo])
                            if score < 0:
                                neg_score += score
                            else:
                                pos_score += score
                    except StopIteration:
                        break

                words[:] = (item for item in words if item != "")  # Remove all blank words

                # Three words combo lookup
                three_combo_lookup = BidirectionalIterator(list(words))
                while True:
                    try:
                        a = three_combo_lookup.curr()
                        a_index = three_combo_lookup.index
                        b = three_combo_lookup.next()
                        b_index = three_combo_lookup.index
                        c = three_combo_lookup.next()
                        c_index = three_combo_lookup.index
                        combo = a + " " + b + " " + c
                        if combo in Dict:
                            words[a_index] = ""
                            words[b_index] = ""
                            words[c_index] = ""
                            score = float(Dict[combo])
                            if score < 0:
                                neg_score += score
                            else:
                                pos_score += score

                        three_combo_lookup.prev()
                    except StopIteration:
                        break

                words[:] = (item for item in words if item != "")  # Remove all blank words

                # Pass remaining words to sentiwordnet
                # Tag each word in list with POS tagger
                tagged_words = nltk.pos_tag(words)

                for i in tagged_words:
                    senti_tag = i[1]
                    # Check if word creates no opinion, else tag them in sentiwordnet format. See nltk.help.upenn_tagset() for tags info
                    if ignore_word(senti_tag):
                        continue
                    else:
                        senti_tag = pos_to_senti_tag(i[1])

                    # Initialize Lemmatizer
                    w_lem = WordNetLemmatizer()
                    # Lemmatize the word according to its tag
                    try:
                        lem_word = w_lem.lemmatize(i[0], senti_tag)
                    except:
                        lem_word = i[0]

                    # Single Lookup in additional dictionary
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
