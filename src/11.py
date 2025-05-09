import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1"

payload = {}
headers= {
  "apikey": "yTQXbpvWrKiapyBvQDW5cmkT4D9WtWoD"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text1