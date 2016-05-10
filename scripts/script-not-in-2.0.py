'''
This script generated the PPDB one-to-many paraphrases that are in version 1.0 but not in 2.0
'''

dict1 = {}

f1 = open("ppdb-phrases-1.0-format.txt", "r")
f2 = open("ppdb-phrases-2.0-format.txt", "r")

f3 = open("ppdb-phrases-not-in-2.0.txt", "w")

for line in f2.readlines():
	word_pair = line.split("\t")
	left = word_pair[0].strip()
	right = word_pair[1].strip()
	dict1[left] = right
	dict1[right] = left

word_list = dict1.keys()

for line in f1.readlines():
	word_pair = line.split("\t")
	word1 = word_pair[0].strip()
	word2 = word_pair[1].strip()
	if word1 not in word_list and word2 not in word_list:
		f3.write(word1 + "\t" + word2 + "\n")
	elif (word1 in word_list) and (word2 != dict1[word1]):
		f3.write(word1 + "\t" + word2 + "\n")
	elif (word2 in word_list) and (word1 != dict1[word2]):
                f3.write(word1 + "\t" + word2 + "\n")

f1.close()
f2.close()
f3.close()
