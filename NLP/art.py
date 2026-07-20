# pip install sumy nltk

import nltk
nltk.download('punkt')

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

file_path = "news.txt"

parser = PlaintextParser.from_file(file_path, Tokenizer("english"))
summarizer = TextRankSummarizer()

print("Top 10 Important Sentences:\n")

for i, sentence in enumerate(summarizer(parser.document, 10), start=1):
    print(f"{i}. {sentence}")