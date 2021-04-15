# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 17:30:30 2021

@author: Professional
"""

# 34-dars JSON
# muallif AQR /////13/04/2021''''''''''''17:32 tm,,,,,,,,,,,


import json
import googlemaps
from apikey import APIKEY

## GoogleMaps
gmaps =  googlemaps.Client(key=APIKEY)

data = gmaps.geocode('Olmazor, Toshkent, Uzbekiston')

#print(geocode_result)

g = json.dumps(data[0], indent = 4, sort_keys=True)
print(g)

#data = geocode_result[0]
#kenglik = data['geometry']['location']['lat']
#uzunlik = data['geometry']['location']['lng']
#print(f"{kenglik},{uzunlik}")
