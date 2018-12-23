def to_norm(x,max,mini):
    list_1 = []
    for i in x:
        if i > max:
            k = 1
        elif i < mini:
            k = 0
        else:
            k = (i-mini)/(max-mini)
        
        list_1.append(k)
    return list_1

#归一化的function

#read函数和save
data = pd.read_csv(r'D:/data/tr1/60003.csv')

def save1(x):
    x.to_csv(r'D:\data\tr1/6000_day_power.csv',index = False)


#文件夹下的所有文件

for i in os.listdir(path):
    data = pd.read_csv(path+i)
    del(data['struct_time'])


#去重加重新排序
data = data.drop_duplicates(['Name','date']).reset_index(drop= True)# 删除重复的，这次没用，保不住以后用到

# year_day和month
data['year_day'] = data['date'].apply(lambda x: time.strptime(x,'%Y-%m-%d')[7])
data['month'] = data['date'].apply(lambda x: time.strftime('%Y-%m',time.strptime(x,'%Y-%m-%d')))
#year_day归一
data['year_day_guiyi'] = to_norm(data['year_day'],366,0) #因为2016年时闰年


#month求和

for i in x['month'].unique():
        list_power.append(x[x['month'].isin([i])]['day_power'].sum())
        list_t_mean.append(x[x['month'].isin([i])]['T_mean'].mean())
        list_t_max.append(x[x['month'].isin([i])]['T_max'].mean())
        list_t_min.append(x[x['month'].isin([i])]['T_min'].mean())
    data_t_1 = x.drop_duplicates(['month'])
    del (data_t_1['day_power'],data_t_1['T_mean'],data_t_1['T_max'],data_t_1['T_min'],
         data_t_1['T_mean_guiyi'],data_t_1['T_min_guiyi'],data_t_1['T_max_guiyi'])
    data_t_1 = data_t_1.copy()
    data_t_1['month_power'] = list_power
    data_t_1['T_mean'] = list_t_mean
    data_t_1['T_max'] = list_t_max
    data_t_1['T_min'] = list_t_min


# 多列求合并到dataframe
weather_data_1[['T_mean', 'T_max', 'T_min']] = pd.DataFrame(get_t(weather_data), index=weather_data_1.index)

# 按照纵向合并
concat
for i in range(1,len(a)):
    data_t = pd.read_csv(path+a[i])
    data = pd.concat([data,data_t],axis = 0, ignore_index= True)


#横向合并
merge

df = df.groupby(['id','name'])[‘score’].mean()
#这句表示将t按照列id和name进行分组，将分组后的每个组根据score求每个#组score的平均值。

#pandas常用函数
#https://blog.csdn.net/sxf1061926959/article/details/56280759

power_data.drop(['T_mean','T_max','T_min','T_max_guiyi','T_min_guiyi','T_mean_guiyi'],axis = 1,inplace = True)

    data.rename(columns={'day_power':'month_power'},inplace=True)#重命名