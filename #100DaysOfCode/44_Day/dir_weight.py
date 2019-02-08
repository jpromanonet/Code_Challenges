# Calling librares and modules

import os

# Defining variables

total_Size = 0
dir = None

# Defining Functions

# Defining logic

print('''Input DIR: ''')
dir = input()

for filename in os.listdir(dir):
      total_Size = total_Size + os.path.getsize(os.path.join(dir, filename))

print(total_Size)
