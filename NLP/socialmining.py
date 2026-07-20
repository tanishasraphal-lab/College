from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

posts = [
    "I love this phone",
    "This movie is great",
    "I hate this product",
    "The service is terrible"
]

labels = [
    "Positive",
    "Positive",
    "Negative",
    "Negative"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(posts)

model = LogisticRegression()
model.fit(X, labels)

test_posts = [
    "I love this movie",
    "This product is terrible"
]

predictions = model.predict(vectorizer.transform(test_posts))

for post, sentiment in zip(test_posts, predictions):
    print("Post:", post)
    print("Sentiment:", sentiment)
    print()