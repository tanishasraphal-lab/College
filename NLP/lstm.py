# pip install tensorflow

import tensorflow as tf
from tensorflow import keras
import numpy as np

texts = [
    "good movie",
    "excellent product",
    "bad movie",
    "poor service"
]

labels = np.array([1, 1, 0, 0])

tokenizer = keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(texts)

X = tokenizer.texts_to_sequences(texts)
X = keras.preprocessing.sequence.pad_sequences(X, maxlen=2)

model = keras.Sequential([
    keras.layers.Embedding(input_dim=20, output_dim=8),
    keras.layers.LSTM(8),
    keras.layers.Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.fit(X, labels, epochs=10, verbose=1)

test = [
    "good product",
    "bad service"
]

X_test = tokenizer.texts_to_sequences(test)
X_test = keras.preprocessing.sequence.pad_sequences(X_test, maxlen=2)

pred = model.predict(X_test)

for t, p in zip(test, pred):
    print(t, ":", "Positive" if p > 0.5 else "Negative")