import MySQLdb
import nltk
from nltk.collocations import *
import sys
import codecs
from nltk.corpus import stopwords
from nltk import WordPunctTokenizer
import re
from nltk import FreqDist 
import string

filename = sys.argv[1]
if filename == None :
    print "Invalid File name "
    exit()

woeid= sys.argv[2]
if filename == None :
    print "Invalid woeid "
    exit()

#f = open('/home/ramya/Anasuya/tune.txt','r')
f = open(filename,'r')
data = f.read()

trendfile = open('/home/ramya/Anasuya/trend.txt',mode='w+')

s=set(stopwords.words('english'))

tokens = WordPunctTokenizer().tokenize(data)

punctuation = re.compile(r'[-.?!,":;()|0-9@/\']') 

tokens = [punctuation.sub('', word) for word in tokens] 

word_list2 = [w.strip() for w in tokens if w.strip() not in nltk.corpus.stopwords.words('english') and len(w)>2 ]

word_list2 = filter(None, word_list2)


db = MySQLdb.connect("localhost","root","rumshenoy","nltk_trends" )

cursor = db.cursor()
sql ='delete from topwords where woeid = %d'%(int(woeid))

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
  



filter(lambda w: not w in s,word_list2)

fd = FreqDist(word_list2)

count =0

for token in fd:
    word = token
    fr = fd[token]
    token = token+' '+str(fd[token])
    trendfile.write(token)
    trendfile.write('\n')
    count= count+1
    if count>20:
        break
    sql ='INSERT INTO topwords(woeid,tweet,frequency) VALUES (%d,"%s",%d)'%(int(woeid),word,fr)
   # try:
    cursor.execute(sql)
    db.commit()
    #except:
     #   db.rollback()


'''

bigram_measures = nltk.collocations.BigramAssocMeasures()
word_fd = nltk.FreqDist(word_list2)
bigram_fd = nltk.FreqDist(nltk.bigrams(word_list2))
finder = BigramCollocationFinder(word_fd, bigram_fd)

finder.apply_word_filter(lambda w: w in ('.', ',','@',':','!',"'",'and'))
scored = finder.score_ngrams(bigram_measures.raw_freq)
print sorted(finder.nbest(bigram_measures.raw_freq,2),reverse=True)

'''

db.close()
