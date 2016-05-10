import sys
import re
import math
import os
import glob
from nltk import word_tokenize
from collections import Counter

filename = sys.argv[1]

freq_dict = []
count = 0

def get_all_files(directory):
        files = []
        for name in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, name)):
                        files.append(os.path.join(directory, name))
        return files

def get_tf(sample):
	tf_dict = dict(Counter(sample))
	return tf_dict

def standardize(rawexcerpt):
	lowercase = rawexcerpt.lower()
	tokens = word_tokenize(lowercase.decode('utf-8'))
	for s in range(0,len(tokens)):
		tokens[s] = tokens[s].encode('utf-8')
	return tokens

def load_file_excerpts(filepath):
	list_file_excerpts = []
	f = open(filepath, "r")
	for line in f.readlines():
		excerpts = standardize(line)
		list_file_excerpts.append(excerpts)
	f.close()
	return list_file_excerpts

def load_directory_excerpts(files):
	files_in_dir = files
	list_dir_excerpts = []
	for file in files_in_dir:
		f = open(file, "r")
		for line in f.readlines():
			excerpts = standardize(line)
			list_dir_excerpts.append(excerpts)
		f.close()
		break
	return list_dir_excerpts

def flatten(listoflists):
	flat_list = []
	for i in listoflists:
		flat_list.extend(i)
	return flat_list

def get_frequencies(morph_file, tf_dict, out_file):
	morph_words = []
	for line in morph_f.readlines():
		morph_words.append(line.strip("\n"))
	words = tf_dict.keys()
	for w in words:
		if w in morph_words:
			print("Word in both: ", w)
			out_file.write(str(tf_dict[w]) + "\t" + w + "\n")

files = sys.argv[2].split(",")
print(len(files))

corpus = load_directory_excerpts(files)
sample = flatten(corpus)
tf_dict = get_tf(sample)
print(tf_dict)
	
morph_f = open("to-be-morphed.txt", "r")
out_f = open("morph_wordlist.txt", "w")

get_frequencies(morph_f, tf_dict, out_f)

morph_f.close()
out_f.close()

