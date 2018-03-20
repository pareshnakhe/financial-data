# financial-data

This code implements Hedge algorithm (Freund-Schapire 97) on stock data from 30 companies from 2010 to 2018.

Data.py: Concerns itself with fetching and processing the stock data.
Hedge.py: Contains two implementations of the Hedge algorithm: The standard one and one where we reinvest the
  return in the next round.
  
example.csv: Contains "tickers" for the company stocks that we want to process. Temp file is just a holder for the remaining tickers.
