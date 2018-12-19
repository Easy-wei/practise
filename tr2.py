import os 
import datetime as dt
import pandas as pd
import os
import matplotlib.pyplot as plt
import time 
import matplotlib.dates as mdates

path = r'D:/data/tr1/'

"""
def read(path):
    a = os.listdir(path)
    data = pd.read_csv(path+a[0])
    for i in range(1,len(a)):
        data_t = pd.read_csv(path+a[i])
        data = pd.concat([data,data_t],axis = 0, ignore_index= True)
    return data
"""
data = pd.read_csv(r'D:/data/tr1/6000_month.csv')

#data['month'] = data['date'].apply(lambda x: time.strftime('%Y-%m',time.strptime(x,'%Y-%m-%d')))

def to_norm(x,max,mini):
    list_1 = []
    for i in x:
        if i > max:
            k = 1
        elif i < mini:
            k = 0
        else:
            k = (i-mini)/(max-mini)
        
        list_1.append(k)
    return list_1

data['month_power_guiyi'] = to_norm(data['month_power'],max(data['month_power']),min(data['month_power']))



data.to_csv(r'D:\data\tr1/6000_month.csv',index = False)

def save(x):
    list_1 = []
    for i in x['month'].unique():
        list_1.append(x[x['month'].isin([i])]['day_power'].sum())
    data_t_1 = x.drop_duplicates(['month'])
    del (data_t_1['day_power'])
    data_t_1['month_power'] = list_1
    data_t_1.to_csv(r'D:\data\tr1/6000_month.csv',index = False)




