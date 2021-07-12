from icecream import ic #bib for debug
import os

from PyPDF2 import PdfFileReader
from pdf2image import convert_from_path
from pathlib import Path

#pdf_path=cwd+
#pdf = PdfFileReader("Portaria 0692 - Maria Cristina Vigorito.pdf")
#first_page = pdf.getPage(0)
#type(first_page)
#print(first_page.extractText())

basic_path="/mnt/c/Users/Johann Pires/OneDrive/Documentos/VS projects/e_python/Com assinatura"

#Esse é um jeito de percorrer a pasta
"""for _, _, arquivo in os.walk("/mnt/c/Users/Johann Pires/OneDrive/Documentos/VS projects/e_python/Com assinatura"):
    ic(arquivo)
"""
#Esse é outro jeito
caminhos = [os.path.join(basic_path, nome) for nome in os.listdir(basic_path)]
ic(caminhos)
"""
for n in caminhos:
    os.rename(n,n[-3]+'PNG')
"""
"""
for n in caminhos:
    pages=convert_from_path(n,dpi=200)
    for page in pages:
        page.save(n,'PNG')
"""

from PIL import Image
import pytesseract

print( pytesseract.image_to_string( Image.open(caminhos[0]), lang='por') )
