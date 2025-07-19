import speech_recognition as sr
import webbrowser
import requests
import io
from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound
import pywhatkit as kit
import OpenAI as ai

recognizer = sr.Recognizer()  # for voice recognition

# Eleven Labs API details
api_key = "api key"  # 11 Labs API key
voice_id = "onwK4e9ZLuTAKqWW03F9"  # voice id
#voice_id = "3gsg3cxXyFLcGIfNbM6C"  # indian voice id (But not working) 
 
headers = {
    "Content-Type": "application/json",
    "xi-api-key": api_key
}
tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

# Function to use Eleven Labs' voice to speak text
def speak(text):
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(tts_url, headers=headers, json=data)
    
    if response.status_code == 200:
        audio_stream = io.BytesIO(response.content)
        audio = AudioSegment.from_mp3(audio_stream)
        play(audio) 
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Function to process user commands
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "play" in c:
        song_name = c.replace("play", "").strip()  # Get the part after "play"
        if song_name:
            speak(f"Playing {song_name} on YouTube")
            kit.playonyt(song_name)  # Use pywhatkit to play the song on YouTube
            
        else:
            speak("I didn't catch the name of the song.")

    elif "stop" in c.lower():
        speak("Sorry Sir, I will stop now.")
        print("Friday is stopping...")
        return False # Return False to indicate stop
    
    else:
        output = output = ai.aiprocess(c)
        output = output.replace("*", "").strip()
        print(output)
        speak(output)

    return True

if __name__ == "__main__":
    # Play the startup wakeup sound
    playsound('Rudra_startup.wav')

    # Obtain audio from the microphone
    while True:
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'Rudra'...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
                word = r.recognize_google(audio)
                
                if word.lower() == "rudra":
                    speak("Yes, how can I assist you?")

                    active = True  # Set assistant as active
                    while active:  # Continuously listen until stopped
                        try:
                            with sr.Microphone() as source:
                                print("Rudra Active...")
                                audio = r.listen(source, timeout=2, phrase_time_limit=5)
                                command = r.recognize_google(audio)
                                print(f"Command: {command}")
                                active = processCommand(command)

                        except sr.UnknownValueError:
                            print("Sorry, I didn't catch that.")
                        except sr.RequestError as e:
                            print(f"Could not request results; {e}")

                elif word.lower() == "goodbye":
                    speak("Goodbye sir........., Have a nice Day.")
                    print("Shutting down Friday...")
                    break

        except Exception as e:
            print(f"Error: {e}")