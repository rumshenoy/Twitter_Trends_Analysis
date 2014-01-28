import random
import string



def InsertAtRandPos(word,times,sentence):
    strArr = string.split(sentence,' ')
    i = 0
    while(i < times): 
        words = len(strArr)
        pos = random.randrange(0,words,1) 
        if (pos < words):
            j = words
            while(j > (words-pos)): 
                strArr.insert(j,strArr.pop(j-1)) 
                j= j-1;
        strArr.insert(pos,word)
        i= i+1
    return ' '.join(strArr)  


