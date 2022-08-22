import csv
import re
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


url = 'https://www.premierleague.com/match/59001'
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get(url)
time.sleep(5)
date =driver.find_element_by_xpath('//*[@id="mainContent"]/div/section[2]/div[2]/section/div[1]/div/div[1]/div[1]')
print(date.text)
