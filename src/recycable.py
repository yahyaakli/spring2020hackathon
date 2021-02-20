import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://solar.world.org/weo/recycle"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

items = soup.find_all('a')
nolinks_items = []
for item in items:
    if 'http' not in item.get('href'):
        nolinks_items.append(item.string)

print(nolinks_items)