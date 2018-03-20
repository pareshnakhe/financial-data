# sum-model refers to the model where one invests exactly one unit of money every round.
# The problem with the sum-model is that it does not have the accumulating effect as observed
# in stock models.

import csv
import quandl
import numpy as np
import matplotlib.pyplot as plt

quandl.ApiConfig.api_key = '7ABd1Z7yaPX8rD4TEaUi'
quandl.ApiConfig.api_version = '2015-04-09'

NO_OF_STOCKS = 0
NO_OF_ROUNDS = 0

dataFrameList = list()


# Plot the actual prices for all stocks
def plt_prices():
    print "start"
    plt.cla()
    prices = list()

    if not dataFrameList:
        print "Empty data Frame"
    else:
        for dataFrame in dataFrameList:
            prices.append([dataFrame.iloc[i][0] for i in range(NO_OF_ROUNDS)])

        for k in range(NO_OF_STOCKS):
            plt.plot(range(NO_OF_ROUNDS), prices[k])
        plt.show()


# Plot profit curve of every stocks
# sum-model
def plt_profit(total_wealth=None, model='prod'):
    plt.cla()
    price_rel = list()
    # compute price relatives for each stock
    for dataFrame in dataFrameList:
        price_rel.append([round(dataFrame.iloc[i][0] / dataFrame.iloc[i][1], 6) for i in range(NO_OF_ROUNDS)])
    # print "price_rel", price_rel

    print NO_OF_ROUNDS
    # setup a profit list
    profit = np.zeros(shape=NO_OF_ROUNDS)
    for k in range(NO_OF_STOCKS):
        profit[0] = price_rel[k][0]
        for j in range(1, NO_OF_ROUNDS):
            if model == 'sum':
                # execute sum model
                profit[j] = profit[j-1] + price_rel[k][j-1]
            else:
                # execute product model
                profit[j] = profit[j - 1] * price_rel[k][j - 1]

        # to better differentiate the performance
        # profit = np.multiply(profit, 100)
        # print "profit", k, profit[NO_OF_ROUNDS-1] / NO_OF_ROUNDS
        plt.plot(range(NO_OF_ROUNDS), profit, linewidth=0.5)

    if total_wealth:
        print "in total_wealth"
        print total_wealth
        plt.plot(range(NO_OF_ROUNDS), total_wealth, label='Hedge', linewidth=1.5)

    legend = plt.legend(loc='upper right', shadow=True)
    plt.xlabel('rounds')
    plt.ylabel('total wealth')
    plt.show()


with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        ticker = ['EOD' + '/' + row[0] + '.1', 'EOD'+ '/' + row[0] + '.4']
        data = quandl.get(ticker, start_date='2008-02-13', end_date='2018-03-15')
        if NO_OF_ROUNDS != data.shape[0]:
            NO_OF_ROUNDS = data.shape[0]
        dataFrameList.append(data)
        NO_OF_STOCKS += 1

# create empty table for price relatives
price_rel_table = np.zeros(shape=(NO_OF_STOCKS, NO_OF_ROUNDS))

k = 0
# populate the table based on opening and closing prices for each stock
# Note: Rows correspond to stocks are columns to rounds.
for dataFrame in dataFrameList:
    price_rel_table[k] = np.array([round(dataFrame.iloc[i][0] / dataFrame.iloc[i][1], 6) for i in range(NO_OF_ROUNDS)])
    k = k + 1

# print price_rel_table
# print NO_OF_STOCKS, NO_OF_ROUNDS
# plt_prices()
# plt_profit(model='prod')

max_price_rel = max([max(price_rel_table[k]) for k in range(NO_OF_STOCKS)])
