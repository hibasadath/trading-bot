import requests

BASE_URL = "https://testnet.binancefuture.com"

def get_price(symbol="BTCUSDT"):
    url = f"{BASE_URL}/fapi/v1/ticker/price"
    params = {"symbol": symbol}

    response = requests.get(url, params=params)
    data = response.json()

    return float(data["price"])