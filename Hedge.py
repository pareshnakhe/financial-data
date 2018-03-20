import Data
import numpy as np
import math
import matplotlib.pyplot as plt

# Initial weight vector
wt = [1.0/Data.NO_OF_STOCKS] * Data.NO_OF_STOCKS
# Optimal value for beta
beta = math.sqrt(2.0 * math.log(Data.NO_OF_STOCKS) / Data.NO_OF_ROUNDS)


# This is the **textbook implementation** of Hedge
# Since the price rel are very small, this additive model
# does not show the effect of the algorithm
def hedge(wt, beta):
    returns = list()
    returns.append(0.0)
    for i in range(Data.NO_OF_ROUNDS):
        allocation = [wt[j] / sum(wt) for j in range(Data.NO_OF_STOCKS)]
        print allocation
        crnt_price_rel_vector = Data.price_rel_table[:, i]

        # returns from the allocation chosen in this round
        returns.append(returns[i] + np.dot(allocation, Data.price_rel_table[:, i]))

        # weight update multipliers used for update
        wt_update_mul = [beta ** (Data.max_price_rel - crnt_price_rel_vector[i]) for i in range(Data.NO_OF_STOCKS)]

        # update the weights
        wt = [wt[j] * wt_update_mul[j] for j in range(Data.NO_OF_STOCKS)]
        if min(wt) <= 0.001:
            wt = [wt[j] * 1000 for j in range(Data.NO_OF_STOCKS)]
        # print wt

    plt.cla()
    plt.plot(range(Data.NO_OF_ROUNDS+1), returns)
    plt.show()



# This function uses the wealth remaining in the previous round
# and invests it according to the weight proportion for current rnd.
def hedge_modified(wt, beta):
    total_rsrc = 1.0
    total_wealth = list()
    total_wealth.append(1.0)

    for i in range(Data.NO_OF_ROUNDS):
        allocation = [wt[j] * total_rsrc / sum(wt) for j in range(Data.NO_OF_STOCKS)]
        # print allocation
        crnt_price_rel_vector = Data.price_rel_table[:, i]

        # returns from the allocation chosen in this round
        total_rsrc = np.dot(allocation, Data.price_rel_table[:, i])
        total_wealth.append(total_rsrc)

        # weight update multipliers used for update
        wt_update_mul = [beta ** (Data.max_price_rel - crnt_price_rel_vector[i]) for i in range(Data.NO_OF_STOCKS)]
        # wt_update_mul = [beta ** (crnt_price_rel_vector[i]) for i in range(Data.NO_OF_STOCKS)]

        # update the weights
        wt = [wt[j] * wt_update_mul[j] for j in range(Data.NO_OF_STOCKS)]
        if min(wt) <= 0.001:
            wt = [wt[j] * 1000 for j in range(Data.NO_OF_STOCKS)]
            # print wt

    # plt.cla()
    total_wealth.pop(0) # since we appended 1.0 in the beginning
    # plots total wealth together with that of the fixed strategies
    Data.plt_profit(total_wealth)
    #plt.plot(range(Data.NO_OF_ROUNDS+1), total_wealth)
    #plt.show()


hedge_modified(wt, beta)
# hedge(wt, beta)