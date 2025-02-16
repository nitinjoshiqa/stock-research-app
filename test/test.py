import streamlit as st
from stock_data import fetch_stock_data
from ui_components import show_stock_data, refresh_data

st.title("📊 Nifty 50 Stock Market Dashboard")

# Fetch & Display Data
df = fetch_stock_data()
show_stock_data(df)

# Add Refresh Button
refresh_data(fetch_stock_data)
