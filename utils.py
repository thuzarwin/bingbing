from __future__ import division
import math
import nltk
import numpy

data = [
    "71 Homes for Sale in Gates, NC. Browse photos, see new properties, get open house info, and research neighborhoods on Trulia.",
    "melinda gates As a dad, I work to protect my kids ... letter from bill and melinda gates Read the philosophy behind the philanthropy.",
    "Gates Buick GMC Nissan of North Windham is here to serve Mansfield, Hartford and Connecticut customers for new and used car financing, auto parts, and service",
    "Gates Corporation is Powering Progress  in the Oil & Gas, Energy, Mining, Marine, Agriculture, Transportation and Automotive Industries.",
    "Product Description... Walk through Gate is 41 height ... down around the house and on the ...",
    "Outdoor | Garden Center | Gates ... You may optionally choose to filter your warehouse selection by selecting one or more of the below services.",
    "Horatio Lloyd Gates (July 26, 1727  April 10, 1806) was a retired British soldier who served as an American general during the Revolutionary War.",
    "Bloom & Breathe by Gates You Are All You Have Left To Fear by gates The Sun Will Rise and Lead Me Home by gates gates we are a band from new brunswick, NJ",
    "Minneapolis, you are two for two in our book. Such a rad city! We are in Ferndale, MI tonight at The Loving Touch. Doors at 8pm, music at 8:30.",
    "Gates Corporation is Powering Progress in the Oil & Gas, Energy, Mining, Marine, Agriculture, Transportation and Automotive Industries."
]

class Corpora:
    def __init__(self, corpora):
        self.corpora = corpora
        self.docCount = len(corpora)
        self.documents = self._parseDocuments(corpora)
        self.bagOfWords = self._constructVocab(self.documents)

    def __repr__(self):
        return "Corpora with %d documents, %d words" % \
                (self.docCount, len(self.bagOfWords))

    def _parseDocuments(self, corpora):
        return [nltk.Text([w.lower() for w in nltk.word_tokenize(doc)]) \
                for doc in corpora]

    def _constructVocab(self, documents):
        words = set()
        for d in documents:
            words.update([w for w in d if w.isalpha()])
        return words

    def tfidf(self, term, doc, documents):
        tf = doc.count(term)
        df = sum([1 for doc in documents if term in set(doc)])
        idf = math.log(len(documents) / df) if df else 0
        return tf * idf

    def vectorize(self, doc):
        words = getVocabulary(results)
        return len(words)

corpora = Corpora(data)
print corpora
