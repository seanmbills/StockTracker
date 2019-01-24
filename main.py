## will use pandas' built-in features allowing it to interact
## with data for this purpose
## written in python3 for now, due to some issues with authentication
##      on the nasdaq site when using Python2.7
import pandas as pd
from pandas_datareader import data, wb
from datetime import datetime
from yahoo_fin import stock_info as si

## get all of the stock exchanges we wish to work with
# NYSE
url_nyse = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download"
# Nasdaq
url_nasdaq = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
# AMEX
url_amex = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download"


## for now we'll just use the NYSE
df = pd.DataFrame.from_csv(url_nyse)

## get all of the abbreviations for stocks on the nyse
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

## loop over stock abbreviations and get value from Yahoo
## stock info
start = '2019-01-01'
end = datetime.now()

for ticker in tickers:
    try:
        ## just want the live price of the stock (since we aren't including
        ##      any predictive features in yet based on past performance)
        value = si.get_live_price(ticker)
        if value is not None:
            currentValues[ticker] = value
            # print (ticker + ": " + str(currentValues[ticker]))
    except ValueError:
        continue
