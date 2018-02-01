import csv
import re

import nltk
import pandas as pd
from nltk.corpus import wordnet as wn, stopwords
import re
import string



# food = wn.synset('food.n.02')
# foodlist1 = list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))

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

def preProcessFood(text):
    text = text.lower()
    words = []
    for word in re.split("_", text)[-1]:
        words.append(word)

    return ''.join(words)


with open('Reviews_preprocessed.csv', 'rb') as f:
    d = {}
    productlist = []
    allproductlist = []
    for row in csv.reader(f):
        userid = row[2]
        productid = row[1]
        allproductlist.append(productid)
        if productid in d.values() and productid not in productlist:
            productlist.append(productid)
        if userid in d:
            d[userid] += ("," + productid)
        else:
            d[userid] = productid


hotproduct = nltk.Counter(allproductlist)
hotproduct = ["B003GTR8IO", "B0090X8IPM","B001EO5Q64","B000KV61FC","B002IEZJMA",
              "B000KV7ZGQ","B002LANN56","B002IEVJRY","B0041NYV8E","B0051COPH6",
              "B0013NUGDE","B007M83302","B000UBD88A","B001RVFEP2","B0026KNQSA",
              "B007M832YY","B004E4CCSQ","B001RVFERK","B006MONQMC","B006HYLW32",
              "B0013A0QXC","B0026KPDG8","B000VK8AVK"]


for key, value in d.items():
    for i in range(0, len(value), 11):
        if len(value) < 12:
            del d[key]
            break
        if value[i:i+10] not in hotproduct:
            del d[key]
            break




print len(hotproduct)
print len(d)
with open('productanduser.csv', 'wb') as f:
    w = csv.writer(f)
    for key in d:
        print d[key]
        w.writerows([[d[key]]])
    # counter = 0
    # # for food in productlist:
    # w.writerows([hotproduct])
    # rowmarker = []
    # for food in hotproduct:
    #     counter += 1
    #     print counter
    #     for key, value in d.items():
    #         if food in value:
    #             rowmarker.append("yes")
    #         else:
    #             rowmarker.append("no")
    # for i in range(0,len(rowmarker), 23):
    #     print i
    #     w.writerows([rowmarker[i:i+23]])







