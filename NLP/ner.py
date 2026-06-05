#NER Tagger Example using NLTK
import nltk

text = "Sachine Tendulkar was born in Mumbai and played for India."
#Tokenization
words = nltk.word_tokenize(text)
#POS Tagging
pos_tags = nltk.pos_tag(words)
#Named Entity Recognition Tagging
ner_tree = nltk.ne_chunk(pos_tags)
print(ner_tree)
