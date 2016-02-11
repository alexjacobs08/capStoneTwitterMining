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
import numpy as np
import nltk
import re





#Beginning of the specific code
start_time = time.time() #grabs the system time

keyword_list = ['bernie, sanders'] #track list      space is "AND", comma is "OR"
time_limit = 60
tweet_limit = 1000
inputFile = "raw_tweets.json"
outputFile ="tweets_out.csv"


auth = OAuthHandler(consumer_key, consumer_secret) #OAuth object
auth.set_access_token(access_token, access_token_secret)

print("starting capturing stream")
#twitterStream = Stream(auth, accessStream.Listener(start_time, time_limit,inputFile))
twitterStream = Stream(auth, accessStream.Listener(tweet_limit, start_time, time_limit, inputFile))  #WHY THE FUCK DOESN'T THIS WORK

twitterStream.filter(track=keyword_list)  #call the filter method to run the Stream Listener

print("done capturing stream")
print("cleaning tweets")


cleanText.jsonUTF8toCsv(inputFile, outputFile)
print("tweets cleaned to CSV. CSV created")


cleanDF = cleanText.csvToPandasDF(outputFile)
print("data frame created.")



print("identifying subject of the tweet")

textList = cleanDF.loc[:, ['text']]

subject_array = []
clean_text = []
#keywords = keyword_list[0].replace(',', '').split() this can only be used in one place or only first word comes through.

for i in xrange(len(textList)):

    subject_array.append(cleanText.identifySubject(textList['text'][i], keyword_list))
    clean_text.append(cleanText.cleanTweetandTokenize(textList['text'][i],remove_stopwords=True)) #change to remove stopwords or not


cleanDF['keyword_array'] = subject_array
cleanDF['text'] = clean_text

print cleanDF.shape











