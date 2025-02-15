
import requests

API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd'

response = requests.get(API_URL)
data = response.json()

print(f"Bitcoin: ${data['bitcoin']['usd']}")
print(f"Ethereum: ${data['ethereum']['usd']}")
