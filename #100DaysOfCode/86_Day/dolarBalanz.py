# Importing libraries and frameworks

import requests

# Defining variables and setting parameters

jsonObject = " "
createJsonObject = " "
url = "https://api.balanz.com/v1/cotizacion/dolar/"
payload = "" 
headers = {
    'Accept': "application/json",
    'Authorization': "A2D3585C-F97D-424D-842F-42DD0DEC02AC",
    'Host': "api.balanz.com",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

# Program logic

 ## Getting dollar value
dolarActual = requests.request("GET", url, data=payload, headers=headers)

 ## Saving the object
jsonObject = dolarActual.text

 ## Creating JSON 
createJsonObject = open('dolar.json', 'w')
createJsonObject.write(str(jsonObject))
createJsonObject.close()