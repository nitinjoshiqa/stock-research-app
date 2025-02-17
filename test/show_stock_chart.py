import plotly.graph_objects as go
import streamlit as st

def show_stock_chart(df):
    """Plot stock price and RSI using Plotly."""
    fig = go.Figure()

    # Stock Price Line
    fig.add_trace(go.Scatter(x=df.index, y=df["Last Price (₹)"], mode="lines", name="Stock Price", line=dict(color='blue')))

    # RSI Line
    fig.add_trace(go.Scatter(x=df.index, y=df["RSI"], mode="lines", name="RSI", line=dict(color='red', dash='dot')))

    # Layout Configuration
    fig.update_layout(
        title="Stock Price & RSI",
        xaxis_title="Date",
        yaxis_title="Stock Price",
        yaxis2=dict(title="RSI", overlaying="y", side="right", showgrid=False),
        legend=dict(x=0, y=1),
    )

    # Display in Streamlit
    st.plotly_chart(fig, use_container_width=True)
