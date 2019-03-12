#! python3

# minimalLogger.py creates a tagged log with a nice format in .html files to simple read and publish

## Calling libraries and frameworks

import random
import os
import datetime

## Defining global variables

userLog = None # Gonna be the user input to concatenate with the htmlStr
htmlStr = None # Gonna be the HTML body
logFileName = None # It's the name with the date
randomCode = 0 # It's the unique ID number of every file.
workingDir = None # It's the dir where the user is gonna save the log file.

## User parameters

print('Please introduce the working directory: ')
workingDir = input()
print(' ')
print('Start writing your log: ')
userLog = input()

## Program Logic

logFileName = datetime.datetime.now().strftime("%Y-%m-%d") # Establish the filename to the date it's create

    # Creating the HTML body structure | Start 

htmlStr = ''' 
            <DOCTYPE! html>
                <html>
                    <head>
                        <title>LOG: ''' + logFileName + '''</title>

                            <!-- Latest compiled and minified CSS -->
                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

                            <!-- Optional theme -->
                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

                            <!-- Latest compiled and minified JavaScript -->
                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
                    </head>
                    <body>
                        <h1 class="bg-primary"> This is a test!</h1>'''+ userLog + ''' 
                    </body>
                </html>
          '''

htmlFile= open(logFileName+'.html',"w")
htmlFile.write(str(htmlStr))
htmlFile.close()