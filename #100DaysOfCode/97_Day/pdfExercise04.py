# Fourth exercise using PDF libraries in Python

# Importing libraries and frameworks

import PyPDF2

# Defining global variables

minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
pdfWriter = PyPDF2.PdfFileWriter()

# Program logic

page.rotateClockwise(90)
pdfWriter.addPage(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()