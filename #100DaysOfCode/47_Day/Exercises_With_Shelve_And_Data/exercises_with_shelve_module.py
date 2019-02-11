# Importing libraries and modules

import shelve

# Declaring global variables

shelf_File = None
profile = None

# Program logic

shelf_File = shelve.open('my_profile_data')
profile = ('Coder','25','Argentinian')

shelf_File['JuanP'] = profile
shelf_File.close()
