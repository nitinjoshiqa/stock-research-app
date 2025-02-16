import yfinance as yf
import pandas as pd

# ✅ Nifty 50 Stock Symbols (Yahoo Finance uses .NS for NSE stocks)
nifty50_symbols = [
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

# Function to fetch stock details
def fetch_stock_data():
    stocks = []
    for symbol in nifty50_symbols:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")

        # Check if data is available
        if not data.empty:
            info = stock.info
            stocks.append({
                "Stock": symbol.replace(".NS", ""),
                "Last Price (₹)": round(data["Close"][-1], 2),
                "Market Cap (Cr)": round(info.get("marketCap", 0) / 1e7, 2),
                "Volume": info.get("volume", "N/A"),
                "52-Week High (₹)": info.get("fiftyTwoWeekHigh", "N/A"),
                "52-Week Low (₹)": info.get("fiftyTwoWeekLow", "N/A"),
                "Change %": round(((data["Close"][-1] - data["Open"][-1]) / data["Open"][-1]) * 100, 2)
            })

    return pd.DataFrame(stocks)
