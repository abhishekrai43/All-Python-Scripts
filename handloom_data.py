import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException



driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
url ='http://www.handloomcensus.gov.in/search.php#'
driver.get(url)
driver.maximize_window()
time.sleep(3)
button = driver.find_element_by_xpath('//a[@id="A1_anchor"]')
actionChains = ActionChains(driver)
actionChains.double_click(button).perform()
time.sleep(3)
ul = driver.find_element_by_xpath('//ul[@class="jstree-children"]')
links = ul.find_elements_by_tag_name('i')
for link in links[12:]: #Change State
    link.click()
    time.sleep(7)
    ul1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[2]/div/ul/li/ul/li[7]/ul/li[2]') #Change dISTRICT
    links2 = ul1.find_elements_by_tag_name('i')
    for lin in links2:
        lin.click()
        time.sleep(10)
        ul2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[2]/div/ul/li/ul/li[7]/ul/li[2]/ul')
        links3 = ul2.find_elements_by_xpath('.//li//a//a')
        links_final = []
        for li in links3:
            li_f = li.get_attribute('href')
            links_final.append(li_f)
        for l in links_final:
            driver.get(l)
            time.sleep(3)
            location = driver.find_element_by_xpath('//div[@class=" col-md-12 col-sm-12 col-lg-12 col-sx-12"]').text
            lo = location.split(':')
            lof = lo[1].replace('>>', "").strip()
            lofi = lof.replace(" ", "_")
            print(lofi)
            dfs = []
            print(lofi)
            tables = driver.find_elements_by_tag_name('table')
            table = tables[1].get_attribute('outerHTML')
            df_i = pd.read_html(table)
            df = pd.concat(df_i)
            dfs.append(df)

            while True:
                try:
                    driver.find_element_by_xpath('//a[@title="Next Page"]').click()
                    time.sleep(3)
                    tables = driver.find_elements_by_tag_name('table')
                    table = tables[1].get_attribute('outerHTML')
                    df_x = pd.read_html(table)
                    df = pd.concat(df_x)
                    dfs.append(df)
                except:
                    break

            df = pd.concat(dfs)
            df.to_excel(f'Handloom/Handloom_{str(lofi)}.xlsx')







