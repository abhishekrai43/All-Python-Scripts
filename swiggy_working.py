import csv
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from csv import reader
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


chrome_options = Options()
scroll = 5
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
header_added = False
header_added1 = False
url = "https://www.swiggy.com/restaurants"
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', options=chrome_options)
driver.maximize_window()

driver.get(url)
time.sleep(3)
search_city = input("Enter the city :")
res_n = input("Enter the Restaurant's name :")
search = driver.find_element_by_xpath('//input[@name="location"]').send_keys(search_city)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[3]/div[1]/span[2]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/header/div/div/ul/li[5]/div/a/span[1]').click()
time.sleep(1)
search_res = driver.find_element_by_class_name('_2BJMh').send_keys(res_n.lower())
time.sleep(5)
driver.find_element_by_class_name('_2BJMh').send_keys(Keys.RETURN)
time.sleep(5)

try:
    driver.find_element_by_class_name('_3FR5S').click()
    time.sleep(5)
except:
    print("restaurant not open")
    driver.quit()

html = driver.find_element_by_tag_name('html')



def get_items():
    type_list = []
    z = 0
    global header_added, types
    global item_dvs
    cats = driver.find_elements_by_class_name('D_TFT')
    cats[1].click()
    time.sleep(3)
    for i in range(5):
        item_dvs = driver.find_elements_by_class_name('_2wg_t')
        types = driver.find_elements_by_tag_name('h2')
        for ty in types:
            type_list.append(ty.text)
        print(len(item_dvs))
        print(len(types))
        driver.execute_script("window.scrollBy(0, 4100)")

    for div in item_dvs:
        name = div.find_element_by_class_name('styles_itemNameText__3bcKX').text
        print(name)
        price = div.find_element_by_class_name('rupee').text
        print(price)
        try:
            desc = div.find_element_by_class_name('styles_itemDesc__MTsVd').text
        except NoSuchElementException:
            desc = None

        print(desc)
        try:
            div.find_element_by_css_selector('div._1C1Fl._23qjy')
            element = div.find_element_by_css_selector('div._1C1Fl._23qjy')
            print("found")
            driver.execute_script("arguments[0].scrollIntoView();", element)
            add = div.find_element_by_css_selector('._1RPOp')
            driver.execute_script("arguments[0].click();", add)
            time.sleep(1)
            add_ons = driver.find_element_by_class_name('_3UzO2').text
            print(add_ons)
            driver.find_element_by_css_selector('button.icon-close-thin.VVWx4').click()

        except (StaleElementReferenceException,NoSuchElementException):
            add_ons = None

        try:
            ty_p = type_list[z]
        except IndexError:
            ty_p = None
        dict1 = {"Type": ty_p, "Item Name": name, "Price": price, "Add Ons :": add_ons, "Description": desc}
        z += 1
        with open(f'{search_city}_{res_n}.csv', 'a+', encoding='utf-8-sig') as f:
            w = csv.DictWriter(f, dict1.keys())
            if not header_added:
                w.writeheader()
                header_added = True
            w.writerow(dict1)


get_items()