from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "I love this movie",
    "This product is excellent",
    "I am very happy",
    "The service is amazing",
    "I hate this movie",
    "This product is terrible",
    "I am very disappointed",
    "The service is very bad"
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Negative",
    "Negative"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

classifier = MultinomialNB()
classifier.fit(X, labels)

test_sentences = [
    "I love this product",
    "The movie was terrible",
    "The service is excellent",
    "I am disappointed"
]

X_test = vectorizer.transform(test_sentences)
predictions = classifier.predict(X_test)

print("Text Classification Results\n")

for sentence, label in zip(test_sentences, predictions):
    print("Sentence:", sentence)
    print("Predicted Class:", label)
    print("-" * 40)