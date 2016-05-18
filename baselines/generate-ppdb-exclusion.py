import os
import sys
import gzip
import operator
import xml.etree.ElementTree as et
from nltk.util import ngrams
from itertools import combinations

def get_all_files(directory):
        files = []
        for name in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, name)):
                        files.append(name)
        return files

def get_ppdb(ppdbfile) : 
	ppdb = set()
	with gzip.open(ppdbfile) as f : 
		for line in f : 
			text = line.split(' ||| ')
			if(len(text) == 6 and text[5].strip() == 'Exclusion'):
				_, x, y, _ = line.strip().split(' ||| ', 3)
				pair = (x,y) if x < y else (y,x)
				ppdb.add(pair)
	return ppdb


sys.stderr.write('loading PPDB.\n')
ppdb = get_ppdb('/nlp/data/ellie/ppdb-2.0-xxxl-all.gz')
sys.stderr.write('done loading PPDB.\n')

sys.stderr.write('writing antonyms.\n')
f = open('exclusion-antonyms.txt', 'w')
antonym_list = list(ppdb)
for entry in antonym_list:
	f.write(entry[0]+"\t"+entry[1]+"\n")
f.close()
sys.stderr.write('done writing antonyms.\n')
