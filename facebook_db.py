#Import Libs
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
import MySQLdb

db = MySQLdb.connect('localhost', 'root', '', 'Facebook')
cursor = db.cursor()
db.autocommit(True)
#Load FireFox Profile
profile = FirefoxProfile(r'C:\Users\user\AppData\Roaming\Mozilla\Firefox\Profiles\ogwfse3l.default-release')
url = input("Enter the profile url :") #Get Url
binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe") #Set Binary
driver = webdriver.Firefox(firefox_binary=binary, executable_path="C:\\geckodriver.exe", firefox_profile=profile)
time.sleep(10)
na = url.split('https://www.facebook.com/')

driver.get(url)
i=-1
profile_name = False
poiff = 0
while True:
    try:

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        main_div = driver.find_element_by_xpath('//div[@data-pagelet="ProfileTimeline"]')
        divs = main_div.find_elements_by_xpath('.//div[@class="j83agx80 cbu4d94t"]')
        if len(divs) > 5:
            for i in range(i+1,len(divs)):
                driver.execute_script("arguments[0].scrollIntoView();", divs[i])
                action = ActionChains(driver)
                action.move_to_element(divs[i]).perform()
                time.sleep(13)
                p_name = divs[i].find_element_by_xpath('.//div[@class="nc684nl6"]//span').text  # poster's name
                pi_link = driver.find_elements_by_xpath('.//div[@class="nc684nl6"]//a')[i]
                p_link = pi_link.get_attribute('href')
                post_content = divs[i].find_elements_by_xpath('//div[@class="l9j0dhe7"]')[i]
                st_link = divs[i].find_elements_by_xpath('//div[@class="l9j0dhe7"]//a')[i]
                post_link = st_link.get_attribute('href')

                if not profile_name:
                    cursor.execute("INSERT INTO profiles(name) VALUES(%s)", (p_name,))
                profile_name = True
                sql = cursor.execute(f"SELECT profileid FROM profiles WHERE name =\'{p_name}\'")
                pid = cursor.fetchone()
                pidf = str(pid)[1:2]
                pidff = int(pidf)


                try:
                    divs[i].find_element_by_xpath(
                        './/div[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"]').click()
                    post_text = divs[i].find_element_by_css_selector('div.ecm0bbzt.hv4rvrfc.ihqw7lf3.dati1w0a').text
                    cursor.execute("INSERT INTO posts(profileid, post, postext) VALUES(%s, %s, %s)", (pidff, post_link, post_text,))
                except:
                    cursor.execute("INSERT INTO posts(profileid, post) VALUES(%s, %s)",
                                   (pidff, post_link,))
                    pass

                '''
                with open(f"Facebook{na[1]}.txt", 'a+', encoding='utf-8') as f:
                    f.write("Posted By :" f'{p_name}\n\n')
                    f.write("\tPosters Link :" f'{p_link}\n\n\n')
                    f.write("\t\tContent Link :" f'{post_link}\n\n\n')
                f.close()'''

                likes_button = divs[i].find_elements_by_xpath('//span[@class="pcp91wgn"]')
                driver.execute_script("arguments[0].click();", likes_button[i]);  # Likes Button Click
                time.sleep(3)
                likes_div = driver.find_element_by_css_selector(
                    'div.q5bimw55.rpm2j7zs.k7i0oixp.gvuykj2m.j83agx80.cbu4d94t.ni8dbmo4.eg9m0zos.l9j0dhe7.du4w35lb.ofs802cu.pohlnb88.dkue75c7.mb9wzai9.l56l04vs.r57mb794.kh7kg01d.c3g1iek1.otl40fxz.cxgpxx05.rz4wbd8a.sj5x9vvc.a8nywdso')
                current_len = len(likes_div.find_elements_by_xpath('//div[@class="q9uorilb"]//a'))
                while True:
                    likes_div.find_element_by_xpath('.//div[@class="q9uorilb"]//a').send_keys(Keys.END)
                    try:
                        WebDriverWait(driver, 5).until(
                            lambda x: len(driver.find_elements_by_xpath('.//div[@class="q9uorilb"]//a')) > current_len)
                        current_len = len(driver.find_elements_by_xpath('.//div[@class="q9uorilb"]//a'))
                    except TimeoutException:
                        name_eles = [name_ele for name_ele in
                                     driver.find_elements_by_xpath('.//div[@class="q9uorilb"]//a')]
                        time.sleep(5)
                        poiff += 1


                        for name in name_eles:
                            nt = name.text
                            n_li = name.get_attribute('href')
                            nlf = n_li.split('?')
                            cursor.execute("INSERT INTO likers(profileid, postid, pliker, lprofile) VALUES(%s, %s,%s,%s)", (pidff, poiff, nt, nlf[0],))
                        '''with open(f"Facebook{na[1]}.txt", 'a+', encoding='utf-8') as f:
                                f.write("\t\t\tLiked By :" f'{name.text}\n')
                                f.write("\t\t\t\tLiker's Profile Link :" f'{n_li}\n\n')
                            f.close()'''
                        close = driver.find_element_by_xpath('//div[@class="cypi58rs pmk7jnqg fcg2cn6m tkr6xdv7"]//div')
                        driver.execute_script("arguments[0].click();", close);
                        break
                try:
                    while True:
                        c = 1
                        try:

                            more_comments = divs[i].find_element_by_xpath('.//span[@class="j83agx80 fv0vnmcu hpfvmrgz"]')
                            driver.execute_script("arguments[0].click();", more_comments);
                            time.sleep(5)
                        except:
                            comment_divs = divs[i].find_elements_by_css_selector(
                                'div.g3eujd1d.ni8dbmo4.stjgntxs.hv4rvrfc')
                            for comment in comment_divs:
                                com_name = comment.find_element_by_xpath('.//a').text
                                com_link = comment.find_element_by_xpath('.//a').get_attribute('href')
                                comf = com_link.split('?')
                                '''with open(f"Facebook{na[1]}.txt", 'a+', encoding='utf-8') as f:
                                    f.write("\t\t\t\t\tComment by :" f'{com_name}\n\n')
                                    f.write("\t\t\t\t\tCommenter's link " f'{com_link}\n\n')
                                f.close()'''
                                try:
                                    comment.find_element_by_xpath(".//div[contains(text(),'See More')]").click()
                                    time.sleep(1)
                                except:
                                    pass
                                com_text = comment.find_element_by_xpath(
                                        './/div[@class="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql"]').text
                                if not com_text:
                                    com_text = "GIF/PHOTO"
                                cursor.execute("INSERT INTO comments(profileid, postid, comby, compro, comtext) VALUES(%s, %s, %s, %s, %s)",
                                               (pidff, poiff, com_name, comf[0], com_text,))
                                '''with open(f"Facebook{na[1]}.txt", 'a+', encoding='utf-8') as f:
                                    f.write("\t\t\t\t\tComment Text :" f'{com_text}\n\n')
                                f.close()'''
                                try:

                                    time.sleep(3)
                                    comment.find_element_by_xpath('.//div[@class="_6cuq"]').click()
                                    time.sleep(3)
                                    com_eles = driver.find_elements_by_xpath('.//div[@class="q9uorilb"]//a')
                                    for com_name in com_eles:
                                        comrename = com_name.text
                                        com_li = com_name.get_attribute('href')
                                        comlf = com_li.split('?')
                                        cursor.execute("INSERT INTO comacts(profileid, postid, commentid, comre, comrepro) VALUES(%s, %s, %s, %s, %s)",
                                            (pidff, poiff, c, comrename, comlf[0],))
                                        c += 1
                                        '''
                                        with open(f"Facebook{na[1]}.txt", 'a+', encoding='utf-8') as f:
                                            f.write("\t\t\t\t\t\tComment reaction by :" f'{com_name.text}\n\n')
                                            f.write("\t\t\t\t\t\tComment reactor's profile :" f'{com_li}\n\n')
                                        f.close()'''
                                    close = driver.find_element_by_xpath('//div[@class="cypi58rs pmk7jnqg fcg2cn6m tkr6xdv7"]//div')
                                    driver.execute_script("arguments[0].click();", close);
                                except:
                                    pass
                            break
                        '''with open(f"Facebook{na[1]}.txt", 'a+', encoding='utf-8') as f:
                            f.write("\t\t\t\t\tComment by :" f'{co_name}\n\n')
                            f.write("\t\t\t\t\tCommenter's link " f'{co_link}\n\n')
                            f.write("\t\t\t\t\tComment Text :" f'{co_text}\n\n')
                        f.close()'''
                except Exception as e:
                    pass
    except Exception as f:
        pass



