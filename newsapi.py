import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from flask import Flask, jsonify

app = Flask(__name__)
options = Options()
options.headless = True
binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")  # Set Binary
driver = webdriver.Firefox(firefox_binary=binary, executable_path="C:\\geckodriver.exe", options=options)
c = 1
#Create the API Endpoint
@app.route('/newsapi/reuters')
def reuters():
    global news_list, links, headlines, times, driver

    driver.get('https://www.reuters.com/world/')
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[4]/div/div[1]/div/div[2]/button/div/span').click()
    driver.execute_script("window.scrollBy(0,1925)", "")
    time.sleep(4)
    headlines_divs = driver.find_elements_by_css_selector('div.StoryCollection__story___3EY8PG')
    news_list = []
    for div in headlines_divs:
        links = div.find_elements_by_tag_name('a')
        headlines = div.find_elements_by_xpath('.//span[2]')
        times = div.find_elements_by_xpath('.//time')
        for link, headline, ti in zip(links, headlines, times):
            dict1 = {"Title": headline.text, "News Link": link.get_attribute('href'), "Time": ti.text}
            news_list.append(dict1)
    driver.quit()
    return jsonify(news_list)

@app.route('/newsapi/bloomberg')
def bloomberg():
    driver.get('https://www.bloomberg.com/')
    driver.execute_script("window.scrollBy(0,1025)", "")
    time.sleep(3)
    links1 = driver.find_elements_by_xpath('//div[@class="story-list-story__info__headline"]//a')
    more_links1 = driver.find_elements_by_xpath('//h3//a')
    news_text = []
    news_links = []
    for link in links1:
        news_text.append(link.text)
    for link in links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links1:
        news_text.append(li.text)
    for link in more_links1:
        news_links.append(link.get_attribute('href'))
    final = []
    for item, link in zip(news_text, news_links):
        dict1 = {"Headline": item, "Link": link}
        final.append(dict1)
    driver.quit()
    return jsonify(final)


@app.route('/newsapi/bloomberg-business')
def bloomberg_bus():
    driver.get('https://www.bloomberg.com/businessweek')
    driver.execute_script("window.scrollBy(0,1025)", "")
    time.sleep(4)
    links1 = driver.find_elements_by_xpath('//h3//a')
    more_links1 = driver.find_elements_by_xpath('//section[@class="single-story-module__eyebrow"]//a')
    more_links2 = driver.find_elements_by_xpath('//div[@class="story-list-story__info__headline"]//a')
    news_text = []
    news_links = []
    for link in links1:
        news_text.append(link.text)
    for link in links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links1:
        news_text.append(li.text)
    for link in more_links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links2:
        news_text.append(li.text)

    for link in more_links2:
        news_links.append(link.get_attribute('href'))
    final = []
    for item, link in zip(news_text, news_links):
        dict1 = {"Headline": item, "Link": link}
        final.append(dict1)
    driver.quit()
    return jsonify(final)

@app.route('/newsapi/ft')
def ft():
    driver.get('https://www.ft.com')
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,1025)", "")
    time.sleep(3)
    links = driver.find_elements_by_xpath('//div[@class="o-teaser__heading"]//a')
    news_text = []
    for link in links:
        news_text.append(link.text)
    news_links = []
    for link in links:
        news_links.append(link.get_attribute('href'))
    final = []
    for item, link in zip(news_text, news_links):
        dict1= {"Headline": item, "Link": link}
        final.append(dict1)
    return jsonify(final)
@app.route('/newsapi/time-news')
def time_n():
    driver.get('https://www.time.com')
    links = driver.find_elements_by_xpath('//h2//a')
    news_text = []
    for link in links:
        news_text.append(link.text)
    news_links = []
    for link in links:
        news_links.append(link.get_attribute('href'))
    final = []
    for item, link in zip(news_text, news_links):
        dict1 = {"Headline": item, "Link": link}
        final.append(dict1)
    driver.quit()
    return jsonify(final)

@app.route('/newsapi/nymag')
def nymag():
    driver.get('https://nymag.com/')
    links1 = driver.find_elements_by_xpath('//div[@class="manual-article-info"]//a')
    more_links1 = driver.find_elements_by_xpath('//li[@class="most-popular-item"]//a')
    more_links2 = driver.find_elements_by_xpath('//li[@class="feed-item   "]//a')

    news_text = []
    news_links = []
    for link in links1:
        news_text.append(link.text)
    for link in links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links1:
        news_text.append(li.text)
    for link in more_links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links2:
        news_text.append(li.text)

    for link in more_links2:
        news_links.append(link.get_attribute('href'))
    final = []
    for item, link in zip(news_text, news_links):
        dict1 = {"Headline": item, "Link": link}
        final.append(dict1)
    driver.quit()
    return jsonify(final)

@app.route('/newsapi/theatlantic')
def theatlantic():
    driver.get('https://www.theatlantic.com/world/')
    driver.execute_script("window.scrollBy(0,1025)", "")
    links1 = driver.find_elements_by_xpath('//h3[@class="o-hed c-tease__hed"]//a')
    more_links1 = driver.find_elements_by_xpath('//li[@class="c-section__item"]//a')
    more_links2 = driver.find_elements_by_xpath('//h2[@class="o-hed c-card__hed"]//a')
    news_text = []
    news_links = []
    for link in links1:
        news_text.append(link.text)
    for link in links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links1:
        news_text.append(li.text)
    for link in more_links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links2:
        news_text.append(li.text)

    for link in more_links2:
        news_links.append(link.get_attribute('href'))
    final = []
    for item, link in zip(news_text, news_links):
        dict1 = {"Headline": item, "Link": link}
        final.append(dict1)
    driver.quit()
    return jsonify(final)

@app.route('/newsapi/vanityfair')
def vanityfair():
    driver.get('https://www.vanityfair.com/')
    driver.execute_script("window.scrollBy(0,1025)", "")
    links1 = driver.find_elements_by_xpath('//a[@class="feature-item-link feature-item-link-hed"]')
    more_links1 = driver.find_elements_by_xpath('//ul[@class="component component-listing landing-trending-container"]//li//a')
    more_links2 = driver.find_elements_by_xpath('//div[@class="feature-item-content"]//a')
    news_text = []
    news_links = []
    for link in links1:
        usel = link.text

        news_text.append(usel)
    for link in links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links1:
        usel1 = li.text

        news_text.append(usel1)
    for link in more_links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links2:
        usel2 = li.text

        news_text.append(usel2)
    for link in more_links2:
        news_links.append(link.get_attribute('href'))

    final = []
    for item, link in zip(news_text, news_links):
        dict1 = {"Headline": item, "Link": link}
        final.append(dict1)
    driver.quit()
    return jsonify(final)

@app.route('/newsapi/si')
def si():
    driver.get('https://www.si.com/')
    driver.execute_script("window.scrollBy(0,1025)", "")
    links1 = driver.find_elements_by_xpath('//phoenix-ellipsis[@class="m-ellipsis m-card--header"]//a')
    news_text = []
    news_links = []
    for link in links1:
        usel = link.text
        news_text.append(usel)
    for link in links1:
        news_links.append(link.get_attribute('href'))
    final = []
    for item, link in zip(news_text, news_links):
        dict1 = {"Headline": item, "Link": link}
        final.append(dict1)
    driver.quit()
    return jsonify(final)
@app.route('/newsapi/oprahdaily')
def oprah():
    driver.get('https://www.oprahdaily.com/')
    driver.execute_script("window.scrollBy(0,1025)", "")
    links1 = driver.find_elements_by_xpath('//div[@class="custom-item-content"]//a')
    news_text = []
    news_links = []
    for link in links1:
        usel = link.text
        news_text.append(usel)
    for link in links1:
        news_links.append(link.get_attribute('href'))
    final = []
    for item, link in zip(news_text, news_links):
        dict1 = {"Headline": item, "Link": link}
        final.append(dict1)
    driver.quit()
    return jsonify(final)
@app.route('/newsapi/thestar')
def thestar():
    driver.get('https://www.thestar.com/?redirect=true')
    driver.execute_script("window.scrollBy(0,1025)", "")
    links1 = driver.find_elements_by_xpath('//div[@class="c-standalone-pack-wrapper"]//a')
    more_links1 = driver.find_elements_by_xpath('//div[@class="c-article-list-flex--2columns c-article-list-flex"]//a')
    more_links2 = driver.find_elements_by_xpath('//div[@class="c-article-list-flex--1columns"]//a')
    news_text = []
    news_links = []
    for link in links1:
        usel = link.text

        news_text.append(usel)
    for link in links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links1:
        usel1 = li.text

        news_text.append(usel1)
    for link in more_links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links2:
        usel2 = li.text

        news_text.append(usel2)
    for link in more_links2:
        news_links.append(link.get_attribute('href'))

    final = []
    for item, link in zip(news_text, news_links):
        dict1 = {"Headline": item, "Link": link}
        final.append(dict1)
    driver.quit()
    return jsonify(final)
@app.route('/newsapi/fortune')
def fortune():
    global time
    driver.get('https://fortune.com/')
    try:
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/img'))).click()
    except:
        pass
    links1 = driver.find_elements_by_xpath('//div[@class="contentItem__card--BUKzk"]//a[2]')
    more_links1 = driver.find_elements_by_xpath('//li[@class="grid__wrapper--3VHv1"]//a[2]')
    news_text = []
    news_links = []
    for link in links1:
        usel = link.text

        news_text.append(usel)
    for link in links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links1:
        usel1 = li.text

        news_text.append(usel1)
    for link in more_links1:
        news_links.append(link.get_attribute('href'))
    final = []
    for item, link in zip(news_text, news_links):
        dict1 = {"Headline": item, "Link": link}
        final.append(dict1)
    driver.quit()
    return jsonify(final)
@app.route('/newsapi/thecipherbrief')
def cipherbrief():
    driver.get('https://www.thecipherbrief.com/article/north-america')
    links1 = driver.find_elements_by_xpath('/html/body/div[1]/div/div/div/div[1]/main/div/a')

    news_text = []
    news_links = []
    for link in links1:
        usel = link.text

        news_text.append(usel)
    for link in links1:
        news_links.append(link.get_attribute('href'))

    final = []
    for item, link in zip(news_text, news_links):
        dict1 = {"Headline": item, "Link": link}
        final.append(dict1)
    driver.quit()
    return jsonify(final)


@app.route('/newsapi/thesfchronicle')
def sfchronicle():
    driver.get('https://www.sfchronicle.com/')
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[2]/div/a/img'))).click()
    except:
        pass
    links1 = driver.find_elements_by_xpath('//div[@class="coreHeadlineList--item-headline bullet"]//a')
    more_links1 = driver.find_elements_by_xpath('//div[@class="centerpiece-tab--main-headline badge"]//a')
    more_links2 = driver.find_elements_by_xpath('//div[@class="badge"]//a')
    news_text = []
    news_links = []
    for link in links1:
        usel = link.text

        news_text.append(usel)
    for link in links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links1:
        usel1 = li.text

        news_text.append(usel1)
    for link in more_links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links2:
        usel2 = li.text
        news_text.append(usel2)
    for link in more_links2:
        news_links.append(link.get_attribute('href'))
    final = []
    for item, link in zip(news_text, news_links):
        dict1 = {"Headline": item, "Link": link}
        final.append(dict1)
    driver.quit()
    return jsonify(final)
@app.route('/newsapi/thehoustonchronicle')
def hchronicle():
    driver.get('https://www.houstonchronicle.com/')
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[2]/div/a/img'))).click()
    except:
        pass

    links1 = driver.find_elements_by_xpath('//div[@class="centerpiece-tab--main-headline badge"]//a')
    more_links1 = driver.find_elements_by_xpath('//div[@class="centerpiece-tab--main-headline badge"]//a')
    more_links2 = driver.find_elements_by_xpath('//div[@class="badge"]//a')
    news_text = []
    news_links = []
    for link in links1:
        usel = link.text

        news_text.append(usel)
    for link in links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links1:
        usel1 = li.text

        news_text.append(usel1)
    for link in more_links1:
        news_links.append(link.get_attribute('href'))
    for li in more_links2:
        usel2 = li.text
        news_text.append(usel2)
    for link in more_links2:
        news_links.append(link.get_attribute('href'))
    final = []
    for item, link in zip(news_text, news_links):
        dict1 = {"Headline": item, "Link": link}
        final.append(dict1)
    driver.quit()
    return jsonify(final)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)






