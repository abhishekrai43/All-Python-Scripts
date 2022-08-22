import time
import csv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
header_added = False
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get('https://www.dice.com/jobs?q=data%20architect&location=New%20York,%20NY,%20USA&latitude=40.7127753&longitude=-74.0059728&countryCode=US&locationPrecision=City&adminDistrictCode=NY&radius=30&radiusUnit=mi&page=1&pageSize=20&language=en') #Enter URL here
time.sleep(3)

def get_data():
    global header_added
    for link in links:
        try:
            driver.execute_script('window.open(arguments[0]);', link)
            all_windows = driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            driver.switch_to.window(child_window)
            time.sleep(8)
            job_title = driver.find_element_by_class_name('jobTitle').text
            company = driver.find_element_by_id('hiringOrganizationName').text
            location = driver.find_element_by_class_name('location').text
            post_time = driver.find_element_by_class_name('posted').text
            job_desc = driver.find_element_by_id('jobdescSec').text
            link_p = driver.current_url
            dict1 = {"Job Title": job_title, "Company": company, "Location": location, "Full Details": job_desc,
                     "Posted": post_time,
                     "Job Link": link_p}
            with open(f'Dice_Jobs.csv', 'a+', encoding='utf-8-sig') as f:
                w = csv.DictWriter(f, dict1.keys())
                if not header_added:
                    w.writeheader()
                    header_added = True
                w.writerow(dict1)
        except:
            pass


        driver.close()
        driver.switch_to.window(parent_window)

links = driver.find_elements_by_xpath('//h5/a')
parent_window = driver.current_window_handle
get_data()
while True:
    try:
        driver.find_element_by_xpath('//li[@class="pagination-next page-item ng-star-inserted"]//a').click()
        time.sleep(5)
        links = driver.find_elements_by_xpath('//h5/a')
        parent_window = driver.current_window_handle
        get_data()
    except:
        print("All Jobs Found")
        driver.quit()
        break


