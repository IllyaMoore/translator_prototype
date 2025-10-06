from translatepy.translators.google import GoogleTranslate

import os 
from dotenv import load_dotenv, dotenv_values

load_dotenv()

TEXT_SAMPLE = os.getenv("SPEECH_TXT_OUTPUT")
TRANSLATIONS_BD = os.getenv("TRANSLATIONS_BD")

with open(TEXT_SAMPLE, "r") as file:
    f = file.read().replace('\n', '')
    

gtranslate = GoogleTranslate()
trans = gtranslate.translate(f, "Ukrainian")

#debug massage 
print(trans)

BD = open("TRANSLATIONS_BD", "w") 

BD.write(f"{trans}, \n")
BD.close()
