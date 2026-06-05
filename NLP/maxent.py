#Maxent Entropy Classifier Example
import nltk
import numpy
from nltk.classify import MaxentClassifier
#Training data
train = [({"good" : True}, "Positive"), ({"excellent" : True}, "Positive"),
         ({"bad" : True}, "Negative"), ({"poor" : True}, "Negative")]
#Train Classifier
classifier = MaxentClassifier.train(train, algorithm='iis', trace=0, max_iter=10)
#Test
test = {"good" : True}
print("Prediction:", classifier.classify(test))