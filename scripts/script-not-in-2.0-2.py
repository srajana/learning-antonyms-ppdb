'''
This script generated the PPDB one-to-many paraphrases that are in version 1.0 but not in 2.0
'''

word_list = []

f1 = open("../PPDB-Phrases/phrases-1.0.txt", "r")
f2 = open("../PPDB-Phrases/phrases-2.0.txt", "r")

f3 = open("../PPDB-Phrases/phrases-not-in-2.0-2.txt", "w")

for line in f2.readlines():
	word_pair = line.split("\t")
	left = word_pair[0].strip()
	right = word_pair[1].strip()
	word_list.append((left, right))
	word_list.append((right, left))


for line in f1.readlines():
	word_pair = line.split("\t")
	word1 = word_pair[0].strip()
	word2 = word_pair[1].strip()
	if (word1, word2) not in word_list:
		f3.write(word1 + "\t" + word2 + "\n")

f1.close()
f2.close()
f3.close()
