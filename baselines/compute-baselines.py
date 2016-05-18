import math
import random

input_files = ['../antonyms/wordnet-antonyms.txt', '../antonyms/wordnet-synonyms-antonyms.txt', '../antonyms/exclusion-antonyms.txt', 'PPDB-Phrases/phrases-2.0-shorter.txt', '../../antonym-list-1.txt', '../../antonym-list-2.txt', '../../antonym-list-3.txt']

baseline_antonyms = set()

for antfile in input_files:
	num_lines = int(randrange(50,100))
	print(antfile, num_lines)
	f = open(antfile, 'r')
	lines = list(antfile.readlines())
	f.close()
	random.shuffle(lines)
	random_lines = lines[:num_lines]
	for l in random_lines():
		pair = l.strip('\n')
		pair = pair.split('\t')
		baseline_antonyms.add((pair[0], pair[1]))

print(len(baseline_antonyms))
antonyms = list(baseline_antonyms)

fout = open('baseline-antonyms.txt', 'w')
for entry in antonyms:
	fout.write(entry[0]+'\t'+entry[1]+'\n')
fout.close()
