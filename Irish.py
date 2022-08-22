#Import Libs
import time
import threading
import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
first_run = True
def telegram_bot_sendtext(bot_message):
    bot_token = '1477854286:AAGnIB-TG8RgcznVyoA3eIocyIc55wpMA8g'
    bot_chatID = '1193030902'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()

def carrigaline(): #Get the first Ad's link
    while True:
        print("Starting First Thread")
        time.sleep(300)
        global first_run
        try:
            page = requests.get(
                'https://www.daft.ie/property-for-sale/carrigaline-and-surrounds-cork?salePrice_from=200000&salePrice_to=300000',
                headers=headers).text
            soup = BeautifulSoup(page, 'html.parser')
            divs = soup.findAll('a', attrs={'class': None})
            fcur_carri = 'https://www.daft.ie' + divs[0].get('href')
            print("Current Ad in Carrigaline :", fcur_carri)
            if not first_run:
                page = requests.get(
                    'https://www.daft.ie/property-for-sale/carrigaline-and-surrounds-cork?salePrice_from=200000&salePrice_to=300000',
                    headers=headers).text
                soup = BeautifulSoup(page, 'html.parser')
                divs = soup.findAll('a', attrs={'class': None})
                ncur_carri = 'https://www.daft.ie' + divs[0].get('href')
                if ncur_carri != fcur_carri:
                    telegram_bot_sendtext(ncur_carri)
                else:
                    continue
        except Exception as e:
            print(e)
            pass

def crosshaven():
    while True:
        print("Starting Second Thread")
        time.sleep(200)
        global first_run
        try:
            page = requests.get(
                'https://www.daft.ie/property-for-sale/crosshaven-cork?salePrice_from=200000&salePrice_to=300000',
                headers=headers).text
            soup = BeautifulSoup(page, 'html.parser')
            divs = soup.findAll('a', attrs={'class': None})
            fcur_haven = 'https://www.daft.ie' + divs[0].get('href')
            print("Current Ad in Crosshaven :", fcur_haven)
            if not first_run:
                page = requests.get(
                    'https://www.daft.ie/property-for-sale/crosshaven-cork?salePrice_from=200000&salePrice_to=300000',
                    headers=headers).text
                soup = BeautifulSoup(page, 'html.parser')
                divs = soup.findAll('a', attrs={'class': None})
                ncur_haven = 'https://www.daft.ie' + divs[0].get('href')
                if ncur_haven != fcur_haven:
                    telegram_bot_sendtext(ncur_haven)
                else:
                    continue
            first_run = False
        except Exception as e:
            print(e)
            pass

def minane():
    while True:
        print("Starting third thread")
        time.sleep(800)
        global first_run
        try:
            page = requests.get(
                'https://www.daft.ie/property-for-sale/minane-bridge-cork?salePrice_from=200000&salePrice_to=300000',
                headers=headers).text
            soup = BeautifulSoup(page, 'html.parser')
            divs = soup.findAll('a', attrs={'class': None})
            fcur_min = 'https://www.daft.ie' + divs[0].get('href')
            print("Current Ad in minane :", fcur_min)
            if not first_run:
                page = requests.get(
                    'https://www.daft.ie/property-for-sale/minane-bridge-cork?salePrice_from=200000&salePrice_to=300000',
                    headers=headers).text
                soup = BeautifulSoup(page, 'html.parser')
                divs = soup.findAll('a', attrs={'class': None})
                ncur_min = 'https://www.daft.ie' + divs[0].get('href')
                if ncur_min != fcur_min:
                    telegram_bot_sendtext(ncur_min)
                else:
                    continue
            first_run = False
        except Exception as e:
            print(e)
            pass
def ballygarvan():
    while True:
        print("starting fourth thread")
        time.sleep(500)
        global first_run
        try:
            page = requests.get('https://www.daft.ie/property-for-sale/ballygarvan-cork?salePrice_from=200000&salePrice_to=300000',
                headers=headers).text
            soup = BeautifulSoup(page, 'html.parser')
            divs = soup.findAll('a', attrs={'class': None})
            fcur_bally = 'https://www.daft.ie' + divs[0].get('href')
            print("Current ad in ballygarvan :", fcur_bally)
            if not first_run:
                page = requests.get('https://www.daft.ie/property-for-sale/ballygarvan-cork?salePrice_from=200000&salePrice_to=300000', headers=headers).text
                soup = BeautifulSoup(page, 'html.parser')
                divs = soup.findAll('a', attrs={'class': None})
                ncur_bally = 'https://www.daft.ie' + divs[0].get('href')
                if ncur_bally != fcur_bally:
                    telegram_bot_sendtext(ncur_bally)
                else:
                    continue
            first_run = False
        except Exception as e:
            print(e)
            pass



if __name__ == "__main__":
    t1 = threading.Thread(target=carrigaline, name='t1')
    t1.start()
    t2 = threading.Thread(target=minane, name='t2')
    t2.start()
    t3 = threading.Thread(target=crosshaven, name='t3')
    t3.start()
    t4 = threading.Thread(target=ballygarvan, name='t4')
    t4.start()

