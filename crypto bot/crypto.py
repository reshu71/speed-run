import requests

def get_trading_signal(coin_id):

    try:

        response =  requests.get(f"https://api.fake-crypto.com/v1/{coin_id}")

        if response.status_code != 200:
            return "HOLD"
        
        # Parse the JSON. Assume the API returns this format: {"id": "bitcoin", "price_usd": 50000}

        price_usd = response.json()

        if price_usd['price'] < 40000:
            return 'BUY'
        if price_usd['price'] >60000:
            return 'SELL'
        else:
            return 'HOLD'
        
    except requests.exceptions.ConnectionError:
        return "NETWORK ERROR"
    