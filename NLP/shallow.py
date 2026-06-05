import nltk
#Sample sentence
sentence = "The boy is playing with a ball"
#Tokenization
words = sentence.split()
#POS Tagging
pos_tags = nltk.pos_tag(words)
#Chunk grammar
grammar = r"""
NP: {<DT>?<JJ>*<NN>}
"""
#Chunk Parser
chunk_parser = nltk.RegexpParser(grammar)
result = chunk_parser.parse(pos_tags)
print(result)