from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

documents = [
    "Machine learning is a branch of artificial intelligence.",
    "Deep learning uses neural networks.",
    "Python is a popular programming language.",
    "Java and Python are programming languages.",
    "Cats are friendly pets.",
    "Dogs are loyal animals.",
    "Artificial intelligence is transforming industries.",
    "Programming helps build software applications."
]

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(documents)

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

print("Text Clustering Results\n")

for i, doc in enumerate(documents):
    print("Document:", doc)
    print("Cluster:", kmeans.labels_[i])
    print("-" * 50)