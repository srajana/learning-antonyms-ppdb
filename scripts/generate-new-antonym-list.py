from nltk.corpus import wordnet as wn
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
from itertools import chain

f1 = open('../antonyms/wordnet-synonyms-antonyms.txt', 'r') 
f2 = open('../PPDB-Phrases/phrases-2.0-shorter.txt', 'r')
f3 = open('../antonyms/wordnet-synset/new-antonym-list.txt', 'w')

count1 = 0
count2 = 0
count3 = 0
count4 = 0

wordnet_antonym_words = []
wordnet_antonym_tuple_list = []
for line in f1.readlines():
	sent = line.split("\t")
	if len(sent) == 2:
		w1 = sent[0].strip()
		w2 = sent[1].strip()
		wordnet_antonym_words.append(w1)
		wordnet_antonym_words.append(w2)
		wordnet_antonym_tuple_list.append((w1,w2))

ppdb_phrase_tuple_list = []
for line in f2.readlines():
	sent = line.split("\t")
	if len(sent) == 1:
		continue
	w1 = sent[0].strip()
	w2 = sent[1].strip()
	ppdb_phrase_tuple_list.append((w1,w2))

for tup in ppdb_phrase_tuple_list:
        w1 = tup[0]
        w2 = tup[1]
	w11 = w1.split()
	w22 = w2.split()
	if len(w11) == 2:
		#Pairs of the form (not happy, happy)
		#f3.write(w1 + "\t" + w11[1] + "\n")
		#count1+=1

		#Pairs of the form (happy, unhappy) from (not happy, unhappy)
		f3.write(w11[1] + "\t" + w2 + "\n")
		count2+=1

		#Pairs of the form forallx(x, happy) antonym(x,sad)
                synonyms = wn.synsets(w11[1])
                lemmas = list(set(chain.from_iterable([word.lemma_names() for word in synonyms])))
                for i in range(len(lemmas)):
                        lemmas[i] = lemmas[i].decode('utf-8')

		#Pairs of the form (happy, sad) from (not happy, unhappy) and (unhappy, sad)
		common = w2
		for t in ppdb_phrase_tuple_list:
			if (common == t[0] and w1 != t[1]):
				f3.write(w11[1] + "\t" + t[1] + "\n")
				count3+=1
				for i in lemmas:
					f3.write(i + "\t" + t[1] + "\n")
					count4+=1
				
				#Pairs of the form forally(sad, y) antonym(happy,y)
                		syn = wn.synsets(t[1])
                		lemma = list(set(chain.from_iterable([word.lemma_names() for word in syn])))
                		for i in range(len(lemma)):
                        		lemma[i] = lemma[i].decode('utf-8')
				for i in lemma:
					f3.write(w11[1] + "\t" + i + "\n")
					count4+=1
				 
			elif (common == t[1] and w1 != t[0]):
				f3.write(w11[1] + "\t" + t[0] + "\n")
				count3+=1
				for i in lemmas:
                                        f3.write(i + "\t" + t[0] + "\n")
                                        count4+=1

				#Pairs of the form forally(sad, y) antonym(happy,y)
                                syn = wn.synsets(t[0])
                                lemma = list(set(chain.from_iterable([word.lemma_names() for word in syn])))
                                for i in range(len(lemma)):
                                	lemma[i] = lemma[i].decode('utf-8')
                                for i in lemma:
                                        f3.write(w11[1] + "\t" + i + "\n")
                                        count4+=1		

		'''
		x = w2
		if x in wordnet_antonym_words:
			for tup in wordnet_antonym_tuple_list:
				if x == tup[0]:
					f3.write(w1 + "\t" + tup[1] + "\n")
				elif x == tup[1]:
					f3.write(w1 + "\t" + tup[0] + "\n")
		'''

	elif len(w22) == 2:
		#Pairs of the form (not happy, happy)
                #f3.write(w2 + "\t" + w22[1] + "\n")
                #count1+=1

                #Pairs of the form (happy, unhappy) from (not happy, unhappy)
                f3.write(w22[1] + "\t" + w1 + "\n")
                count2+=1

                #Pairs of the form forallx(x, happy) antonym(x,sad)
                synonyms = wn.synsets(w22[1])
                lemmas = list(set(chain.from_iterable([word.lemma_names() for word in synonyms])))
                for i in range(len(lemmas)):
                        lemmas[i] = lemmas[i].decode('utf-8')
		
		#Pairs of the form (happy, sad) from (not happy, unhappy) and (unhappy, sad)
                common = w1
                for t in ppdb_phrase_tuple_list:
                        if (common == t[0] and w2 != t[1]):
                                f3.write(w22[1] + "\t" + t[1] + "\n")
                                count3+=1
				for i in lemmas:
                                        f3.write(i + "\t" + t[1] + "\n")
                                        count4+=1

				#Pairs of the form forally(sad, y) antonym(happy,y)
                                syn = wn.synsets(t[1])
                                lemma = list(set(chain.from_iterable([word.lemma_names() for word in syn])))
                                for i in range(len(lemma)):
                                	lemma[i] = lemma[i].decode('utf-8')
                                for i in lemma:
                                        f3.write(w22[1] + "\t" + i + "\n")
                                        count4+=1

                        elif (common == t[1] and w2 != t[0]):
                                f3.write(w22[1] + "\t" + t[0] + "\n")
                                count3+=1
				for i in lemmas:
                                        f3.write(i + "\t" + t[0] + "\n")
                                        count4+=1

				#Pairs of the form forally(sad, y) antonym(happy,y)
                                syn = wn.synsets(t[0])
                                lemma = list(set(chain.from_iterable([word.lemma_names() for word in syn])))
                                for i in range(len(lemma)):
                                	lemma[i] = lemma[i].decode('utf-8')
                                for i in lemma:
                                        f3.write(w22[1] + "\t" + i + "\n")
                                        count4+=1
		
		'''
		x = w1
		if x in wordnet_antonym_words:
                        for tup in wordnet_antonym_tuple_list:
                                if x == tup[0]:
                                        f3.write(w2 + "\t" + tup[1] + "\n")
                                elif x == tup[1]:
                                        f3.write(w2 + "\t" + tup[0] + "\n")
		'''


#print(count1)
print(count2)
print(count3)
print(count4)

f1.close()
f2.close()
f3.close()
