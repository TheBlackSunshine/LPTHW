directions = ('north', 'south', 'east', 'west', 'up', 'down', 'up', 'left', 'right', 'back')
verbs = ('go', 'stop', 'kill', 'eat')
stops = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')

def get_tuple(word):
	if word in directions:
		return ('direction', word)
	elif word in verbs:
		return ('verb', word)
	elif word in stops:
		return ('stop', word)
	elif word in nouns:
		return ('noun', word)
	elif word.isdigit():
		return ('number', word)
	else:
		return ('error', word)

def scan(sentence):
	words = sentence.split()
	return[get_tuple(word) for word in words]