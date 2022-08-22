import csv
import re
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
header_added = False
header_added1 = False
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
url ='https://pubmed.ncbi.nlm.nih.gov/?linkname=pubmed_pubmed&from_uid=28958615'
page = driver.get(url)
articles = driver.find_elements_by_xpath('//a[@class="docsum-title"]')
articles = articles[:2]
parent_window = driver.current_window_handle
names_l = []
text_l = []
for article in articles:
    driver.execute_script('window.open(arguments[0]);', article)
    driver.maximize_window()
    all_windows = driver.window_handles
    child_window = [window for window in all_windows if window != parent_window][0]
    driver.switch_to.window(child_window)
    time.sleep(3)
    title = driver.find_element_by_class_name('heading-title')

    expand = driver.find_element_by_class_name('inline-authors')
    names = expand.find_elements_by_class_name('full-name')
    for name in names:
        names_l.append(name.text)
    main_div = driver.find_element_by_xpath('//*[@id="toggle-authors"]').click()
    time.sleep(1)
    div = driver.find_element_by_class_name('item-list')
    descs = div.find_elements_by_tag_name('li')
    for desc in descs:
        if '@' in desc.text:
            emails = re.findall(r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)',desc.text)
            for email in emails:
                print(desc.text)
                dict1 = {"Title": title.text, "Email": email, "Affiliation": desc.text}
                with open(f'Pub_med.csv', 'a+', encoding='utf-8') as f:
                    r = csv.reader(f)
                    w = csv.DictWriter(f, dict1.keys())
                    if not header_added:
                        w.writeheader()
                        header_added = True
                    w.writerow(dict1)
                    num = desc.text[0]

    driver.refresh()
    time.sleep(3)
    divs = driver.find_elements_by_class_name('authors-list-item ')
    for div in divs:
        name = div.find_element_by_class_name('full-name')
        sup = div.find_element_by_class_name('affiliation-links')
        if num in sup.text:
            auth_name = name.text
            dict2 = {"Name": name.text}
            with open(f'Pub_med.csv', 'a+', encoding='utf-8') as f:
                w = csv.writer(f)
                for row in dict2:
                    w.writerow([dict2["Name"], dict2[1]])
            break


    driver.close()
    driver.switch_to.window(parent_window)

