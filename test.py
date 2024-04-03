from django.core.files.storage import FileSystemStorage
from openpyxl import Workbook
import cv2
import os
import datetime
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from pytesseract import image_to_string

def process_image(image_path):
  try:
    # Load the image
    img = cv2.imread(image_path)

    # Convert image to RGB (required by pytesseract)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Use pytesseract to extract text (specify language)
    text = image_to_string(rgb_img, config='--psm 6 lang=por')  # Adjust 'psm' if needed

    # Print extracted text
    print(text)

  except Exception as e:
    print(f"Error processing image: {e}")

# Get list of files in the input directory
input_dir = 'input'
for filename in os.listdir(input_dir):
  image_path = os.path.join(input_dir, filename)

  # Process the image
  process_image(image_path)

