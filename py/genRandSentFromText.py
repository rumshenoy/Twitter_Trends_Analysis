import markovgenpy
import codecs
import sys
import nltk

def generateRandom(filename):
    #file_ = open("jeeves.txt")
    #file_ = codecs.open("firefox.txt", "r", "utf-8")
    file_ = open(filename)
    #markov = markovgenpy.Markov(file_)
    #sentence = markov.generate_markov_text()
    #file_ = codecs.open(filename,'rb','utf-8')
    #file_ = open("firefox.txt")
    markov = markovgenpy.Markov(file_)
    sentence = markov.generate_markov_text()
    return sentence




if len(sys.argv) < 2:
    print "Please specify a number as input."
    exit()

n = int(sys.argv[1])

if(n==0):
    print "Invalid Input. Please enter some number greater than 0."
    exit()
filename = sys.argv[2]
if(filename == None):
    print "Invalid filename"


f = codecs.open("tweets.txt",'wb','utf-8-sig')
#f = open("tweets.txt")
while(n>0):
    sentence = generateRandom(filename) 
    print sentence
    f.write(sentence)
    f.write("\n")
    n = n-1

