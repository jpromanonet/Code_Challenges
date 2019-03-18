#! python3

# dictio.py it's a simple webscrapping online dictionary

# Importing libraries and frameworks

import webbrowser

# Creating global variables

searchWord = None # The word that the user is gonna search.
fullSearchPath = None # Sum of the dictio path and the key search word.
selectBrowser = None # Choose the browser to open the web.

# User parameters

    ## Selecting the browser
print('Which browser do you want to use?')
print(' ')
print('Chrome... 1')
print('Firefox.. 2')
print('Default.. 3')
selectBrowser = input()

    ## Input of the word to search in the dictionary
print('What word do you want to search?')
searchWord = input() # Word the user wants to search
fullSearchPath = ('https://www.dictionary.com/browse/'+str(searchWord)) # Full path with the word to search.

# Program logic

    ## Conditional to select the browser, open it and search the word meaning.

        ### Chrome
if selectBrowser == '1':
    webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s').open(fullSearchPath)

        ### Firefox
if selectBrowser == '2':
    webbrowser.get('"C:/Program Files/Mozilla Firefox/firefox.exe" %s').open(fullSearchPath)

        ### Default browser(recommended for Linux)
if selectBrowser == '3':
    webbrowser.open(fullSearchPath)