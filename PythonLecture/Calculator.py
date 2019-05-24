import tkinter
from tkinter import *

#横条框架
def frame(root,side):
    f=Frame(root)
    f.pack(side=side,expand=YES,fill=BOTH)
    return f
#按钮样式与风格
def button(root,side,text,command=None):
    btn=Button(root,text=text,font=('思源宋体','12'),command=command)
    btn.pack(side=side,expand=YES,fill=BOTH)
    return btn
#继承Frame类，初始化
class Calculator(Frame):
    def calc(self,display):
        display.set(eval(display.get()))
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand= YES,fill=BOTH)
        self.master.title('caculator')
        display=StringVar()
        #显示数字结果的文本框
        Entry(self,relief = SUNKEN,font=('思源宋体','20','bold'),\
            textvariable = display).pack(side=TOP,expand=YES,fill=BOTH)
        #清除按钮
        clearF = frame(self,TOP)
        button(clearF,LEFT,'delete',lambda w = display:w.set(''))
        #添加横条框架和里面的按钮
        for key in ('123+','456-','789*','.0=/'):
            keyF=frame(self,TOP)
            for char in key:
                if char=='=':
                    btn = button(keyF,LEFT,char),\
                    btn.bind('<ButtonRelease-1>',\
                            lambda e,s=self, w=display:s.calc(w),'+')
                else:
                    btn=button(keyF,LEFT,char,\
                            lambda w=display,c=char:w.set(w.get()+c))
if __name__ == "__main__":
    print('ok')
    Calculator().mainloop()
 