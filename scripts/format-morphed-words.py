import sys
import os

morphed_file = sys.argv[1]
prefixes = ['in', 'anti', 'de', 'un']

f1 = open(morphed_file, "r")
f2 = open(morphed_file+"-formatted2.txt", "w")

for line in f1.readlines():
	sent = line.split("\t")
	key = sent[0].strip()
	value = sent[1].strip("\n")
	values = value.split("+")
	if len(values) == 2:
		prefix = values[0]
		prefix = prefix.strip("()").lower()
		if prefix in prefixes:
			root = values[1].strip().lower()
			root = root.strip("()")
			value = root.strip()
			value = value.strip("(")
			value = value.strip(")")
			value = value.lower()
			f2.write(key + "\t" + value.replace("*","") + "\n")
	elif len(values) == 3:
		prefix = values[0]
		prefix = prefix.strip("()").lower()
		if prefix in prefixes:
			root = values[1].strip().lower()
			root = root.strip("()")
			suffix = values[2].strip()
			suffix = suffix.strip("()").lower()
			value = root + suffix
			value = value.strip("(")
			value = value.strip(")")
			value = value.lower()
			f2.write(key + "\t" + value.replace("*","") + "\n")
	elif len(values) == 4:
                prefix = values[0]
		prefix = prefix.strip("()").lower()
		if prefix in prefixes:
                	root = values[1].strip().lower()
			root = root.strip("()")
                	suffix = values[2].strip()
			suffix2 = values[3].strip()
                	suffix = suffix.strip("()").lower()
                	suffix2 = suffix2.strip("()").lower()
                	value = root + suffix + suffix2
                	value = value.strip("(")
			value = value.strip(")")
                	value = value.lower()
			f2.write(key + "\t" + value.replace("*","") + "\n")
	elif len(values) == 5:
                prefix = values[0]
		prefix = prefix.strip("()").lower()
		if prefix in prefixes:
                	root = values[1].strip().lower()
                	root = root.strip("()")
                	suffix = values[2].strip()
                	suffix2 = values[3].strip()
			suffix3 = values[4].strip()
                	suffix = suffix.strip("()").lower()
                	suffix2 = suffix2.strip("()").lower()
                	suffix3 = suffix3.strip("()").lower()
                	value = root + suffix + suffix2 + suffix3
                	value = value.strip("(")
			value = value.strip(")")
                	value = value.lower()
			f2.write(key + "\t" + value.replace("*","") + "\n")
f1.close()
f2.close()

# Clean the file
f3 = open(morphed_file+"-formatted2.txt", "r")
f4 = open(morphed_file+"-cleaned2.txt", "w")
for line in f3.readlines():
	sent = line.lower()
	f4.write(sent)	
f3.close()
f4.close()
