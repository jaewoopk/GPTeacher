from nltk.corpus import wordnet as wn
'''
for synset in wn.synsets('good'):
    #print(synset.name())
    print(synset.lemma_names())
    #print(synset.lemmas()[0].antonyms())

print("---------------------------------")
'''
'''
synonyms = []
for syn in wn.synsets("travel"):
    for lm in syn.lemmas():
        synonyms.append(lm.name())

print (set(synonyms))

antonyms = []
for syn in wn.synsets("increase"):
    for lm in syn.lemmas():
        if lm.antonyms():
            antonyms.append(lm.antonyms()[0].name()) 
print(set(antonyms))
'''
