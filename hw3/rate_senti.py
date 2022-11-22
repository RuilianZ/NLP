#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 14:53:57 2022

@author: roxy
"""
 
import numpy as np
import pandas as pd
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import warnings
from utils import *
warnings.filterwarnings('ignore')

# import data
pos = open("/Users/roxy/Desktop/NLP/hw/hw3/data/positive-words.txt", "r")
pos_all = pos.readlines()
pos_list = []
for word in pos_all:
    pos_list.append(word.replace("\n", ""))

neg = open("/Users/roxy/Desktop/NLP/hw/hw3/data/negative-words.txt", "r", encoding = "ISO-8859-1")
neg_all = neg.readlines()
neg_list = []
for word in neg_all:
    neg_list.append(word.replace("\n", ""))


# create a function that tokenize inout text
# and compares each token with defined positive and negative words list
# returns a score
# the text without defined positive and negative words are ignored
def gen_senti(text):
    token = re.sub("[^A-Za-z]+", " ", text.lower()).split()
    pos_count = 0
    neg_count = 0
    for word in token:
        if word in pos_list:
            pos_count += 1
        elif word in neg_list:
            neg_count += 1
    if pos_count + neg_count == 0:
        return None
    return (pos_count - neg_count) / (pos_count + neg_count)
    
# get the corpuses data
path = ("/Users/roxy/Desktop/NLP/corpuses")
the_data = file_reader(path)

# apply gen_senti to the courpuses data and add a column called "simple_senti"
the_data["simple_senti"] = the_data.body.apply(gen_senti)

# use vaderSentiment, apply the “compound” value of sentiment for each corpus
# on a new column of the_data called “vader” 

analyzer = SentimentIntensityAnalyzer()
# create a function applying SentimentIntensityAnalyzer to data
def get_compound_senti(text):
    token = re.sub("[^A-Za-z]+", " ", text.lower())
    return analyzer.polarity_scores(token)['compound']

the_data['vader'] = the_data['body'].apply(get_compound_senti)

# count the mean, median and standard_deviations of both sentiment measures
# “simple_senti” and “vader”
statistics = the_data.agg(['mean', 'median', 'std'])
print(statistics)



