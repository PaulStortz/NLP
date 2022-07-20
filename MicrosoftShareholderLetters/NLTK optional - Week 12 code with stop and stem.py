# Word Count Starter Program
# Based on Chuck Severance's Python Code - Romeo Section 9.4
# from Python for Informatics 3
# http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
#
# Code changes by Carrie Beam and Nivedita Bijlani for UMUC DATA 620
# Last updated Feb 5, 2016

import string
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
lmtzr = WordNetLemmatizer()
# Import the corpus of English stop words
stop = stopwords.words('english')
# Uncomment the print statement below to see what words are included by default
# print (stop)
# Append our own stop words to this list based on context
stop.append("•")
stop.append("amazoncom")
stop.append("1997")

for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()

# Remove stop words
    for word in words:
        if word not in stop:
            # Lemmatize - Lemmatizing is similar to stemming but reduces the word to its root as defined in the dictionary
            lmtzr.lemmatize(word)
            # Now add to counts dictionary if it does not exist
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

word_list = [(counts[w], w) for w in counts]
word_list.sort()
word_list.reverse()
print("The 10 most frequent words are")
print("Rank\tCount\tWord")

i = 1

# Top 10
for x, word in word_list[:10]:
    print('%2s\t%4s\t%s' %(i, x, word))
    i += 1



