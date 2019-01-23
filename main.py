## will use pandas' built-in features allowing it to interact
## with data for this purpose
## written in python3 for now, due to some issues with authentication
##      on the nasdaq site when using Python2.7
import pandas as pd

## get all of the stock exchanges we wish to work with
# NYSE
url_nyse = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download"
# Nasdaq
url_nasdaq = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
# AMEX
url_amex = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download"

## for now we'll just use the NYSE
df = pd.DataFrame.from_csv(url_nyse)

nyseStocksAbbrevs = df.index.tolist()

print (nyseStocksAbbrevs)
