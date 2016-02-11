import json
import csv
import io
import pandas as pd
import sys
import numpy as np
import nltk
import re
from bs4 import BeautifulSoup
from nltk.tokenize import TweetTokenizer



def jsonUTF8toCsv(inputFile,outputFile):

    data_json = io.open(inputFile, mode='r', encoding='utf-8').read() #reads in the JSON file
    data_python = json.loads(data_json)

    csv_out = io.open(outputFile, mode='w', encoding='utf-8') #opens csv file


    fields = u'created_at,text,screen_name,followers,friends,rt,fav' #field names
    csv_out.write(fields)
    csv_out.write(u'\n')

    for line in data_python:

        #writes a row and gets the fields from the json object
        #screen_name and followers/friends are found on the second level hence two get methods
        row = [line.get('created_at'),
               '"' + line.get('text').replace('"','""') + '"', #creates double quotes
               line.get('user').get('screen_name'),
               unicode(line.get('user').get('followers_count')),
               unicode(line.get('user').get('friends_count')),
               unicode(line.get('retweet_count')),
               unicode(line.get('favorite_count'))]

        row_joined = u','.join(row)
        csv_out.write(row_joined)
        csv_out.write(u'\n')

    csv_out.close()


def jsonASCIItoCsv(inputFile,outputFile):
    data_json = open(inputFile, mode='r').read() #reads in the JSON file into Python as a string
    data_python = json.loads(data_json) #turns the string into a json Python object

    csv_out = open(outputFile, mode='w') #opens csv file
    writer = csv.writer(csv_out) #create the csv writer object

    fields = ['created_at', 'text', 'screen_name', 'followers', 'friends', 'rt', 'fav'] #field names
    writer.writerow(fields) #writes field

    for line in data_python:

        #writes a row and gets the fields from the json object
        #screen_name and followers/friends are found on the second level hence two get methods
        writer.writerow([line.get('created_at'),
                         line.get('text').encode('unicode_escape'), #unicode escape to fix emoji issue
                         line.get('user').get('screen_name'),
                         line.get('user').get('followers_count'),
                         line.get('user').get('friends_count'),
                         line.get('retweet_count'),
                         line.get('favorite_count')])

    csv_out.close()



def csvToPandasDF(inputCSV):
    df = pd.read_csv(inputCSV)
    return df

class Tweet(object):

    def __init__(self,created_at=None,text=None,screen_name=None,followers=None,friends=None,rt=None,fav=None,pandaRow=None,tweetID=None):
        self.created_at = created_at
        self.text = text
        self.screen_name = screen_name
        self.followers = followers
        self.friends = friends
        self.rt = rt
        self.fav = fav
        self.pandaRow = pandaRow
        self.tweetID = tweetID

    def get_time(self, pandaRow=None, tweetID=None):
        return self.created_at

    def get_text(self, pandaRow=None, tweetID=None):
        return self.text


# method will return an array[] for length(keyword_list). if the keyword
# appears in the text, then the value will be the index in the text
# otherwise it will be -1 showing that the text did not contain the value
def identifySubject(text, keyword_list):

    keywords = keyword_list[0].replace(',', '').split()

    keyword_array = np.zeros(len(keywords))

    count = 0
    #print len(keywords)
    for keyword in keywords:
        #print count
        #print keyword
        keyword_array[count] = text.find(keyword)
        count += 1

    return

# clean tweet of username and urls
# tokenize tweet by word
# remove stop words... still deciding if this will be neccesary or not but will try both ways
def cleanTweetandTokenize(text, remove_stopwords=False):

    tknzr = TweetTokenizer()

    clean_text = BeautifulSoup(text, 'lxml').get_text()
    #clean_text = BeautifulSoup(text).get_text()
    #cleaner_text = re.sub()
    clean_token = str(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",clean_text).split()))
    #line from http://stackoverflow.com/questions/8376691/how-to-remove-hashtag-user-link-of-a-tweet-using-regular-expression
    #not sure how to preserve hashtag

    clean_token = tknzr.tokenize(clean_token)

    if remove_stopwords:
            stops = set(nltk.corpus.stopwords.words("english"))
            words = clean_token
            clean_token = [w for w in words if not w in stops]

    return clean_token


def findRetweet(text):
    pass















