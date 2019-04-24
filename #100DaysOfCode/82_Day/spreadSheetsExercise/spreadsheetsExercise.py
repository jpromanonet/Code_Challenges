#! python3

# Exercise with SpreadSheets Workbooks

# Importing frameworks and libraries

import openpyxl

# Defining global variables
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active

# Program Logic

for rowOfCellObjects in sheet['B1':'B7']:
	for cellObj in rowOfCellObjects:
		print(cellObj.value)
	print('--- END OF ROW ---')