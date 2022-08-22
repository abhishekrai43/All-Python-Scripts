import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

#Load FireFox Profile
profile = FirefoxProfile(r'C:\Users\user\AppData\Roaming\Mozilla\Firefox\Profiles\ogwfse3l.default-release')

binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe") #Set Binary
driver = webdriver.Firefox(firefox_binary=binary, executable_path="C:\\geckodriver.exe", firefox_profile=profile)
driver.get('https://www.ambitionbox.com/')
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[1]/div[1]/div[1]/div[3]').click() #sign in with google
time.sleep(10)