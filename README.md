# 📊 **Time Series Explorer**

A modular, transparent, and extensible **time-series analysis &
forecasting** application built with **Python** and **Streamlit**.\
Users can enter any financial ticker symbol and the app automatically
runs a full pipeline: data fetching → preprocessing → seasonality
detection → decomposition → multi-model forecasting → visualization.

## ⭐ **Features**

### 🔹 1. Automatic Data Fetching

-   Downloads historical market data from **Yahoo Finance**
-   Supports custom tickers & date ranges
-   Cleans and standardizes the "Close" column into a `price` series

### 🔹 2. Preprocessing & Transformations

-   Modular transformations, including:
    -   Differencing
    -   De-trending
    -   Log transforms
-   Completely swappable / extendable modules

### 🔹 3. Automatic Seasonality Detection

-   Uses **autocorrelation (ACF)** to infer dominant seasonal periods
-   Removes the need for user guesswork
-   Robust to noisy financial data

### 🔹 4. Classical Time Series Decomposition

Performed using `statsmodels`, including: - 📈 Trend - ♻️ Seasonality -
🔧 Residuals

Supports both **additive** and **multiplicative** models, all visualized
clearly.

### 🔹 5. Forecasting Models Implemented

Multiple statistical forecasting approaches are fit & compared: - Mean -
Naive - Drift - Holt-Winters Exponential Smoothing - Auto-ARIMA

The architecture allows easy "plug-in" of future models.

### 🔹 6. Interactive Streamlit Interface

-   Clean UI
-   Interactive charts at every step
-   Full analysis pipeline displayed transparently
-   Ideal for reports, learning, or exploratory analysis

## 🏗️ **Project Architecture**

    src/
    │── fetch_data.py
    │── seasonality.py
    │── decomposition.py
    │── transformations.py
    │── forecasting_simple.py
    │── forecast_smoothing.py
    │── forecasting_arima.py
    .gitignore.py
    app.py
    README.md
    requirements.txt

## 🎯 **Purpose of the Project**

This app is designed to **teach**, **visualize**, and **demonstrate**
statistical time-series techniques in a transparent and interpretable
way, in to just show apply a some things i learnt in my stats course this year.

It goes beyond "black-box forecasting" by showing: - How data changes
through each transformation - How decomposition works internally - How
different models interpret the same data - Where seasonality and trends
actually come from

Perfect for students, quants, researchers, and analysts.

## 🚀 **How to Run**

### 1. Install dependencies

``` bash
pip install -r requirements.txt
```

### 2. Run the Streamlit app

``` bash
streamlit run app.py
```

## 🧪 **Usage**

1.  Enter a valid Yahoo Finance ticker (e.g., `AAPL`, `TSLA`, `CORN`,
    `BTC-USD`)
2.  Select an optional date range
3.  The app automatically:
    -   Fetches data
    -   Detects seasonality
    -   Runs decomposition
    -   Fits forecasting models
    -   Displays everything visually

## 🔮 **Future Enhancements**

-   SARIMA models
-   Facebook Prophet
-   LSTM / GRU neural networks
-   Regime-switching models
-   GARCH volatility modeling
-   Portfolio & multi-asset analysis

## 🛠️ **Tech Stack**

-   Python 3
-   Streamlit
-   pandas / numpy
-   statsmodels
-   yfinance
-   matplotlib / seaborn

## 📄 **License**

MIT (or your preferred license)

## 👤 **Author**

**Gema**\
Just a guy waiting for exam results --- UCT