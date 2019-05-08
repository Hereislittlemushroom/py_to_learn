from tkinter import *
win=Tk()
win.geometry('500x150')
win.title('密码验证')

#提交按钮事件
def mClick():
    txt=txt2.get()
    if(txt=='abc'):
        txt3.set("欢迎进入本系统")
#创建几个组件元素
lab1=Label(win,text="请输入用户名：",font=('华文新魏','16'))
lab2=Label(win,text="请输入密  码：",font=('华文新魏','16'))
txt1=StringVar()
txt2=StringVar()
txt3=StringVar()
txt3.set("请输入用户名和密码")

entry1=Entry(win,textvariable=txt1,width=16,font=('宋体','16'))
entry2=Entry(win,textvariable=txt2,width=16,show='*',font=('宋体','16'))
button=Button(win,text='提交',command=mClick,font=('宋体','16'))

lab3=Label(win,textvariable=txt3,relief='ridge',width=30,font=('华文新魏','16'))
#布局设置
lab1.grid(row=0,column=0)
lab2.grid(row=1,column=0)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
lab3.grid(row=2,column=0,columnspan=2)
button.grid(row=2,column=2)

win.mainloop()







