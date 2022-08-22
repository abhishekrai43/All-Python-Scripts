import requests
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=Sent from python&language=english&route=p&numbers=9818084139,9910054139"
headers = {
'authorization': "gE1y04plwnYzDNJxuGcFvdAiMQkqRIHjKOf9a2mVSrhCUPBLb8eN8vqCzEd2ygifpkMj476tVmcPOGFR",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)