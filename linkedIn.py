import csv
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

tor_proxy = "49.12.0.103:42775"
chrome_options = Options()
chrome_options.add_argument('--proxy-server=%s' % tor_proxy)
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', options=chrome_options)
driver.maximize_window()

header_added = False
salons = {}
driver.get("https://www.justdial.com/Noida/Salons/nct-10418299")
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="best_deal_div"]/section/span'))).click()
except:
    pass
def get_items():
    global header_added
    phones = []
    driver.execute_script("window.scrollBy(0, 2400)")
    divs = driver.find_elements_by_css_selector('div.col-sm-5.col-xs-8.store-details.sp-detail.paddingR0')

    for div in divs:
        phone = div.find_element_by_xpath('//*[@id="bcard0"]/div[1]/section/div[1]/p[2]/span/a/b').text
        phones.append(phone)

    for div, phone in zip(divs, phones):
        dict1 = {"Name and address": div.text, "Phone": phone}
        with open('Salons.csv', 'a+', encoding='utf-8') as f:
            w = csv.DictWriter(f, dict1.keys())
            if not header_added:
                w.writeheader()
                header_added = True
            w.writerow(dict1)
    driver.find_element_by_xpath('//a[@rel="next"]').click()

for i in range(5):
    get_items()
