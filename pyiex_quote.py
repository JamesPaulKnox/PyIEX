from pyiex_config import *


def calculationPrice(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["calculationPrice"]


def openPrice(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["open"]


def openTime(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["openTime"]


def closePrice(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["close"]


def closeTime(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["closeTime"]


def highPrice(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["high"]


def lowPrice(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["low"]


def latestPrice(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["latestPrice"]


def latestSource(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["latestSource"]


def latestTime(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["latestTime"]


def latestUpdate(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["latestUpdate"]


def latestVolume(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["latestVolume"]


def iexRealtimePrice(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["iexRealtimePrice"]


def iexRealtimeSize(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["iexRealtimeSize"]


def iexLastUpdated(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["iexLastUpdated"]


def delayedPrice(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["delayedPrice"]


def delayedPriceTime(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["latestPrice"]


def extPrice(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["extendedPrice"]


def extChange(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["extendedChange"]


def extChangePercent(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["extendedChangePercent"]


def extPriceTime(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["extendedPriceTime"]


def changePrice(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["change"]


def changePercent(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["changePercent"]


def iexMarketPercent(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["iexMarketPercent"]


def iexVolume(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["iexVolume"]


def avgTotalVolume(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["avgTotalVolume"]


def iexBidPrice(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["iexBidPrice"]


def iexBidSize(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["iexBidSize"]


def iexAskPrice(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["iexAskPrice"]


def iexAskSize(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["iexAskSize"]


def marketCap(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["marketCap"]


def peRatio(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["peRatio"]


def yearHigh(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote".format(percent)).json()["week52High"]


def yearLow(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["week52Low"]


def ytdChange(symbol):
    return requests.get(base_url + version +"/stock/" + symbol +
           "/quote?displayPercent=false").json()["ytdChange"]


def yearChange(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["week52change"]
