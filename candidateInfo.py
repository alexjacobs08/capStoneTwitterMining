

candidateList = ['bernie_sanders','donald_trump','hillary_clinton','marco_rubio']

class Candidate(object):

    def __init__(self,name,key_words):
        self.name = name
        self.key_words = key_words

    def setName(self,name): #name should be first and last with an underscore sperating ex: 'bernie_sanders'
        self.name = name

    #key_words should be a single string of words, space is "AND", comma is "OR"
    # ex: 'bernie, sanders' will capture tweets with the word bernie or the word sanders
    # ex: 'bernie sanders' will capture tweets with the word bernie AND the word sanders
    def setKey_words(self,key_words):

        self.key_words = key_words


    def getName(self):
        return self.name

    def getKey_words(self):
        return self.key_words

