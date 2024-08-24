from websockets.sync.client import connect
import asyncio
import websocket
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:5555')

with connect("wss://stream.binance.com:9443/ws") as websocket:
    #Subscription
    json_subscribe = '{"method": "SUBSCRIBE", "params": ["shibusdt@kline_1s","maticusdt@kline_1s","solusdt@kline_1s","btcusdt@kline_1s","bnbusdt@kline_1s","dogeusdt@kline_1s"],  "id": 2}' #other pairs
    websocket.send(json_subscribe)
    while True:
        message = "CRYPTO " + websocket.recv()
        socket.send_string(message)
        print(f"Received: {message}")

# import math
# import time
# import random
# import zmq
# context = zmq.Context()
# socket = context.socket(zmq.PUB)
# socket.bind('tcp://127.0.0.1:5555')

# class InstrumentPrice(object):
#     def __init__(self):
#         self.symbol = 'SYMBOL'
#         self.t = time.time()
#         self.value = 100.
#         self.sigma = 0.4
#         self.r = 0.01
    
#     def simulate_value(self):

#         t = time.time()
#         dt = (t - self.t) / (252 * 8 * 60 * 60)
#         dt *= 500
#         self.t = t
#         self.value *= math.exp((self.r - 0.5 * self.sigma ** 2) * dt +
#         self.sigma * math.sqrt(dt) * random.gauss(0, 1))
#         return self.value

# ip = InstrumentPrice()
# while True:
#     msg = '{} {:.2f}'.format(ip.symbol, ip.simulate_value())
#     print(msg)
#     socket.send_string(msg)
#     time.sleep(random.random() * 2)