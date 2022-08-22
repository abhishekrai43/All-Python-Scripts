from selenium import webdriver
import csv
import time
import pandas as pd
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
url = 'https://www.groupemichel.com/vehicules?field_etat_value=Occasion&carrosserie_selective=All&marque_selective=All&modele_selective=All&field_energie_target_id_entityreference_filter=All&field_transmission_target_id_entityreference_filter=All&field_prix_value[min]=&field_prix_value[max]=&field_kilometrage_value[min]=&field_kilometrage_value[max]=&page=7'
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
        pub_time = driver.find_element_by_xpath('//meta[@property="article:published_time"]').get_attribute('content')
        mod_time = driver.find_element_by_xpath('//meta[@property="article:modified_time"]').get_attribute('content')
        name_div = driver.find_element_by_css_selector('div.modeleGM')
        car_name = name_div.find_element_by_tag_name('h1').text
        car_sub_name = name_div.find_element_by_tag_name('h2').text
        price = driver.find_element_by_css_selector('div.prixGM').text
        mileage = driver.find_element_by_css_selector('p.kilometres').text
        features = driver.find_elements_by_xpath('//p[@class="texteCaracteristiques"]')
        release = features[0].text
        fuel = features[1].text
        power = features[2].text
        guarantee = features[3].text
        transmission = features[4].text
        color = features[5].text
        model_year = features[6].text
        number_vo = features[8].text
        address = driver.find_element_by_css_selector('div.ficheConcession').text
        dict1 = {"Published Time": pub_time, "Modified Time": mod_time, "Car Name": car_name, "Car Sub Name": car_sub_name, "Price": price, "Mileage": mileage, "Release": release, "Energy": fuel, "Power": power, "Guarantee": guarantee, "Transmission" :transmission, "Color": color, "Year": model_year, "Number": number_vo, "Address": address}
        with open(f'Car_Details2.csv', 'a+', encoding='utf-8-sig') as f:
            w = csv.DictWriter(f, dict1.keys())
            if not header_added:
                w.writeheader()
                header_added = True
            w.writerow(dict1)
        driver.close()
        driver.switch_to.window(parent_window)



for _ in range(113):
    divs = driver.find_elements_by_css_selector('div.relative')
    links = []
    for div in divs:
        link = div.find_element_by_tag_name('a')
        links.append(link)
    get_data()
    links.clear()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    next = driver.find_element_by_xpath('//*[contains(text(),"suivant")]')
    driver.execute_script("arguments[0].click();", next)
    time.sleep(2)





