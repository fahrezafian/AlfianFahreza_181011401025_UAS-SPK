#alfianfahreza 181011401025 
from googletrans import Translator

translate = Translator()

out = translate.translate("indonesia alfian fahreza indonesia", dest="en")

print(out.text)