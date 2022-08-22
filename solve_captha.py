from selenium import webdriver
import time
import requests
import base64
from PIL import Image
from pytesseract import pytesseract
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
options = webdriver.ChromeOptions()
options.add_argument("download.default_directory=cheapshit")
year_list = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016','2017', '2018', '2019', '2020', '2021']
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
url = 'http://www.aduanet.gob.pe/cl-ad-itconsultadwh/ieITS01Alias?accion=consultar&CG_consulta=1'
driver.get(url)
time.sleep(3)

def get_data():
    try:
        parent_window = driver.current_window_handle
        driver.implicitly_wait(10)
        link_l = driver.find_elements_by_xpath('//table[3]//a')
        for i in range(len(link_l) - 1):
            driver.find_elements_by_xpath('//table[3]//a')[i].click()
            driver.find_element_by_xpath(
                '/html/body/form[1]/table[2]/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr[2]/td[3]/a').click()
            all_windows = driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            driver.switch_to.window(child_window)
            time.sleep(3)

            captcha = driver.find_element_by_xpath('/html/body/form/center/font/img')
            # get the captcha as a base64 string
            img_captcha_base64 = driver.execute_async_script("""
                      var ele = arguments[0], callback = arguments[1];
                      ele.addEventListener('load', function fn(){
                        ele.removeEventListener('load', fn, false);
                        var cnv = document.createElement('canvas');
                        cnv.width = this.width; cnv.height = this.height;
                        cnv.getContext('2d').drawImage(this, 0, 0);
                        callback(cnv.toDataURL('image/jpeg').substring(22));
                      }, false);
                      ele.dispatchEvent(new Event('load'));
                      """, captcha)

            # save the captcha to a file
            with open(r"captcha.jpg", 'wb') as f:
                f.write(base64.b64decode(img_captcha_base64))

            path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            image_path = r"captcha.jpg"

            # Opening the image & storing it in an image object
            img = Image.open(image_path)

            # Providing the tesseract executable
            # location to pytesseract library
            pytesseract.tesseract_cmd = path_to_tesseract

            # Passing the image object to image_to_string() function
            # This function will extract the text from the image
            text = pytesseract.image_to_string(img)
            text = text.replace(" ","")
            try:
                driver.find_element_by_xpath('/html/body/form/center/font/input').send_keys(text)
                '''WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/center/font/a/input[3]'))).click()
                print("I am here")'''
                page = driver.page_source
                soup = BeautifulSoup(page, 'html.parser')
                tables = soup.findAll('table')
                dfs = []
                for table in tables:
                    df_x = pd.read_html(str(table))
                    print(df_x)
                    df = pd.concat(df_x)
                    dfs.append(df)
                df_f = pd.concat(dfs)
                df_f.to_csv(f'result{year}_{i}.csv')
            except:
                pass
            driver.close()
            driver.switch_to.window(parent_window)
            driver.back()
    except:
        pass
with open ('codes.txt','r') as file:
    next(file)
    for line in file:
        driver.refresh()
        code = line[0:11]
        print(code)
        f_input = driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[2]/td/input[1]')
        f_input.send_keys(str(code))
        try:
            for year in year_list:
                driver.find_element_by_xpath(f'//select[@name="CG_Ano"]/option[text()=\"{year}\"]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//select[@name="CG_regimen"]/option[text()="EXPORTACION"]').click()
                driver.find_element_by_xpath('/html/body/center/form/center/input[1]').click()
                time.sleep(2)
                try:
                    link_l = driver.find_elements_by_xpath('//table[3]//a')
                    get_data()
                except NoSuchElementException:
                    driver.back()
                    continue
                driver.back()

        except:
            pass










