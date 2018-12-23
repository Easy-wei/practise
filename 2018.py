import datetime as dt
import pandas as pd
import os
import time
from chinese_calendar import is_workday


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


path = r'D:\data\2018/'


a = os.listdir(path)
data = pd.read_csv(path+a[0])


for i in range(1, len(a)):
    if os.path.splitext(path+a[i])[-1]=='.csv':
        data_t = pd.read_csv(path+a[i])
        data = pd.concat([data, data_t], axis=0, ignore_index=True)

data = data.drop_duplicates(['Name','Data_Time']).reset_index(drop= True)
print(data.tail())

def pre_treat(data):
    data.drop(['RecNo', 'Type', 'Energysid', 'Expertsid', 'compsid',
               'buildingsid', 'Load_Time', 'areaenergysid'], axis=1, inplace=True)
    data['struct_time'] = data.Data_Time.apply(
        lambda x: time.strptime(x, '%d/%m/%Y %H:%M:%S'))
    data['date_time'] = data['struct_time'].apply(lambda x: time.strftime('%Y/%m/%d',x))
    data['weekday'] = data.struct_time.apply(lambda x: x[6])  # 0代表周一同理得到其他的日子
    data['month'] = data['struct_time'].apply(lambda x: time.strftime('%Y-%m',x))
    data['year_day'] = data['struct_time'].apply(lambda x:x[7])
    data['year_day_guiyi'] = to_norm(data['year_day'],366,0)
    # 得到格式化的struct_time，为以后时间的变化做基础
    data['weekday'] = data.struct_time.apply(lambda x: x[6])  # 0代表周一同理得到其他的日子

    # 妈的，写了datetime格式为了chinesecalendar的接口，只认datatime格式，靠
    data['date'] = data.struct_time.apply(
        lambda x: dt.datetime.fromtimestamp(time.mktime(x)))
    data['is_workday'] = data.date.apply(lambda x: 0 if is_workday(x) else 1)

    data.drop(['Data_Time','struct_time'],axis =1,inplace = True)
    return data

data =pre_treat(data) 
print(data.tail())

data_time = data.drop_duplicates('date_time')
data_time.drop(['Name','Value','posisid','date','Equsid'],axis = 1, inplace = True)
data_time = data_time.reset_index(drop=True)
#data_time.to_csv(r'D:\data\data_time.csv')

#存储为地理位置的4000，6000的每日
def pos_data(data,x=[]):
    data_pos = data[data['posisid'].isin(x)].groupby(['date_time'])['Value'].sum().to_frame()
    data_pos.rename(columns={'Value':'day_power'},inplace=True)
    data_pos = pd.merge(data_pos,data_time,on='date_time').reset_index(drop = True)
    data_pos['day_power_guiyi'] = to_norm(data_pos['day_power'],max(data_pos['day_power']),min(data_pos['day_power']))
    return data_pos



def id_data(data,x = [] ):
    data_id = data[data['Equsid'].isin(x)].groupby(['date_time'])['Value'].sum().to_frame()
    data_id.rename(columns={'Value':'day_power'},inplace=True)
    data_id = pd.merge(data_id,data_time,on='date_time').reset_index(drop = True)
    data_id['day_power_guiyi'] = to_norm(data_id['day_power'],max(data_id['day_power']),min(data_id['day_power']))
    return data_id

def save(x,y):
    x.to_csv(r'D:\data\2018\tr/'+str(y)+'.csv',index = False)


day_power = id_data(data,[150300000109])
save(day_power,109)
day_power = id_data(data,[150300000110])
save(day_power,110)
day_power = id_data(data,[150300000111])
save(day_power,111)
day_power = id_data(data,[150300000112])
save(day_power,112)
day_power = id_data(data,[150500000078])
save(day_power,78)
day_power = id_data(data,[150500000081])
save(day_power,81)

pos_data(data,[4000]).to_csv(r'D:\data\2018\tr\4000.csv',index = False)
pos_data(data,[6000]).to_csv(r'D:\data\2018\tr\6000.csv',index = False)
pos_data(data,[6000,4000]).to_csv(r'D:\data\2018\tr\all.csv',index = False)

