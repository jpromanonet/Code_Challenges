# First exercise using PDF libraries in Python

# Importing libraries and frameworks 

import PyPDF2

# Declaring variables

pdfFileObject = open('combinedminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

# Calling the library
pageObject = pdfReader.getPage(0)
pageObject.extractText()

# Exercise output

print(pdfReader.numPages)