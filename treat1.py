import datetime
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

path = r'D:\data\af_tr/'

a = os.listdir(path)
data = pd.read_csv(path+a[0])


for i in range(1,len(a)):
    data_t = pd.read_csv(path+a[i])
    data = pd.concat([data,data_t],axis = 0, ignore_index= True)

data = data.drop_duplicates(['Name','date']).reset_index(drop= True)# 删除重复的，这次没用，保不住以后用到

# 因为在北京，所以默认冬天不开空调，认为夏天才开空调




def save(x):
    for i in x['Name'].unique():
        data_x = x[x['Name'].isin([i])].sort_values(by = 'date')
        data_x.to_csv(r'D:\data\tr1/'+str(i)+'.csv',index = False)

def save2(x):
    for i in x['posisid'].unique():
        list_a = []
        data_x = x[x['posisid'].isin([i])].sort_values(by = 'date')
        for j in data_x['date'].unique():
            list_a.append(data_x[data_x['date'].isin([j])]['day_power'].sum())
        data_x_1 = data_x.drop_duplicates(['date'])
        del(data_x_1['day_power'],data_x_1['Name'])
        data_x_1 = data_x_1.copy()# 否则会报错
        data_x_1['day_power'] = list_a
        data_x_1.to_csv(r'D:\data\tr1/'+str(i)+'2.csv',index = False)

#save2(data)

def plot_power(x):
    plt.title(x['Name'][0])
    x.plot(x= 'date',y='day_power')
    plt.show()

def delete_line(x):
    if x['day_power'].max()>10000:
        x = x.drop(x[x['day_power'].isin([x['day_power'].max()])].index.unique())

"""
for i in data['Name'].unique():
    data_1 = data[data['Name'].isin([i])].reset_index(drop = True)
    #print(data_1['date'].unique())
    data_1.sort_values(by = 'date')
    fig = data_1.plot(x= 'date',y = 'day_power')
    plt.show()
"""