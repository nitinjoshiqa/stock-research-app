import pandas as pd
import numpy as np

def calculate_rsi(data, window=14):
    """Calculate RSI (Relative Strength Index)."""
    delta = data["Last Price (₹)"].diff()
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)

    avg_gain = pd.Series(gain).rolling(window=window, min_periods=1).mean()
    avg_loss = pd.Series(loss).rolling(window=window, min_periods=1).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    data["RSI"] = rsi  # Add RSI column to DataFrame
    return data

