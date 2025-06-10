import json
import random
import pickle

import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Download tokenizer
nltk.download('punkt')

# Load intents
with open('data/intents.json', 'r') as f:
    intents = json.load(f)

X = []  # patterns
y = []  # tags

# Prepare data
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        X.append(pattern)
        y.append(intent["tag"])

# Create pipeline: vectorizer + classifier
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train model
model.fit(X, y)

# Save model
with open('model/chatbot_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to model/chatbot_model.pkl")
