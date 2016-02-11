import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import io
import sys
import os
import json
from keys import consumer_secret,consumer_key,access_token_secret,access_token
import cleanText


class Listener(StreamListener):

    #def __init__(self, start_time, time_limit=60,inputFile = None):
    def __init__(self, tweet_limit, start_time, time_limit,inputFile = None):   #WHY THE FUCK DOESN'T THIS WORK

        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []
        self.inputFile = inputFile
        self.num_tweets = 0
        self.tweet_limit = tweet_limit

    def on_data(self, data):

        saveFile = io.open('raw_tweets.json', 'a', encoding='utf-8')
        tweet_data = []

        #while (time.time() - self.time) < self.limit:
        #while self.num_tweets < 20:

        while self.num_tweets < self.tweet_limit:

            try:
                #print(self.tweet_data)

                self.tweet_data.append(data.lower()) # for some reason this can only take a string, not sure why it matters
                self.num_tweets += 1
                #print(self.num_tweets)
                return True


            except BaseException, e:
                print('failed ondata,', str(e))
                time.sleep(5)
                return True




        saveFile = io.open('raw_tweets.json', 'w', encoding='utf-8')
        saveFile.write(u'[\n')
        saveFile.write(','.join(self.tweet_data))
        saveFile.write(u'\n]')
        saveFile.close()
        return False

    def on_error(self, status):

        print(status)

    def on_disconnect(self, notice):

        print('bye')

