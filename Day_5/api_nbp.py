import requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/usd"

response = requests.get(url)
print(response)

print(response.text)

data = response.json()
print(data)

print(data['rates'])
print(data['rates'][0])
print(data['rates'][0]['mid'])


