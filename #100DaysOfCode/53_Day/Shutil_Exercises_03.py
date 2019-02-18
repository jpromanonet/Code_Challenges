######## Shutil Exercises 3

# Import modules and libraries

import shutil
import os
import sys

# Defining global variables

dir_To_Del = None

# Program logic

os.rmdir('C:\\Shutil_Exercise_3')
os.chdir('C:\\')
os.makedirs('C:\\Shutil_Exercise_3')

	# User parameters
	
print('Do you want to delete the directory? Y/N')
dir_To_Del = input()

if dir_To_Del == 'Y':
	os.rmdir('C:\\Shutil_Exercise_3')
else:
	('Ok then')

####### End Shutil Exercises 3