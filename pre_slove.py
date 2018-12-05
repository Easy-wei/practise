import pandas as pd
import time 

data = pd.read_csv(r"D:\data\201602.csv")


del (data["Type"] , data["Energysid"],data["Expertsid"],data["compsid"],data["areaenergysid"],data['Equsid'],data['buildingsid'],data['Load_Time'])

data['struct_time'] = data.Data_Time.apply( lambda x: time.strptime(x,'%d/%m/%Y %H:%M:%S'))
# 得到格式化的struct——time，为以后时间的变化做基础
data['unix_time'] = data.struct_time.apply(lambda x: time.mktime(x))
data['weekday'] = data.struct_time.apply(lambda x: x[6])#0代表周一同理得到其他的日子
data["year_day"] = data.struct_time.apply(lambda x: x[7])# 一年的第几天
del(data['Data_Time'])

print (data.head(5))
print (data.iat[0,7])
print (type(data.iat[0,7]))

data1 = data[(data['year_day']==32) & (data['Name']=='JF_2ATC_SC701110_EC')]
data1 = data1.reset_index(drop=True)
print (data1)
a = data1['Value'].sum()
print (a)