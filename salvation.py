import json
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
state = 'Michigan'
def get_data(state):

    driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    driver.get('https://www.salvationarmyusa.org/usn/')
    driver.maximize_window()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[4]/div').click()
    time.sleep(1)
    search = driver.find_element_by_xpath('//input[@name="query"]')
    search.send_keys(state)
    search.submit()
    div = driver.find_element_by_id('gdos_results')
    links = div.find_elements_by_tag_name('a')
    parent_window = driver.current_window_handle
    for link in links:
        driver.execute_script('window.open(arguments[0]);', link)
        all_windows = driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        driver.switch_to.window(child_window)
        time.sleep(5)

        names_list = []
        names = driver.find_elements_by_tag_name('h3')
        for name in names:
            ntxt = names_list.append(name.text)


        tables = driver.find_elements_by_tag_name('table')
        addresses = []
        for table in tables:
            address = table.find_element_by_class_name('centerdetails')
            fadd = address.text.replace('\n','')
            addresses.append(fadd)
        stores_list = []
        for name , address in zip(names_list, addresses):
            record = {'Store Name': name, 'Store Address': address}
            stores_list.append(record)

        f = open('output.json', 'w')
        # f.write(json.dumps(all_jobs)) # all in one line
        f.write(json.dumps(stores_list, indent=2))
        f.close()


get_data(state)


























