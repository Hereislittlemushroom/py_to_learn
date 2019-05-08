import tkinter
from tkinter import *
win=tkinter.Tk()
win.title("学生信息")
L1=Label(win,text="学生信息",font='Helvetica -36 bold')
L2=Label(win,text="学号",font='song -20')
L3=Label(win,text="姓名",font='song -20')
L4=Label(win,text="专业",font='song -20')
L1.grid(row=0,column=1)
L2.grid(row=1)
L3.grid(row=2)
L4.grid(row=3)
photo=PhotoImage(file="timg.gif")
L_Phot=Label(image=photo)
L_Phot.image=photo
L_Phot.grid(row=0,column=2,columnspan=2,rowspan=4)

e1=Entry(win,width=20,font='song -20')
e2=Entry(win,width=20,font='song -20')
e3=Entry(win,width=20,font='song -20')

e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
Button(win, text="查询",font='song -20').grid(row=4, column=0) #查询按钮右侧贴紧
Button(win, text="取消",font='song -20').grid(row=4, column=1) #取消按钮左侧贴紧

win.mainloop()


