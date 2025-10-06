import speech_recognition as sr
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()


VOICE_FILE = os.getenv("VOICE_FILE")
SPEECH_TXT_OUTPUT = os.getenv("SPEECH_TXT_OUTPUT")

r = sr.Recognizer()

with sr.AudioFile(VOICE_FILE) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)

with open(SPEECH_TXT_OUTPUT, 'w') as f:
    f.write(text);
