import math
import random
import os
import glob

input_files = ['../../antonyms/wordnet-antonyms.txt', '../../antonyms/wordnet-synonyms-antonyms.txt', '../../antonyms/exclusion-antonyms.txt', '../../antonyms/not-antonyms.txt', '../../antonyms/antonym-list-1.txt', '../../antonyms/antonym-list-3.txt']

baseline_antonyms = set()

for antfile in input_files:
	#num_lines = int(random.randrange(50,100))
	num_lines = 300
	new_name = os.path.basename(antfile) + '.out'
	f2 = open(new_name, 'w')
	print(antfile, num_lines)
	f = open(antfile, 'r')
	lines = list(f.readlines())
	f.close()
	random.shuffle(lines)
	random_lines = lines[:num_lines]
	for l in random_lines:
		pair = l.strip('\n')
		pair = pair.split('\t')
		if(len(pair) >= 2):
			baseline_antonyms.add((pair[0], pair[1]))
			f2.write(pair[0]+'\t'+pair[1]+'\n')
	f2.close()

print(len(baseline_antonyms))
antonyms = list(baseline_antonyms)
random.shuffle(antonyms)

fout = open('labelled-antonyms.txt', 'w')
for entry in antonyms:
	fout.write(entry[0]+'\t'+entry[1]+'\t'+'antonym'+'\n')
fout.close()
