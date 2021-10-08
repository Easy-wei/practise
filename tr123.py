import os 
import datetime as dt
import pandas as pd
import os
import matplotlib.pyplot as plt
import time 
import matplotlib.dates as mdates


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

def deal(data):
    del(data['struct_time'],data['datetime'])
    data['year_day'] = data['date'].apply(lambda x: time.strptime(x,'%Y-%m-%d')[7])
    data['year_day_guiyi'] = to_norm(data['year_day'],366,0)
    data['month'] = data['date'].apply(lambda x: time.strftime('%Y-%m',time.strptime(x,'%Y-%m-%d')))

    data['T_mean_guiyi'] = to_norm(data['T_mean'],32,-10)
    data['T_max_guiyi'] = to_norm(data['T_max'],38,-2)
    data['T_min_guiyi'] = to_norm(data['T_min'],25,-14)
    data['day_power_guiyi'] = to_norm(data['day_power'],max(data['day_power']),min(data['day_power']))

def power_0_del(data):
    data_1 = data[~data['day_power'].isin([0])]
    return data_1.reset_index(drop = True)

def save_1(data,name):
    data.to_csv(r'D:\data\1/'+str(name)+'.csv',index = False)

def save_2(data,name):
    data_1 = power_0_del(data)
    data_1.to_csv(r'D:\data\1/'+str(name)+'without_0_power.csv',index = False)

data = pd.read_csv(r'D:\data/1/JF_2ATC_SC701111_EC.csv')

deal(data)

save_1(data,111)
print (data.tail())

save_2(data,111)


    