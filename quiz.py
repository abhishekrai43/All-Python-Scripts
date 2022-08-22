import itertools
import requests
from bs4 import BeautifulSoup
import csv
import concurrent.futures
import xlrd


'''alpha_list = ['A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']


def get_links(alphabet):
    print(f"Getting {alphabet} numbers")
    page = requests.get(f'https://www.motscroises.fr/lettre/{alphabet}').text
    soup = BeautifulSoup(page, 'html.parser')
    main_div = soup.find('div', class_='search-result-box')
    lis = main_div.findAll('li')
    semis = []
    link_append = []
    for li in lis:
        a_tag = li.find('a')
        brack = a_tag.text
        bra = brack.split('-')
        semi = bra[0]
        semis.append(semi)
    for se in semis:
        new = se.split('[')
        print(new)
        news = new[1]
        link_append.append(news[1:])

    return link_append


questions_links = []
questions_links = questions_links[4134:]

def get_questions(alph, link):
    print(f"Getting {alph} {link} questions")
    global questions_links
    page = requests.get(f'https://www.motscroises.fr/lettre/{alph}/{link}').text
    soup = BeautifulSoup(page, 'html.parser')
    ques = soup.findAll('div', class_='questions')
    for que in ques:
        asn = que.text
        print(asn)
        questions_links.append(asn.upper())


full_link_list = []


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    result = executor.map(get_links, alpha_list)
    full_link_list.append(result)


merged = list(itertools.chain(*full_link_list))

for index, alpha in enumerate(alpha_list):
    for number in merged[index]:
       get_questions(alpha, number)


header_added = False
i = 39802

'''
file_location = "Urls.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
all_links = []
for row in range(1, 10001):
     all_links.append(sheet.cell_value(row,0))

i = 0
def get_solution(url):
    global header_added, i
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    ques_div = soup.find('p', class_='header-description')
    ques = ques_div.find('span').text
    ans_divs = soup.findAll('div', class_='puzzle-solution')
    ans = ans_divs[0].text
    print("Solution ", i)
    i += 1
    dict1 ={"Words": ques, "Solution": ans}
    with open('Puzzle10k.csv', 'a+', encoding='utf-8') as f:
        w = csv.DictWriter(f, dict1.keys())
        if not header_added:
            w.writeheader()
            header_added = True
        w.writerow(dict1)



with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
    result = executor.map(get_solution, all_links)





