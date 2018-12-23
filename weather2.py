import pandas as pd
import time
import matplotlib.pyplot as plt
from chinese_calendar import is_workday
import datetime as dt

weather_data = pd.read_csv(r'D:\data\weather.csv')

weather_data['datetime'] = weather_data.times.apply(lambda x: time.strptime(x, '%d/%m/%Y %H:%M:%S'))
weather_data['date'] = weather_data.datetime.apply(lambda x: time.strftime('%Y/%m/%d',x))


def get_t(data):
    list_1 = []
    for i in data['date'].unique():
        data_t = data[data['date'].isin([i])]
        list_1.append([round(data_t['t_10'].mean(), 3), round(data_t['t_10'].max(), 3), round(data_t['t_10'].min(), 3)])
        # 忽略湿度
    return list_1

weather_data_1 = weather_data.drop_duplicates(['date'])

del (weather_data_1['t_10'], weather_data_1['rh_10'],
     weather_data_1['times'], weather_data_1['projectinfo_id'],
     weather_data_1['updatedata_date'],weather_data_1['id'],weather_data_1['datetime']
    )
weather_data_1 = weather_data_1.copy()
weather_data_1[['T_mean', 'T_max', 'T_min']] = pd.DataFrame(get_t(weather_data), index=weather_data_1.index)
weather_data_1 = weather_data_1.reset_index(drop=True)  # 重排索引

weather_data_1.to_csv(r'e:\weather_tr.csv',index =False)

#print(weather_data.head())
#print(weather_data_1.head())
#print (weather_data_1.iat[0,1],type(weather_data_1.iat[0,1]))
