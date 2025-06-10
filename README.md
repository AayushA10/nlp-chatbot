# 🧠 Voice-Enabled NLP Chatbot (Offline, No API)

A fully offline NLP-powered chatbot with both **text and voice input/output**, built using classic machine learning and Python. No external APIs, no Docker — just pure local intelligence.

---

## 🚀 Features

- 🎙️ **Voice & Text Input** using `speech_recognition` and `input()`
- 🗣️ **Text-to-Speech** output using `pyttsx3`
- 🧠 **Intent Detection** using `scikit-learn` and `nltk`
- 📝 **Chat Logging** to `chat_log.txt`
- ✅ Completely offline (no OpenAI, no internet required)

---

## 🛠 Tech Stack

- Python 3.11+
- scikit-learn
- nltk
- speech_recognition
- pyttsx3
- pyaudio

---

## 📁 Project Structure

nlp-chatbot/
├── chatbot.py # Main chatbot with voice & logging
├── train_bot.py # Trains the ML intent classifier
├── chat_log.txt # Stores timestamped conversations
├── data/
│ └── intents.json # Training data (user intents)
├── model/
│ └── chatbot_model.pkl # Trained model


---

## 🧪 How to Run

### 1. Install Requirements

```bash
pip install nltk scikit-learn speechrecognition pyttsx3 pyaudio

For macOS users:

bash
Copy
Edit
brew install portaudio
2. Train the Model
bash
Copy
Edit
python3 train_bot.py
3. Start Chatbot
bash
Copy
Edit
python3 chatbot.py
Choose between:

1 = Voice mode

2 = Text mode

Say or type:

"Hi", "Who made you?", "Tell me a joke", "quit"

