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
			_, x, y, _ = line.strip().split(' ||| ', 3)
			pair = (x,y) if x < y else (y,x)
			ppdb.add(pair)
	return ppdb

def get_antonyms(antonymfile):
	antonyms = set()
	f = open(antonymfile, "r")
	for line in f.readlines():
		line = line.strip("\n")
		words = line.split("\t")
		x = words[0]
		y = words[1]
		pair = (x,y) if x<y else (y,x)
		antonyms.add(pair)
	f.close()
	return antonyms

def get_dependency_graph(elemdeps) : 
	G = {}
	for d in elemdeps : 
		typ = d.get('type')
		g = d.find('governor').text.strip()
		d = d.find('dependent').text.strip()
		if g not in G : G[g] = {}
		if d not in G : G[d] = {}
		G[g][d] = (typ, '->')
		G[d][g] = (typ, '<-')
	return G

def get_tokens(elemtoks) : 
	return {t.get('id').strip() : (t.find('word').text.strip().lower(), t.find('lemma').text.strip().lower(), t.find('POS').text.strip()) for t in elemtoks}

def get_paths(graph, source, sinks, toks, nhops) : 
	if nhops == 0: 
		if source == '0' : src = 'ROOT'
		else : _,src,_ = toks[source]
		if source in sinks : return [('[Y]', set([source]))]
		else: return []

	paths = []
	for edge in graph[source] : 
		edgetype, edgedir  = graph[source][edge]
		for path, visited in get_paths(graph, edge, sinks, toks, nhops-1) : 
			if source not in visited : 
				if source == '0' : src = 'ROOT'
				else : _,src,_ = toks[source]
				if edgedir == '->' : paths.append(('['+src+']-'+edgetype+edgedir+path, visited|set([source])))
				elif edgedir == '<-' : paths.append(('['+src+']'+edgedir+edgetype+'-'+path, visited|set([source])))
	return paths

def print_paths(G, x, y, toks, maxlen=6) :
	xtxt = ' '.join([toks['%s'%i][0] for i in x])
	ytxt = ' '.join([toks['%s'%i][0] for i in y])
	pair = (xtxt, ytxt) if xtxt < ytxt else (ytxt, xtxt)
	if pair in antonyms : 
		xltxt = ' '.join([toks['%s'%i][1] for i in x])
		yltxt = ' '.join([toks['%s'%i][1] for i in y])
		xpos = ' '.join([toks['%s'%i][2] for i in x])
		ypos = ' '.join([toks['%s'%i][2] for i in y])
		sent = ' '.join([toks[str(t+1)][0] for t in range(len(toks))])
		# for each token in x, follow all paths up to maxlen. if the path ends at any token in y, print it. 
		for i in x : 
			idx = str(i)
			if idx in G:
				for l in range(1,maxlen):
					for path, _ in get_paths(G, idx, [str(j) for j in y], toks, l)  : 
						_, rest = path.split(']',1)
						path = '[X]'+rest
						try : print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s'%(xtxt, ytxt, xltxt, yltxt, xpos, ypos, path, sent)
						except UnicodeEncodeError : continue

#sys.stderr.write('Reading PPDB ...\n')
#ppdb = get_ppdb('/nlp/data/ellie/ppdb-2.0-xxxl-all.gz')
#sys.stderr.write('done loading PPDB.\n')

sys.stderr.write('Reading antonyms ...\n')
antonyms = get_antonyms(sys.argv[1])
sys.stderr.write('Done loading antonyms.\n')

rootdir = '/nlp/data/corpora/LDC/LDC2012T21/data/xml/'

#for fname in os.listdir(rootdir) : 
#	if fname.startswith(sys.argv[1]) : 
#		sys.stderr.write('Processing %s (%.02f MB) ...'%(fname, os.path.getsize('%s/%s'%(rootdir,fname))/1000000))
#		source = gzip.open('%s/%s'%(rootdir,fname))

#infiles = sys.argv[1].split(',')
infiles = get_all_files(rootdir)
for fname in infiles : 
	source = gzip.open('%s/%s'%(rootdir,fname))
	sys.stderr.write('Processing %s (%.02f MB) ...'%(fname, os.path.getsize('%s/%s'%(rootdir,fname))/1000000))
	context = iter(et.iterparse(source, events=("start", "end")))
	event, root = context.next()
	count = 0
	for event, elem in context:
	    if count % 10000000 == 0 :  sys.stderr.write('.')
	    count += 1
	    if event == "end" and elem.tag == "sentences":
		for s in elem : 
			toks = get_tokens(s.find('tokens'))
			dg = get_dependency_graph(s.find('basic-dependencies'))
			#ngms = reduce(operator.add, [ngrams(range(1,len(toks)+1),n) for n in [1,2,3]], [])
			ngms = []
			for n in [1,2,3]: 
   				for ngm in ngrams(range(1,len(toks)+1), n):
     					ngms.append(ngm)
			for x,y in combinations(ngms, 2) :
				if len(set(x) & set(y)) == 0 : print_paths(dg, x, y, toks)
	        root.clear()
		sys.stderr.write('done.\n')
sys.stderr.write('Extraction complete.\n')

