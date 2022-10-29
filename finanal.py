import yfinance as yf
import streamlit as st
import pandas as pd
import plotly.express as px

# Here you can use markdown language to make your app prettier
st.write("""
# Financial
""")

# We will use Amazon stocks
# stock = 'MMM'
#
# # Get stock data
# get_stock_data = yf.Ticker(stock)
#
# # Set the time line of your data
# ticket_df = get_stock_data.history(period='1h', start='2000-1-02', end='2023-12-12')
#
# div = get_stock_data.dividends
#
#
# # Show your data in line chart
# st.line_chart(ticket_df.Close)
# st.line_chart(ticket_df.Volume)
# st.line_chart(div)
#
# get_stock_data.info['longBusinessSummary']
# div
filename = 'myportfolio.txt'
try:
    with open(filename) as f:
        tickers = set(f.read().splitlines())
except (FileNotFoundError, IndexError):
    ticker = 'AAPL'


def add():
    tickers.add(selected_stock)
    print(selected_stock)
    with open(filename, 'w') as f:
        f.writelines(line + '\n' for line in tickers)


def update():
    stock_data = yf.Ticker(rd_tickers)
    info = stock_data.info

    with st.expander("Click to see raw data"):
        st.write("Info method from yfinance")
        info


    col1, col2, col3 = st.columns(3)

    col1.write(f'Ticker: {info["symbol"]}')
    col2.write(info['shortName'])

    logo_url = info.get('logo_url', '')
    try:
        if logo_url != '':
            col2.image()
    except TypeError:
        pass
    web = info.get('website', '')

    col3.write(f'[{web}]({web})')
    col1.write(f'Sector: {info.get("sector", "")}')
    col3.write(f'Industry: {info.get("industry", "")}')

    div = stock_data.dividends
    fig = px.scatter(div, color_discrete_sequence=['yellow'])
    st.plotly_chart(fig)


    #st.line_chart(div)

    descr = stock_data.info['longBusinessSummary']
    st.write(descr)


# if __name__ == "__main__":
#     go()


st.sidebar.subheader("""my portfolio analysis""")
selected_stock = st.sidebar.text_input("Add ticker to list", '')
button_clicked = st.sidebar.button("ADD")

if button_clicked:
    add()

rd_tickers = st.sidebar.radio(
    "Choose ticker",
    tickers,
    help=f"tickers from file {filename}",
)


if rd_tickers:
    update()