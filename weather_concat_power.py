import pandas as pd 
import os 
import time

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

weather_data = pd.read_csv(r'e:\weather_tr.csv')

weather_data['T_mean_guiyi'] = to_norm(weather_data['T_mean'],32,-10)
weather_data['T_max_guiyi'] = to_norm(weather_data['T_max'],38,-2)
weather_data['T_min_guiyi'] = to_norm(weather_data['T_min'],25,-14)

print(type(weather_data['date'][0]))
print(weather_data['date'][0])
path = r'D:\data\2018\tr/'

for i in os.listdir(path):
    if os.path.splitext(path+i)[-1]=='.csv':
        power_data = pd.read_csv(path+i)
        print(power_data.tail())
        print(type(power_data['date_time'][0]))
        print(power_data['date_time'][0])
    #power_data.drop(['T_mean','T_max','T_min','T_max_guiyi','T_min_guiyi','T_mean_guiyi'],axis = 1,inplace = True)
        power_data = pd.merge(power_data,weather_data,how='left',left_on=['date_time'],right_on=['date'])
        print(power_data.tail())
        power_data.to_csv(r'D:\data\2018\tr\weather/'+i,index = False)
        