import requests
import time
import csv
import timeit
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import urllib.parse

zip_add = '10011'
start_time = time.perf_counter()
print("Starting at ", start_time)
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get('https://locator.infusioncenter.org/')
time.sleep(2)
driver.find_element_by_id('who').click()
time.sleep(2)
choice1 = driver.find_elements_by_tag_name('li')
choice1[8].click()
time.sleep(2)
driver.find_element_by_id('what').click()
choice2 = driver.find_elements_by_tag_name('li')
choice2[2].click()
time.sleep(2)
driver.find_element_by_id('why').click()
choice3 = driver.find_elements_by_tag_name('li')
choice3[2].click()
time.sleep(2)
driver.find_element_by_xpath('//button[@type="submit"]').click()
time.sleep(10)
search = driver.find_element_by_xpath('//input[@name="search"]')
search.send_keys(zip_add)
search.send_keys(Keys.ENTER)
time.sleep(10)
header_added = False
def get_address():
    global text1, lat, long, header_added
    divs = driver.find_elements_by_xpath('//div[@class="locator-result-container"]')
    print(len(divs))
    for div in divs[:5]:
        text1 = div.text
        splits = text1.split('\n')
        address = splits[-1]
        print(address)
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
        lat_long_url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) + '?format=json'
        lat_long = requests.get(url=lat_long_url, headers=headers).json()
        lat = lat_long[0]["lat"]

        long = lat_long[0]["lon"]

        dict1 = {"Name and Address": text1, "Latitude": lat, "Longitude": long}
        with open(f'Infusion_t{zip_add}.csv', 'a+', encoding='utf-8-sig') as f:
            w = csv.DictWriter(f, dict1.keys())
            if not header_added:
                w.writeheader()
                header_added = True
            w.writerow(dict1)
        f.close()
    return True


def get_info():
    global header_added
    header_added = False
    global me, sp
    try:
        links = driver.find_elements_by_xpath('//div[@class="locator-results-container"]//a')
        parent_window = driver.current_window_handle
        for link in links[:5]:
            driver.execute_script('window.open(arguments[0]);', link)
            all_windows = driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            driver.switch_to.window(child_window)
            meds_divs = WebDriverWait(driver, 25).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.medication.lato')))
            meds = [med.text for med in meds_divs]
            specs_divs = driver.find_elements_by_css_selector('div.specialty.lato')
            specs = [spec.text for spec in specs_divs]
            for me, sp in zip(meds, specs):

                with open(f'(Infusion_final{zip_add}.csv', 'w', encoding='utf-8-sig', newline='') as f:
                    w = csv.writer(f)
                    w.writerow(['Medicines', 'Specalities'])  # replace colX with the names of the original columns
                    for me, sp in zip(meds, specs):
                        print(me, sp)
                        with open(f'Infusion_t{zip_add}.csv', 'r') as read:
                            reader = csv.reader(read)
                            for row in reader:
                                row.append(me)
                                row.append(sp)
                                w.writerow(row)
                f.close()
            driver.close()
            driver.switch_to.window(parent_window)
    except Exception as e:
        raise e

if get_address():
    p = get_info()
    driver.quit()
    print (time.perf_counter() - start_time, "seconds")
