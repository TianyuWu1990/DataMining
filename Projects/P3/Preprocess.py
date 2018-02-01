import re
import string
from collections import Counter
import pandas as pd
import nltk
import pandas as pd

import csv

from nltk.corpus import stopwords


def preProcessing(text):
    cachedStopWords = stopwords.words("english")
    stemmer = nltk.stem.SnowballStemmer('english')
    text = text.strip().lower()
    words = []
    for word in re.split("\s+",text):
        exclude = set(string.punctuation)
        word = ''.join(ch for ch in word if ch not in exclude)
        if word not in cachedStopWords:
            word = stemmer.stem(word)
            words.append(word)
    return ' '.join(words)


# with open('Reviews.csv', 'rb') as inp, open('Reviews_preprocessed.csv', 'wb') as out:
#     writer = csv.writer(out)
#     count = 0
#     for row in csv.reader(inp):
#         if count == 0:
#             count += 1
#             writer.writerow(row)
#         else:
#             words = row[9].split()
#             wordcount = len(words)
#             if wordcount >= 100 and wordcount < 110:
#                 count += 1
#                 print wordcount
#                 writer.writerow(row)

with open('Reviews_preprocessed.csv', 'rb') as inp, open('Reviews_preprocessed_stem.csv', 'wb') as out:
    row_counter = 1
    writer = csv.writer(out)
    for row in csv.reader(inp):
        row[9] = preProcessing(row[9])
        writer.writerow(row)

