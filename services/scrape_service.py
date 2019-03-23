import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/wiki/Yoga')

soup = BeautifulSoup(response.text, 'html.parser')

scrapes = soup.find_all(class_ ='mw-body-content')

print(scrapes)
