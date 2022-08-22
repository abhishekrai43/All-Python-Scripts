import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
profile = FirefoxProfile("C:\\Users\\user\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\ogwfse3l.default-release")
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9150)
driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary, executable_path="C:\\geckodriver.exe")
driver.maximize_window()
driver.get('https://www.gmail.com')


