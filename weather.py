import pandas as pd
import time
import datetime as dt

data1 = pd.read_csv(r'D:\data\weather.csv')

data1['datetime'] = data1.times.apply(
    lambda x: dt.datetime.strptime(x, '%d/%m/%Y %H:%M:%S'))
data1['date'] = data1.datetime.apply(lambda x: dt.datetime.date(x))


def get_t(data):
    list_1 = []
    for i in data['date'].unique():
        data_t = data[data['date'].isin([i])]
        list_1.append([round(data_t['t_2'].mean(), 3), round(data_t['t_2'].max(), 3), round(data_t['t_2'].min(), 3), 
                       round(data_t['rh_2'].mean(), 3), round(data_t['rh_2'].max(), 3), round(data_t['rh_2'].min(), 3)])
    return list_1

data1_1 = data1.drop_duplicates(['date'])

del (data1_1['t_2'], data1_1['rh_2'],
     data1_1['times'], data1_1['projectinfo_id'])

data1_1[['T_mean', 'T_max', 'T_min','rh_mean','rh_max','rh_min']] = pd.DataFrame(get_t(data1), index=data1_1.index)
data1_1 = data1_1.reset_index(drop=True)  # 重排索引


print(data1.head(10))
print(data1_1.head(10))

""""
        RecNo                 Name  posisid                        struct_time  weekday  year_day month_day   datetime  is_workday  day_power
0   374376080  JF_2ATC_SC701109_EC     4000   (2016, 2, 1, 0, 0, 0, 0, 32, -1)        0        32      0201 2016-02-01           0   4009.728
1   374400612  JF_2ATC_SC701109_EC     4000   (2016, 2, 2, 0, 0, 0, 1, 33, -1)        1        33      0202 2016-02-02           0   2661.504
2   374425136  JF_2ATC_SC701109_EC     4000   (2016, 2, 3, 0, 0, 0, 2, 34, -1)        2        34      0203 2016-02-03           0    698.496
3   374449664  JF_2ATC_SC701109_EC     4000   (2016, 2, 4, 0, 0, 0, 3, 35, -1)        3        35      0204 2016-02-04           0  11785.472
"""
