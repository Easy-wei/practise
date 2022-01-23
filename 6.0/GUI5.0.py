from ttkbootstrap import Style
from tkinter import StringVar, ttk
from tkinter import messagebox as mb
import os
import ctypes
import pandas as pd
import sqlite3 as sql
from tkinter import filedialog as file

"""
数据读取
"""
conn = sql.connect("info_persons.db")
# 创建游标对象
cur = conn.cursor()
# 将老师的姓名和ID取出，对学工和学院的分开
cur.execute("select * from xuegong")
info_xuegong = cur.fetchall()  # 取出ID，和name，目前是以元组列表存储
dict_xuegong = dict(info_xuegong)  # id和姓名生成字典
ID_xuegong, name_xuegong = zip(*info_xuegong)  # zip函数反解压
ID_xuegong = list(ID_xuegong)
name_xuegong = list(name_xuegong)

cur.execute("select * from xueyuan")
info_xueyuan = cur.fetchall()
dict_xueyuan = dict(info_xueyuan)
ID_xueyuan, name_xueyuan = zip(*info_xueyuan)  # zip函数反解压
ID_xueyuan = list(ID_xueyuan)
name_xueyuan = list(name_xueyuan)

cur.close()
conn.commit()
conn.close()

"""
文件逻辑处理
"""
def read_clean(file_path="data.xlsx"):
    df = pd.read_excel(file_path)
    df.drop(df.head(2).index, inplace=True)
    data = df.iloc[:, [0, 8]]
    data.columns = ["Job_num", "Check_in_time"]  # 更新列名称
    data.index = range(len(data))  # 重置索引从0 开始
    month_list = []
    weekday_list = []
    day_list = []
    hour_list = []
    minute_list = []
    for i in range(0, len(data)):
        month_list.append(data.iloc[i, 1].month)
        weekday_list.append(data.iloc[i, 1].weekday() + 1)
        day_list.append(data.iloc[i, 1].day)
        hour_list.append(data.iloc[i, 1].hour)
        minute_list.append(data.iloc[i, 1].minute)

    data.loc[:, "month"] = month_list
    data.loc[:, "month"] = month_list
    data.loc[:, "weekday"] = weekday_list
    data.loc[:, "day"] = day_list
    data.loc[:, "hour"] = hour_list
    data.loc[:, "minute"] = minute_list
    data1 = data[
        (0 <= data["weekday"])
        & (data["weekday"] <= 5)
        & (
            ((data["hour"] <= 17) & (data["hour"] >= 8))
            | ((data["hour"] == 7) & (data["minute"] >= 30))
            | ((data["hour"] == 18) & (data["minute"] <= 30))
        )
    ]
    # 按照时间筛选符合条件的打卡，周一到周五，早上7点半-下午6点半之间打卡有效

    return data1


def count(ID, data, flag=0):
    # flag 作为标志位，0表示学工，1表示学院，两种计算打卡工资计算不一样
    data_to_save = []
    for i in ID:
        data_temp = []  # 临时存储清空
        data_temp = data[data["Job_num"] == str(i)]
        data_temp.drop_duplicates("day", keep="first", inplace=True)  # 以第几号去重
        if flag == 0:
            data_to_save.append(
                [
                    i,dict_xuegong[i],len(data_temp),
                    (2000 if len(data_temp) >= 12 else len(data_temp) * 100),
                ]
            )
        else:
            data_to_save.append(
                [
                    i,dict_xueyuan[i],len(data_temp),
                    (2000 if len(data_temp) >= 20 else len(data_temp) * 100),
                ]
            )

    return data_to_save  # 返回一个工号+打卡次数的+补贴

def save(data):
    data = pd.DataFrame(data, columns=["工号", "姓名", "本月打卡次数", "应发补助"])
    data.to_excel("统计结果.xlsx", index=False)

def run(file_path="data.xlsx"):
    if os.path.exists(file_path):
        save(
            count(ID_xuegong, read_clean(file_path), flag=0)
            + count(ID_xueyuan, read_clean(file_path), flag=1)
        )
    else:
        mb.showerror("报错信息", "文件夹内没有:data.xlsx文件")


"""
GUI界面设置
"""
# 告诉操作系统使用程序自身的dpi适配
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# 获取屏幕的缩放因子
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)

style = Style(
    theme="litera",
)
top = style.master

top.title("打卡统计小工具")
top.rowconfigure(0, weight=1)
top.columnconfigure(2, weight=1)
top.tk.call("tk", "scaling", ScaleFactor / 75)  # 设置程序缩放


fr1 = ttk.Frame(top, bootstyle="dark", width=45, relief="flat")
check_page = ttk.Button(fr1, text='打卡\n统计',style ="success.solid.TButton" )
check_page.grid(column=0,row=0,sticky='n',padx=2,pady=5)
info_person = ttk.Button(fr1, text="人员\n信息", style="success.solid.TButton")
info_person.grid(column=0, row=1, sticky="s", padx=2, pady=5)
fr1.grid(column=0, row=0, rowspan=3, sticky="n" + "s" + "w")

file_path = StringVar()

def open():
    filename = file.askopenfilename()
    file_path.set(filename)
    
open_button = ttk.Button(top,text='选择文件',command= lambda: open(),style="success.solid.TButton")
open_button.grid(column=1,row=0,pady=10,padx=10,sticky='w')
file_path_label = ttk.Entry(top, textvariable=file_path, width='40', style='success').grid(
    row=0, column=2, pady=10, padx=10,sticky='w'+'e')

A = ttk.Button(
    top, text="统计结果", command=lambda: run(file_path.get()), style="success.Outline.TButton"
)
A.grid(row=1, column=1, sticky="n", pady=10)
save_label = ttk.Label(top, text='拆分结果将保存在本程序所在文件夹下', style='dark')
save_label.grid(row=1, column=2, padx=10, sticky='w')


top.mainloop()
