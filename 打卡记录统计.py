from os import name
import xlrd
import pandas as pd


num_list = [
    6120170064, 6120180090,
    6120170072, 6120104587,
    7220210027, 6120200072,
    6120103412, 7220210054,
    6120103408, 7220210062,
    6120110079, 7220180261,
    6120140008, 6120180095,
    6120104232, 7220210137,
    7520210017, 7220190008,
    6120210140, 7220171004,
    7220200001, 7220210078,
    6120120020, 6120104312
]
name_list = [
    "陈丽健",
    "蒂娜",
    "冯愉涵",
    "苟曼莉",
    "冀秀荣",
    "贾秋阳",
    "李旭珊",
    "李艳",
    "陆宝萍",
    "穆红波",
    "苏瑞锐",
    "隋玲玉",
    "汪明春",
    "王浩",
    "王泰鹏",
    "魏石磊",
    "夏国萍",
    "夏妍",
    "徐仕琦",
    "杨菲",
    "杨楠",
    "张婧",
    "钟芸",
    "周芳集",
]

num_name_dict = dict(zip(num_list,name_list))
#名字和工号的字典，以工号为键，名字为值

df = pd.read_excel("data.xlsx")
df.drop(df.head(2).index,inplace=True)  #丢弃前两行，
data = df.iloc[:,[0,8]]              #只保留工号和打卡时间

#只保留打卡早7，晚10以内
print(data.iloc[0,1])
print(data.iloc[0,1].hour)


#time = pd.to_datetime(data.iloc[0,1])
#print(time)
#print(time.dt.hour)

#print(data)
#print (df)


"""
添加新的打卡人
name_list = list(df.iloc[:,1])
name_in_this = list(set(name_list)).sort(key=name_list.index)
num_in_this = df.iloc[:,0]
print(name_in_this)
"""