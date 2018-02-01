# -*- coding: utf-8 -*-
import re
import string
import nltk
import csv
from nltk.corpus import stopwords


def preProcessing(text):
    cachedStopWords = stopwords.words("english")
    stemmer = nltk.stem.WordNetStemmer()
    text = text.strip().lower()
    words = []
    for word in re.split("\s+", text):
        exclude = set(string.punctuation)
        word = ''.join(ch for ch in word if ch not in exclude)
        if word not in cachedStopWords:
            word = stemmer.stem(word)
            words.append(word)
    return ' '.join(words)


with open('winemag-data_first150k_remove.csv', 'rb') as inp,  open('wine_stem.csv', 'wb') as out:
    data = csv.reader(inp)
    writer = csv.writer(out)
    counter = 0
    for row in data:
        list = []
        counter += 1
        for col in row:
            list.append(preProcessing(col))
        writer.writerow(list)
        print counter




