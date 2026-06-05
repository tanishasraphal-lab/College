#N-gram Tagger Example using NLTK
import nltk
from nltk.corpus import brown
from nltk.tag import UnigramTagger, BigramTagger, TrigramTagger

# Download datasets
nltk.download('brown')
nltk.download('universal_tagset')

# Training and testing data
train_data = brown.tagged_sents()[:3000]
test_data = brown.tagged_sents()[3000:]

# Unigram Tagger
unigram_tagger = UnigramTagger(train_data)

# Bigram Tagger
bigram_tagger = BigramTagger(train_data, backoff=unigram_tagger)

# Trigram Tagger
trigram_tagger = TrigramTagger(train_data, backoff=bigram_tagger)

# Test sentence
sentence = "the dog sat on the mat".split()

# Tagging
tagged_sentence = trigram_tagger.tag(sentence)

print("Tagged Sentence:")
print(tagged_sentence)

# Accuracy
print("\nUnigram Accuracy :", unigram_tagger.accuracy(test_data))
print("Bigram Accuracy  :", bigram_tagger.accuracy(test_data))
print("Trigram Accuracy :", trigram_tagger.accuracy(test_data))