import pandas as pd
from pandas_datareader import data, wb
from datetime import datetime
from yahoo_fin import stock_info as si


def updateStockValuations(tickers, currentValues):
    while True:
        for ticker in tickers:
            try:
                ## just want the live price of the stock (since we aren't including
                ##      any predictive features in yet based on past performance)
                value = si.get_live_price(ticker)
                if value is not None:
                    priceChange = percentChanged(currentValues[ticker], value)
                    currentValues[ticker] = value
                    print (ticker + ": " + str(currentValues[ticker]))
            except ValueError:
                continue

def updateCurrentTotalValuation(currentValues, totalOwned, currentTotalValuation):
    while True:
        currentTotalValuation = 0.0
        for owned in list(totalOwned.keys()):
            currentTotalValuation += (currentValues[owned] * totalOwned[owned])
            print("Total Valuation: " + str(currentTotalValuation))

def percentChanged(oldValue, newValue):
    change = (oldValue - newValue) / 100
    return change

def manualWatchlistUpdate(watchlist):
    while True:
        userSpecification = input()
        processUserInput(userSpecification)

def processUserInput(input):
    args = input.split(" ")
    
