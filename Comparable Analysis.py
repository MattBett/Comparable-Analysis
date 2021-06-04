from numpy.core.fromnumeric import mean
import yahoo_fin.stock_info as yf
import pandas as pd
import numpy as np

balance_sheet = []
income_statement = []
cfs = []
valuation = []
years = []

ticker_value = "BHP"
tickers = ["AMD", "ADI", "AAPL", "AMAT", "CSCO", "AVGO", "INTC", "LRCX", "MU", "QCOM", "TXN"]
#tickers = ["AAL", "RIO", "SCCO", "VALE"]

market_multiples = pd.DataFrame({}, index=tickers, columns=["EV/Sales", "EV/Ebitda", "P/E"])
market = pd.DataFrame({}, index=["mean", "median"], columns=["EV/Sales", "EV/Ebitda", "P/E"])

def get_data(ticker):
    #global balance_sheet
    global income_statement
    #global cfs
    global valuation
    global years
    #balance_sheet = yf.get_balance_sheet(ticker)
    income_statement = yf.get_income_statement(ticker)
    #cfs = yf.get_cash_flow(ticker)
    valuation = yf.get_stats_valuation(ticker)
    years = income_statement.columns

a = 0
denA = 0
b = 0
denB = 0
c = 0
denC = 0

for ticker in tickers:
    get_data(ticker)
    market_multiples['EV/Sales'][ticker] = valuation[1][7]
    market_multiples['EV/Ebitda'][ticker] = valuation[1][8]
    market_multiples['P/E'][ticker] = valuation[1][2]
    if valuation[1][7] == valuation[1][7]:
        a += float(valuation[1][7])
        denA += 1

    if valuation[1][8] == valuation[1][8]:
        b += float(valuation[1][8])
        denB += 1
    
    if valuation[1][2] == valuation[1][2]:
        c += float(valuation[1][2])
        denC += 1

if denA != 0:
    a = a / denA

if denB != 0:
    b = b / denB

if denC != 0:
    c = c / denC

print(market_multiples)

print('\nEV/Sales Mean: ', a)
print('EV/Ebitda Mean: ', b)
print('P/E Mean: ', c)