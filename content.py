import tkinter as tk
from tkinter import messagebox
import webbrowser as web

content = tk.Tk()
content.title('一九班历课表系统 Betav0.1')
content.geometry('700x500')
content.resizable(0,0) 

def chooseClass(a):    
    global className
    className = a
    print(className)
    content.destroy()

# 关于
def about():
    messagebox.showwarning(title = "关于",message="一九班历课程表程序作者：TengKongTec(2509-张腾立)\n当前版本：betav0.1\n联系部署班级课表：Q2219655314\n未经授权，禁止使用源代码")

# 一九班历跳转
def onCalender():
    web.open('https://HclassHelper.github.io/OnCalender/index.html')

# 左侧侧边栏
tk.Label(content).grid(row=0,column=0)
tk.Label(content,text='课表系统\n启动器',font=('',25)).grid(row=1,column=1)
tk.Button(content,text='选择班级',font=('',20),width=8,bg='lightgrey',relief='flat',activeforeground='blue').grid(row=2,column=1)
tk.Button(content,text='系统设置',font=('',20),width=8,bg='lightgrey',relief='flat',activeforeground='blue').grid(row=3,column=1)
tk.Button(content,text='一九班历',font=('',20),width=8,bg='lightgrey',relief='flat',activeforeground='blue',command=onCalender).grid(row=4,column=1)
tk.Button(content,text='关于',font=('',20),width=8,bg='lightgrey',relief='flat',activeforeground='blue',command=about).grid(row=5,column=1)


# 右侧主界面
tk.Label(content,font=('',25),width=2).grid(column=2)
tk.Label(content,font=('',25),width=25,background='lightgrey',text='当前已部署班级').grid(row=1,column=3)
tk.Button(content,font=('',20),text='高一九班',width=20,command=lambda:chooseClass(9)).grid(row=2,column=3)

content.mainloop()