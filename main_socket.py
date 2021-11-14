import websocket , json
from binance import Client
from coin_finder import *
from historicals import *
from livesma import *
from RSI import *

api_key = 'fCBUzQtECIrp4dfeuc4AsahRalt48Or0HKbagFyMgdqXia112FjevdjSe7qdAgC4'
api_secret = 'nVdJOZXc42vZYPtX2GBHzHHXMueHAL6atAMYIN4I08nscaqM6Cyj6zM9gnevJmLg'

client = Client(api_key, api_secret)

asset = coin()

histST, histMT, histLT = gethistoricals(asset, 495)
    
def on_message(ws, message):
    json_message = json.loads(message)
    candle = json_message['k']
    candle_close = candle['x']
    close_price = candle['c']
    print(candle_close)
    print(close_price)
    
    if candle_close:
        livest, livemt, livelt, rsiMT = liveSMA(histST, histMT, histLT, close_price)
        #rsi(rsiMT)
        print(livest, livemt, livelt)
        '''if liveST > liveLT: place order'''
        '''this closes connection allwing for you to do a while true loop'''
        #ws.keep_running = False
        

ws = websocket.WebSocketApp(f'wss://stream.binance.com:9443/ws/{asset.lower()}t@kline_1m', on_message = on_message)
ws.run_forever()
