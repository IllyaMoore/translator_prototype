from transformers import VitsModel, AutoTokenizer
import torch
import torchaudio
import soundfile as sf

import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

TRANSLATIONS_BD = os.getenv("TRANSLATIONS_BD")

# --- Параметри ---
with open(TRANSLATIONS_BD, 'r') as file:
    text = file.read().replace('\n', '')


pitch_shift = 4  # кількість півтонів: >0 – вищий тон, <0 – нижчий

# --- Завантаження моделі і токенізатора ---
model = VitsModel.from_pretrained("facebook/mms-tts-ukr")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-ukr")

# --- Токенізація ---
inputs = tokenizer(text, return_tensors="pt")

# --- Перевірка на порожній input ---
if inputs["input_ids"].shape[1] == 0:
    raise ValueError("Tokenized input is empty. Check your text.")

# --- Приведення input_ids до LongTensor для Embedding ---
inputs["input_ids"] = inputs["input_ids"].long()

# --- Генерація аудіо ---
with torch.no_grad():
    output = model(**inputs).waveform  # [1, num_samples]

waveform = output.squeeze(0).cpu()  # [num_samples]

# --- Зміна тону ---
if pitch_shift != 0:
    waveform = torchaudio.functional.pitch_shift(
        waveform.unsqueeze(0),  # додаємо batch dim
        sample_rate=24000,
        n_steps=pitch_shift
    ).squeeze(0)

# --- Збереження аудіо ---
sf.write("output.wav", waveform.numpy(), samplerate=24000)
print(f"Audio saved to output.wav with pitch shift {pitch_shift} semitones.")

