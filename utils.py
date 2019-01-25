import pandas as pd
from pandas_datareader import data, wb
from datetime import datetime
from yahoo_fin import stock_info as si


def updateStockValuations(tickers, currentValues, stockHistory):
    while True:
        for ticker in tickers:
            try:
                ## just want the live price of the stock (since we aren't including
                ##      any predictive features in yet based on past performance)
                value = si.get_live_price(ticker)
                if value is not None and value != currentValues[ticker]:
                    addHistory(currentValues[ticker], value, stockHistory)

                    currentValues[ticker] = value
                    print (ticker + ": " + str(currentValues[ticker]))
            except ValueError:
                continue

def addHistory(oldVal, newVal, history):
    priceChange = percentChanged(currentValues[ticker], value)
    if ticker not in history.keys():
        history[ticker] = []
    history[ticker].append(priceChange)
    ## NEED TO IMPLEMENT LOGIC TO BUY/SELL-OFF STOCK

def AsyncBuySellStock(totalOwned, individualPurchases, currentValues,
    stockHistory, watchlist, availableFunds):
    for ticker in watchlist:
        ## first case is that we don't own a stock and its price is going up
        ## which for now we want to mean an automatic buy (later will implement
        ## logic to make sure we can afford the purchase)
        history = stockHistory[ticker]
        currVal = currentValues[ticker]
        if ticker not in totalOwned.keys() and history[len(history) - 1] > 0 and currVal <= availableFunds:
            ## BUY STOCK
            if ticker not in stockHistory.keys():
                stockHistory[ticker] = []
            ## for now just want to buy half of the stock we can afford,
            ##      in order to save some capital for other stocks we come across
            buyAmount = int(availableFunds/(currVal * 2))
            totalOwned[ticker] += buyAmount
            individualPurchases.append((ticker, buyAmount, currentValues[ticker]))
            availableFunds -= buyAmount * currVal
        ## next case is own stock and its price starts to dip in which case
        ## we want to automatically sell (for now)
        if ticker in totalOwned.keys() and history[len(history) - 1] < 0:
            ## Sell stocks
            ## update total owned to not include that key anymore
            ## update individual purchases to not include any key dictionaries with
            ##      that ticker name
            ## later need to update the amount of money available to the algorithm
            ##      by adding in the currentValue at the time of sale * # sold
            ## possibly "clear" the stockHistory at this point??
            pass

def updateCurrentTotalValuation(currentValues, totalOwned, currentTotalValuation):
    while True:
        currentTotalValuation = 0.0
        for owned in list(totalOwned.keys()):
            currentTotalValuation += (currentValues[owned] * totalOwned[owned])
            print("Total Valuation: " + str(currentTotalValuation))

def percentChanged(oldValue, newValue):
    change = ((oldValue - newValue) / oldVal) * 100
    return change







def processManualInput(watchlist):
    while True:
        userSpecification = input()
        response = processUserInput(userSpecification, watchlist)
        if response is not None:
            print(response)
        else:
            print("Sorry, your request could not be processed. Please make"
                + " sure your inputs match the expected form.")


def processUserInput(input, watchlist, totalOwned):
    args = input.split(" ")
    if args[0] == "-b" or args[0] == "-B":
        processPurchaseRequest(args[1:])
    if args[0] == "-s" or args[0] == "-S":
        processSellRequest(args[1:])
    if args[0] == "-w" or args[0] == "-W":
        if len(args) == 6:
            return processWatchRequest(args[1], args[2], args[3], args[4], args[5], watchlist)
        else:
            return None
    if args[0] == "-rw" or args[0] == "-RW" or args[0] == "-rW" or args[0] == "-Rw":
        if len(args) == 2:
            return processRemoveWatchRequest(args[1], watchlist, totalOwned)
        else:
            return None
    return None

def processWatchRequest(abbrev, lowSell, highSell, lowBuy, highBuy, watchlist):
    order = WatchOrder(abbrev, lowSell, highSell, lowBuy, highBuy)
    if order not in watchlist:
        watchlist.append(order)
        return "Successfully added your watch request!"
    else:
        for x in xrange(len(watchlist)):
            if watchlist[x] == order:
                watchlist[x] = order
        return "This stock is already in your watchlist! Updated your buy/sell thresholds with the new values."

def processRemoveWatchRequest(stock, watchlist, totalOwned):
    if totalOwned[stock] == 0:
        for x in xrange(len(watchlist)):
            if watchlist[x].getAbbrev() == stock.upper():
                del watchlist[x]
                return "Successfully removed watchlist for " + stock.upper()
    else:
        return "Failure! Cannot remove a watch for a stock you own."
