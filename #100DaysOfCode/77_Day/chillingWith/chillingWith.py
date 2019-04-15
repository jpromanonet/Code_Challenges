#! python3

# chillingWith.py it's an app to list the series and movies pending to watch where you could rate them after.

# --------------------------------------------------------------------------------------------------------------

# Calling libraries and frameworks

import random
import os
import datetime
import shelve
import sys

# Declaring global variables

    ## Input user parameters, DB(shelf file) and front-end doc construction environment variables.

    ## Movies parameters
movieTitle = ''
releaseYear = ''
orderInSaga = ''
pendingMovie = ''

    ## Series parameters
serieTitle = ''
numberOfSeasons = ''
startedYear = ''
numberOfChapters = ''
pendingSerie = ''

    ## DB Files
moviesFile = ''
seriesFile = ''

    ## FrontEnd Files

finalHtmlFile = ''

# Declaring functions

    ## Movies Functions

def addMovie(title, releaseDate, sagaNumber, pendingToWatch):
    moviesFile = shelve.open('moviesDB')
    movieTitle = title
    moviesFile[movieTitle] = [title, releaseDate, sagaNumber, pendingToWatch]
    moviesFile.close()

def deleteMovie(title):
    movieTitle = title
    moviesFile = shelve.open('moviesDB')
    del moviesFile[movieTitle]
    moviesFile.close()

    ## Series Functions

def addSeries(title, seasons, releaseDate, chapters, pendingToWatch):
    seriesFile = shelve.open('seriesDB')
    serieTitle = title
    seriesFile[serieTitle] = [title, seasons, releaseDate, chapters, pendingToWatch]
    seriesFile.close()

def deleteSeries(title):
    serieTitle = title
    seriesFile = shelve.open('seriesDB')
    del seriesFile[serieTitle]
    seriesFile.close()

# Program logic

print('Insert title: ')
movieTitle = input()
print("Insert Release Date: ")
release = input()
print('''Insert order in the movie saga (if it's a solo movie, leave it blank)''')
orderInSaga = input()
print('Pending to watch? y/n ')
toWatch = input()

addMovie(movieTitle, release, orderInSaga, toWatch)