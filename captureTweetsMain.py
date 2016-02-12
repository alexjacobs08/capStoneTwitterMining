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
import candidateInfo
from multiprocessing import Process



keyword_list = ['bernie, sanders','trump','hillary, clinton','marco, rubio'] #track list      space is "AND", comma is "OR"
time_limit = 60
tweet_limit = 30



#jsonFile = "raw_tweets.json"
#csv_outFile ="tweets_out.csv"

auth = OAuthHandler(consumer_key, consumer_secret) #OAuth object
auth.set_access_token(access_token, access_token_secret)


canList = []
count = 0
#creates candidate objects
for candidate_name in candidateInfo.candidateList:
    canList.append(candidateInfo.Candidate(candidate_name,keyword_list[count]))
    count+=1


print("start capture")

def startCapture(name, tweet_limit, start_time, time_limit, jsonFile, csv_outFile):

    twitterStream = Stream(auth, accessStream.Listener(tweet_limit, start_time, time_limit, jsonFile))  #WHY THE FUCK DOESN'T THIS WORK
    twitterStream.filter(track=keyword_list)



canCount = 0

processes = []
processes2 = []
for can in canList:

    name = can.getName()
    keywords = can.getKey_words()
    start_time = time.time()
    jsonFile = str(name) + "_raw_tweets.json"
    csv_outFile = str(name) + "_tweets_out.csv"

    processname = str(name) + "_stream"

    processes.append(Process(target = startCapture(name, tweet_limit, start_time, time_limit, jsonFile, csv_outFile)))
    processes2.append(Process(target= cleanText.jsonUTF8toCsv(jsonFile, csv_outFile) ))




    print name
    print keywords
    print jsonFile
    print csv_outFile

processes.start()

living_processes = [p.is_alive() for p in processes]
while living_processes != False:
    print 'done'
    pass

processes2.start()


