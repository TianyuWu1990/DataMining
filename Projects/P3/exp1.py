import nltk
import re
import string
import csv as csv
import pandas as pd
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# read data set
train = pd.read_csv("Reviews_preprocessed.csv")

# does basic preprocessing of a review DOES NOT do word selection
def review_to_words(raw_review):
    #remove html
    review_text = BeautifulSoup(raw_review).get_text()
    #remove non-alphanumeric characters
    alphanum_only = re.sub("[^a-zA-A0-9]", " ", review_text)
    #the below method turns "we'd" into "wed" this does not seem correct
    #alphanum_only_v2 = raw_review.translate(None, string.punctuation)  
    #convert to lowercase, split into individual words
    words = alphanum_only.lower().split()
    # convert to set
    stops = set(stopwords.words("english"))
    meaningful_words = [w for w in words if not w in stops]
    # do stemming
    snowball_stemmer = SnowballStemmer("english")
    word_stems = [snowball_stemmer.stem(w) for w in meaningful_words]
    # re-string words, space seperated entry
    return(" ".join(word_stems))

# iterates over train["Text"] performing review_to_words and creates a set out of the results
def review_to_set():
    num_reviews = train["Text"].size
    clean_train_reviews =[]
    
    for i in xrange(0, num_reviews):
        if ((i+1)%1000 ==0):
            print "Review %d of %d\n"%(i+1, num_reviews)
        clean_train_reviews.append(review_to_words(train["Text"][i]))
    return clean_train_reviews

# removes quotes from train["ProfileName"] and creates a list of these values
def remove_name_quotes():
    num_reviews = train["ProfileName"].size
    clean_train_names = []
    #delete quote marks
    for i in xrange(0, num_reviews):
        if ((i+1)%1000 == 0):
            print "Name %d of %d\n"%(i+1, num_reviews)
        clean_train_names.append(train["ProfileName"][i].translate(None, string.punctuation))
    return clean_train_names

# runs review_to_set() and remove_name_qutes() and builds a csv from the original data and
# these processed fields.  The summary field is OMITTED since we are not using it.
def output_to_csv():
    clean_reviews = review_to_set()
    clean_names = remove_name_quotes()
    output = pd.DataFrame(data={"Id":train["Id"], "ProductId":train["ProductId"]
                                , "UserId":train["UserId"], "ProfileName":clean_names
                                , "HelpfulnessNumerator":train["HelpfulnessNumerator"]
                                , "HelpfulnessDenominator":train["HelpfulnessDenominator"]
                                , "Score":train["Score"], "Time":train["Time"]
                                , "Text":clean_reviews})
    output.to_csv("simple_preprocessed_reviews.csv", index=False, quoting=csv.QUOTE_NONE, escapechar="/")
    return


output_to_csv()