# An implementation of a reverse dictionary using txtai

[Simon Willison](https://simonwillison.net/) recently starred
[txtai](https://github.com/neuml/txtai), a neato multitool for
building AI-powered search apps, and I realized then that the
library could be used to make something I've wanted since the
dawn of time: a good [reverse dictionary](https://en.wikipedia.org/wiki/Conceptual_dictionary).

Most of the existing ones suck because humans have a tendency
to [paraphrase](https://en.wikipedia.org/wiki/Paraphrase), meaning
the concept of a word in your head doesn't
match up with what the dictionary authors think. Understanding
language through brute-force with transformers seems to do the trick now a days,
so I thought I'd give an AI twist on the concept it a try.

## Creation

I was able to make a command-propmpt prototype in about an hour due to the excellent
[wn](https://github.com/goodmami/wn) library and txtai's great tutorials.

WordNet is a perfect dictionary for this project, as it clearly separates definitions
(synsets) from their words, which helps us to account for synonyms and the like.

All in all, I was able to go from idea to prototype in about an hour
(that includes training 120,039 synsets for 163,161 words), which is honestly
amazing. It isn't perfect, but I'm sure there's a lot of knobs I can turn in order to
make it better, along with getting a larger dictionary. Transformers are the future, baby!

## Run

```
git clone https://github.com/supersonichub1/reverse-dictionary
cd reverse-dictionary
poetry install
poetry run python create_index.py
poetry run python query_index.py
```

## Demonstration
```
$ python query_index.py
> bird that sings
Closest words: songster, songbird (score of 0.7369604110717773)
> to copy someone else in jest
Closest word: impersonate (score of 0.7036008834838867)
> an outing with a love interest
Closest word: date (score of 0.5460328459739685)
> something that stores data
Closest word: descriptor (score of 0.5796446800231934)
> something that doesn't catch fire
Closest words: smoulder, smolder (score of 0.5455739498138428)
> board game where you buy properties
Closest word: Monopoly (score of 0.7235665321350098)
> see-through object
Closest words: prism, optical prism (score of 0.6346988677978516)
> ball of rice
Closest word: rice (score of 0.5870095491409302)
> a machine that does tasks according to its programming 
Closest words: run, execute (score of 0.6618992686271667)
> distress caused by being away from home
Closest words: lonely, lonesome (score of 0.5635539889335632)
```

## Future Improvements
- use the [semantic graph](https://github.com/neuml/txtai/blob/master/examples/38_Introducing_the_Semantic_Graph.ipynb) to connect synsets to their [relations](https://wn.readthedocs.io/en/latest/api/wn.html#wn.Synset.relations)
- make a web UI
- use a [multilingual WordNet](https://github.com/goodmami/wn#open-multilingual-wordnet-omw-collection) with a multilingual model
