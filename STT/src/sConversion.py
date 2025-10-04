import speech_recognition as sr
 
filename = "/home/moore/CodeProjects/translator_prototype/STT/recordings/voice-sample.wav"

r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)
