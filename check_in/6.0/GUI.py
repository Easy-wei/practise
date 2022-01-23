from ttkbootstrap import Style
from tkinter import StringVar, ttk
from tkinter import messagebox as mb


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
