from ttkbootstrap import Style
from tkinter import StringVar, ttk
import ctypes
from tkinter import filedialog as file
import pandas as pd


def read_to(file_path='data.xlsx'):
    df = pd.read_excel(file_path, sheet_name=None)
    for i in df.keys():
        date = pd.read_excel(file_path, sheet_name=i)
        date.to_excel(i+'.xlsx', index=False)
    return()


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
# top.geometry("600x200")
top.title("流调拆分小工具")
top.rowconfigure(0, weight=1)
top.columnconfigure(1, weight=1)
top.tk.call("tk", "scaling", ScaleFactor / 75)  # 设置程序缩放

file_path = StringVar()


def open():
    filename = file.askopenfilename()
    file_path.set(filename)


open_button = ttk.Button(
    top, text='选择文件', command=lambda: open(), style="success.solid.TButton")
open_button.grid(column=0, row=0, pady=10)
file_path_label = ttk.Entry(top, textvariable=file_path, width='40', style='success').grid(
    row=0, column=1, pady=10, padx=10,sticky='w'+'e')

A = ttk.Button(
    top, text="拆分结果", command=lambda: read_to(file_path.get()), style="success.Outline.TButton"
)
A.grid(row=1, column=0, pady=10)
save_label = ttk.Label(top, text='拆分结果将保存在本程序所在文件夹下', style='dark')
save_label.grid(row=1, column=1, padx=10, sticky='w')

top.mainloop()
