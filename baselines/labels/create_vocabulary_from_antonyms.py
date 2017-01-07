import math
import random
import os
import glob

input_files = ['../../antonyms/wordnet-antonyms.txt', '../../antonyms/wordnet-synonyms-antonyms.txt', '../../antonyms/exclusion-antonyms.txt', '../../antonyms/not-antonyms.txt', '../../antonyms/antonym-list-1.txt', '../../antonyms/antonym-list-3.txt']

baseline_antonyms = set()

for antfile in input_files:
	print("Processing file: " + antfile)

	fin = open(antfile, 'r')
	lines = list(fin.readlines())
	fin.close()
	
	random.shuffle(lines)
	print("Num of lines: " + str(len(lines)))

	for l in lines:
		pair = l.strip('\n')
		pair = pair.split('\t')
		if(len(pair) >= 2):
			baseline_antonyms.add(pair[0])
			baseline_antonyms.add(pair[1])

antonyms = list(baseline_antonyms)
random.shuffle(antonyms)
print("Total number of antonym words: " + str(len(antonyms)))

print("Writing words to file...")
fout = open('vocabulary.txt', 'w')
for entry in antonyms:
	fout.write(entry + '\n')
fout.close()
