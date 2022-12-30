import tkinter as tk
import time
from content import className
root = tk.Tk()
root.geometry('50x800')

#根据时间定义课表
if className == 9:
    cmon = ["外","化","数","地","语","理","艺","体","班"]
    ctue = ["数","语","理","史","外","政","数","自","自"]
    cwed = ["语","外","数","技","理化","语","生","体","自"]
    cthu = ["数","理","外","理","外","化","数","政","自"]
    cfri = ["数","语","生","史","地","化","理","外","自"]
    csat = ["当","前","星","期","值","暂","无","课","表"]
    csun = ["当","前","星","期","值","暂","无","课","表"]
#根据日期抽取课表
localtime = time.localtime(time.time())
classLists = [cmon,ctue,cwed,cthu,cfri,csat,csun]
weekDay = localtime[6]
classList = classLists[weekDay]
print(classList)
print(weekDay)

#定义可变变量，文本框内容
a = tk.StringVar()
b = tk.StringVar()
c = tk.StringVar()
d = tk.StringVar()
e = tk.StringVar()
f = tk.StringVar()
g = tk.StringVar()
h = tk.StringVar()
i = tk.StringVar()
#为for循环提供的变量名称表
varList = [a,b,c,d,e,f,g,h,i]

#for循环更改变量值（显示内容）
for num in range(9):
    varList[num].set(classList[num])
    print(a,b,c,d,e,f,g,h,i)

#tk的显示
tk.Label(root).grid(column=0)
tk.Label(root).grid(column=1)
tk.Label(root,text=1,font=('',50),height=1,textvariable=a,pady=3).grid(column=1,row=0)
tk.Label(root,text=1,font=('',50),height=1,textvariable=b,pady=3).grid(column=1,row=1)
tk.Label(root,text=1,font=('',50),height=1,textvariable=c,pady=3).grid(column=1,row=2)
tk.Label(root,text=1,font=('',50),height=1,textvariable=d,pady=3).grid(column=1,row=3)
tk.Label(root,text=1,font=('',50),height=1,textvariable=e,pady=3).grid(column=1,row=4)
tk.Label(root,text=1,font=('',50),height=1,textvariable=f,pady=3).grid(column=1,row=5)
tk.Label(root,text=1,font=('',50),height=1,textvariable=g,pady=3).grid(column=1,row=6)
tk.Label(root,text=1,font=('',50),height=1,textvariable=h,pady=3).grid(column=1,row=7)
tk.Label(root,text=1,font=('',50),height=1,textvariable=i,pady=3).grid(column=1,row=8)

root.mainloop()