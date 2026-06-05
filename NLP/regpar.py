#Regular Expression Parser
import nltk
sentence = "The cat sat on the mat"
words = sentence.lower().split()
grammar = r"""
NP: {<DT><NN>}
PP: {<IN><NP>}
VP: {<VBD><PP>}
"""
pos_tags = nltk.pos_tag(words)
cp = nltk.RegexpParser(grammar)
result = cp.parse(pos_tags)
print(result)