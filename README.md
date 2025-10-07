# Voice Translator (English → Ukrainian)

A simple voice translation tool that converts English speech to Ukrainian text and audio.

## Features

- Real-time speech recognition (English)
- Text translation to Ukrainian
- Speech synthesis (Ukrainian voice output)
- Audio file export

## Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the translator:
```bash
python3 main.py
```

Speak in English, and the application will:
1. Recognize your speech
2. Translate it to Ukrainian
3. Display the translation
4. Play the Ukrainian audio

## Project Structure

- `main.py` - Main application
- `STT/` - Speech-to-Text modules
- `Trans/src` - Translation logic
- `TTS/src` - Text-to-Speech modules
- `TRANSLATIONS_BD` - Translation database/history
- `output.wav` - Generated audio output
