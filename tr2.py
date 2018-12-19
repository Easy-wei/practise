import os 
import datetime
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

path = r'D:/data/tr1/1/'

def read(path):
    a = os.listdir(path)
    data = pd.read_csv(path+a[0])
    for i in range(1,len(a)):
        data_t = pd.read_csv(path+a[i])
        data = pd.concat([data,data_t],axis = 0, ignore_index= True)
    return data

data = read(path)

print(data.tail())
data = data.drop_duplicates(['Name','date']).reset_index(drop= True)# 删除重复的，
print(data.tail())