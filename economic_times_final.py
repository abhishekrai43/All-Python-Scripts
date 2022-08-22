import requests
from bs4 import BeautifulSoup
import pandas as pd
header_added = False
titles = []
authors = []
times = []
descs = []
verticals = []
links = []
url = 'https://economictimes.indiatimes.com/archivelist/year-2018,month-1,starttime-43101.cms'
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')
divs = soup.findAll('ul', class_='content')
for div in divs:
    lis = div.findAll('a')
    for link in lis:
        links.append(link['href'])
print(len(links))