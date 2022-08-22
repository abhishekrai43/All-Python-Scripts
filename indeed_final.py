import time
import csv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException



header_added = False
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get('https://www.indeed.com/jobs?q=Software+Tester&l=New+York')

def get_data():
    global header_added
    for title in titles:
        link = title.find_element_by_tag_name('a')
        link_p = link.get_attribute('href')
        driver.execute_script('window.open(arguments[0]);', link)
        all_windows = driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        driver.switch_to.window(child_window)
        time.sleep(5)
        company = ""
        location = ""
        job_desc = ""
        days = ""
        try:
            job_desc = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="jobDescriptionText"]'))).text

            title = driver.find_element_by_tag_name('h1').text
            print(title)

            try:
                company = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="icl-u-lg-mr--sm icl-u-xs-mr--xs"]//a'))).text
                print(company)

            except:

                company = driver.find_element_by_xpath('//div[@class="icl-u-lg-mr--sm icl-u-xs-mr--xs"]').text
                print(company)
            time.sleep(2)
            try:
                location = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div/div[1]/div[4]/div[1]/div[2]/div/div/div[2]').text
            except:
                location = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/div/div/div[2]').text
            print(location)
            days = driver.find_element_by_css_selector('#viewJobSSRRoot > div.jobsearch-JobComponent.icl-u-xs-mt--sm.jobsearch-JobComponent-bottomDivider > div.jobsearch-JobTab-content > div.jobsearch-JobMetadataFooter > div:nth-child(2)').text
            print(days)

        except:
            pass
        dict1 = {"Job Title": title, "Company": company, "Location": location, "Full Details": job_desc, "Posted": days,
                 "Job Link": link_p}
        with open(f'Indeed__Software_Tester_Jobs.csv', 'a+', encoding='utf-8-sig') as f:
            w = csv.DictWriter(f, dict1.keys())
            if not header_added:
                w.writeheader()
                header_added = True
            w.writerow(dict1)

        driver.close()
        driver.switch_to.window(parent_window)


parent_window = driver.current_window_handle
titles = driver.find_elements_by_tag_name('h2')
get_data()
for i in range(26):
    if i == 25:
        driver.quit()
    try:
        driver.find_element_by_xpath('//a[@aria-label="Next"]').click()
        titles = driver.find_elements_by_tag_name('h2')
        try:
            WebDriverWait(driver, 9).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Close"]'))).click()
            get_data()
        except NoSuchElementException:
            get_data()
    except:
       pass




