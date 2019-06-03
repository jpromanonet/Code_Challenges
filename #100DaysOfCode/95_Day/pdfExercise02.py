# Second exercise using PDF libraries in Python

# Importing libraries and frameworks

import PyPDF2

# Defining variables

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted

# Program Logic

pdfReader.decrypt('rosebud')
pagina = pdfReader.getPage(0)

print(pagina)