#! python3

# lucky.py | Open several Google search results

# Import libraries and frameworks

import requests
import webbrowser
import bs4
import sys

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

