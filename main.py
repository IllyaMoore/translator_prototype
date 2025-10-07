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
subprocess.run(["python3", GET_SPEECH_TXT])

subprocess.run(["python3", TRANSLATE])

subprocess.run(["python3", TTS])
print(f"Time to get to full execution {format(time.time() - _test_timer, '.0f')} sec")

print("\n")


