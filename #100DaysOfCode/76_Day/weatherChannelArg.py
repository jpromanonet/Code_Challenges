#! python3

# weatherChannelArg.py lets u choose a province to show the temperature in the WeatherChannel website 
# or the temperature in the place you currently are.

# Importing libraries and frameworks

import webbrowser
import os
import sys
import datetime

# Creating global variables

weatherArea = None # it's the area that the user select to watch.

# Defining list and values

weatherArea = [
    'https://weather.com/es-AR/',
    'https://weather.com/es-AR/tiempo/hoy/l/-54.81,-68.32'
]

# Defining functions

# User parameters

# Program logic