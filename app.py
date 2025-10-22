import datetime as dt                   # For dates
import pandas as pd                     # For data handling
import streamlit as st                  # Web UI
import yfinance as yf                   # Yahoo Finance access

# ---------- Page setup ----------
st.set_page_config(page_title="Yahoo Finance Chart", page_icon="📈")
st.title("Yahoo Finance — Quick Price Chart")

# Short instructions for the user
st.caption("Type a ticker (e.g., **AAPL**, **MSFT**, **TSLA**). Choose a period or custom dates, then view the chart.")

# ---------- Controls ----------
# Text input for ticker
ticker = st.text_input(
    label="Ticker",
    value="AAPL",                      # Default example; user can change
    help="Enter a valid Yahoo Finance symbol (e.g., AAPL, MSFT, TSLA, AMZN)."
).strip().upper()

# Choice between quick period presets or custom date range
mode = st.radio(
    "Date selection mode",
    options=["Preset period", "Custom range"],
    horizontal=True
)

# Preset periods supported by yfinance: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
preset = None
start_date = None
end_date = None

if mode == "Preset period":
    preset = st.selectbox(
        "Period",
        options=["1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"],
        index=3
    )
else:
    # Default to the past year if user picks custom
    default_end = dt.date.today()
    default_start = default_end - dt.timedelta(days=365)

    start_date = st.date_input("Start date", value=default_start)
    end_date = st.date_input("End date", value=default_end)

    # Safety: force start <= end
    if start_date > end_date:
        st.error("Start date must be on or before end date.")
        st.stop()

# Interval selection (granularity)
interval = st.selectbox(
    "Interval (granularity)",
    options=["1d", "1wk", "1mo"],       # Daily/weekly/monthly to keep it simple
    index=0
)

# ---------- Data loader with cache ----------
@st.cache_data(show_spinner=True, ttl=60*10)  # Cache for 10 minutes
def load_prices(tkr: str, period: str | None, start: dt.date | None, end: dt.date | None, interval: str) -> pd.DataFrame:
    """
    Download OHLCV prices for a given ticker using yfinance.
    Either 'period' OR ('start' and 'end') is provided.
    Returns a DataFrame with a DatetimeIndex.
    """
    try:
        if period is not None:
            # Using a preset period (yfinance handles end date internally)
            df = yf.download(tickers=tkr, period=period, interval=interval, progress=False, auto_adjust=False)
        else:
            # Using explicit start/end
            df = yf.download(tickers=tkr, start=start, end=end + dt.timedelta(days=1), interval=interval, progress=False, auto_adjust=False)
            # Note: add one day to end so the chosen end date is inclusive

        # Ensure a DataFrame comes back and has rows
        if not isinstance(df, pd.DataFrame) or df.empty:
            return pd.DataFrame()

        # Normalise column names (sometimes yfinance returns multi-index)
        df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]
        return df
    except Exception:
        # Return empty on failure; UI will show an error
        return pd.DataFrame()

# ---------- Fetch + display ----------
if not ticker:
    st.info("Enter a ticker to begin.")
    st.stop()

with st.spinner("Fetching data from Yahoo Finance..."):
    prices = load_prices(ticker, preset, start_date, end_date, interval)

# Validate result
if prices.empty:
    st.error("No data returned. Check the ticker symbol (or try a different period/interval).")
    st.stop()

# Show a small summary
st.subheader(f"{ticker} — price data")
st.caption(f"Rows: {len(prices)} | Range: {prices.index.min().date()} → {prices.index.max().date()} | Interval: {interval}")

# Show head (preview)
st.dataframe(prices.head(), use_container_width=True)

# ---------- Chart ----------
st.subheader("Close price chart")
if "Close" not in prices.columns:
    st.error("Downloaded data did not include a 'Close' column.")
else:
    st.line_chart(prices["Close"], use_container_width=True)

# ---------- Optional extras ----------
# Toggle: show volume below
with st.expander("Show volume chart"):
    if "Volume" in prices.columns:
        st.line_chart(prices["Volume"], use_container_width=True)
    else:
        st.info("No Volume column available for this combination of period/interval.")

# Download CSV
st.download_button(
    label="Download CSV",
    data=prices.to_csv(index=True),
    file_name=f"{ticker}_{interval}.csv",
    mime="text/csv"
)
