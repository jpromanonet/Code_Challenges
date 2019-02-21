######## Shutil Exercises 4

# Import modules and libraries

import os

# Defining global variables

working_Dir = None

# User parameters

print('Define the working directory: ')
working_Dir = input()

# Program logic

os.chdir(str(working_Dir))

for folderName, subfolder, filenames in os.walk(str(working_Dir)):
    print('The current folder is: ' + folderName)
    print('-------------------------------------------')
    for subfolder in subfolder:
        print('Subfolder of ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('File inside ' + folderName + ': ' + filename)
    print('')

####### End Shutil Exercises 4
