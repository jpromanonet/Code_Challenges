#! python3

# minimalLogger.py creates a tagged log with a nice format in .html files to simple read and publish

# --------------------------------------------------------------------------------------------------------------

# Calling libraries and frameworks

import random
import os
import datetime

# Defining global variables

userInputLog = None # Gonna be the user input to concatenate with the htmlStr
fullInputLog = None # It takes the userInputLog and adds bootstrap style
htmlStr = None # Gonna be the HTML body without end tags
htmlStrEndTags = None # Gonna be the HTML end tags
logFileName = None # It's the name with the date
logDateTime = None # Datetime of every log
randomCode = 0 # It's the unique ID number of every file.
fullFileName = None # It's the sum of logFileName and randomCode
workingDir = None # It's the dir where the user is gonna save the log file.
keepLogging = True # Value = False stop logging
option = None # Conditional choose to keep writing or not

# User parameters

print('Please introduce the working directory: ')
workingDir = input()
os.chdir(str(workingDir))
print(' ')

# Program Logic

    ## Creating the filename 
logFileName = datetime.datetime.now().strftime("%Y-%m-%d") # Establish the filename to the date it's create
randomCode = random.randint(1,10000000) # It's create the serial random number to validate the file
fullFileName = str(logFileName) + '_(Sn#' + str(randomCode) + ').html' # Full file name

    ## Creating the HTML body structure | Without end tags

htmlStr = ''' 
            <DOCTYPE! html>
                <html>
                    <head>
                        <title>LOG: ''' + fullFileName + '''</title>

                            <!-- Latest compiled and minified CSS -->
                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

                            <!-- Optional theme -->
                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

                            <!-- Latest compiled and minified JavaScript -->
                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
                    </head>
                    <body>
                        <header class="bg-primary">
                            <div class="container">
                                <div class="row">
                                    <div class="col-lg-12 col-md-12 col-sm-12 col-sx-12">
                                        <center>
                                            <h1 class><b>FULL LOG | '''+str(logFileName)+''' | Sn: '''+str(randomCode)+'''</b></h1>
                                        </center> 
                                    </div>
                                </div>
                            </div>
                        </header>
                        <main>
                            <div class="container">
                                <div class="row">'''

    ## Creating the HTML body structure | End Tags to close the document

htmlStrEndTags = '''        </div>
                        </div>
                    </main>
                    <footer class="bg-info">
                    </footer>
                </body>
            </html>'''

    ## Here starts the HTML document
htmlFile= open(fullFileName,"w")
htmlFile.write(str(htmlStr))

    ## Here starts the loggin module
while keepLogging == True:
        ### Creating the log header
    logDateTime = datetime.datetime.now().strftime("%Y-%m-%d at %H:%M:%S")
        ### User input log
    print('Start writing your log: ')
    userInputLog = input()
        ### Now it creates the log input with the style and the user input
    fullInputLog = '''</br></br>
                    <div class = "col-lg-12 col-md-12 col-sm-12 col-sx-12">
                        <div class="panel panel-success">
                            <div class="panel-heading">Log time: <b>'''+logDateTime+'''</b></div>'''+userInputLog+'''</div>
                    </div>'''
    htmlFile.write(str(fullInputLog))
        ### Ask if the user wants to keep adding logs
    print(' ')
    print('Do you want to keep writing? y/n')
    option = input()
    if option == 'y':
        keepLogging = True
    elif option == 'Y':
        keepLogging = True
    else:
        break

    ## Here ends the HTML document
htmlFile.write(str(htmlStrEndTags))
htmlFile.close()