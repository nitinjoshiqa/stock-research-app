import sys
sys.path.append(".")

import streamlit as st
from ui_components import show_stock_data, refresh_data, filter_stocks
from stock_data import fetch_stock_data
from calculate_rsi import calculate_rsi  # ✅ Import RSI function
from show_stock_chart import show_stock_chart  # ✅ Import Chart function

st.set_page_config(layout="wide")
st.title("📊 Nifty 50 Stock Market Dashboard")

# ✅ Fetch & Display Data
df = fetch_stock_data()
df = calculate_rsi(df)  # ✅ Calculate RSI
show_stock_data(df)

# ✅ Add Filter Search Bar
filter_stocks(df)

# ✅ Add Refresh Button
refresh_data(fetch_stock_data)

# ✅ Show Stock Data Table
st.data_editor(
    df,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Stock": "🏦 Stock",
        "Last Price (₹)": "💰 Last Price",
        "Change %": st.column_config.ProgressColumn("📊 Change %", format="%.2f", min_value=-10, max_value=10),
    }
)

# ✅ Show Stock Chart with RSI
show_stock_chart(df)  # 📈 Append RSI Chart at the Bottom
