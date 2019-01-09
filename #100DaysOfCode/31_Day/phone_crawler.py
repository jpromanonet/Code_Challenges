# Importing libraries

import re

# Defining global values

telephone_Number = None
result = None
match_Object = None

# Defining functions

def isPhoneNumber(text):

    if len(text) != 9:
        return False
       
    if text[4] != '-': 
        return False
        
    phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d\d')
    match_Object = phoneNumRegex.search(text)
    print('Phone number found: ' + match_Object.group())

# Script logic

print('Insert a text with a phone number to set apart.')
telephone_Number = input()

result = isPhoneNumber(str(telephone_Number))