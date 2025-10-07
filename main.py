import subprocess

import os

from dotenv import load_dotenv, dotenv_values

load_dotenv()

CAPTURE_VOICE = os.getenv("CAPTURE_VOICE")

GET_SPEECH_TXT = os.getenv("GET_SPEECH_TXT")

TRANSLATE = os.getenv("TRANSLATE")

TTS = os.getenv("TTS")


# subprocess.run(["python3", CAPTURE_VOICE])
print("\n")
subprocess.run(["python3", GET_SPEECH_TXT])

subprocess.run(["python3", TRANSLATE])

subprocess.run(["python3", TTS])

