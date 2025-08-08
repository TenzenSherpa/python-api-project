import requests

BASE_URL = "https://api.coingecko.com/api/v3/simple/price"

def get_crypto_price(coin, currency):

    # building params
    params = {
        "ids":coin,
        "vs_currencies":currency,
    
    }
    # Since we are sending params as dict, 
    # the requests converts it into something like
    # https://api.openweathermap.org/data/2.5/weather?q={city}&appi={API_key}
    response = requests.get(BASE_URL, params=params)
    # make the GET request to the api.

    # Check if the request failed or not
    if response.status_code != 200:
        print("Error:", response.status_code)
        return None
    
    # Parse JSON response into python dictionary
    data = response.json()

    # data looks like {
#   "bitcoin": {
#     "usd": 67187.3358936566,
#     "usd_market_cap": 1317802988326.25,
#     "usd_24h_vol": 31260929299.5248,
#     "usd_24h_change": 3.63727894677354,
#     "last_updated_at": 1711356300
#   }
# }
    # EXAMPLE
    #coin = "bitcoin"
    #currency = "usd"
    price = data.get(coin, {}).get(currency)

    if price:
        print(f"The currency price of {coin} is {price} {currency}.")
    else:
        print("Coin or currency not found")