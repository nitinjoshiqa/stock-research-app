import streamlit as st
import pandas as pd

# Function to display stock data in Streamlit
def show_stock_data(df: pd.DataFrame):
    st.subheader("📈 Nifty 50 Stock Tracker")
    st.dataframe(df)

# Function to add a refresh button
def refresh_data(callback):
    if st.button("🔄 Refresh Data"):
        df = callback()
        show_stock_data(df)

# Function to filter stocks based on user input
def filter_stocks(df: pd.DataFrame):
    search_query = st.text_input("🔍 Search for a stock", "")
    if search_query:
        filtered_df = df[df["Stock"].str.contains(search_query.upper(), na=False)]
        show_stock_data(filtered_df)
