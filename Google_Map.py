import pandas as pd, numpy as np
import requests
import json
import time
final_data = []
# Parameters
coordinate= '53.5511'+","+'9.9937'
keyword = 'gym  '
radius = '1000'
api_key = 'AIzaSyC1ZR7xxekD_tNuRSHxZA9SEJMhsKHewss' #insert your Places API
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + coordinate + '&radius=' + str(
    radius) + '&keyword=' + str(keyword) + '&key=' + str(api_key)
while True:
    print(url)
    respon = requests.get(url)
    jj = json.loads(respon.text)
    print(jj)
    results = jj['results']
    for result in results:
        name = result['name']
        place_id = result['place_id']
        lat = result['geometry']['location']['lat']
        lng = result['geometry']['location']['lng']
        rating = result['rating']
        types = result['types']
        vicinity = result['vicinity']
        data = [name, place_id, lat, lng, rating, types, vicinity]
        final_data.append(data)
        time.sleep(5)
        df = pd.DataFrame.from_records(final_data, columns=['Place Name', 'Place ID', 'Latitude', 'Longitude', 'Types', 'Vicinity', 'Address'])
        df.to_csv('gym_Hamburg.csv')

    if 'next_page_token' in jj:

        next_page_token = jj['next_page_token']
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=' + str(api_key) + '&pagetoken=' + str(
            next_page_token)
        labels = ['Place Name', 'Place ID', 'Latitude', 'Longitude', 'Types', 'Vicinity', 'Address']
        df = pd.DataFrame.from_records(final_data, columns=labels)
        df.to_csv('gym_Hamburg.csv')
    else:
        break






