import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import acf
from fetch_data import ts_data

def detect_seasonality(ts: pd.DataFrame, column: str = "price", max_lag: int = 365) -> int:
    """
    Detects the dominant seasonality in a time series using autocorrelation.

    Parameters:
        ts (pd.DataFrame): DataFrame with a time series column.
        column (str): Name of the column containing the time series.
        max_lag (int): Maximum lag to consider for seasonality (in days).

    Returns:
        int: Estimated seasonal period. Returns 1 if no clear seasonality is found.
    """
    # Ensure the series is a 1D array
    series = ts[column].dropna().values
    
    # Calculate autocorrelation for lags up to max_lag
    autocorr = acf(series, nlags=max_lag, fft=True)
    
    # Whats the point of even returning autocorrelation at lag 0, because it always 1 :>)
    autocorr[0] = 0
    
    # Find the lag with the maximum autocorrelation
    seasonal_period = int(np.argmax(autocorr))
    
    # # If the max autocorrelation is too low, assume no seasonality
    # if autocorr[seasonal_period] < 0.3:  # I think this a good base threshold, ill come back to optimise for a each stock
    #     return 1
    
    return seasonal_period