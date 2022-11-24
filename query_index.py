from txtai.embeddings import Embeddings
import wn
import readline

# wn.download('oewn:2021')
en = wn.Wordnet('oewn:2021')

embeddings = Embeddings()
embeddings.load('reverse-dictionary')

while True:
	try:
		query = input("> ")
		synset_id, score = embeddings.search(query, 1)[0]
		lemmas = en.synset(synset_id).lemmas()
		print(f"Closest word{'' if len(lemmas) == 1 else 's'}:", ', '.join(lemmas), f"(score of {score})")
	except KeyboardInterrupt as e:
		print()
		exit()
