import streamlit as st
from PIL import Image 
import pytesseract
from pytesseract import Output

image_file =st.file_uploader('Upload a Buisness Card',type=['png','jpeg','jpg'])
if image_file  is not None:
    image = Image.open(image_file)
    d = pytesseract.image_to_data(image, output_type=Output.DICT)
