import quandl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


quandl.ApiConfig.api_key = '7ABd1Z7yaPX8rD4TEaUi'
quandl.ApiConfig.api_version = '2015-04-09'

#data = quandl.get('NSE/OIL')
#print data.head()

#data = quandl.get("FRED/GDP", start_date="2001-12-31", end_date="2002-12-31")
#print data

#data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['ticker', 'date', 'close'] }, ticker = ['AAPL', 'MSFT'], date = { 'gte': '2016-01-01', 'lte': '2016-12-31' })
#print data

# The End-of-Day US Stock Prices database (EOD) is only available in time series format
# https://www.quandl.com/data/EOD-End-of-Day-US-Stock-Prices

#data = quandl.get('EOD/V', start_date='2018-03-13', end_date='2018-03-15')
#print type(data)

# 1st and the 2nd column refers to the opening and closing price.

# Visa Inc.
# data1 = quandl.get(['EOD/V.1', 'EOD/V.4'], start_date='2010-02-13', end_date='2018-03-15')

# UnitedHealth Group
# data = quandl.get(['EOD/UNH.1', 'EOD/UNH.4'], start_date='2010-02-13', end_date='2018-03-15')


# data.shape
# data.to_csv("./visainc.csv")


# plt.hist(data['EOD/V - Open'], color='blue')
# plt.plot(data['EOD/V - Open'])

# =============================

import csv
import Hedge

NO_OF_STOCKS = 2
NO_OF_ROUNDS = 3


dataFrameList = list()

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        ticker = ['EOD'+ '/' + row[0] + '.1', 'EOD'+ '/' + row[0] + '.4']
        data = quandl.get(ticker, start_date='2018-03-13', end_date='2018-03-15')
        dataFrameList.append(data)


price_rel_table = np.zeros(shape=(NO_OF_STOCKS, NO_OF_ROUNDS))

k = 0
for dataFrame in dataFrameList:
    price_rel_table[k] = np.array([round(dataFrame.iloc[i][0] / dataFrame.iloc[i][1], 6) for i in range(3)])
    k = k + 1

print price_rel_table

Hedge.hedge(0.1, 10)

# https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python#question2
# for dataFrame in dataFrameList:
#     # print dataFrame
#     print [round(dataFrame.iloc[i][0] / dataFrame.iloc[i][1], 6) for i in range(3)]