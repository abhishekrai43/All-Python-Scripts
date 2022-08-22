import time
import csv
from selenium import webdriver

n = 0
header_added = False
driver =  webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get('https://rejestr.io/newlogin')
time.sleep(5)
driver.find_element_by_xpath('//input[@name="email"]').send_keys('louise.bammel@europeanclimate.org')
password = driver.find_element_by_xpath('//input[@name="password"]')
password.send_keys('Networkanalysis7')
password.submit()
time.sleep(4)

driver.get('https://rejestr.io/organizacje')
time.sleep(5)

def get_data():
    global finances, n, header_added, name, details, industries, partners
    parent_window = driver.current_window_handle
    for link in links[n:]:
        driver.execute_script('window.open(arguments[0]);', link)
        all_windows = driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        driver.switch_to.window(child_window)
        time.sleep(3)
        try:
            na = driver.find_element_by_css_selector('div.org-name').text
            name = na[12:]
            details = driver.find_element_by_css_selector('div.data-container').text
            details.replace('\n', '')
            industries = driver.find_element_by_css_selector('div.card.card-industries.mb-4').text
            fin_divs = driver.find_elements_by_css_selector('div.card.mb-4')
            for div in fin_divs:
                if 'FINANSE' in div.text:
                    finances = div.find_element_by_css_selector('div.card-body').text
                    break
                else:
                    finances = "Finance Data Not Available"
            part = driver.find_elements_by_class_name('name')
            partners = []
            for pa in part:
                partners.append(pa.text)
        except:
            pass



        dict1 = {'Company Name': name, "Details": details, "Industries": industries, "Finances": finances,
                 "Partners": partners}
        with open(f'Polish_Orgs.csv', 'a+', encoding='utf-8-sig') as f:
            w = csv.DictWriter(f, dict1.keys())
            if not header_added:
                w.writeheader()
                header_added = True
            w.writerow(dict1)
        driver.close()
        driver.switch_to.window(parent_window)

while True:
    links = []
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    divs = driver.find_elements_by_css_selector('div.media-body')
    print(len(divs))
    for div in divs:
        link = div.find_element_by_tag_name('a')
        links.append(link)
    get_data()
    try:
        driver.find_element_by_class_name('Cookie__button').click()
    except:
        pass
    time.sleep(1)
    driver.find_element_by_css_selector('div.text-center.py-3').click()
    time.sleep(5)
    n += 20
