import os
import pandas as pd 
import time

path = r'D:\data\3/'

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

def month_power(x):
    data_power = x.groupby(['month'])['day_power'].sum().to_frame()#原来是一个series，加了.to_frame()生成为dataframe
    data_t = x.groupby(['month'])['T_mean','T_max','T_min','T_mean_guiyi','T_max_guiyi','T_min_guiyi',].mean()
    data = pd.merge(data_t,data_power,on='month')
    data.rename(columns={'day_power':'month_power'},inplace=True)#重命名
    data['month_power_guiyi'] = to_norm(data['month_power'],max(data['month_power']),min(data['month_power']))
    return (data)

for i in os.listdir(path):
    data = pd.read_csv(path+i)
    data = month_power(data)
    data.to_csv(path+'month_'+i)


