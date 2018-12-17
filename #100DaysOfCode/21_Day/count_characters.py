# Importing external libraries

import pprint

# Defining global values

message = None
total_Len = None

# Defining functions

def counting_text(text_Len):
  
    count = {}

    for character in message:
      count.setdefault(character, 0)
      count[character] = count[character] + 1
    
    pprint.pprint(count)

# Input values

print('Please, type some text')
message = input()

# Processing data

counting_text(message)