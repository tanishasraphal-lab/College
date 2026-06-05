#POS Tagging
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Input text
text = "NLP helps computer understand human language."

# Tokenization
words = word_tokenize(text)

# POS Tagging
tags = pos_tag(words)

# Display Output
print("POS Tags:\n")
for word, tag in tags:
    print(word, "->", tag)
