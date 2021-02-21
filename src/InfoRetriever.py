from recycable import *
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import PorterStemmer
import difflib

porter = PorterStemmer()
class InfoRetriever():
    def __init__(self,dict):
        self.__wordDict = []
        self.__numwords = 0
        for words in dict:
            self.__wordDict.append(words)
            self.__numwords+=1

    def findMatching(self,query):
        query.lower()
        counter = [0] * self.__numwords
        n = 0
        for words in self.__wordDict:
            counter[n] = difflib.SequenceMatcher(None, query, words.lower()).ratio()
            n+=1
        m = counter.index(max(counter))

        #print(counter)
        return (self.__wordDict[m], max(counter))

#R = Recyable()
#I = InfoRetriever(R.getRecycables())
#print(I.findMatching("plastic bottle"))

def Sort_Tuple(tup):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    tup.sort(key=lambda x: x[1],reverse = True)
    return tup