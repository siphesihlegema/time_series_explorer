import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from fetch_data import ts_data
from seasonality import detect_seasonality
from decomposition import ClassicalDecomposition

st.title("📈 Time Series Explorer")

ticker = st.text_input("Ticker", "AAPL")
start_date = st.date_input("Start", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End", pd.to_datetime("2025-01-01"))

ts = ts_data(ticker, start=start_date, end=end_date)

seasonal_period = detect_seasonality(ts)
st.write(f"Estimated seasonal period: {seasonal_period} days")

decomp = ClassicalDecomposition(ts["price"], freq=seasonal_period)
fig, axes = plt.subplots(4, 1, figsize=(12, 10), sharex=True)
axes[0].plot(ts.index, ts["price"], label="Original"); axes[0].legend()
axes[1].plot(ts.index, decomp.trend, label="Trend", color="orange"); axes[1].legend()
axes[2].plot(ts.index, decomp.seasonal, label="Seasonal", color="green"); axes[2].legend()
axes[3].plot(ts.index, decomp.residual, label="Residual", color="red"); axes[3].legend()
plt.tight_layout()
st.pyplot(fig)
