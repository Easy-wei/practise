import pandas as pd
import time
import matplotlib.pyplot as plt
from chinese_calendar import is_workday
from datetime import datetime

data1 = pd.read_csv(r"D:\data\201602.csv")


def pre_treat(data):
    del (data["Type"], data["Energysid"], data["Expertsid"], data["compsid"],
         data["areaenergysid"], data['Equsid'], data['buildingsid'], data['Load_Time'])
    data['struct_time'] = data.Data_Time.apply(lambda x: time.strptime(x, '%d/%m/%Y %H:%M:%S'))

    # 得到格式化的struct_time，为以后时间的变化做基础
    data['weekday'] = data.struct_time.apply(lambda x: x[6])  # 0代表周一同理得到其他的日子
    data["year_day"] = data.struct_time.apply(lambda x: x[7])  # 一年的第几天
    data['month_day'] = data.struct_time.apply(lambda x: time.strftime('%m%d', x))
    #妈的，写了datetime格式为了chinesecalendar的接口，只认datatime格式，靠
    data['date'] = data.struct_time.apply(lambda x:datetime.fromtimestamp(time.mktime(x)))
    data['is_workday'] = data.date.apply(lambda x: 0 if is_workday(x) else 1)
    del(data['Data_Time'])

    return data

def get_date(x):
    return [time.strftime("%Y",x),time.strftime("%m",x),time.strftime("%d",x)]


def split(data):
    list_1 = []
    for i in data['Name'].unique():
        pd = data[data.Name.isin([i])].reset_index(drop=True)
        # 先以month_day为去重的标准，然后删除Value这一列
        pd_1 = pd.drop_duplicates(['month_day'])
        del (pd_1['Value'])
        list_2 = []
        for j in pd['month_day'].unique():
            list_2.append(pd[pd.month_day.isin([j])].Value.sum())
        pd_1 = pd_1.copy()
        pd_1['day_power'] = list_2  # 老是提示这句话用的不合要求，但是能用，我担心这里埋雷,后来加了上面那句copy
        list_1.append(pd_1.reset_index(drop=True))
    return list_1

# 判断节假日，利用了chinesecalender这个库，来判断是否是工作日，如果是工作日，那么用data里用0标注，否则用1标注

data1 = split(pre_treat(data1))
print(data1[0].head(20))
"""
for j in data1:
    j.plot(x='month_day', y='day_power')

plt.show()
"""