#! python3

# DirStats counts your files trought the time and make statistics based in dirs grow.

# Importing frameworks and librearies

import os
import sys

# Declaring global variables

files_Counter = 0
path_To_Count = None

# Declaring functions

def fileCount(amount):
    for filename in os.listdir(path_To_Count):
        files_Counter = files_Counter + 1

# User parameters

# Program Logic
