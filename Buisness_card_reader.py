import streamlit as st
from PIL import Image 
import cv2
import pytesseract
from pytesseract import Output

tessdata_dir_config =r'C:\Users\HachemSfar\Desktop\BC\tesseract.exe'

image_file =st.file_uploader('Upload a Buisness Card',type=['png','jpeg','jpg'])
if image_file  is not None:
    image = Image.open(image_file)
    d = pytesseract.image_to_data(image, output_type=Output.DICT,config=tessdata_dir_config)
    
    text=pytesseract.image_to_string(image,config=tessdata_dir_config)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            image = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    st.image(image)

