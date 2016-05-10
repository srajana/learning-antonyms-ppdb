import sys
import re
from nltk import word_tokenize
filename = sys.argv[1]

word_dict = {}
count = 0

f = open(filename, "r")
for line in f.readlines():
	text = line.split("|||")
	source = text[1]
	source1 = word_tokenize(source.decode('utf-8'))
	target = text[2]
	target1 = word_tokenize(target.decode('utf-8'))
	if 'not ' in source and len(source1) == 2:
		word_dict[source] = target
	if 'not ' in target and len(target1) == 2:
		word_dict[target] = source
f.close()


f1 = open("ppdb-phrases3.txt", "w")
keys = word_dict.keys()
count = len(keys)
for word in keys:
	f1.write(word + "\t" + word_dict[word] + "\n")
f1.write("count: " + str(count) + "\n")
f1.close()

