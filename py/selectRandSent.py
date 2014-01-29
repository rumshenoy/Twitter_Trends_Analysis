import random
import sys
from InsertAtRandPos import *

def usage():
    print 'Usage:python selectRandSent.py wordToSub NoOfLines'

if len(sys.argv) < 3 or len(sys.argv) > 4:
    usage()
    exit()
filename = sys.argv[3]


word = sys.argv[1]
newSentences = []
lines = int(sys.argv[2])
while(lines >= 1):
    sentences = list(open(filename))
    sentence = random.choice(sentences)
    #ix = sentences.index(sentence)
    sentence = InsertAtRandPos(word,1,sentence)
    #sentences.insert(ix,sentence)
    newSentences.insert(0,sentence)
    #print sentence
    lines = lines-1

f = open('tune.txt','w')
for sentence in newSentences:
    f.write(sentence)
    
