#This code defines a simple context-free grammar (CFG) and generates sentence based in that grammar using nltk
import nltk
from nltk import CFG
from nltk.parse.generate import generate
#Define grammar
grammar = CFG.fromstring("""
S -> NP VP
NP -> 'John' | 'Mary'
VP -> V NP
V -> 'likes' | 'hates'
""")
#Generate sentences
for sentence in generate(grammar, n=10):
    print(' '.join(sentence))                                                 