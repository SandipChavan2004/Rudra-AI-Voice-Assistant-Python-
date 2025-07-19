# 🤖 Rudra – AI Voice Assistant (Python)

**Rudra** is a voice-controlled AI assistant built in Python. It listens for the wake word "Rudra", accepts spoken commands, and performs smart tasks using online services like YouTube, Google, Facebook, and Eleven Labs for text-to-speech responses.

---

## 🧠 Features

- 🎤 **Speech Recognition** via `speech_recognition`
- 🗣️ **Text-to-Speech (TTS)** using Eleven Labs API
- 🎶 **Play YouTube Songs** via `pywhatkit`
- 🌐 **Open Websites** with `webbrowser`
- 🤖 **AI Responses** via OpenAI integration
- 🔊 Plays custom startup and shutdown sounds
- 🛑 Understands "stop" and "goodbye" to terminate interaction

---

## 📂 Project Structure

```bash
Rudra/
├── main.py                  # Entry point for the voice assistant
├── rudra_core.py            # Command processing, TTS, and AI logic
├── Rudra_startup.wav        # Custom startup sound
├── requirements.txt         # List of Python dependencies
├── .env                     # (Optional) for securely storing API keys
└── README.md
```


## 🚀 Getting Started

1. Clone the Repository: 
    git clone https://github.com/your-username/Rudra.git
    cd Rudra

2. Install Dependencies: 
    pip install -r requirements.txt

3. Add Eleven Labs API Key
    Create a .env file:
    ELEVEN_API_KEY=your_api_key_here
    VOICE_ID=onwK4e9ZLuTAKqWW03F9

4. Run the Assistant
    python main.py


## 🛠️ Tech Stack
Feature	                                                 Library
Voice Input	                                        speech_recognition
Web Automation	                                    webbrowser, pywhatkit
TTS (voice output)	                                pydub, requests, Eleven Labs
AI Chat Responses	                                OpenAI (or your own module)
Audio Playback	                                    pydub, playsound


## 🗣️ Supported Commands

    "Rudra" – Wake word
    "Open Google" – Opens https://google.com
    "Open Facebook" – Opens https://facebook.com
    "Open YouTube" – Opens https://youtube.com
    "Play <song name>" – Plays music on YouTube
    "Stop" – Stops the assistant temporarily
    "Goodbye" – Exits completely

    Other questions will be processed via your AI module


## 🔐 Security Notice
    Never hardcode API keys in your source. Use .env or a config file.
    Regenerate your Eleven Labs key if it was accidentally exposed.


## ✅ To-Do / Future Features
 Integrate OpenAI GPT-4 via API for smarter replies
 Add support for weather/news/jokes
 Use natural language understanding for complex queries
 Add wake-word detection using ML or pre-trained model
 GUI using PyQt5 or Tkinter

## 🙌 Contribution
Pull requests are welcome! Please fork the repo and submit your improvements or ideas

## Created by Sandip Chavan
Project: Rudra – Personal AI Assistant