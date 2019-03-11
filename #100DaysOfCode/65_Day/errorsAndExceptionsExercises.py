# Exercise 1

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

print(symbol * width)

for i in range(height - 2):
    print(symbol + (' ' * (width - 2)) + symbol)
print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))

# End Exercise 1

# Exercise 2

import traceback

def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

spam()

# End Exercise 2

# Exercise 3

import traceback

try:
         raise Exception('This is the error message.')
except:
         errorFile = open('errorInfo.txt', 'w')
         errorFile.write(traceback.format_exc())
         errorFile.close()
         print('The traceback info was written to errorInfo.txt.')

# End Exercise 3

# Exercise 4

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stopLight):
    for key in stopLight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stopLight[key] == 'yellow':
            stopLight[key] = 'red'
        elif stopLight == 'red':
            stopLight[key] = 'green'

switchLights(market_2nd)

# End exercise 4