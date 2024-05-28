import requests
#FreeCurrencyAPI
API_KEY = 'fca_live_yCdlQVr55o5RGyj0rhcRwROH2gMUByiNztWARI0Y'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES) #list to string
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid currency")
        return None

while True:
    money = input("Enter currency type (q for quit): ").upper()
    if money == "Q":
        break
    data = convert_currency(money)
    if not data:
        continue

    del data[money]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")