import time
import websocket , json
from binance import Client
import pandas as pd

api_key = 
api_secret = 

client = Client(api_key, api_secret)

li = []
li2 = []
li3 = []

counter = 0

asset = ''

def coin():
    x = pd.DataFrame(client.get_symbol_ticker())
    y = x[x.symbol.str.contains('USD')]
    z = y[~(y.symbol.str.contains('BUSD') | y.symbol.str.contains('UP') | y.symbol.str.contains(
        'DOWN') | y.symbol.str.contains('USDT') | y.symbol.str.contains('USDC'))]

    for i in z.symbol:
        global li
        li.append(i)

    for i in li:
        global li2
        xx = (client.get_ticker(symbol=i))
        yy = xx['priceChangePercent']
        li2.append(yy)

    for i in li2:
        li3.append(float(i))
    
    global asset
    
    di = dict(zip(li, li3))

    max_key = max(di, key=di.get)

    di.pop(max_key)

    sec_key = max(di, key=di.get)

    di.pop(sec_key)

    third_key = max(di, key=di.get)

    if counter == 0:
        asset = str(max_key)
        print(max_key)
        return asset

    if counter == 1:
        asset = str(sec_key)
        print(sec_key)
        return sec_key

    if counter == 2:
        asset = str(third_key)
        print(third_key)
        return third_key

    if counter >= 3:
        print(f'other top 3 coins didnt work so going back to first {max_key}')
        asset = str(max_key)
        return max_key
