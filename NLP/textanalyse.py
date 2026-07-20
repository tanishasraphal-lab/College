import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download("punkt")
nltk.download("stopwords")

text = """
Chennai Super Kings defeated Kolkata Knight Riders in the IPL 2021 final.
MS Dhoni led Chennai Super Kings to their fourth IPL title.
Faf du Plessis scored important runs while Ravindra Jadeja contributed with both bat and ball.
"""

words = word_tokenize(text.lower())

stop_words = set(stopwords.words("english"))

words = [w for w in words if w.isalpha() and w not in stop_words]

freq = Counter(words)

print("Top 10 Frequent Words:\n")

for word, count in freq.most_common(10):
    print(word, ":", count)