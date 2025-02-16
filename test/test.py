import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Title of the App
st.title("📈 Stock Research Dashboard")

# User input: Enter stock symbol
ticker = st.text_input("Enter Stock Symbol (e.g., TCS.NS, RELIANCE.NS)", "TCS.NS")

# Fetch Stock Data
if ticker:
    stock = yf.Ticker(ticker)

    # Display Basic Stock Info
    info = stock.info
    st.subheader(f"📊 {info.get('longName', ticker)} Overview")
    st.write(f"**Sector:** {info.get('sector', 'N/A')}")
    st.write(f"**Market Cap:** {info.get('marketCap', 'N/A')}")
    st.write(f"**P/E Ratio:** {info.get('trailingPE', 'N/A')}")
    st.write(f"**Dividend Yield:** {info.get('dividendYield', 'N/A')}")
    st.write(f"**52-Week High:** {info.get('fiftyTwoWeekHigh', 'N/A')}")
    st.write(f"**52-Week Low:** {info.get('fiftyTwoWeekLow', 'N/A')}")

    # Fetch Historical Data
    st.subheader("📉 Stock Price Chart (Last 6 Months)")
    data = stock.history(period="6mo")

    # Plot Closing Price Chart
    fig, ax = plt.subplots()
    ax.plot(data.index, data['Close'], label='Close Price', color='blue')
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    st.pyplot(fig)

    # Display Financials
    st.subheader("📊 Key Financials")
    try:
        financials = stock.financials.T
        st.dataframe(financials)
    except:
        st.write("Financial data not available.")

    # Show News
    st.subheader("📰 Latest News")
    news = stock.news
    if news:
        for article in news[:3]:  # Show top 3 articles
            st.write(f"[{article['title']}]({article['link']})")
    else:
        st.write("No recent news available.")

# Run the app: `streamlit run app.py`
