import requests
from bs4 import BeautifulSoup


page = requests.get('https://www.hl.co.uk/shares/shares-search-results/m/microsoft-corporation-com-stk-us$').text
soup = BeautifulSoup(page, 'html.parser')
imgs = soup.findAll('img')
for img in imgs:
    link = img['src']
    if 'chart' in link:
        r = requests.get(link, stream=True)
        if r.status_code == 200:
            with open('chart_x.png', 'wb') as f:
                for chunk in r:
                    f.write(chunk)

