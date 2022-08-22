#Import Libs
import time
import csv
from selenium import webdriver
import concurrent.futures


MAX_WORKERS = 4
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
years = ['2011', '2012', '2017', '2018']
def get_data(year):
    driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    header_added = False
    months = ['January', 'June', 'December']
    driver.get('https://idv.gicouncil.in/')
    driver.maximize_window()
    time.sleep(3)
    driver.find_element_by_xpath("//select[@name='vehicletype']/option[text()='Two Wheeler']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//select[@name='city']/option[text()='Delhi']").click()
    time.sleep(1)
    driver.find_element_by_xpath(f"//select[@name='year']/option[text()={year}]").click()
    time.sleep(2)
    for month in months:
        driver.find_element_by_xpath(f"//select[@name='month']/option[text()=\'{month}\']").click()
        time.sleep(1)
        makes = driver.find_element_by_xpath("//select[@name='make']")
        makes_list = makes.text
        makes_s = makes_list[16:]
        makes_f = makes_s.split('\n')
        for make in makes_f:
            driver.find_element_by_xpath(f"//select[@name='make']/option[text()=\'{make}\']").click()
            time.sleep(3)
            models = driver.find_element_by_xpath("//select[@name='model']")
            models_list = models.text
            models_s = models_list[16:]
            models_f = models_s.split('\n')
            mod = models_f[1:]
            for model in mod:
                try:
                    driver.find_element_by_xpath(f"//select[@name='model']/option[text()=\'{model}\']").click()
                    time.sleep(4)
                    variant = driver.find_element_by_xpath("//select[@name='variant']")
                    var = variant.text
                    variant_s = var[16:]
                    variant_f = variant_s.split('\n')
                    for variant in variant_f[1:]:
                        dict1 = {'Year': year, "Month": month, "Company Make": make, "Model": model, "Variants": variant}
                        with open(f'TW_Details{year}.csv', 'a+', encoding='utf-8-sig') as f:
                            w = csv.DictWriter(f, dict1.keys())
                            if not header_added:
                                w.writeheader()
                                header_added = True
                            w.writerow(dict1)
                except:
                    pass

with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:

    tasks = [executor.submit(get_data, year) for year in years]

    for f in concurrent.futures.as_completed(tasks):
        res = f.result()
