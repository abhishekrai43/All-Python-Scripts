import requests

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/87.0.4280.141 Safari/537.36'
start = input("Enter the start date. E.g 2020-12-01 :")
end = input("Enter the end date :")
with requests.Session() as session:
    session.headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'X-Requested-With': 'XMLHttpRequest',
        'Authorization': 'Basic cG9ydGFsOg==',
        'User-Agent': user_agent,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://portal.volleymetrics.hudl.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://portal.volleymetrics.hudl.com/',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    data = {
        'grant_type': 'password',
        'username': 'merin_sinha24',
        'password': 'Dwayne4321'
    }
    response = session.post('https://api.volleymetrics.hudl.com/acct/oauth/token', data=data)
    token = response.json()['access_token']
    session.headers.update({'Authorization': 'Bearer ' + token})

    match_videos = dict()
    page = 1
    while True:
        params = (
            ('page', page),
            ('size', '20'),
            ('sort', ['matchDate,desc', 'id,desc']),
            ('startDate', f'{start}T00:00:00.000'),
            ('endDate', f'{end}T09:48:47.310'),
            ('matchType', 'match'),
        )
        response = session.get('https://api.volleymetrics.hudl.com/portal/events/other', params=params)

        matches = response.json()['content']


        for match in matches:

            r = session.get(f'https://api.volleymetrics.hudl.com/analysis/matches/{match["id"]}')
            video_url = r.json()['encodedVideoUrl']
            print(video_url)

            file_name = video_url.split('/')[-1]

            print("Downloading file:%s" % file_name)
            r = requests.get(video_url, stream=True)

            # download started
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)

                print("%s downloaded!\n" % file_name)

            print("All videos downloaded!")








