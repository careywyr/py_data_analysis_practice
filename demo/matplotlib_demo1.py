# -*- coding: utf-8 -*-
"""
Count days

@author: Dazhuang
"""

import requests
import re
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import time


def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]

def create_aveg_open(stock_code):
    quotes = retrieve_quotes_historical(stock_code)
    list1 = []
    for i in range(len(quotes)):
        x = date.fromtimestamp(quotes[i]['date'])
        y = date.strftime(x,'%Y-%m-%d')   
        list1.append(y)
    quotesdf_ori = pd.DataFrame(quotes, index = list1)
    listtemp = []
    for i in range(len(quotesdf_ori)):
        temp = time.strptime(quotesdf_ori.index[i],"%Y-%m-%d")
        listtemp.append(temp.tm_mon)
    tempdf = quotesdf_ori.copy()
    tempdf['month'] = listtemp
    meanopen = tempdf.groupby('month').open.mean()
    return meanopen
                  
open1 = create_aveg_open('INTC')
open2 = create_aveg_open('IBM')
plt.subplot(211)          
plt.plot(open1.index,open1.values,color='r',marker='o')
plt.subplot(212)
plt.plot(open1.index,open2.values,color='green',marker='o')