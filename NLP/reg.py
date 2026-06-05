from nltk.tag import RegexpTagger

# Define tagging patterns
patterns = [
    (r'.*ing$', 'VBG'),      # Gerund
    (r'.*ed$', 'VBD'),       # Past tense
    (r'.*es$', 'VBZ'),       # Verb ending with es
    (r'.*ould$', 'MD'),      # Modal verbs
    (r".*'s$", 'NNS'),       # Possessive nouns
    (r'.*s$', 'NNS'),        # Plural nouns
    (r'^-?[0-9]+$', 'CD'),   # Numbers
    (r'.*', 'NN')            # Default noun
]

# Create Regexp Tagger
regexp_tagger = RegexpTagger(patterns)

# Test sentence
sentence = "The boys are playing cricket and scored 50 runs".split()

# Perform tagging
tagged = regexp_tagger.tag(sentence)

print("Regexp Tagger Output:\n")
for word, tag in tagged:
    print(word, "->", tag)