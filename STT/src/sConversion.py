import speech_recognition as sr
 
filename = "/home/moore/code/translator_prototype/STT/src/recordings/voice-sample.wav"

r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)

with open('/home/moore/code/translator_prototype/STT/src/cSpeech/name.txt', 'w') as f:
    f.write(text);
