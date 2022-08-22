import threading

import requests
import xlrd
import concurrent.futures
from bs4 import BeautifulSoup
import csv


header_added = False
file_location = "Urls.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
all_links = []
for row in range(9749, 12300):
     all_links.append(sheet.cell_value(row,0))
print(len(all_links))
i = 9749
def get_solution(url):
    global header_added, i, ques, ans, soup
    print("Solution", i)
    i += 1
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    try:
        ques_div = soup.find('p', class_='header-description')
        if not ques_div:
            p = soup.find('span', class_='puzzle-name').text
            if not p:
                ques_td = ques_div.findAll('td', class_='puzzle-name').text
                p = ques_td[0].text
        else:
            p = ques_div.find('span').text
        ques = p
        ans_divs = soup.findAll('div', class_='puzzle-solution')
        ans = ans_divs[0].text

    except:
        with open('errors.txt','a+') as f:
            f.write(url+'\n')



    dict1 = {"Words": ques, "Solution": ans}
    with open('balance.csv', 'a+', encoding='utf-8') as f:
        w = csv.DictWriter(f, dict1.keys())
        if not header_added:
            w.writeheader()
            header_added = True
        w.writerow(dict1)

for link in all_links:
    print(link)
    get_solution(link)
