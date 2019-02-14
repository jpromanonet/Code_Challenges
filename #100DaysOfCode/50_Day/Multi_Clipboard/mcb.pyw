#! python3


# mcb.pyw - Saves and loads pieces of text to the clipboard

# USAGE: py mcb.pyw save <keyword> | Saves clipboard to keyword
#		 py mcb.pyw list | Loads all keywords to clipboard
#		 py mcb.pyw delete <keyword> | Delete keyword from clipboard
#		 py mcb.pyw celar | Delete all keywords from clipboard

# Importing libraries and frameworks

import shelve
import pyperclip
import sys
import os

# Defining global variables
 
mcb_Shelf = shelve.open('mcb')
command = sys.argv[1].lower()
 
# Program Logic

	# Save option
if command == 'save':
    mcb_Shelf[sys.argv[2]] = pyperclip.paste()
	# List options
elif command == 'list':
    print("\n".join(mcb_Shelf.keys()))
	# Delete one item option
elif command == 'delete':
    del mcb_Shelf[sys.argv[2]]
	# Clear full list
elif command == 'clear':
    mcb_Shelf.clear()
else:
    pyperclip.copy(mcb_Shelf[sys.argv[1]])

mcb_Shelf.close()