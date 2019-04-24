#! python3

# readCensusExcel.py | Tabulates population and number of census tracts for 
# each US County.

# Importing libraries and frameworks

import openpyxl
import pprint

# Declaring global variables

wb = ''
sheet = ''
countyData = {}

# Program logic

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']

for row in range(2, sheet.max_row + 1):
    ## Each row in the spreadsheet has data for one census tract.
    state  = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop    = sheet['D' + str(row)].value