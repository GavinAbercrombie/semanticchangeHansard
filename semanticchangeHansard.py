import sys
from gensim.models import Word2Vec

# load models -- plain or POS tagged (change in line 18)
model1 = Word2Vec.load("aligned1.model")
model2 = Word2Vec.load("aligned2.model")
both_models = [model1, model2]
model1pos = Word2Vec.load("aligned1pos.model")
model2pos = Word2Vec.load("aligned2pos.model")
both_models_pos = [model1pos, model2pos]

# wois = words of interest
wois = open(sys.argv[1]).read().split(',')

for ow in wois:
	if ow in model1.wv.vocab:
		print("\n'"+ow+"':")
		for m in both_models: # select both_models or both_models_pos
			result = ''	
			for entry in m.wv.most_similar(positive=ow)[:-1]:
				result = result + entry[0] + ', '
			result = result + m.wv.most_similar(positive=ow)[-1][0]
			print(result)
