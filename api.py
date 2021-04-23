import requests
import json
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

headers = {
    'x-rapidapi-key': "x",
    'x-rapidapi-host': "coinranking1.p.rapidapi.com"
    }

btcurl = "https://coinranking1.p.rapidapi.com/coin/1"
ethurl = "https://coinranking1.p.rapidapi.com/coin/2"
xrpurl = "https://coinranking1.p.rapidapi.com/coin/3"
bccurl = "https://coinranking1.p.rapidapi.com/coin/4"

def obj_dict(obj):
    return obj.__dict__

class coin:
        name = ""
        symbol = ""
        price = 0
        volume = 0
        hundred = 0
        quarter = 0
        fivegrand = 0

@app.route('/coins', methods=['GET'])
def api_all():
    coins = []
    response = requests.request("GET", btcurl, headers=headers)
    responseJson=response.json()
    coin1 = coin()
    coin1.name = responseJson["data"]["coin"]["name"]
    coin1.symbol = responseJson["data"]["coin"]["symbol"]
    coin1.price = round(float(responseJson["data"]["coin"]["price"]), 2)
    coin1.volume = responseJson["data"]["coin"]["volume"]
    coin1.hundred = int(float(responseJson["data"]["coin"]["price"])/100)
    coin1.quarter = int(float(responseJson["data"]["coin"]["price"])/250)
    coin1.fivegrand = int(float(responseJson["data"]["coin"]["price"])/5000)
    coins.append(coin1)
    
    response = requests.request("GET", ethurl, headers=headers)
    responseJson=response.json()
    coin1 = coin()
    coin1.name = responseJson["data"]["coin"]["name"]
    coin1.symbol = responseJson["data"]["coin"]["symbol"]
    coin1.price = round(float(responseJson["data"]["coin"]["price"]), 2)
    coin1.volume = responseJson["data"]["coin"]["volume"]
    coin1.hundred = int(float(responseJson["data"]["coin"]["price"])/100)
    coin1.quarter = int(float(responseJson["data"]["coin"]["price"])/250)
    coin1.fivegrand = int(float(responseJson["data"]["coin"]["price"])/5000)
    coins.append(coin1)
    
    response = requests.request("GET", xrpurl, headers=headers)
    responseJson=response.json()
    coin1 = coin()
    coin1.name = responseJson["data"]["coin"]["name"]
    coin1.symbol = responseJson["data"]["coin"]["symbol"]
    coin1.price = round(float(responseJson["data"]["coin"]["price"]), 2)
    coin1.volume = responseJson["data"]["coin"]["volume"]
    coin1.hundred = int(float(responseJson["data"]["coin"]["price"])/100)
    coin1.quarter = int(float(responseJson["data"]["coin"]["price"])/250)
    coin1.fivegrand = int(float(responseJson["data"]["coin"]["price"])/5000)
    coins.append(coin1)
    
    response = requests.request("GET", bccurl, headers=headers)
    responseJson=response.json()
    coin1 = coin()
    coin1.name = responseJson["data"]["coin"]["name"]
    coin1.symbol = responseJson["data"]["coin"]["symbol"]
    coin1.price = round(float(responseJson["data"]["coin"]["price"]), 2)
    coin1.volume = responseJson["data"]["coin"]["volume"]
    coin1.hundred = int(float(responseJson["data"]["coin"]["price"])/100)
    coin1.quarter = int(float(responseJson["data"]["coin"]["price"])/250)
    coin1.fivegrand = int(float(responseJson["data"]["coin"]["price"])/5000)
    coins.append(coin1)
    return json.dumps(coins, default=obj_dict)

app.run()