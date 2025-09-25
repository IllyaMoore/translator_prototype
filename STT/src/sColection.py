import sounddevice as sd
from scipy.io.wavfile import write
from pathlib import Path

base_dir = (Path(__file__).parent).parent
out_path = base_dir / "recordings" / "output.wav"

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype='float32')

sd.wait() 

write(out_path, fs, myrecording)  # Save as WAV file 