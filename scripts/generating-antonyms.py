from nltk.corpus import wordnet as wn
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
from itertools import chain
antonyms = {}
antonyms_synonyms = {}
stemmer = PorterStemmer()
stemmer1 = SnowballStemmer("english")
for i in wn.all_synsets():
	for j in i.lemmas():
		if j.antonyms():
			w1 = j.name()
			w2 = j.antonyms()[0].name()
			if w1 < w2:
				key = w1
				value = w2
			else:
				key = w2
				value = w1
			antonyms[key] = value
			antonyms_synonyms[key] = value
			synonyms = wn.synsets(j.name())
			syns = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
			for s in syns:
				antonyms_synonyms[s.decode('utf-8')] = j.antonyms()[0].name()

# Antonyms from Wordnet
'''f = open("wordnet-antonyms.txt", "w")
f.write("Number of pairs: " + str(len(antonyms.keys())) + "\n")
for k in antonyms.keys():
	f.write(k + "\t" + antonyms[k] + "\n")
f.close()'''

#Antonyms from Wordnet plus Synonym combinations
f = open("wordnet-synonyms-antonyms.txt", "w")
f.write("Number of pairs: " + str(len(antonyms_synonyms.keys())) + "\n")
for k in antonyms_synonyms.keys():
        f.write(k + "\t" + antonyms_synonyms[k] + "\n")
f.close()

# Antonyms from Wordnet plus their stemmed versions
'''for k in antonyms.keys():
	antonyms[stemmer1.stem(k)] = stemmer1.stem(antonyms[k])
f = open("wordnet-antonyms-plus-snowball-stemmed.txt", "w")
f.write("Number of pairs: " + str(len(antonyms.keys())) + "\n")
for k in antonyms.keys():
	f.write(k + "\t" + antonyms[k] + "\n")
f.close()'''
