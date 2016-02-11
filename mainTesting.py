__author__ = 'Alex'
"""
file for testing things before adding them to pipeline
"""

import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import io
import os
import json
from keys import consumer_secret,consumer_key,access_token_secret,access_token
import accessStream
import cleanText
#from main import keyword_list

df = cleanText.csvToPandasDF("tweets_out.csv")

#print df.head(1)
#print df.shape

df.insert(0, 'uID', range(0, df.shape[0]))

#print df.head(4)
#print df.shape

#keyword_list = ['bernie, sanders, hillary, clinton']
keyword_list = ['bernie, sanders, hillary, clinton']
keywords = keyword_list[0].replace(',', '').split()
#keywords = keyword_list[0].replace(',', '').split()
#print keywords

#df['keyword_array'] = None
#print df.shape
#print df.head(4)

textList = df.loc[:, ['text']]




subject_array = []
for i in xrange(len(textList)):
    subject_array.append(cleanText.identifySubject(textList['text'][i], keywords))

#df['subject_array'] = subject_array

#print df.head(5)
keywords= keyword_list[0].replace(',', '').split()

print len(keywords)
