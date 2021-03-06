## will use pandas' built-in features allowing it to interact
## with data for this purpose
## written in python3 for now, due to some issues with authentication
##      on the nasdaq site when using Python2.7
import pandas as pd
from pandas_datareader import data, wb
from datetime import datetime
from yahoo_fin import stock_info as si
from threading import Thread
from utils import *

## get all of the stock exchanges we wish to work with
# NYSE
url_nyse = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download"
# Nasdaq
url_nasdaq = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
# AMEX
url_amex = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download"


## gets the NYSE stock company abbreviations
df = pd.DataFrame.from_csv(url_nyse)

## reads data from the csv to a list format
tickers = df.index.tolist()

## dictionary to track stock live stock price
## Key: stock Val: current price
currentValues = {}
## dictionary to track current owned stock
## Key: Stock Abbrev. Value: total # owned (across all purchase orders?)
totalOwned = {}
## dictionary to track individual purchases of a stock to price purchased at
## Key: a dictionary of form:
##      {Key: stock purchased
##      Value: amount purchased in this purchase}
## Value: price purchased at
individualPurchases = {}
## keeps track of valuation of current stocks:
currentTotalValuation = 0.0

## track the running threads (each executing a different function for reading/
##      updating values in our dictionary)
threads = []

## track all of the stocks the user wants to keep an eye on
##      stocks that are purchased should automatically be added to this list
##      but selling a stock shouldn't remove it immediately
watchlist = []

## track changes over time of the stock since last purchase/sell-off
stockHistory = {}


def main():
    ## create threads to run each of the method that needs to check the current
    ## valuation of stocks and update the current valuation of the user's
    ## owned stocks
    updateStockValueProcess = Thread(target=updateStockValuations, args=[tickers, currentValues, stockHistory])
    updateStockValueProcess.start()
    threads.append(updateStockValueProcess)
    updateCurrentTotalValueProcess = Thread(target=updateCurrentTotalValuation, args=[currentValues, totalOwned, currentTotalValuation])
    updateCurrentTotalValueProcess.start()
    threads.append(updateCurrentTotalValueProcess)

if __name__ == "__main__":
    main()
