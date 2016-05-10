import sys

brown_out_file = sys.argv[1]
ppdb_prefix_file = sys.argv[2]

brown_morph_dict = {}
antonym_dict = {}

f1 = open(brown_out_file, "r")
for line in f1.readlines():
	sent = line.split("\t")
	brown_morph_dict[sent[0].strip()] = sent[1].strip("\n")
f1.close()

f2 = open(ppdb_prefix_file, "r")
f3 = open("morph-analysed-list2.txt", "w")

for word in f2.readlines():
	word = word.strip()
	if word in brown_morph_dict.keys():
		 f3.write(word + "\t" + brown_morph_dict[word] + "\n")
	else:
		print(word)

f2.close()
f3.close()
