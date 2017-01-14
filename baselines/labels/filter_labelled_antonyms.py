import math
import random
import os
import glob
import sys
from docopt import docopt

def main():
	'''
	Only includes antonym pairs contained in the vocabulary
	'''

	# Get the arguments
	'''
	args = docopt("""Filters out antonym pairs that are not in the vocabulary

	Usage:
		filter_labelled_antonyms.py <labelled_antonyms_file> <vocabulary_file>
		<labelled_antonyms_file> = File containing a tab separated antonym pair on each line along with its label, formatted as x\ty\tclass 
		<vocabulary_file> = File containing phrases in the vocabulary, formatted as one word on each line.
	""")

	labelled_antonyms_file = args['<labelled_antonyms_file>']
	vocabulary_file = args['<vocabulary_file>']
	'''
	labelled_antonyms_file = sys.argv[1]
	vocabulary_file = sys.argv[2]

	with open(vocabulary_file,'r') as f_in:
		vocabulary = [line.strip() for line in f_in]

	with open(labelled_antonyms_file,'r') as f_in:
		antonym_pairs = [tuple(line.strip().split('\t')) for line in f_in]

	with open('filtered-labelled-antonyms.txt', 'w') as f_out:
		for pair in antonym_pairs:
			if len(pair) == 3:
				phrase1 = pair[0].strip()
				phrase2 = pair[1].strip()
				label = pair[2].strip()
				if(phrase1 in vocabulary):
					print "Phrase1: " + phrase1
					if(phrase2 in vocabulary):
						print "Phrase2: " + phrase2
						f_out.write(phrase1 + '\t' + phrase2 + '\t' + label + '\n')
				print " "

if __name__ == '__main__':
    main()
