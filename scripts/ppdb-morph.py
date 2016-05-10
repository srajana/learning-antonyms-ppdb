import sys
import re
from nltk import word_tokenize
filename = sys.argv[1]

word_dict = []
count = 0
#morph_words = []

f = open(filename, "r")
for line in f:
	text = line.split("|||")
	source = text[1]
	source1 = word_tokenize(source.decode('utf-8'))
	target = text[2]
	target1 = word_tokenize(target.decode('utf-8'))
	if len(source1) == 1:
		source = source.strip()
		if (source.startswith('in') or source.startswith('un') or source.startswith('anti') or source.startswith('de')):
			#morph_words.append(source)
			word_dict.append((source, target))
	if len(target1) == 1:
		target = target.strip()
		if (target.startswith('in') or target.startswith('un') or target.startswith('anti') or target.startswith('de')):
			#morph_words.append(target)
			word_dict.append((target, source))
f.close()

'''
morph_words = list(set(morph_words))
f2 = open("ppdb-2.0-morph-words.txt", "w")
for wrd in morph_words:
	f2.write(wrd + "\n")
f2.close()
'''
f1 = open("ppdb-2.0-morph-phrases-2.txt", "w")
#keys = word_dict.keys()
count = len(word_dict)
f1.write("count: " + str(count) + "\n")
for tup in word_dict:
	word1 = tup[0].strip("\n")
	word2 = tup[1].strip("\n")
	f1.write(word1 + "\t" + word2 + "\n")
f1.close()

