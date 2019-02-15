######## Shutil Exercises 2

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
print('If the directory does not exist, it will create a new one')
destiny_Dir = input()

# Program logic

os.chdir(str(working_Dir))
shutil.copytree(str(source_Dir), str(destiny_Dir))

####### End Shutil Exercises 2