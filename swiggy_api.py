import time
import csv
import requests
import urllib.parse
from csv import reader

header_added = False
timestr = time.strftime("%Y%m%d-%H%M%S")
print("Welcome to Restaurant Search")
time.sleep(1)
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
address = input("Enter the City name :")
lat_long_url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
lat_long = requests.get(url=lat_long_url, headers=headers).json()
time.sleep(3)
name = input("Enter the name of the Restaurant :")
search_url = f'https://www.swiggy.com/dapi/restaurants/search/v2_2?lat={lat_long[0]["lat"]}&lng={lat_long[0]["lon"]}&trackingId=ebaedb8a-d86d-2e0b-69c8-4a3643e7a397&str={name}&sld=false&non_partner_search=false'
n = False
info1 = requests.get(search_url).json()
restaurant = info1["data"]['restaurants']
for v in restaurant:
    restaurant_name = [v['restaurants']]
    for v in restaurant_name:

        for k in v:
            if not n:
                print("Restaurant Name: {}".format(k['name']))
                print("City: {}".format(k['city']))
                print("Area: {}".format(k['area']))
                print("Ratings: {}".format(k['avgRating']))

link = info1["data"]["restaurants"]

for i in link:
    for k, v in i.items():
        for item in v:
            if type(item) is dict:
                for a, b in item['slugs'].items():
                    if not n:
                        slug = b
                        print("Restaurant Address: -",slug.strip('-'))
                        n = True

rest_url = f'https://www.swiggy.com/dapi/menu/v4/full?&slug={slug}'
info = requests.get(rest_url).json()
menu_items = info["data"]["menu"]["items"]
header_added1 = False
for k, v in menu_items.items():
    print("Name: {}".format(v["name"]))
    print("Price: {}".format(int(v["price"] / 100)))
    print("Description: {}".format(v["description"]))
    if v["isVeg"] == 1:
        veg = "Veg"
    else:
        veg = "Non-Veg"
    dict1 = {"Item": v["name"], "Price": int(v["price"] / 100), "Veg/Non-Veg": veg, "Description": v["description"]}
    with open(f'{name}_{address}.csv', 'a+', encoding='utf-8') as f:
        w = csv.DictWriter(f, dict1.keys())
        if not header_added:
            w.writeheader()
            header_added = True
        w.writerow(dict1)


    if "addons" in v.keys():
        for i in v["addons"]:
            print("\t{}".format(i["group_name"]))
            for j in i["choices"]:
                print("\t\tName: {}".format(j["name"]))
                print("\t\tPrice: {}".format(int(j["price"] / 100)))
                new_col = {"Description": i["group_name"], "Addon Name": j["name"], "AddOn Price": int(j["price"] / 100)}
                with open(f'{name}_{address}.csv', 'a+', encoding='utf-8', newline='') as f:
                    reader1 = reader(f)
                    w = csv.DictWriter(f, new_col.keys())
                    for row in reader1:
                        if not header_added1:
                            w.writeheader()
                            header_added = True
                        row.append(new_col)
                    w.writerow(new_col)

