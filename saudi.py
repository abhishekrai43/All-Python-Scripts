import csv
import time
from selenium import webdriver
import pandas as ad
import matplotlib.pyplot as plt

# create an instance of browser
driver_path = 'C:/chromedriver.exe'
driver = webdriver.Chrome('C:/chromedriver.exe')

# creating a dictionary for storing the information after scraping
jobs = {"roles": [],
        "companies": [],
        "locations": [],
        "experience": []}

# we will iterate over first 50 pages; each page contains 20 results
# for each job we will scrape the role,company, location, experience, key skills.
header_added = False
for i in range(10):

    driver.get("https://www.naukrigulf.com/data-scientist-jobs-in-saudi-arabia-{}".format(i))
    driver.maximize_window()
    time.sleep(3)
    driver.implicitly_wait(10)
    role = driver.find_elements_by_xpath('//h2[@class="info-position logo-true web-job"]')
    company = driver.find_elements_by_xpath('//div[@class="has-logo"]')
    location = driver.find_elements_by_xpath('//span[@class="info-loc has-logo"]')
    exp = driver.find_elements_by_xpath('//span[@class="info-exp has-logo"]')
    for rol, com, lo, ex in zip(role, company, location, exp):
        dict1 = {'Role': rol.text, "Company": com.text, "Location": lo.text, "Experience": ex.text}
        with open('SaudiJobs.csv', 'a+', encoding='utf-8-sig') as f:
            w = csv.DictWriter(f, dict1.keys())
            if not header_added:
                w.writeheader()
                header_added = True
            w.writerow(dict1)