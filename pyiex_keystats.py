from pyiex_config import * 


def beta(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["beta"]


def shortInterest(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["shortInterest"]


def shortDate(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["shortDate"]


def dividendRate(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["dividendRate"]


def dividendYield(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["dividendYield"]


def exDividendDate(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["exDividendDate"]


def sharesOutstanding(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["sharesOutstanding"]


def float(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["float"]


def returnOnEquity(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["returnOnEquity"]


def ebitda(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["EBITDA"]


def revenue(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["revenue"]


def grossProfit(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["grossProfit"]


def cash(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["cash"]


def debt(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["debt"]


def revenuePerShare(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["revenuePerShare"]


def revenuePerEmployee(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["revenuePerEmployee"]


def peRatioHigh(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["peRatioHigh"]


def peRatioLow(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["peRatioLow"]


def returnOnAssets(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["returnOnAssets"]


def returnOnCapital(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["returnOnCapital"]


def profitMargin(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["profitMargin"]


def priceToSales(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["priceToSales"]


def priceToBook(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["priceToBook"]


def day200MovingAvg(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["day200MovingAvg"]


def day50MovingAvg(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["day50MovingAvg"]


def institutionPercent(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["institutionPercent"]


def insiderPercent(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["insiderPercent"]


def shortRatio(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["shortRatio"]


def year5ChangePercent(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["year5ChangePercent"]


def year2ChangePercent(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["year2ChangePercent"]


def year1ChangePercent(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["year1ChangePercent"]


def ytdChangePercent(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["ytdChangePercent"]


def month6ChangePercent(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["month6ChangePercent"]


def month3ChangePercent(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["month3ChangePercent"]


def month1ChangePercent(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["month1ChangePercent"]


def day5ChangePercent(symbol):
    return requests.get(base_url + version + "/stock/" \
           + symbol + "/stats") .json()["day5ChangePercent"]
