#! python3
# downloadXkcd.py - Downloads every single XKCD comic

# Import libraries and frameworks

import requests
import os
import bs4 

# Declaring variables

url = ''

# Program logic

    ## Starting URL
url = 'http://xkcd.com'

    ## Store comics in ./xkcdComics
os.makedirs('xkcdComics', exist_ok=True)  

