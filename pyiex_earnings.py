from pyiex_config import *

def generic(key, symbol, quarter=None):
    resp_str = requests.get(base_url + version +
               "/stock/" + symbol + "/earnings").json()
    earnings = {}
    if quarter > 3:
        quarter = 3
    if quarter == None:
        for i in resp_str["earnings"]:
            earnings[i["fiscalPeriod"]] = i[key]
    else:
        earnings[resp_str["earnings"][quarter]["fiscalPeriod"]] \
        = resp_str["earnings"][quarter][key]
    return earnings

def actualEPS(symbol, quarter=None):
    return generic("actualEPS", symbol, quarter)


def consensusEPS(symbol, quarter=None):
    return generic("consensusEPS", symbol, quarter)


def estimatedEPS(symbol, quarter=None):
    return generic("estimatedEPS", symbol, quarter)


def announceTime(symbol, quarter=None):
    return generic("announceTime", symbol, quarter)


def numberEstimates(symbol, quarter=None):
    return generic("numberOfEstimates", symbol, quarter)


def surpriseEPS(symbol, quarter=None):
    return generic("EPSSurpriseDollar", symbol, quarter)


def reportDate(symbol, quarter=None):
    return generic("EPSReportDate", symbol, quarter)


def fiscalEnd(symbol, quarter=None):
    return generic("fiscalEndDate", symbol, quarter)


def yearAgo(symbol, quarter=None):
    return generic("yearAgo", symbol, quarter)


# CP = Change Percent
def yearCP(symbol, quarter=None):
    return generic("yearAgoChangePercent", symbol, quarter)


# CP = Change Percent
def estCP(symbol, quarter=None):
    return generic("estimatedChangePercent", symbol, quarter)
