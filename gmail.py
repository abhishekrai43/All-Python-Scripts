import time
import csv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

proxy_list = []

with open("proxies.txt", "r") as f:
    file_lines1 = f.readlines()
    for line1 in file_lines1:
        proxy_list.append(line1.strip())

link='https://www.gmail.com'

options = Options()  # Runs Chrome in headless mode.
options.add_argument('--no-sandbox')  # # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('--user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data')
options.add_argument('--profile-directory=Default')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path='C:/chromedriver.exe')

def get_gmail(proxy):

    options.add_argument('--proxy-server={}'.format(proxy))
    print("Using Proxy :", proxy)

    driver.get(link)
    time.sleep(30)



for proxy in proxy_list:
    print("Using Proxy :", proxy)
    get_gmail(proxy)





