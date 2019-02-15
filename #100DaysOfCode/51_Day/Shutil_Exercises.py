######## Shutil Exercises 1

# Import modules and libraries

import shutil
import os
import sys

# Defining global variables

source_Dir = None
destiny_Dir = None
working_Dir = None

# User parameters

print('Input working path(with \\): ')
working_Dir = input()
print(' ')
print('Input source path(with \\): ')
source_Dir = input()
print(' ')
print('Input destiny path(with \\): ')
destiny_Dir = input()

# Program logic

os.chdir(str(working_Dir))
shutil.copy(str(source_Dir), str(destiny_Dir))

####### End Shutil Exercises 1

####### Shutil Exercises 2