import sys
sys.path.append(".")

from ui_components import show_stock_data, refresh_data, filter_stocks
import streamlit as st
from stock_data import fetch_stock_data


st.title("📊 Nifty 50 Stock Market Dashboard")

# Fetch & Display Data
df = fetch_stock_data()
show_stock_data(df)

# Add Filter Search Bar
filter_stocks(df)

# Add Refresh Button
refresh_data(fetch_stock_data)
