import pandas as pd

cur_month = 11  # 当前月,需要填写确定的
name_list = ["陈丽健",             "蒂娜",               "冯愉涵",           "苟曼莉",             "冀秀荣",
             "贾秋阳",             "李旭珊",             "李艳",             "陆宝萍",             "穆红波",
             "苏瑞锐",             "隋玲玉",             "汪明春",           "王浩",               "王泰鹏",
             "魏石磊",             "夏国萍",             "夏妍",             "徐仕琦",             "杨菲",
             "杨楠",                "张婧",              "钟芸",             "周芳集", ]
job_num_list = [6120170064,    6120180090,    6120170072,    6120104587,    7220210027,
                6120200072,    6120103412,    7220210054,    6120103408,    7220210062,    6120110079,
                7220180261,    6120140008,    6120180095,    6120104232,    7220210137,    7520210017,
                7220190008,    6120210140,    7220171004,    7220200001,    7220210078,    6120120020,
                6120104312]
num_name_dict = dict(zip(job_num_list, name_list))  # 工号为键，姓名为值

df = pd.read_excel("data.xlsx")
df.drop(df.head(2).index, inplace=True)

data = df.iloc[:, [0, 1, 8]]
data.columns = ['Job_num', 'name', 'Check_in_time']  # 更新列名称
data.index = range(len(data))  # 重置索引从0 开始

month_list = []
day_list = []
hour_list = []
weekday_list = []

for i in range(0, len(data)):
    month_list.append(data.iloc[i, 2].month)
    day_list.append(data.iloc[i, 2].day)
    hour_list.append(data.iloc[i, 2].hour)
    weekday_list.append(data.iloc[i, 2].weekday()+1)

data.loc[:, 'month'] = month_list
data.loc[:, 'day'] = day_list
data.loc[:, 'hour'] = hour_list
data.loc[:, 'weekday'] = weekday_list

data1 = data[(data['month'] == cur_month) & (0 <= data['weekday']) & (
    data['weekday'] <= 5) & (data['hour'] <= 21) & (data['hour'] >= 6)]
# 按照时间筛选符合条件的打卡，当前月，周一到周五，早上7点-21之间打卡有效


def statistics(job_num_list, data):
    data_to_save = []
    for i in job_num_list:
        data_temp = []  # 临时存储清空
        data_temp = data[data['Job_num'] == str(i)]
        data_temp.drop_duplicates('day', keep='first', inplace=True)  # 以第几号去重

        data_to_save.append([i, num_name_dict[i], len(
            data_temp), (2000 if len(data_temp) >= 12 else len(data_temp)*100)])

    return(data_to_save)  # 返回一个工号+打卡次数的+补贴


data_write = pd.DataFrame(statistics(job_num_list, data1), columns=[
                          '工号', '姓名', '本月打卡次数', '应发补助'])
data_write.to_excel(str(cur_month)+'月统计结果.xlsx', index=False)  # 写到本地文件为excel文件

#if __name__ =="__main__" :


"""
输出陈老师这个月的所有符合要求的打卡，作为示范
data_1 = data1[data1['Job_num']=='6120170064']
data_1.drop_duplicates('day',keep='first',inplace=True)
data_to_save = []
data_to_save.append([6120170064,num_name_dict[6120170064],len(data_1),(2000 if len(data_1)>=12 else len(data_1)*100)])
print(data_to_save)
"""
