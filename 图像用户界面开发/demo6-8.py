from tkinter import *
import tkinter as tk

win=Tk()
win.geometry('400x120')
win.title('单选按钮和复选框示例')

#显示选择状态的标签
txt=StringVar()
txt.set("请选择")
lab=Label(win,textvariable=txt,relief='ridge',width=30)

#复选框
chVarDis=tk.IntVar() #定义状态变量对象
check1=tk.Checkbutton(win,text="c 语言",variable=chVarDis,state='disabled')
check1.select()

chVarUn=tk.IntVar() #定义状态变量对象
check2=tk.Checkbutton(win,text="Java",variable=chVarUn)
check2.deselect()

chVarEn=tk.IntVar() #定义状态变量对象
check3=tk.Checkbutton(win,text="Python",variable=chVarEn)
check3.select()

#单选按钮

chk=["鲜花","鼓掌","鸡蛋"]  #定义几个选项的全局变量

#单选按钮回调函数
def radCall():
    radSel=radVar.get()
    if radSel==0:
        txt.set(chk[0])
    elif radSel==1:
        txt.set(chk[1])
    elif radSel==2:
        txt.set(chk[2])
    print(radVar.get())

radVar=tk.IntVar()
for i in range(3):
    curRad=tk.Radiobutton(win,text=chk[i],variable=radVar,value=i,command=radCall)
    curRad.grid(column=i,row=5,sticky=tk.W)

#布局设置
lab.grid(row=0,column=0,columnspan=3)
check1.grid(row=4,column=0,sticky=tk.W)
check2.grid(row=4,column=1,sticky=tk.W)
check3.grid(row=4,column=2,sticky=tk.W)

win.mainloop()




    




