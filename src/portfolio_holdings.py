import pandas as pd
import yfinance as yf

from index_holdings import index_holdings


def portfolio_holdings(file):
       raw_data = pd.read_csv(file)
       
       holdings = (raw_data.groupby("Ticker Symbol").agg(Shares=("Shares", "sum")))
       
       for ticker in holdings.index:
               holdings.loc[ticker, "Price"] = yf.Ticker(ticker).fast_info["last_price"]
        
       holdings["Price"] = holdings["Price"].round(2)
       holdings["Value"] = (holdings["Shares"] * holdings["Price"]).round(2)
       holdings["Proportion"] = (holdings["Value"] / holdings["Value"].sum() * 100).round(2)
       
       return holdings


