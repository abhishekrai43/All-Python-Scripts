import csv
import multiprocessing

import requests
import xlrd
from bs4 import BeautifulSoup

sess = requests.Session()


def get_solution(url):
    try:
        print(url)
        resp = sess.get(url)
        resp.raise_for_status()
        page = resp.text
        soup = BeautifulSoup(page, "html.parser")
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
        return {"URL": url, "Words": ques, "Solution": ans, "Error": ""}
    except Exception as exc:
        print(url, "Error:", exc)
        return {"URL": url, "Words": "", "Solution": "", "Error": str(exc)}


def read_links(file_location):
    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_index(0)
    all_links = []
    for row in range(12290, 114212):
        all_links.append(sheet.cell_value(row, 0))
    return all_links


def main():
    links = read_links("./Urls.xlsx")
    with open("BtoZ.csv", "w", encoding="utf-8") as f:
        with multiprocessing.Pool() as p:  # (or multiprocessing.pool.ThreadPool)
            for i, result in enumerate(p.imap_unordered(get_solution, links, chunksize=16)):
                if i == 0:
                    writer = csv.DictWriter(f, result.keys())
                    writer.writeheader()
                writer.writerow(result)
                f.flush()  # Ensure changes are written immediately
                if i % 100 == 0:  # Progress indicator
                    print(i)


if __name__ == "__main__":
    main()