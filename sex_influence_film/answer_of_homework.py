# -*- coding: utf-8 -*-
"""

@author: CareyWYR
"""

import pandas as pd

data_file = '../source/ml-100k/u.data'
user_file = '../source/ml-100k/u.user'

def get_data():
    data_set = pd.read_table(data_file,header=None,sep='	',names=['user_id','item_id','rating','timestamp'])
    data_user = pd.read_table(user_file,header=None,sep='|',names=['user_id','age','gender','occupation','zip_code'])
    data_detail = pd.merge(data_set,data_user)
    grouped_rating = data_detail['rating'].groupby([data_detail['gender'],data_detail['user_id']])
    series = grouped_rating.mean()
    print('M',series['M'].std())    
    print('F',series['F'].std())
