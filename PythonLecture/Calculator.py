import tkinter
from tkinter import *

def frame(root,side):
    return f
def button(root,side,text,command=None):
    return btn
class Calculator(Frame):
    def calc(self,display):
        display.set(eval(display.get()))
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand= YES,fill=BOTH)
        self.master.title('caculator')
        display=StringVar()
        Entry(self,relief=SUNKEN,font=('思源宋体','20','bold'),\
            textvariable=display).pack(side=TOP,expand=YES,fill=BOTH)
        clearF=frame(self,TOP)
if __name__ == "__main__":
    print('ok')
    Calculator().mainloop()
