

# DATA 620 Assignment 12.1
# Written by Paul Stortz
# Last Updated April 4, 2021

# This program splits a text file into different words, then deletes
# punctuation, deletes bullets, deletes stopwords, strips plural words,
# and makes them sigular words, strips past tense words, makes adverbs regular verbs,
# then displays the top 50 words

import sys
import math
import re
from collections import Counter

# Use the file name YYYY_Letter.txt as the file name
# If file not valid, exit

try:
    fname = input("Enter file name: ")
    fh = open(fname, encoding="utf8")
    r = fh.read()
except:
    print("Invalid file name")
    exit(1)

   
#Define stopwords
stopwords = set(line.strip() for line in open('stopwords.txt'))

#Define all verbs that end in e for stripping past tense
e_words = set(line.strip() for line in open('verbs_e.txt'))


wordcount = {}

    
for word in r.lower().split():
    
    #Delete punctuation
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("*","")
    word = word.replace("?","")
    word = word.replace("\'","")
    word = word.replace("-","")


    #Delete bullets
    word = word.replace(u'\u2022', "")

    #Lower case all words so there are no duplicates for capitalization
    word = word.lower()

    #Strip out plural words, adverbs, past tense words, and special 'ies'  plural words
    if word not in stopwords:
        if word.endswith("ly"):
            word = word[0:-2]
       # elif word.endswith("ing"):
       #     word = word[0:-3]
        elif word.endswith("ies"):
            word = word[0:-3] + "y"
        elif word.endswith("ied"):
            word = word[0:-3] + "y"
            
        #Words like love/loved only need 1 character removed where others need 2 char removed
        #We must check the dictionary of verbs ending in e before assigning the value
            
        elif word[0:-1] in e_words and word.endswith("ed"):
            word = word[0:-1]
        elif word[0:-2] not in e_words and word.endswith("ed"):
            word = word[0:-2]
        elif word[0:-1] in e_words and word.endswith("es"):
            word = word[0:-1]
        elif word[0:-2] not in e_words and word.endswith("es"):
            word = word[0:-2]

        #Remove remaining plurals except business
        elif word.endswith("s") and word != 'business':
            word = word[0:-1]

                        
    #Do not count stopwords
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
            

    
#Count the words
word_counts = Counter(wordcount)

#Only print the top 50 words
for word, count in word_counts.most_common(50):
    print(word, ": ", count)




# End of script
