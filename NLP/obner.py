# Named Entity Recognition using NLTK
import nltk
#Sample text
text = "Barack Obama was born in Hawaii and served as president of the United States."
#Tokenization
words = nltk.word_tokenize(text)
#POS Tagging
pos_tags = nltk.pos_tag(words)
#Named Entity Recognition
ner_tree = nltk.ne_chunk(pos_tags)
print("Named Entities:")
print(ner_tree)