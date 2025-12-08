import yfinance as yf
import pandas as pd

def ts_data(ticker: str, start: str = None, end: str = None) -> pd.DataFrame:
    df = yf.download(ticker, start=start, end=end)
    price_df = df[["Close"]].rename(columns={"Close": "price"})
    return price_df
