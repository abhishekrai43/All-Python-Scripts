import time
import csv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


header_added = False
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get('https://www.glassdoor.co.in/index.htm')
time.sleep(3)
login = driver.find_element_by_css_selector('#SiteNav > nav > div.d-lg-none.d-flex.align-items-center.justify-content-between.px-std.py-xsm.px-md-lg.py-md-std.LockedHomeHeaderStyles__bottomBorder.LockedHomeHeaderStyles__fullWidth > div.d-flex.justify-content-center.order-1.order-md-2.LockedHomeHeaderStyles__flexibleContainer > button')
driver.execute_script('arguments[0].click();', login)
div = driver.find_elements_by_css_selector('div.fullContent')
driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', div)
user = driver.find_element_by_xpath('//input[@id="userEmail"]')
user.send_keys('infidel09@protonmail.com')
passw = driver.find_element_by_xpath('//input[@id="userPassword"]')
passw.send_keys('boinkboink')
button = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/button').click()
time.sleep(3)
driver.get('https://www.glassdoor.co.in/Reviews/india-reviews-SRCH_IL.0,5_IN115.htm')
time.sleep(3)
def get_element(label):
    try:
        driver.execute_script("arguments[0].scrollIntoView();", label)
        return driver.find_element_by_xpath(label).text

    except (NoSuchElementException, TimeoutException):
        return ""


links = driver.find_elements_by_xpath('//div[@class="col-3 logo-and-ratings-wrap"]//a')
parent_window = driver.current_window_handle
for i in range(len(links)):
    driver.execute_script('window.open(arguments[0]);', links[i])
    all_windows = driver.window_handles
    child_window = [window for window in all_windows if window != parent_window][0]
    driver.switch_to.window(child_window)
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,2525)", "")
    elem = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div/div/div/article[2]/div[2]/div/div[1]/div[2]/div/div[2]/div')
    driver.execute_script("arguments[0].scrollIntoView();", elem)
    el_a = elem.value_of_css_property('background')
    per = el_a.split('%')
    usel = per[0]
    numb = int((usel[-2:]))
    over_all_rating = numb / 20
    print(over_all_rating)
    num_ratings = get_element('/html/body/div[3]/div/div/div/div/div[1]/div/div/div/article[2]/div[2]/div/div[1]/div[3]')
    print(num_ratings)





