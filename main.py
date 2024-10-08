import pytesseract
from docx import Document
import os

pytesseract.pytesseract.tesseract_cmd = r'Your  tesseract.exe file directory here' 

image_path = r'Your Image file path'

image_name, image_extension = os.path.splitext(os.path.basename(image_path))

res = pytesseract.image_to_string(image_path)

doc = Document()
doc.add_paragraph(res)

output_path = os.path.join(os.path.dirname(image_path), f'{image_name}.docx')

doc.save(output_path)

print(f'Text successfully in file {output_path} saved.')
