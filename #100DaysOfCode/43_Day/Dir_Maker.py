# Defining global variables

new_Dir = None
working_Dir = None
full_Dir = None

# Importing libraries

import os

# Defining the script logic

working_Dir = os.getcwd()

print('Choose a name for your new folder')
new_Dir = input()

full_Dir = working_Dir+'/'+new_Dir

print('Creating' + full_Dir)

os.makedirs(full_Dir)
