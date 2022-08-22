import time
import csv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException

header_added = False
area = input("Enter the City Name :")
timestr = time.strftime("%Y%m%d-%H%M%S")
chrome_options = Options()
chrome_options.add_argument('--user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data')
chrome_options.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', options=chrome_options)
driver.maximize_window()
driver.get('https://www.facebook.com/marketplace/')
time.sleep(4)
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[7]/div[2]').click()
time.sleep(2)
box = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/label/div/div[2]/input')
box.click()
time.sleep(1)
box.send_keys(u'\ue009' + u'\ue003')
box.send_keys(area)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/ul/li[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div[1]/span').click()
driver.find_element_by_xpath('//span[@class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p bwm1u5wc"]').click()
time.sleep(5)


def get_data():
    links = []
    global time, area, header_added, url, description_div, description, location, duration
    link_eles = driver.find_elements_by_xpath('//div[@class="kbiprv82"]//a')
    for item in link_eles:
        link = item.get_attribute('href')
        links.append(link)

    for a in range(len(links)):
        driver.get(links[a])
        time.sleep(3)
        try:
            title = driver.find_element_by_xpath('//span[@class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 qg6bub1s fe6kdd0r mau55g9w c8b282yb iv3no6db o0t2es00 f530mmz5 hnhda86s oo9gr5id"]').text
            print(title)
        except:
            title = 'No title'
        try:
            price = driver.find_element_by_xpath('//span[@class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb mdeji52x a5q79mjw g1cxx5fr ekzkrbhg oo9gr5id"]').text
            print(price)
        except:
            price = 'No Price Mentioned'
        url = driver.current_url
        print(url)
        try:
            description_div = driver.find_element_by_xpath('//div[@class="ii04i59q a8nywdso f10w8fjw rz4wbd8a pybr56ya"]')
            if description_div:
                try:
                    description_div.find_element_by_xpath('.//span[@class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh jq4qci2q a3bd9o3v lrazzd5p oo9gr5id"]').click()
                except NoSuchElementException:
                    pass
                description = description_div.text
        except:
            pass

        print(description)
        try:
            category = driver.find_element_by_xpath('//span[@class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh e9vueds3 j5wam9gi knj5qynh m9osqain"]').text
            print(category)
        except:
            category= 'Not in a Category'
        try:
            tl_div = driver.find_element_by_xpath('//div[@class="aov4n071 sjgh65i0"]')
            duration = tl_div.find_element_by_xpath('.//span[@class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb mdeji52x e9vueds3 j5wam9gi knj5qynh m9osqain"]').text
            location = tl_div.find_element_by_tag_name('a').text
        except:
            pass
        print(location)
        img = driver.find_element_by_xpath('//span[@class="j83agx80 tkr6xdv7"]').find_element_by_tag_name('img')
        img_link = img.get_attribute('src')
        print(img_link)
        try:
            seller = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[2]').text
            print(seller)
        except:
            seller = 'No seller info available'
        time.sleep(1)
        dict1 = {"Title": title, "Price": price, "Link": url, "Description": description, "Category": category,
                 "Posted": duration, "Image Link": img_link, "Seller": seller}
        with open(f'Facebook_Market_{area}.csv', 'a+', encoding='utf-8-sig') as f:
            w = csv.DictWriter(f, dict1.keys())
            if not header_added:
                w.writeheader()
                header_added = True
            w.writerow(dict1)
        time.sleep(1)
        driver.back()





while True:
    get_data()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(6)






