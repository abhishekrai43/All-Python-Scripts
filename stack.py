from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import pyautogui

start = input("Enter the start date. E.g 01122020 :")
end = input("Enter the start date. E.g 01012021 :")

chrome_options = Options()
prefs = {"download.default_directory" : "C:\\Users\\user\\Desktop\\"}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('C:/chromedriver.exe', options=chrome_options)
driver.get('https://portal.volleymetrics.hudl.com/#/auth/login')
actionChains = ActionChains(driver)
driver.maximize_window()
user = driver.find_element_by_xpath('//*[@id="username"]')
user.send_keys('merin_sinha24')
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Dwayne4321') #That is not the password
driver.find_element_by_xpath('//*[@id="login-content"]/form/button').click()
WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#left-menu-container > div.left-menu-button-container-top > left-menu-button:nth-child(2)'))).click()
driver.find_element_by_xpath('//*[@id="portal-matches-tabs"]/vm-tabs/div/div[2]').click()
time.sleep(10)
driver.find_element_by_xpath('//*[@id="portal-matches-advanced-filters-text"]').click()
time.sleep(5)
start_d = driver.find_element_by_xpath('//*[@id="portal-matches-advanced-filters-container"]/div/ng-transclude/div[1]/div[2]/div[1]/vm-input-box/div[2]/div/input')
start_d.send_keys(f'{start}')
end_d = driver.find_element_by_xpath('//*[@id="portal-matches-advanced-filters-container"]/div/ng-transclude/div[1]/div[2]/div[2]/vm-input-box/div[2]/div/input')
end_d.send_keys(f'{end}')
driver.find_element_by_xpath('//*[@id="portal-matches-advanced-filters-container"]/div/ng-transclude/div[3]/button[1]').click()
time.sleep(5)
main_div = driver.find_elements_by_xpath('//div[@class="generic-table-two-row-group"]')
main_div = main_div[1]
links = main_div.find_elements_by_class_name('my-matches-table-row-container')
count = 0
while(len(links)!=count):
    links = main_div.find_elements_by_class_name('my-matches-table-row-container')
    for link in links:
        link.click()
        parent_window = driver.current_window_handle
        all_windows = driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        driver.switch_to.window(child_window)
        time.sleep(10)
        error = driver.find_element_by_class_name('video-message')
        if error.text == 'No video to display.':
            driver.close()
            driver.switch_to.window(parent_window)
            continue
        else:
            video = WebDriverWait(driver, 80).until(EC.visibility_of_element_located((By.ID, 'vm-match-video')))
            if not video:
                break
            else:
                div1 = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'vm-match-actions-directive')))
                divs2 = div1.find_elements_by_class_name('button-container')
                count2 = 0
                while (len(divs2) != count2):
                    divs2 = div1.find_elements_by_class_name('button-container')
                    div = divs2[count2]
                    count2 += 1
                    WebDriverWait(driver, 80).until(EC.visibility_of_element_located((By.ID, 'vm-match-video')))
                    try:
                        driver.find_element_by_xpath(
                            '//*[@id="portal-match-controls-column"]/div[3]/vm-match-actions/div/div/div[1]/div[4]/span[2]').click()
                        driver.find_element_by_xpath('//button[contains(text(),"I Accept")]').click()
                        time.sleep(6)
                        break
                    except:
                        break

            driver.close()
            driver.switch_to.window(parent_window)



