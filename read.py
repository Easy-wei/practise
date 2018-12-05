import pandas as pd

data = pd.read_csv(r"D:\data\201602.csv")
#print(data.head(10))
#print (data['Name'])
#print (data.Name)
print(data["Type"].unique())
print(data["Equsid"].unique())
print(data["Energysid"].unique())
print(data["Expertsid"].unique())
print(data["compsid"].unique())
print(data["posisid"].unique())
print(data["buildingsid"].unique())
print(data["areaenergysid"].unique())

del (data["Type"] , data["Energysid"],data["Expertsid"],data["compsid"],data["areaenergysid"])

print (data.head(10))

data1 = data[data.posisid.isin([4000])]
print (data1.head())
print(data1["buildingsid"].unique())
print(data1["Equsid"].unique())

"""
通过上文数据分析，可以得到posisid 和buildingsid还有Equsid一一对应，可以删除两个
"""

data=data.drop(columns=['buildingsid'])
print (data.head(10))

"""
然后我们就能看到数据格式为
       RecNo                 Name          Data_Time  Value        Equsid  posisid          Load_Time
0  374376080  JF_2ATC_SC701109_EC  1/2/2016 00:00:00    0.0  1.503000e+11     4000  6/5/2016 02:20:48
1  374376081  JF_2ATC_SC701110_EC  1/2/2016 00:00:00    0.0  1.503000e+11     4000  6/5/2016 02:20:48
2  374376082  JF_2ATC_SC701111_EC  1/2/2016 00:00:00    0.0  1.503000e+11     4000  6/5/2016 02:20:48
3  374376083  JF_2ATC_SC701112_EC  1/2/2016 00:00:00    0.0  1.503000e+11     4000  6/5/2016 02:20:48
4  377254132  JF_2AES_SC100478_EC  1/2/2016 00:00:00    0.0  1.505000e+11     6000  7/5/2016 21:46:37

其实loadtime是无用信息，但是我保留，万一有用呢。Name和 Equsid是一一对应，我个人感觉保留Equsid好一些，因为都是数字，可能更好处理写吧。由于Equsid都是科学计数法，导致unique显示有问题
"""