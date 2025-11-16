import streamlit as st
import pandas as pd
import yfinance as yf

st.title("📈 Future-Oriented Finance Dashboard")

# Dropdown for asset selection
asset = st.selectbox("Choose an asset:", ["AAPL", "TSLA", "BTC-USD", "ETH-USD"])

# Fetch data
data = yf.download(asset, period="6mo")

# Show line chart
st.subheader(f"Price trend for {asset}")
st.line_chart(data['Close'])

# Comparison feature
compare = st.multiselect("Compare with:", ["AAPL", "TSLA", "BTC-USD", "ETH-USD"])
if compare:
    for comp in compare:
        comp_data = yf.download(comp, period="6mo")
        st.line_chart(comp_data['Close'])

# Export option
csv = data.to_csv().encode('utf-8')
st.download_button("Download data as CSV", csv, f"{asset}_data.csv", "text/csv")
