import pytesseract
import os
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract" #Path to the tesseract 

def convert():
    img = Image.open('img.png')
    text = pytesseract.image_to_string(img)
    print(text)

convert()