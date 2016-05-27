from nltk.corpus import wordnet as wn
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
from itertools import chain
from nltk import word_tokenize
import sys
import gzip
import operator

def get_synonyms(word, ppdbfile):
        synlist = []
	ppdb_list = list(ppdb)
	for tup in ppdb_list:
		x = tup[0]
		y = tup[1]
		if x == word:
			synlist.append(y)
		if y == word:
			synlist.append(x)		
        return synlist

def get_ppdb(ppdbfile) :
        ppdb = set()
        with gzip.open(ppdbfile) as f :
                for line in f :
                        _, x, y, _ = line.strip().split(' ||| ', 3)
                        pair = (x,y) if x < y else (y,x)
                        ppdb.add(pair)
        return ppdb

f1 = open('../antonyms/not-antonyms.txt', 'r')
f3 = open('new-antonym-list-using-ppdb2.txt', 'w')
ppdbfile = '/nlp/data/ellie/ppdb-2.0-xxxl-all.gz'

print("Retreiving ppdb\n")
ppdb = get_ppdb(ppdbfile)
print("Finished retreiving ppdb\n")

not_antonym_tuple_list = []
for line in f1.readlines():
        sent = line.split("\t")
        if len(sent) == 2:
                w1 = sent[0].strip()
                w2 = sent[1].strip()
                not_antonym_tuple_list.append((w1,w2))
f1.close()

print("Total number of not-antonyms: " + str(len(not_antonym_tuple_list)) + "\n")
i = 1
for tup in not_antonym_tuple_list:
	print("Processing antonym pair#: " + str(i) + "\n")
        w1 = tup[0].strip()
        w2 = tup[1].strip()
        #antonyms of the form (w1,synonyms(w2))
        syns_w2 = get_synonyms(w2, ppdbfile)
        for word in syns_w2:
                f3.write(w1 + '\t' + word + '\n')
        #antonyms of the form (synonyms(w1), w2)
        syns_w1 = get_synonyms(w1, ppdbfile)
        for word in syns_w1:
                f3.write(word + '\t' + w2 + '\n')
	i+=1
f3.close()
