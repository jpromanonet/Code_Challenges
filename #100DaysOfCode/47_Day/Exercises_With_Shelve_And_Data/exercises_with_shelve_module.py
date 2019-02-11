# Importing libraries and modules

import shelve

# Declaring global variables

shelf_File = None
profile = None
export = None

# Program logic

shelf_File = shelve.open('my_profile_data')
profile = ('Coderx','21','Argentinian')

shelf_File['JuanPa'] = profile
shelf_File.close()

export = open('datos.xls','a')
export.write(str(profile))
export.close()
