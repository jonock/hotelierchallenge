import os                              #to assist csv-import
import pandas as pd                    #to read csv-import
import time                            #to measure how long processes take

import re                              #to use regular expressions to clean data if needed
from pprint import pprint              #pretty print

import numpy as np                     #for mathematical calculations

import matplotlib                      #python plotting library

import matplotlib.pyplot as plt        #matplot for donut charts

import sklearn                                    #scikit learn
import mglearn                                    #for plotting purposes
from sklearn.preprocessing import LabelEncoder    #encode the labels pos, neg, neut into numbers
from sklearn.feature_extraction.text import CountVectorizer    #featureextraction, features aus Texten extrahieren
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression

import string

import time

# Multiprocessing: to be able to use all available cores
import multiprocessing
NUM_JOBS = multiprocessing.cpu_count() -1

start = time.time()

#User Input
enter_text = input('Please enter a swiss german text: ')
type_enter_text =type(enter_text)

try:
    int(enter_text)
    print('-'*50)
    print('Warning: Please make sure to enter text, not numbers. Thanks!')
except:
    print('-'*50)
    enter_text = "".join([word.lower() for word in enter_text if word not in string.punctuation])
    print('Checking sentiment for:', enter_text)


text = pd.read_csv('data/HateSpeechDetectionLR.csv', sep=',')  #csv import
text.drop('Dialekt', axis=1, inplace=True)
text.drop(text.loc[text['Sentiment'] == 'neut'].index, inplace=True)

def clean_text(text):
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    return text

text['new_text'] = text['Text'].apply(lambda x: clean_text(x))

lbl_enc = LabelEncoder()

labels = text ['Sentiment'].tolist()
full_text = text ['new_text'].tolist()
lbl_enc.fit(sorted(labels))
enc_label = lbl_enc.transform(labels)

vect = CountVectorizer().fit(full_text)
vect_text = vect.transform(full_text)

from sklearn.linear_model import LogisticRegression

logisticRegr = LogisticRegression(C=10.0, solver='lbfgs', n_jobs=-1)
lr_model_full = logisticRegr.fit(vect_text, enc_label)

d = {'sentence': [1],'text_to_check': enter_text}
df = pd.DataFrame(d)
df

user_text = df['text_to_check'].tolist()
vectorized_text = vect.transform(user_text)
predict_test = lr_model_full.predict(vectorized_text).tolist()
n = -1
for x in predict_test:
    n +=1
    pred = lbl_enc.inverse_transform([x])
    for i in pred:
        print('The prediction of sentence', n,'is:', str(i))

end = time.time()
time_result = (end - start)
print('Seconds to run the Logistic Regression: ', round(time_result,2))
