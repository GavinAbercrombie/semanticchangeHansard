from gensim.models import Word2Vec

# load models
model1 = Word2Vec.load("aligned1pos.model")
model2 = Word2Vec.load("aligned2pos.model")
both_models = [model1, model2]
model1pos = Word2Vec.load("aligned1pos.model")
model2pos = Word2Vec.load("aligned2pos.model")
both_models_pos = [model1pos, model2pos]

# wois = words of interest

# known words of interest -- from selection of prior work
knownwois = ['atomic', 'bitch', 'broadcast', 'broadcast', 'broadcast', 'checking', 'diet', 'gay', 'honey', 'monitor', 'mouse', 'peck', 
			'plastic', 'propaganda', 'record', 'recording', 'sex', 'tape', 'transmitted']

knownwois_pos = ['atomic_JJ', 'bitch_NN', 'broadcast_VBN', 'checking_VBG', 'diet_NN', 'gay_JJ', 'honey_NN', 
			'monitor_NN', 'mouse_NN', 'peck_VBN', 'plastic_JJ', 'propaganda_NN', 'record_NN', 
			 'recording_NN', 'sex_NN', 'tape_NN', 'transmitted_VBN']

# obsolete words of interest -- from OED
obsoletewois = ['assert', 'harry', 'sailing', 'walter', 'rifle', 'morocco', 'bull', 'impress', 'fortune', 'expire', 'contradict', 'militia', 'vacant', 'suffrage', 'cheer', 'cheese', 'fond', 'infant', 'unworthy', 'weigh', 'embark', 'vice', 'contest', 'keenly', 'depart', 'famine', 'wine', 'expedite', 'fined', 'boots', 'fat', 'bow', 'ripe', 'earnest', 'convict', 'drill', 'bitter', 'obey', 'worn', 'forbid', 'notorious', 'sink', 'seller', 'prejudicial', 'instruct', 'butter', 'distribute', 'mill', 'rebellion', 'receiver', 'peel', 'delicate', 'shoot', 'vigour', 'defy', 'mode', 'dispense', 'folly', 'misfortune', 'inspect', 'dislike', 'tended', 'execute', 'trunk', 'pardon', 'lent', 'entertain', 'vain', 'mount', 'trace', 'meal', 'sergeant', 'sunk', 'pleasant', 'raw', 'strand', 'admiral', 'drunk', 'refrain', 'deem', 'obstacle', 'iron', 'clyde', 'indifferent', 'grain', 'mercy', 'prevail', 'eve', 'calculate', 'cave', 'crowd', 'file', 'resent', 'riot', 'calculating', 'waive', 'plead', 'copper', 'elicit', 'presently', 'keir', 'reside', 'lever', 'prohibit', 'zeal', 'apportion', 'shore', 'indefinite', 'pretence', 'entail', 'customary', 'allay', 'par', 'procure', 'imperfect', 'rival', 'indemnity', 'lake', 'solemn', 'dust', 'ordnance', 'earl', 'preamble', 'hinder', 'accord', 'farce', 'soil', 'solitary', 'inflict', 'plainly', 'plot', 'devote', 'incomplete', 'apt', 'cargo', 'subordinate', 'sub', 'tyranny', 'lays', 'pronounce', 'wreck', 'attribute', 'summon', 'curtail', 'void']

for ow in knownwois: # change as required
	if ow in model1.wv.vocab:
		print("\n'"+ow+"':")
		for m in both_models:
			result = ''	
			for entry in m.wv.most_similar(positive=ow)[:-1]:
				result = result + entry[0] + ', '
			result = result + m.wv.most_similar(positive=ow)[-1][0]
			print(result)
