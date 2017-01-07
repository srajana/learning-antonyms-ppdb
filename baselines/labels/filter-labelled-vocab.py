import math
import random
import os
import glob

#Only include antonyms in the vocabulary

input_files = ['../../antonyms/wordnet-antonyms.txt', '../../antonyms/wordnet-synonyms-antonyms.txt', '../../antonyms/exclusion-antonyms.txt', '../../antonyms/not-antonyms.txt', '../../antonyms/antonym-list-1.txt', '../../antonyms/antonym-list-3.txt']

baseline_antonyms = set()

vocab_file = open('wikiEntities.txt','r')
vocabulary = list(vocab_file.readlines())
vocab_file.close()

for antfile in input_files:
	print("Processing file: " + antfile)
	
	num_lines = 300
	count = 0

	new_name = os.path.basename(antfile) + '.out'
	f2 = open(new_name, 'w')
		
	f = open(antfile, 'r')
	lines = list(f.readlines())
	f.close()
	print("Num of lines: " + str(len(lines)))
	
	random.shuffle(lines)
	#random_lines = lines[:num_lines]
	
	for l in lines:
		pair = l.strip('\n')
		pair = pair.split('\t')
		if((len(pair) >= 2) and (pair[0] in vocabulary) and (pair[1] in vocabulary)):
			
			count += 1
			print("Running count: " + count)
			if(count > num_lines):
				break

			baseline_antonyms.add((pair[0], pair[1]))
			f2.write(pair[0]+'\t'+pair[1]+'\n')
	f2.close()
	print("Finished processing file: " + antfile)

print(len(baseline_antonyms))
antonyms = list(baseline_antonyms)
random.shuffle(antonyms)

print("Writing pairs to file...")
fout = open('filtered-antonyms.txt', 'w')
for entry in antonyms:
	fout.write(entry[0]+'\t'+entry[1]+'\t'+'antonym'+'\n')
fout.close()
