import csv
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


chrome_options = Options()
scroll = 5
chrome_options.add_experimental_option("useAutomationExtension", False)  #Set Selenium automted bar notification false
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
header_added = False
header_added1 = False
url = "https://www.swiggy.com/restaurants"
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', options=chrome_options)  #Set The Driver
driver.maximize_window() #Maximize Window to lessen suspicion of being a bot

driver.get(url)
time.sleep(3)
search_city = input("Enter the city :")
res_n = input("Enter the Restaurant's name :")
search = driver.find_element_by_xpath('//input[@name="location"]').send_keys(search_city)
time.sleep(2) #Hard Coded Sleeps WARNING:- DO NOT USE WEBDRIVER WAIT
driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[3]/div[1]/span[2]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/header/div/div/ul/li[5]/div/a/span[1]').click()
time.sleep(1)
search_res = driver.find_element_by_class_name('_2BJMh').send_keys(res_n.lower())
time.sleep(5)
driver.find_element_by_class_name('_2BJMh').send_keys(Keys.RETURN)
time.sleep(5)

try:
    driver.find_element_by_class_name('_3FR5S').click() # Check If Restaurant is open and serviceable
    time.sleep(5)
except:
    print("restaurant not open")
    driver.quit()

html = driver.find_element_by_tag_name('html')  #Find Page HTML to Scroll
add_ress = driver.current_url #Get Address
address = add_ress.rsplit('/', 1)[1]
def get_items():

    type_list = []
    z = 0
    global header_added, types, address
    global item_dvs
    cats = driver.find_elements_by_class_name('_2dS-v')  #Find Categories
    for ca in cats:
        cat =ca.text  #Category Name
        item_dvs = ca.find_elements_by_class_name('_2wg_t')  # Item Details Div


        for div in item_dvs:
            name = div.find_element_by_class_name('styles_itemNameText__3bcKX').text  # Item Name

            price = div.find_element_by_class_name('rupee').text  # Item Price

            try:
                desc = div.find_element_by_class_name('styles_itemDesc__MTsVd').text  # Check if Description is present
            except NoSuchElementException:
                desc = None

            try:
                div.find_element_by_css_selector('div._1C1Fl._23qjy')  # Check if item is Customisable
                element = div.find_element_by_css_selector('div._1C1Fl._23qjy')
                driver.execute_script("arguments[0].scrollIntoView();", element)
                add = div.find_element_by_css_selector('._1RPOp')
                driver.execute_script("arguments[0].click();", add)  # Click the ADD button
                time.sleep(1)
                add_ons = driver.find_element_by_class_name('_3UzO2').text  # Get Add On Details

                driver.find_element_by_css_selector('button.icon-close-thin.VVWx4').click()  # Close the Add on Pop-up

            except (StaleElementReferenceException, NoSuchElementException):
                add_ons = None

            try:
                ty_p = type_list[z]  # Category list Index out of range error handling
            except IndexError:
                ty_p = None
            dict1 = {"Address": address, "Type": cat, "Item Name": name, "Price": price, "Add Ons :": add_ons,
                     "Description": desc}  # Write Dictionary Keys
            address = None
            z += 1
            with open(f'{search_city}_{res_n}.csv', 'a+',
                      encoding='utf-8-sig') as f:  # File name with Restaurant Name and City
                w = csv.DictWriter(f, dict1.keys())
                if not header_added:
                    w.writeheader()
                    header_added = True
                w.writerow(dict1)


get_items()  # Call the Function to start the Scrape

