import os
import pandas as pd 


path = r'D:\data\3\day_power\all_data\1'

data = pd.read_csv(r'D:\data\3\day_power\all_data/109.csv')
for i in os.listdir(path):
    power_data = pd.read_csv(path+'/'+i)
    data = pd.concat([data,power_data],axis= 0 ).reset_index(drop= True)
print(data.tail())
data.drop_duplicates(['Name','date']).reset_index(drop = True)

print(data.tail())

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


def save_day(x,y):
    data_1 = x.groupby(['posisid','date'])['day_power'].sum().to_frame()
    x.drop(['Name','day_power','day_power_guiyi'],axis = 1,inplace = True)
    x = x.drop_duplicates(['posisid','date']).reset_index(drop = True)
    x = pd.merge(x,data_1,on = ['posisid','date'])
    #x.rename(columns={'day_power':'month_power'},inplace=True)#重命名
    x['day_power_guiyi'] = to_norm(x['day_power'],max(x['day_power']),min(x['day_power']))
    data_re = x[x['posisid'].isin([y])].reset_index(drop = True)
    return data_re
#print(save_day(data,6000).tail())
data_1 = save_day(data,4000)
data_2 = save_day(data,6000)

data_1.to_csv(r'D:\data\3\6000\4000_day.csv',index = False)
data_2.to_csv(r'D:\data\3\6000\6000_day.csv',index = False)

def month_power(x):
    data_power = x.groupby(['month'])['day_power'].sum().to_frame()#原来是一个series，加了.to_frame()生成为dataframe
    data_t = x.groupby(['month'])['T_mean','T_max','T_min','T_mean_guiyi','T_max_guiyi','T_min_guiyi',].mean()
    data = pd.merge(data_t,data_power,on='month')
    data.rename(columns={'day_power':'month_power'},inplace=True)#重命名
    data['month_power_guiyi'] = to_norm(data['month_power'],max(data['month_power']),min(data['month_power']))
    return (data)

#month_power(data_2).to_csv(r'D:\data\3\6000\6000_month.csv')
month_power(data_1).to_csv(r'D:\data\3\6000\4000_month.csv')

"""
print(data.tail())
data_1 = data.groupby(['posisid','date'])['day_power'].sum().to_frame()

data.drop(['Name','day_power','day_power_guiyi'],axis = 1,inplace = True)
data = data.drop_duplicates(['posisid','date']).reset_index(drop = True)


data = pd.merge(data,data_1,on = ['posisid','date'])

print(data.tail())
"""
