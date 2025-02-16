import yfinance as yf
import pandas as pd
import streamlit as st

# List of Nifty 50 stocks
nifty50 = [
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "HINDUNILVR.NS", "SBIN.NS", "ITC.NS", "BAJFINANCE.NS", "BHARTIARTL.NS",
    "KOTAKBANK.NS", "LT.NS", "AXISBANK.NS", "ASIANPAINT.NS", "HCLTECH.NS",
    "MARUTI.NS", "SUNPHARMA.NS", "TITAN.NS", "ULTRACEMCO.NS", "TATASTEEL.NS",
    "WIPRO.NS", "NTPC.NS", "POWERGRID.NS", "INDUSINDBK.NS", "NESTLEIND.NS",
    "GRASIM.NS", "ONGC.NS", "JSWSTEEL.NS", "TECHM.NS", "BAJAJFINSV.NS",
    "COALINDIA.NS", "ADANIENT.NS", "M&M.NS", "BRITANNIA.NS", "CIPLA.NS",
    "TATAMOTORS.NS", "BPCL.NS", "APOLLOHOSP.NS", "DIVISLAB.NS", "EICHERMOT.NS",
    "HDFCLIFE.NS", "HEROMOTOCO.NS", "BAJAJ-AUTO.NS", "UPL.NS", "DRREDDY.NS",
    "SBILIFE.NS", "SHREECEM.NS", "ICICIPRULI.NS", "ADANIPORTS.NS", "HINDALCO.NS"
]

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
