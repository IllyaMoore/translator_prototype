from translatepy.translators.google import GoogleTranslate

text = ""

with open(text, "r") as file:
    f = file.read().replace('\n', '')
    

gtranslate = GoogleTranslate()
trans = gtranslate.translate(f, "Ukrainian")
print(trans)
