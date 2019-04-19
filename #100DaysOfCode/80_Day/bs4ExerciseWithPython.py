# importing libraries and frameworks

import requests
import bs4

# Declaring variables

res = requests.res('http://nostartch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)
