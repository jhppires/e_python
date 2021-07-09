from PyPDF2 import PdfFileReader
from pathlib import Path

#import os 
#cwd = os.getcwd()
#print(cwd)

#pdf_path=cwd+
pdf = PdfFileReader("Portaria 0692 - Maria Cristina Vigorito.pdf")
first_page = pdf.getPage(0)
type(first_page)
print(first_page.extractText())
