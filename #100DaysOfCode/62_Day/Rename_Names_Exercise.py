#! python3

# Rename_Names_Exercise.py is the first exercise of chapter nine from the book 'Automating the boring stuff with python'

# Importing libraries and frameworks

import shutil
import os
import re

# Declaring global variables

date_Pattern = None

# User parameters

# Program logic

    # Create a regex that matches files with the American date format

date_Pattern = re.compile(r(.*?) # all text before the date
       ((0|1)?\d)-               # one or two digits for the month
       ((0|1|2|3)?\d)-           # one or two digits for the day
       ((19|20)\d\d)             # four digits for the year
       (.*?)$                    # all text after the date
          , re.VERBOSE)


