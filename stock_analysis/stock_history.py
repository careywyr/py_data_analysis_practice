# -*- coding: utf-8 -*-

"""

@author: CareyWYR
"""

import tushare as ts
import matplotlib.pyplot as plt
import numpy as np

def get_companies():
    companies = ts.get_stock_basics()
    companies.to_csv('../source/stocks/companies.csv')

def get_history_stock(code):
    history_stock = ts.get_k_data(code,start='2018-01-01',end='2018-09-29')
    plt.plot(history_stock['date'],history_stock['open'],'r')
    plt.plot(history_stock['date'],history_stock['close'],'g')
    plt.xticks(history_stock['date'][::30])
    plt.yticks(np.arange(9, 15, 0.5))