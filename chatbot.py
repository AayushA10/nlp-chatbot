import json
import random
import pickle
import speech_recognition as sr
import pyttsx3
import datetime

# Load model
with open('model/chatbot_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load intents
with open('data/intents.json', 'r') as f:
    intents = json.load(f)

# Text-to-speech
engine = pyttsx3.init()
def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

# Voice-to-text
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        try:
            audio = r.listen(source, timeout=5)
            user_input = r.recognize_google(audio)
            print("You (voice):", user_input)
            return user_input
        except:
            speak("Sorry, I didn't catch that.")
            return ""

# Intent prediction
def get_response(user_input):
    tag = model.predict([user_input])[0]
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "I'm not sure how to answer that."

# 📝 Chat logger
def log_chat(user, bot):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_log.txt", "a") as f:
        f.write(f"[{timestamp}] You: {user}\n")
        f.write(f"[{timestamp}] Bot: {bot}\n\n")

# Chat loop
print("🧠 Chatbot is online! Say 'quit' or type 'quit' to exit.")
speak("Voice chatbot is online. You can speak or type.")

while True:
    print("\nChoose input mode:\n1. 🎙️ Voice\n2. ⌨️ Text")
    choice = input(">> ")

    if choice == "1":
        user_input = listen()
    else:
        user_input = input("You (text): ")

    if user_input.lower() == "quit":
        speak("Goodbye!")
        break

    if user_input:
        reply = get_response(user_input)
        speak(reply)
        log_chat(user_input, reply)
