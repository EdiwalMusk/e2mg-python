import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp('Weather is good peter, peter borrow money!')
print(doc.ents)