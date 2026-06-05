import nltk
from nltk.corpus import treebank
from nltk.tag import UnigramTagger
from nltk.tag.brill import Pos
from nltk.tbl.template import Template
from nltk.tag.brill_trainer import BrillTaggerTrainer

# Download corpus
nltk.download('treebank')

# Training and testing data
train_data = treebank.tagged_sents()[:2000]
test_data = treebank.tagged_sents()[2000:]

# Initial tagger
unigram_tagger = UnigramTagger(train_data)

# Templates
templates = [
    Template(Pos([-1])),
    Template(Pos([1]))
]

# Train Brill Tagger
trainer = BrillTaggerTrainer(unigram_tagger, templates)
brill_tagger = trainer.train(train_data)

# Test sentence
sentence = "The cat is sleeping".split()

print("Tagged Sentence:")
print(brill_tagger.tag(sentence))

# Accuracy
accuracy = brill_tagger.accuracy(test_data)
print(f"\nAccuracy of the Brill Tagger: {accuracy:.2f}")