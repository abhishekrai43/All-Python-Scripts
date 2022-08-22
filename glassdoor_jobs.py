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
driver.find_element_by_class_name('locked-home-sign-in').click()
div = driver.find_elements_by_css_selector('div.fullContent')
driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', div)
user = driver.find_element_by_xpath('//input[@id="userEmail"]')
user.send_keys('infidel09@protonmail.com')
passw = driver.find_element_by_xpath('//input[@id="userPassword"]')
passw.send_keys('boinkboink')
button = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/button').click()
time.sleep(3)
driver.get('https://www.glassdoor.co.in/Job/new-york-data-architect-jobs-SRCH_IL.0,8_IC1132348_KO9,23.htm') #Enter URL here
time.sleep(3)
'''search = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="sc.keyword"]')))
search.send_keys('data architect')
location = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="sc.location"]')))
location.send_keys(Keys.CONTROL + "a");
location.send_keys(Keys.DELETE);
location.send_keys('New York')
time.sleep(2)
suggestion = driver.find_element_by_css_selector('div.autocomplete-suggestions ')
driver.execute_script("arguments[0].click();", suggestion);
driver.find_element_by_xpath('//button[@type="submit"]').click()'''
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@alt="Close"]'))).click()
except:
    pass
time.sleep(3)
def get_data():
    global header_added
    dates_list = []
    dates = driver.find_elements_by_xpath('//div[@data-test="job-age"]')
    for date in dates:
        dates_list.append(date.text)
    jobs_links = driver.find_elements_by_xpath('//a[@class="jobLink css-1rd3saf eigr9kq2"]')
    parent_window = driver.current_window_handle
    i = 0
    for job in jobs_links:
        try:
            driver.execute_script('window.open(arguments[0]);', job)
            all_windows = driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            driver.switch_to.window(child_window)
            time.sleep(5)
            job_url = driver.current_url
            title = driver.find_element_by_css_selector('div.css-17x2pwl.e11nt52q6').text
            com = driver.find_element_by_css_selector('div.css-16nw49e.e11nt52q1').text
            co = com.split('\n')
            company = co[0]
            print(company)
            location = driver.find_element_by_css_selector('div.css-1v5elnn.e11nt52q2').text
            driver.find_element_by_css_selector('div.css-t3xrds.ecgq1xb2').click()
            time.sleep(2)
            job_desc = driver.find_element_by_xpath('//div[@id="JobDescriptionContainer"]').text
            dict1 = {"Job Title": title, "Company": company, "Location": location, "Full Details": job_desc,
                     "Posted": dates_list[i],
                     "Job Link": job_url}
            with open(f'Glassdoor_Jobs.csv', 'a+', encoding='utf-8-sig') as f:
                w = csv.DictWriter(f, dict1.keys())
                if not header_added:
                    w.writeheader()
                    header_added = True
                w.writerow(dict1)
                i += 1
        except:
            pass
        driver.close()
        driver.switch_to.window(parent_window)

get_data()
for _ in range(4):
    try:
        driver.find_element_by_xpath('//a[@data-test="pagination-next"]').click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@alt="Close"]'))).click()
        get_data()
    except:
        pass
driver.quit()
