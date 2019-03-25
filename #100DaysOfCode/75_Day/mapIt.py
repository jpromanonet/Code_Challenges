#! python3

# mapIt.py - Launches a map in the browser using an address from the 
# command line or clipboard

# Importing libraries and frameworks

import webbrowser
import sys

# Defining global variables

address = None

# Program Logic

if len(sys.argv) > 1:
    ## Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)