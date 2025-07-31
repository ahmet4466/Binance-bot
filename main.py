from binance.client import Client
from binance.enums import *
import os, time

client = Client(os.environ["BINANCE_API_KEY"], os.environ["BINANCE_API_SECRET"])

symbol = "ORDIUSDT"
quantity = 0.05

def get_price():
    return float(client.get_symbol_ticker(symbol=symbol)["price"])

def place_order():
    order = client.futures_create_order(
        symbol=symbol,
        side=SIDE_BUY,
        type=ORDER_TYPE_MARKET,
        quantity=quantity
    )
    print("Order:", order)

while True:
    price = get_price()
    print("Price:", price)
    if price < 100:
        place_order()
        break
    time.sleep(5)
