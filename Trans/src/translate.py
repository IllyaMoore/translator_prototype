from translatepy.translators.google import GoogleTranslate

text = "" 

with open(text, "r") as file:
    f = file.read().replace('\n', '')
    

gtranslate = GoogleTranslate()
trans = gtranslate.translate(f, "Ukrainian")

#debug massage 
print(trans)

BD = open("translations/translationTestBD.txt", "w") 

BD.write(f"{trans}, \n")
BD.close()
