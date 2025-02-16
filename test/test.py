import yfinance as yf
import pandas as pd
import streamlit as st

# List of Nifty 50 stocks
nifty50 = ["TCS.NS", "INFY.NS", "HDFCBANK.NS", "RELIANCE.NS", "SBIN.NS"]

gainers = []

for stock in nifty50:
    data = yf.Ticker(stock).history(period="1d")
    change = ((data["Close"][-1] - data["Open"][-1]) / data["Open"][-1]) * 100
    gainers.append((stock, change))

# Sort by % Change
gainers.sort(key=lambda x: x[1], reverse=True)

# Convert to DataFrame
df = pd.DataFrame(gainers, columns=["Stock", "% Change"])

# Display in Streamlit
st.subheader("📈 Top 5 Gainers in Nifty 50")
st.dataframe(df.head(5))
