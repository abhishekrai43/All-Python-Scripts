import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import concurrent.futures
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random

proxy_list = []

with open("proxies.txt", "r") as f:
    file_lines1 = f.readlines()
    for line1 in file_lines1:
        proxy_list.append(line1.strip())



links=['https://www.snapchat.com/add/co.ducks',
'https://www.snapchat.com/add/rebekkaoulie',
'https://www.snapchat.com/add/derrengt',
'https://www.snapchat.com/add/vaumurtch',
'https://www.snapchat.com/add/akseltrefall']
options = Options()  # Runs Chrome in headless mode.
options.add_argument('--headless')
options.add_argument('--no-sandbox')  # # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
i_list = list(range(100))
def get_screenshot(link, i, proxy):

    _start = time.time()

    options.add_argument('--proxy-server={}'.format(proxy))

    driver = webdriver.Chrome(options=options, executable_path='C:/chromedriver.exe')
    driver.get(link)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By. CLASS_NAME,'css-1motqmv')))
    driver.save_screenshot(f'screenshot-headless{i}.png')
    driver.quit()
    _end = time.time()
    i += 1

    print('Total time for headless {}'.format(_end - _start))


