import os 
import datetime as dt
import pandas as pd
import os
import matplotlib.pyplot as plt
import time 
import matplotlib.dates as mdates

path = r'D:/data/tr1/'

data = pd.read_csv(r'D:/data/tr1/40002.csv')
data['year_day'] = data['date'].apply(lambda x: time.strptime(x,'%Y-%m-%d')[7])
data['month'] = data['date'].apply(lambda x: time.strftime('%Y-%m',time.strptime(x,'%Y-%m-%d')))

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

data['T_mean_guiyi'] = to_norm(data['T_mean'],32,-10)
data['T_max_guiyi'] = to_norm(data['T_max'],38,-2)
data['T_min_guiyi'] = to_norm(data['T_min'],25,-14)
data['day_power_guiyi'] = to_norm(data['day_power'],16904,2567)
data['year_day_guiyi'] = to_norm(data['year_day'],366,0) #因为2016年时闰年

def t_to_norm(x):
    x['T_mean_guiyi'] = to_norm(x['T_mean'],32,-10)
    x['T_max_guiyi'] = to_norm(x['T_max'],38,-2)
    x['T_min_guiyi'] = to_norm(x['T_min'],25,-14)


del(data['struct_time'])
print(data.tail())

#data.to_csv(r'D:\data\tr1/4000_month.csv',index = False)

def save1(x):
    x.to_csv(r'D:\data\tr1/4000_day_power.csv',index = False)

def save(x):
    list_power = []
    list_t_mean = []
    list_t_max = []
    list_t_min = []
    for i in x['month'].unique():
        list_power.append(x[x['month'].isin([i])]['day_power'].sum())
        list_t_mean.append(x[x['month'].isin([i])]['T_mean'].mean())
        list_t_max.append(x[x['month'].isin([i])]['T_max'].mean())
        list_t_min.append(x[x['month'].isin([i])]['T_min'].mean())
    data_t_1 = x.drop_duplicates(['month'])
    del (data_t_1['day_power'],data_t_1['T_mean'],data_t_1['T_max'],data_t_1['T_min'],
         data_t_1['T_mean_guiyi'],data_t_1['T_min_guiyi'],data_t_1['T_max_guiyi'])
    data_t_1 = data_t_1.copy()
    data_t_1['month_power'] = list_power
    data_t_1['T_mean'] = list_t_mean
    data_t_1['T_max'] = list_t_max
    data_t_1['T_min'] = list_t_min
    t_to_norm(data_t_1)
    data_t_1['month_power_guiyi'] = to_norm(data_t_1['month_power'],max(data_t_1['month_power']),min(data_t_1['month_power']))
    data_t_1.to_csv(r'D:\data\tr1/4000_month_power.csv',index = False)

save(data)
save1(data)
