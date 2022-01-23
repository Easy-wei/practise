import tkinter as tk
from tkinter.constants import BOTTOM, CENTER, LEFT, RIGHT
from tkinter.filedialog import *
import os

def run():
    os.system('python D:\Code\practise\check_in\check_in.py')

top = tk.Tk()
top.geometry("400x240")
top.title('打卡统计小工具')
li = ['C', 'python', 'php', 'html', 'SQL', 'java']

listb = tk.Listbox(top)  # 创建两个列表组件

for item in li:
    listb.insert(1, item)

title = tk.Label(top, text='将Excel文件拖入框\n或者点击打开文件', font=("SimHei", 16,'bold'))  # label文本元素
A = tk.Button(top, text="生成Excel文件", bg='#E91E63',command=run,
              activebackground='#1E88E5', bd=1, fg='white', activeforeground='white')

C = tk.Button(top,command=top.destroy,text="关闭当前窗口")

month_input = tk.Entry(top)
input_label = tk.Label(top,text='请输入要统计的月份(数字)')

title.pack()
A.pack()
input_label.pack(side= LEFT)
month_input.pack(side=LEFT)
C.pack(side=BOTTOM)
top.mainloop()
