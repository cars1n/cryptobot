from binance import Client
import pandas as pd

api_key = 
api_secret = 

client = Client(api_key, api_secret)

liveLT = []
liveMT = []
liveST = []

def gethistoricals(symbol, LT):
    closes = (client.get_historical_klines(symbol, '5m', str(LT) + 'minutes ago UTC', '1 minute ago UTC'))
    for i in closes:
        liveLT.append(i[4])
    
    liveMT = liveLT[74:]
    liveST = liveMT[18:]
    
    return liveST, liveMT, liveLT
