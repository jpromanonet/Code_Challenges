# Third exercise using PDF libraries in Python

# Importing libraries and frameworks

import PyPDF2

# Defining Global Variables

pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

# Program logic

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObject = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObject)

for pageNum in range(pdf2Reader.numPages):
    pageObject = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObject)

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()