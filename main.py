import pytesseract
from docx import Document
import os

# Setting the Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r'Your  tesseract.exe file directory here' 

# Image file path
image_path = r'Your Image file path'

# Read file name and extension
image_name, image_extension = os.path.splitext(os.path.basename(image_path))

# Read text from image
res = pytesseract.image_to_string(image_path)

# Create a new Word document
doc = Document()
doc.add_paragraph(res)

# The path to save the Word file
output_path = os.path.join(os.path.dirname(image_path), f'{image_name}.docx')

# Save the Word document
doc.save(output_path)

print(f'Text successfully in file {output_path} saved.')
