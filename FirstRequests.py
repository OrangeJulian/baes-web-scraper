# FirstRequests.py
# Accessing Star Wars API to find information on SW universe.
# "Bae's Theorem" - Team Name


import requests
from bs4 import BeautifulSoup

#planets = []

# url = "http://swapi.co/api/planets/1/"

# for i in range(1,
# 	61):

# 	url = "http://swapi.co/api/people/"+str(i)+"/"

# 	sw = requests.get(url)
# 	planets.append(sw.text)

# for i in range(60):
# 	print(planets[i])


url1 = "http://pinchofyum.com/recipes"

r = requests.get(url1)

print(r.text)