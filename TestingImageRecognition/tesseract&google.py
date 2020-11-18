# ********************************************************************************************************
# IMPORTS

# imports to recognize the image file
try:
    from PIL import Image
except ImportError:
    import Image

# this is working with the PyTesseract
# 'brew install tesseract' --- this was done in the file where the code is
import pytesseract
# location can be found using 'brew info tesseract'

# working with google translate api
import googletrans
from googletrans import Translator

# ********************************************************************************************************
# WORKING WITH PYTESSERACT

# necessary line - identifies where the tesseract executable file is that you downloaded with homebrew
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

# for reading the text itself
text = pytesseract.image_to_string(Image.open('img/input/image4.jpeg'), lang='eng', timeout=5)

print(text)

# for testing purposes
tmpLines = text.split('\n')
lines = []
for line in tmpLines:
    if len(line) > 2:
        lines.append(line)

# print("ACTUAL TEXT STARTING HERE\n", text)

# ********************************************************************************************************
# WORKING WITH GOOGLE TRANSLATE API

# creating a translator object
translator = Translator()
result = translator.translate(lines, src='english', dest='french')

i = 0
for num in range(len(lines)):
    print(i, '. (eng, french)')
    print(lines[num])
    print(result[num].text)
    i = i+1
