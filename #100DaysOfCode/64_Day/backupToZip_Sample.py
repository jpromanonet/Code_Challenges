#! python3

# backupToZip_Sample.py is the sample for the future backup app that i will be working on

# It generates an autoincremental filename ZIP file.

# Importing libraries and frameworks

import os
import zipfile
import datetime
import shutil

# Defining global variables

zipFileName = None 
folder = None

# User parameters

print('Input the directory to zip')
folder = input()

# Program logic

shutil.make_archive('NewZipFile', 'zip', str(folder))