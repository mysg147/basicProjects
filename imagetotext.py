import pytesseract
import os
from PIL import Image
import json


pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract" #Path to the tesseract 

def convert():
    data={}
    image_name=input()
    img = Image.open(image_name)
    text = pytesseract.image_to_string(img)
    data[image_name]={"text":text}
    with open('imageToText.json','w') as fp:
        json.dump(data,fp,indent=4)
    print(text)

convert()