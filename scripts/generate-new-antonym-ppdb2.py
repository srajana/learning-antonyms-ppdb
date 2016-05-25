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
        with gzip.open(ppdbfile) as f :
                for line in f :
                        _, x, y, _ = line.strip().split(' ||| ', 3)
                        source = x.strip()
                        target = y.strip()
                        if source == word:
                                synlist.append(target)
                        if target == word:
                                synlist.append(source)
        return synlist

f1 = open('../antonyms/not-antonyms.txt', 'r')
f3 = open('new-antonym-list-using-ppdb.txt', 'w')
ppdbfile = '/nlp/data/ellie/ppdb-2.0-xxxl-all.gz'

not_antonym_tuple_list = []
for line in f1.readlines():
        sent = line.split("\t")
        if len(sent) == 2:
                w1 = sent[0].strip()
                w2 = sent[1].strip()
                not_antonym_tuple_list.append((w1,w2))
f1.close()

for tup in not_antonym_tuple_list:
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
f3.close()
