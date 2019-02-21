######## Shutil Exercises 4

# Import modules and libraries

import os

# Defining global variables

working_Dir = None
folder_Name = None
sub_Folder = None
file_Names = None
file_Name = None

# User parameters

print('Define the working directory: ')
working_Dir = input()

# Program logic

os.chdir(str(working_Dir))

for folder_Name, sub_Folder, file_Names in os.walk(str(working_Dir)):
    print('The current folder is: ' + folder_Name)
    print('-------------------------------------------')
    for sub_Folder in sub_Folder:
        print('Subfolder of ' + folder_Name + ': ' + sub_Folder)
    for file_Name in file_Names:
        print('File inside ' + folder_Name + ': ' + file_Name)
    print('')

####### End Shutil Exercises 4
