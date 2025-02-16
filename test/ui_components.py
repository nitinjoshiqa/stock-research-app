import streamlit as st
import pandas as pd

# Function to display stock data in Streamlit
def show_stock_data(df: pd.DataFrame):
    st.subheader("📈 Nifty 50 Stock Tracker")
    st.dataframe(df)

# Function to add refresh button
def refresh_data(callback):
    if st.button("🔄 Refresh Data"):
        df = callback()
        show_stock_data(df)
