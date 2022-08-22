import requests
from bs4 import BeautifulSoup

agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'} #using agent to solve the blocking issue
url = 'http://iir.circ.gov.cn/'
page = requests.get(url, headers=agent).text
soup = BeautifulSoup(page, 'html.parser')
img = soup.findAll('div')
for im in img:
    print(im.text)

