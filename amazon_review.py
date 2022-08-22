#Import Libs
import time
import csv
import random
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

def get_data():
    parent_window = driver.current_window_handle
    is_prod = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//h2/a')))
    global dates
    is_prod.click()
    prod_url = driver.current_url
    all_windows = driver.window_handles
    child_window = [window for window in all_windows if window != parent_window][0]
    driver.switch_to.window(child_window)  # Switch Window
    try:

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="acrCustomerReviewLink"]'))).click()
        driver.find_element_by_css_selector('#reviews-medley-footer > div.a-row.a-spacing-medium > a').click()
        time.sleep(5)
        prod_title = driver.find_element_by_css_selector('div.a-row.product-title').text
        driver.execute_script("window.scrollBy(0, 510);")
        ratings_div = driver.find_element_by_id('cm_cr-review_list')
        names_list = []
        stars = []
        titles = []
        dates = []
        names = ratings_div.find_elements_by_class_name('a-profile-content')
        for name in names:
            names_list.append(name.text)
            a_divs = driver.find_elements_by_xpath('//div[@id="cm_cr-review_list"]//div[@class="a-row"]')
            dates = driver.find_elements_by_css_selector('span.a-size-base.a-color-secondary.review-date')
            reviews = driver.find_elements_by_css_selector('span.a-size-base.review-text.review-text-content')
            verified = driver.find_elements_by_xpath('//span[@data-hook="avp-badge"]')
            img_links = []
            img_divs = driver.find_elements_by_xpath('//div[@class="review-image-tile-section"]//img')
            for img_div in img_divs:
                img_link = img_div.get_attribute('src')
                img_links.append(img_link)

            for a in a_divs:
                elems = a.find_elements_by_tag_name('a')
                stars.append(elems[0].get_attribute('title'))
                titles.append(elems[1].text)

            for name, star, title, date, veri, review in zip(names_list, stars, titles, dates, verified,
                                                             reviews):
                dict1 = {'Title': title, "Content": review.text, "Verified": veri.text, "Author": name,
                         "Rating": star[0], "Product": prod_title, "Product Url": prod_url}
                with open(f'Amazon1_Reviews.csv', 'a+', encoding='utf-8-sig') as f:
                    w = csv.DictWriter(f, dict1.keys())
                    if not header_added:
                        w.writeheader()
                        header_added = True
                    w.writerow(dict1)
    except:
        pass
    driver.close()
    driver.switch_to.window(parent_window)
gap = random.randint(10,20)
header_added = False
with open('ASIN.txt') as f:
    lines = f.readlines()
    for asin in lines:
        driver.get('https://www.amazon.in')
        time.sleep(gap)
        search = driver.find_element_by_id('twotabsearchtextbox')
        search.send_keys(asin)
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        try:
            error = WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.a-section.a-spacing-base.a-spacing-top-medium')))
            if error.text == 'No results for ':
                time.sleep(3)
                continue
            else:

                get_data()
        except:
            pass




