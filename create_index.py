# https://wn.readthedocs.io/en/latest/index.html
# https://github.com/goodmami/wn#available-wordnets

from txtai.embeddings import Embeddings
import wn

# https://wn.readthedocs.io/en/latest/api/wn.constants.html#wn.constants.PARTS_OF_SPEECH
PARTS_OF_SPEECH = {
	'n': "noun",
	'v': "verb",
	'a': "adjective",
	'r': "adverb",
	's': "adjective satellite",
	't': "phrase",
	'c': "conjunction",
	'p': "adposition",
	'x': "other",
	'u': "unknown",
}
wn.download('oewn:2021')
en = wn.Wordnet('oewn:2021')



# https://wn.readthedocs.io/en/latest/api/wn.html#wn.Synset
# TODO: tags?
documents = [
	(
		synset.id,
		f"""{synset.definition()}
Part of speech: {PARTS_OF_SPEECH[synset.pos]}
Examples: {', '.join(synset.examples())}
Lemmas: {', '.join(synset.lemmas())} 
""",
	None
	)
	for synset in en.synsets()	
]

embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2", "content": True, "objects": True})
embeddings.index(documents)
embeddings.save("reverse-dictionary")
