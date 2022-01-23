
import ctypes
import tkinter as tk
import tkinter.ttk as ttk
import ttkbootstrap as ts

# 告诉操作系统使用程序自身的dpi适配
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# 获取屏幕的缩放因子
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
style = ts.Style()
style = ts.Style(theme='litera')


root = style.master
root.title('多页面测试')
root.geometry('800x400')
tab_main=ttk.Notebook()#创建分页栏
tab_main.pack()
#place(relx=0.02,rely=0.02,relwidth=0.8,relheight=0.8)

tab1 = ttk.Frame(tab_main)
tab1.pack()
tab_main.add(tab1,text='第一页')#将第一页插入分页栏中


button = ttk.Button(tab1,text='1',width=5)
button.pack()
button = ttk.Button(tab1,text='2',width=5)
button.pack()
T1 = tk.Text(tab1)#显示文本框
T1.pack()

tab2 = ttk.Frame(tab_main)
tab2.pack()
tab_main.add(tab2,text='第二页')
button2 = ttk.Button(tab2,text="dakai")
button2.pack()
label2 = ttk.Label(tab2,text= '这里风光独好').pack()


root.mainloop()