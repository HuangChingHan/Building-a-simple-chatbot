# -*- coding: utf-8 -*-
"""
Data : 2019/03/26

This is a chatbot.

"""
# Step 1 : Things we need
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# Things we need for Tensorflow 
import numpy as np
#import tflearn
import tensorflow as tf
import random

# Step 2 : Import our chat-bot intents file
import json
with open('valid.json') as json_data:
    intents = json.load(json_data)  
            
words = []
classes = []
documents = []
# loop through each sentence in our intents patterns
for example in intents:
    for data in example['messages-so-far']:
        print(data['utterance'])


# Step 3 : Create training data
training = []

























