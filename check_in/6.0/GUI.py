import ctypes
from ttkbootstrap import Style
from tkinter import StringVar, ttk
from tkinter import filedialog as file
from logic import run

"""
GUI界面设置
"""
# 告诉操作系统使用程序自身的dpi适配
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# 获取屏幕的缩放因子
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)

style = Style(theme="litera",)
top = style.master
top.title("打卡统计小工具")
top.rowconfigure(0, weight=1)
top.columnconfigure(0, weight=1)
top.tk.call("tk", "scaling", ScaleFactor / 75)  # 设置程序缩放

#fr1 = ttk.Frame(top, bootstyle="dark", width=45, relief="flat")

tab_main = ttk.Notebook(style='info')  # 创建分页栏
tab_main.grid(column=0, row=0,columnspan=2, sticky="n" + "s" + "w"+"e",pady=10,padx=10)
# place(relx=0.02,rely=0.02,relwidth=0.8,relheight=0.8)

tab1 = ttk.Frame(tab_main)
tab1.grid(column=0, row=0, sticky='n', padx=2, pady=5)
tab_main.add(tab1, text='打卡统计')  # 将第一页插入分页栏中


tab2 = ttk.Frame(tab_main)
tab2.grid(column=1, row=0, sticky='n', padx=2, pady=5)
tab_main.add(tab2, text='人员信息')  # 将第一页插入分页栏中

file_path = StringVar()
def open():
    filename = file.askopenfilename()
    file_path.set(filename)
    
tab1.columnconfigure(1, weight=1)#保证tab1的第二列元素宽度自适应
open_button = ttk.Button(tab1, text='选择文件', command=lambda: open(), style="success.solid.TButton")
open_button.grid(column=0, row=0, pady=10, padx=10, sticky='w')
file_path_label = ttk.Entry(tab1, textvariable=file_path, width='40', style='success')
file_path_label.grid(row=0, column=1, pady=10, padx=10, sticky='w'+'e')

count_button = ttk.Button(
    tab1, text="统计结果",  style="success.TButton"
)  # command=lambda: run(file_path.get()),
count_button.grid(row=1, column=0, sticky="n", pady=10)

save_label = ttk.Label(tab1, text='统计结果将保存在本程序所在文件夹下', style='dark')
save_label.grid(row=1, column=1, padx=10, sticky='w')

info_person = ttk.Label(tab2,text="以下功能正在开发").grid(row=0,column=0,columnspan=3)

tab2.columnconfigure(3, weight=1)#保证tab2的第4列元素宽度自适应 就是下列的宽度
name_label = ttk.Label(tab2,text='姓名').grid(row=2,column=0,sticky='n'+'s',padx=10,pady=10)
name_input = ttk.Entry(tab2,style='success',width='10').grid(row=2,column=1,sticky='w')
ID_label = ttk.Label(tab2,text='工号').grid(row=2,column=2,sticky='n'+'s',padx=10,pady=10)
ID_input = ttk.Entry(tab2,style='success').grid(row=2,column=3,columnspan=3,sticky='w'+'e',padx=10,pady=10)

info_serach = ttk.Button(tab2,text='查询',style='success').grid(row=3,column=0,sticky='n'+'s',padx=10,pady=10)
info_serach = ttk.Button(tab2,text='删除',style='success').grid(row=3,column=1,sticky='n'+'s',padx=10,pady=10)
info_to_excel = ttk.Button(tab2,text='导出全部人员信息',style='success').grid(row=3,column=3,sticky='w',padx=10,pady=10)

insert_label = ttk.Label(tab2,text='请输入姓名、工号后选择学工or学院，然后点击添加按钮').grid(row=4,column=0,columnspan=4,sticky='w',padx=10,pady=10)
info_xuegong = ttk.Radiobutton(tab2,text='学工',style='success').grid(row=5,column=0,sticky='w',padx=10,pady=10)
info_xueyuan = ttk.Radiobutton(tab2,text='学院',style='success').grid(row=5,column=1,sticky='w',padx=10,pady=10)
info_insert = ttk.Button(tab2,text='添加',style='success').grid(row=5,column=2,sticky='w',padx=10,pady=10)

top.mainloop()
