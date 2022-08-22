from selenium import webdriver
import csv
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException


driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
url = 'https://www.bpmgroup.fr/voitures/occasion/?price.min=5500'
driver.get(url)
time.sleep(3)
def get_data():
    global header_added
    header_added = False
    parent_window = driver.current_window_handle
    for link in links:
        driver.execute_script('window.open(arguments[0]);', link)
        all_windows = driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        driver.switch_to.window(child_window)
        time.sleep(3)
        mod_time = driver.find_element_by_xpath('//meta[@property="article:modified_time"]').get_attribute('content')
        name_div = driver.find_element_by_class_name('vehicle-heading__brand-details')
        name = name_div.find_element_by_tag_name('h1').text
        sub_name = name_div.find_element_by_tag_name('p').text
        price = driver.find_element_by_css_selector('span.js-price-val.price__val.title--p-2').text
        features = driver.find_elements_by_xpath('//span[@class="feature-content__value"]')
        mileage = features[0].text
        category = features[1].text
        energy = features[2].text
        transmission = features[3].text
        color = features[4].text
        release = features[5].text
        p_real = features[6].text
        p_fiscal = features[7].text
        address = driver.find_element_by_css_selector('div.dealer-contacts__info.u-padding-l').text
        dict1 = {"Modified Time": mod_time, "Car Name": name, "Category": category,
                 "Car Sub Name": sub_name, "Price": price, "Mileage": mileage, "Release": release, "Energy": energy,
                 "Transmission": transmission, "Color": color,
                 "P.real(ch)": p_real, "P.fiscal(CV)": p_fiscal, "Address": address}
        with open(f'New_Car_Details.csv', 'a+', encoding='utf-8-sig') as f:
            w = csv.DictWriter(f, dict1.keys())
            if not header_added:
                w.writeheader()
                header_added = True
            w.writerow(dict1)
        driver.close()
        driver.switch_to.window(parent_window)


for n in range(2, 52):
    divs = driver.find_elements_by_tag_name('article')
    links = []
    for div in divs:
        link = div.find_element_by_tag_name('a')
        links.append(link)
    get_data()
    links.clear()
    driver.get(f'https://www.bpmgroup.fr/voitures/occasion/?currentPage={n}&offset=30&price.min=5500')
