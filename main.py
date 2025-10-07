import subprocess
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

import time 
_test_timer = time.time()

CAPTURE_VOICE = os.getenv("CAPTURE_VOICE")

GET_SPEECH_TXT = os.getenv("GET_SPEECH_TXT")

TRANSLATE = os.getenv("TRANSLATE")

TTS = os.getenv("TTS")


# subprocess.run(["python3", CAPTURE_VOICE])
print("\n")
subprocess.run(["python3", GET_SPEECH_TXT])
print("\n")
subprocess.run(["python3", TRANSLATE])
print("\n")
subprocess.run(["python3", TTS])
print("\n")
print(f"Time for execution {format(time.time() - _test_timer, '.0f')} sec")
print("\n")


