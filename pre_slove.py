import pandas as pd
import time
import matplotlib.pyplot as plt

data = pd.read_csv(r"D:\data\201602.csv")


del (data["Type"], data["Energysid"], data["Expertsid"], data["compsid"],
     data["areaenergysid"], data['Equsid'], data['buildingsid'], data['Load_Time'])

data['struct_time'] = data.Data_Time.apply(
    lambda x: time.strptime(x, '%d/%m/%Y %H:%M:%S'))
# 得到格式化的struct_time，为以后时间的变化做基础
data['weekday'] = data.struct_time.apply(lambda x: x[6])  # 0代表周一同理得到其他的日子
data["year_day"] = data.struct_time.apply(lambda x: x[7])  # 一年的第几天
data['month_day'] = data.struct_time.apply(lambda x: int(time.strftime('%m%d', x)))
del(data['Data_Time'])


def split(data):
    list_1 = []
    for i in data['Name'].unique():
        pd = data[data.Name.isin([i])].reset_index(drop=True)
        pd_1 = pd.drop_duplicates(['month_day']) # 先以month_day为去重的标准，然后删除Value这一列
        del (pd_1['Value'])
        list_2 = []
        for j in pd['month_day'].unique():
            list_2.append(pd[pd.month_day.isin([j])].Value.sum())
        pd_1['day_power'] = list_2 # 老是提示这句话用的不合要求，但是能用，我担心这里埋雷
        list_1.append(pd_1.reset_index(drop=True))
    return list_1

for j in split(data):
    j.plot(x='month_day',y = 'day_power')

plt.show()

