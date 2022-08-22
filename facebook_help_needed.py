import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


#Load FireFox Profile
profile = FirefoxProfile(r'C:\Users\user\AppData\Roaming\Mozilla\Firefox\Profiles\ogwfse3l.default-release')
url = input("Enter the profile url :") #Get Url
binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe") #Set Binary
driver = webdriver.Firefox(firefox_binary=binary, executable_path="C:\\geckodriver.exe", firefox_profile=profile)
'''driver.get('https://www.facebook.com')
time.sleep(5)
driver.find_element_by_xpath("//input[@name='email']").send_keys('')
password = driver.find_element_by_xpath("//input[@name='pass']")
password.send_keys('')
password.submit()
time.sleep(5)'''
na = url.split('https://www.facebook.com/')
print(na[1]) #Profile Name
driver.get(url)
time.sleep(5)

com_names = []
com_links = []
com_texts = []
names_list = []
names_links = []

while True:

    time.sleep(5)
    main_div = driver.find_element_by_xpath('//div[@data-pagelet="ProfileTimeline"]')
    divs = main_div.find_elements_by_xpath('.//div[@class="rq0escxv l9j0dhe7 du4w35lb hybvsw6c ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi k4urcfbm ni8dbmo4 stjgntxs sbcfpzgs"]')
    if len(divs) > 5:
        try:
            for div in divs:
                Post_Title = div.find_element_by_xpath('.//div[@class="pybr56ya dati1w0a hv4rvrfc n851cfcs btwxx1t3 j83agx80 ll8tlv6m"]').text
                Post_Div = div.find_element_by_xpath('.//div[@class="ecm0bbzt hv4rvrfc e5nlhep0 dati1w0a"]')
                try:
                    Post_Div.find_element_by_xpath('.//div[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"]').click()
                    time.sleep(1)
                    Post_Text = Post_Div.find_element_by_xpath('.//div[@class="qzhwtbm6 knvmm38d"]').text
                except:
                    pass
                    Post_Text = Post_Div.find_element_by_xpath('.//div[@class="qzhwtbm6 knvmm38d"]').text
                sec_div = div.find_element_by_xpath('.//div[@class="stjgntxs ni8dbmo4 l82x9zwi uo3d90p7 h905i5nu monazrh9"]')
                try:
                    com_button = sec_div.find_element_by_xpath('.//div[@class="gtad4xkn"]').click()
                    time.sleep(2)
                    com_div = div.find_element_by_xpath('.//div[@class="cwj9ozl2 tvmbv18p"]')
                    while True:
                        more_com = com_div.find_element_by_xpath('div[@class="oajrlxb2 bp9cbjyn g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 pq6dq46d mg4g778l btwxx1t3 g5gj957u p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys p8fzw8mz qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh gpro0wi8 m9osqain buofh1pr"]').click()
                        time.sleep(1)
                        mcomment_divs = com_div.find_elements_by_css_selector('div.g3eujd1d.ni8dbmo4.stjgntxs.hv4rvrfc')
                        for mcomment in mcomment_divs:
                            mcom_name = mcomment.find_element_by_xpath('//a').text
                            com_names.append(mcom_name)
                            mcom_link = mcomment.find_element_by_xpath('//a').get_attribute('href')
                            com_links.append(mcom_link)
                            mcom_text = mcomment.find_element_by_css_selector('div.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.c1et5uql').text
                            com_texts.append(mcom_text)
                except:
                    break
                for co_name, co_link, co_text in zip(com_names, com_links, com_texts):
                    with open(f"Facebook{na[1]}.txt", 'a+', encoding='utf-8') as f:
                        f.write("\t\t\t\t\tComment by :" f'{co_name}\n\n')
                        f.write("\t\t\t\t\tCommenter's link " f'{co_link}\n\n')
                        f.write("\t\t\t\t\tComment Text :" f'{co_text}\n\n')
                    f.close()
        except:
            pass