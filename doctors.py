#Import Libs
import requests
from bs4 import BeautifulSoup
import csv
from random import randint
from time import sleep



header_added = False
def get_docs(base_url):
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    global header_added, z
    page1 = requests.get(base_url, headers=agent).text
    soup = BeautifulSoup(page1, 'html.parser')
    uls = soup.find('ul', class_='list-4-col')
    lis = uls.findAll('li')
    links = []
    names = []
    for li in lis:
        li_a = li.find('a')
        link = li_a['href']
        links.append(link)
        name = li_a.text
        names.append(name)
    for i in range(len(links)):
        try:
            url = 'https://www.doximity.com/'+links[i]
            doc_page = requests.get(url).text
            soup2 = BeautifulSoup(doc_page, 'html.parser')
            doc_name = names[i]
            print(doc_name)
            speciality = 'Oncology'

            try:
                edt = soup2.find('ul', class_="profile-sectioned-list training").text
            except:
                edt = 'No Education Details listed'
            try:
                cert_i = soup2.find('section', class_="certification-info").text
                cert = cert_i[26:]
            except:
                cert = 'No Certifications'

            profile_url = url
            dict1 = {"Name":doc_name, "Speciality": speciality,"Education & Training": edt, "Certifications & Licensure":cert, "Profile Link":profile_url}
            with open('Doc_ONC_missing_AZ.csv', 'a+', encoding='utf-8') as f:
                w = csv.DictWriter(f, dict1.keys())
                if not header_added:
                    w.writeheader()
                    header_added = True
                w.writerow(dict1)
            z += 1
            print("Doctor", z)
        except:
            pass
    return links

burl = 'https://www.doximity.com/directory/md/specialty/oncology?after=pub%2Famy-matecki-md'
g = get_docs(burl)
z = 500
while True:
    sleep(randint(10, 100))
    p_url = str(g[-1])
    url = 'https://www.doximity.com/directory/md/specialty/oncology?after=' + p_url[1:]
    print(url)
    g = get_docs(url)
