'''
This is a script to generate a formatted txt file containing the phrases from ppdb containing the word 'not' that have been genearted from a Unix command.
'''

#f1 = open("ppdb-phrases-1.0.txt", "r")
#f2 = open("ppdb-phrases-1.0-format.txt", "w")

f3 = open("../PPDB-Phrases/ppdb-phrases-2.0.txt", "r")
f4 = open("../PPDB-Phrases/phrases-2.0.txt", "w")

'''for line in f1.readlines():
	text = line.split("|")
	f2.write(text[1] + "\t" + text[2])'''

for line in f3.readlines():
	text = line.split("|")
	f4.write(text[1] + "\t" + text[2])

#f1.close()
#f2.close()
f3.close()
f4.close()
