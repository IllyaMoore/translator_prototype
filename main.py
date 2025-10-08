import subprocess
import os
from dotenv import load_dotenv, dotenv_values

import pygame

load_dotenv()

import time 
_test_timer = time.time()

CAPTURE_VOICE = os.getenv("CAPTURE_VOICE")

GET_SPEECH_TXT = os.getenv("GET_SPEECH_TXT")

TRANSLATE = os.getenv("TRANSLATE")

TTS = os.getenv("TTS")

AUDIO_FILE = os.getenv("AUDIO_FILE")


# subprocess.run(["python3", CAPTURE_VOICE])
subprocess.run(["python3", GET_SPEECH_TXT])

subprocess.run(["python3", TRANSLATE])

subprocess.run(["python3", TTS])
print(f"Time to get to full execution {format(time.time() - _test_timer, '.0f')} sec")


#play the audio
pygame.mixer.init()
pygame.mixer.music.load(AUDIO_FILE)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass
print("\n")


