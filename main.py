import subprocess

capture_voice = "/home/moore/code/translator_prototype/STT/src/sColection.py"

get_speech = "/home/moore/code/translator_prototype/STT/src/sConversion.py"

translate = "/home/moore/code/translator_prototype/Trans/src/translate.py"

text_to_speech = ""



subprocess.run(["python3", get_speech])
print("\n")
subprocess.run(["python3", translate])



