# Importing libraries

import re

# Defining global values

telephone_Number = None
result = None

# Defining functions

def isPhoneNumber(text):

    if len(text) != 9:
        return False
       
    for i in range(0, 3):
        phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d\d')
        if not text[i].isdecimal():
            return False
        if text[4] != '-':
            return False

# Script logic

print('Insert a telephone number')
telephone_Number = input()

result = isPhoneNumber(str(telephone_Number))

if result == True:
    print(telephone_Number + ' is a telephone number!')
else:
    print('Please insert a valid number')