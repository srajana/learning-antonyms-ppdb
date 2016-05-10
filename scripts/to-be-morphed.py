import sys
import re
import math
from nltk import word_tokenize

filename = sys.argv[1]

freq_dict = []
count = 0
morph_words = []

morph_f = open("to-be-morphed.txt", "r")
for line in morph_f.readlines():
	morph_words.append(line.strip("\n"))
morph_f.close()

ppdb_f = open(filename, "r")
for line in ppdb_f:
	text = line.split("|||")
	if len(text) == 6:
		source = text[1].strip()
		target = text[2].strip()
		if (source in morph_words):
			paraphrase_scores = text[3]
			scores = paraphrase_scores.split(" ")
			for entry in scores:
				if(entry.startswith("RarityPenalty")):
					rarity_penalty = entry.split("=")[1]
					print(float(rarity_penalty))
					try:
						estimated_freq = int(1 - math.log(float(rarity_penalty)))
					except:
						estimated_freq = 0
					freq_dict.append((estimated_freq, source))
					print(estimated_freq, source)
		elif (target in morph_words):
			paraphrase_scores = text[3]
			scores = paraphrase_scores.split(" ")
			for entry in scores:
				if(entry.startswith("RarityPenalty")):
					rarity_penalty = entry.split("=")[1]
					print(float(rarity_penalty))
					try:
						estimated_freq = int(1 - math.log(float(rarity_penalty)))
					except:
						estimated_freq = 0
					freq_dict.append((estimated_freq, target))
					print(estimated_freq, target)
ppdb_f.close()

out_f = open("morph_wordlist.txt", "w")
for tup in freq_dict:
	out_f.write(str(tup[0]) + "\s" + str(tup[1]) + "\n")
out_f.close()
