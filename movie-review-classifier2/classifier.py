import nltk
import random
import os
import io
import pickle
from nltk.tokenize import TweetTokenizer
from datetime import datetime
from nltk.classify import ClassifierI
from statistics import mode

class VoteClassifier(ClassifierI):
    def __init__(self,*classifiers):
        self._classifiers = classifiers
        
    def classify(self,features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)
    def confidence(self,features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return votes.count(mode(votes))/len(list)

word_pickle = open("word_list.pickle","rb")
red_word_pickle = pickle.load(word_pickle)
word_pickle.close()

def make_feature(document):
    tknrsr = TweetTokenizer()
    words = tknrsr.tokenize(document)
    document = []
    for w in words:
        document.append(w.lower())
    words = set(document)
    features = {}
    for w in red_word_pickle:
        features[w] = (w in words)
    return features

save_naivebayes = open("MNB.pickle","rb")
MNB_classifier = pickle.load( save_naivebayes)
save_naivebayes.close()

save_naivebayes = open("BNB_classifier.pickle","rb")
BNB_classifier = pickle.load( save_naivebayes)
save_naivebayes.close()

save_naivebayes = open("naive_bayes.pickle","rb")
naiveBayes_classifier = pickle.load(save_naivebayes)
save_naivebayes.close()

save_naivebayes = open("LG_classifier.pickle","rb")
LG_classifier = pickle.load( save_naivebayes)
save_naivebayes.close()

save_naivebayes = open("SGD_classifier.pickle","rb")
SGD_classifier = pickle.load( save_naivebayes)
save_naivebayes.close()

save_naivebayes = open("SVC_classifier.pickle","rb")
SVC_classifier = pickle.load( save_naivebayes)
save_naivebayes.close()

save_naivebayes = open("LinearSVC_C.pickle","rb")
LinearSVC_C= pickle.load( save_naivebayes)
save_naivebayes.close()

vote_classifier = VoteClassifier(MNB_classifier,naiveBayes_classifier,LinearSVC_C,SVC_classifier,SGD_classifier,BNB_classifier)

def classify_it(text):
    ans = vote_classifier.classify(make_feature(text))
    print("it is",ans)
    return