import requests # type: ignore

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

def get_bitcoin_price():
    try:
        response = requests.get(url)    
        data = response.json()
        price = float(data['price'])
    
        print("HTTP STATUS CODE: ", response.status_code)
        print(f"Bitcoin (BTC) Current Price is: {price:.2f} $")
    
    except Exception as e:
        print("*** ERROR ***")
        print("An error has occurred fetching data, check internet connection")

def main():
    get_bitcoin_price()


if __name__ == "__main__":
    main()
