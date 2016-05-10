import sys

def get_ppdb_phrases(ppdb_file):
	ppdb = set()
	f = open(ppdb_file, "r")
	for line in f.readlines():
		sent = line.strip("\n")
		phrase_pair = sent.split("\t")
		ppdb.add((phrase_pair[0], phrase_pair[1]))
	f.close()
	return ppdb

def get_morph_mapping(morph_file):
	mapping = {}
	f = open(morph_file, "r")
	for line in f.readlines():
		sent = line.strip("\n")
		word_pair = sent.split("\t")
		if(word_pair[0] in mapping.keys()):
			print(word_pair[0])
		else:
			mapping[word_pair[0]] = word_pair[1]
	f.close()
	return mapping

def get_antonym_pairs(ppdb_phrases, morph_mapping, morph_words):
	antonyms = set()
	for pp in ppdb_phrases:
		phrase1 = pp[0]
		phrase2 = pp[1]
		if(phrase1 in morph_words):
			antonyms.add((morph_mapping[phrase1], phrase2))
			print(phrase1, phrase2)
			print(morph_mapping[phrase1], phrase2)
			print() 
	return antonyms

morph_analysed_file = sys.argv[1]
ppdb_phrases_file = sys.argv[2]
out_file = "new_antonym_list-morph2.txt"

ppdb_phrases = get_ppdb_phrases(ppdb_phrases_file)

morph_mapping = get_morph_mapping(morph_analysed_file)
morph_words = morph_mapping.keys()

antonym_pairs = get_antonym_pairs(ppdb_phrases, morph_mapping, morph_words)

fout = open(out_file, "w")
for item in antonym_pairs:
	fout.write(str(item[0]) + "\t" + str(item[1]) + "\n")
fout.close()
