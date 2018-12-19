import pandas as pd
import time
import matplotlib.pyplot as plt
from chinese_calendar import is_workday
import datetime as dt

weather_data = pd.read_csv(r'D:\data\weather.csv')

weather_data['datetime'] = weather_data.times.apply(lambda x: dt.datetime.strptime(x, '%d/%m/%Y %H:%M:%S'))
weather_data['date'] = weather_data.datetime.apply(lambda x: dt.datetime.date(x))


def get_t(data):
    list_1 = []
    for i in data['date'].unique():
        data_t = data[data['date'].isin([i])]
        list_1.append([round(data_t['t_2'].mean(), 3), round(data_t['t_2'].max(), 3), round(data_t['t_2'].min(), 3), 
                       round(data_t['rh_2'].mean(), 3), round(data_t['rh_2'].max(), 3), round(data_t['rh_2'].min(), 3)])
    return list_1

weather_data_1 = weather_data.drop_duplicates(['date'])

del (weather_data_1['t_2'], weather_data_1['rh_2'],
     weather_data_1['times'], weather_data_1['projectinfo_id'])

weather_data_1[['T_mean', 'T_max', 'T_min','rh_mean','rh_max','rh_min']] = pd.DataFrame(get_t(weather_data), index=weather_data_1.index)
weather_data_1 = weather_data_1.reset_index(drop=True)  # 重排索引

weather_data_1.to_csv('weather_tr',index =False)

#print(weather_data.head())
#print(weather_data_1.head())
#print (weather_data_1.iat[0,1],type(weather_data_1.iat[0,1]))


def pre_treat(data):
    del (data['RecNo'],data["Type"], data["Energysid"], data["Expertsid"], data["compsid"],
         data["areaenergysid"], data['Equsid'], data['buildingsid'], data['Load_Time'])
    data['struct_time'] = data.Data_Time.apply(lambda x: time.strptime(x, '%d/%m/%Y %H:%M:%S'))

    # 得到格式化的struct_time，为以后时间的变化做基础
    data['weekday'] = data.struct_time.apply(lambda x: x[6])  # 0代表周一同理得到其他的日子
    data['month_day'] = data.struct_time.apply(lambda x: time.strftime('%m%d', x))
    #妈的，写了datetime格式为了chinesecalendar的接口，只认datatime格式，靠
    data['date'] = data.struct_time.apply(lambda x:dt.datetime.date(dt.datetime.fromtimestamp(time.mktime(x))))
    data['is_workday'] = data.date.apply(lambda x: 0 if is_workday(x) else 1)
    del(data['Data_Time'])
    return data


def split(data):
    list_1 = []
    for i in data['Name'].unique():
        pd = data[data.Name.isin([i])].reset_index(drop=True)
        # 先以month_day为去重的标准，然后删除Value这一列
        pd_1 = pd.drop_duplicates(['month_day'])
        del (pd_1['Value'])
        list_2 = []
        for j in pd['month_day'].unique():
            list_2.append(pd[pd.month_day.isin([j])].['Value'].sum())
        pd_1 = pd_1.copy()
        pd_1['day_power'] = list_2  # 老是提示这句话用的不合要求，但是能用，我担心这里埋雷,后来加了上面那句copy
        list_1.append(pd_1.reset_index(drop=True))
    return list_1

# 判断节假日，利用了chinesecalender这个库，来判断是否是工作日，如果是工作日，那么用data里用0标注，否则用1标注

def save(list_1):
    i = 0 
    for j in list_1:
        i+=1
        j = pd.merge(j,weather_data_1)
        j.to_csv(r'D:\data\af_tr\panel_'+str(i)+'_'+str(j.iat[0,5])+'.csv',index= False)

for i in range(10,13):
    power_data = pd.read_csv(r"D:\data\2016"+str(i)+".csv")
    power_data = split(pre_treat(power_data))
    save(power_data)

#print(power_data[0].head(),'\n',type(power_data[0].iat[0,5]))