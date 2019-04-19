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

    ## Input user parameters
optionMenu = ''

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
    moviesFile[movieTitle] = {'Title: ':title, 'Year: ':releaseDate, 'Movie N° ':sagaNumber, 'Peding: ':pendingToWatch}
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

# User parameters

print('Select an option: ')
print('')
print('---------------------')
print('Add a movie........ 1')
print('')
print('Add a serie........ 2')
print('')
print('---------------------')
print('Delete a movie..... 3')
print('')
print('Delete a serie..... 4')
print('')
print('---------------------')
print('Open List.......... 5')
print('---------------------')
print('Close.............. 6')
optionMenu = input()

# Program logic
#if (optionMenu == '1'):
    #addMovie()