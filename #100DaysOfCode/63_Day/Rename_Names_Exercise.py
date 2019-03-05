#! python3

# Rename_Names_Exercise.py is the first exercise of chapter nine from the book 'Automating the boring stuff with python'

# Importing libraries and frameworks

import shutil
import os
import re

# Declaring global variables

datePattern = None
amerFileName = None

# User parameters

# Program logic

    # Create a regex that matches files with the American date format

datePattern = re.compile(r(.*?) # all text before the date
       ((0|1)?\d)-               # one or two digits for the month
       ((0|1|2|3)?\d)-           # one or two digits for the day
       ((19|20)\d\d)             # four digits for the year
       (.*?)$                    # all text after the date
          , re.VERBOSE)

    # Loop over the files in the working directory

for amerFileName in os.listdir('.'):
    mo = datePattern.search(amerFileName)

    # Skip files without a date

    if mo == None:
        continue

    # Get the different parts of the filename

    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    # Form the european style filename.

    euroFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get full, absolute file paths

    absWorkingDir = os.path.abspath('.')
    amerFileName = os.path.join(absWorkingDir, amerFileName)
    euroFileName = os.path.join(absWorkingDir, euroFileName)

    # Rename the files
print('Renaming "%s" to "%s"...' % (amerFileName, euroFileName))
# shutil.move(amerFileName, euroFileName) #uncomment after testing!!!    