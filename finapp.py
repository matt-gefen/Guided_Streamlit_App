# Streamlit Guided Web App

# This script will be following Chanin Nantasenamat's article (Medium)
# How to Build a Data Science Web App in Python
# Link: https://towardsdatascience.com/how-to-build-a-data-science-web-app-in-python-61d1bed65020
# The main goal here will be to build a simple, functioning web app
# Displays stock prices and volume using the streamlit package


# Importing Packages

import yfinance as yf
import streamlit as st

# Heading
st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of VMWare!
""")

# Define the stock we're looking at
tickerSymbol = 'VMW'

# Establish the actual dataset
tickerData = yf.Ticker(tickerSymbol)

# Define the date range
tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2020-6-13')

# Two charts will be the centerpiece of this app

# Closing Price Chart
st.write("""
## Closing Price
""")
st.line_chart(tickerDF.Close)

# Volume Chart
st.write("""
## Volume
""")
st.line_chart(tickerDF.Volume)
