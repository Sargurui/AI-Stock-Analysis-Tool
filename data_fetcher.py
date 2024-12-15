import yfinance as yf
import pandas as pd
import numpy as np

# Function to fetch company data
def get_company_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        fundamentals = {
            "Company Name": info.get("longName", "N/A"),
            "Market Cap": info.get("marketCap", "N/A"),
            "P/E Ratio": info.get("trailingPE", "N/A"),
            "Forward P/E": info.get("forwardPE", "N/A"),
            "EPS": info.get("trailingEps", "N/A"),
            "Dividend Yield": info.get("dividendYield", "N/A"),
            "Profit Margins": info.get("profitMargins", "N/A"),
            "Revenue": info.get("totalRevenue", "N/A"),
            "Debt to Equity": info.get("debtToEquity", "N/A"),
            "Return on Equity": info.get("returnOnEquity", "N/A"),
        }
        return fundamentals
    except Exception as e:
        print("Error fetching company data:", e)
        return None

# Function to calculate 50-day and 200-day SMA
def sma(data, window):
    return data["Close"].rolling(window=window).mean()

# Function to calculate RSI
def rsi(data, window):
    delta = data["Close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

# Function to calculate Bollinger Bands
def bollinger_bands(data, window):
    sma_value = data["Close"].rolling(window=window).mean()
    std = data["Close"].rolling(window=window).std()
    upper_band = sma_value + (std * 2)
    lower_band = sma_value - (std * 2)
    return upper_band, lower_band

# Function to fetch technical analysis data
def get_technical_analysis(ticker):
    try:
        data = yf.download(ticker, period="3mo", interval="1d")
        data["SMA_50"] = sma(data, 50)
        data["SMA_200"] = sma(data, 200)
        data["RSI"] = rsi(data, 14)
        data["Upper Bollinger Band"], data["Lower Bollinger Band"] = bollinger_bands(data, 20)

        latest = data.iloc[-1]
        technicals = {
            "50-Day SMA": round(latest["SMA_50"], 2),
            "200-Day SMA": round(latest["SMA_200"], 2),
            "RSI (14)": round(latest["RSI"], 2),
            "Upper Bollinger Band": round(latest["Upper Bollinger Band"], 2),
            "Lower Bollinger Band": round(latest["Lower Bollinger Band"], 2),
            "Current Price": round(latest["Close"], 2),
        }
        return technicals
    except Exception as e:
        print("Error fetching technical analysis:", e)
        return None
