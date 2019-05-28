'''
win=tkinter.Tk()
win.title('new')
win.geometry('250x120')
'''

#
'''
def change(event):
    win.update()
    print("x:"+str(win.winfo_x()))
    print("y:"+str(win.winfo_y()))
win.update()
win.bind("<Configure>",change)
print("x:"+str(win.winfo_x()))
print("y:"+str(win.winfo_y()))
win.mainloop()
'''
#
'''
label=tkinter.Label(win,\
                    text='大蟒蛇',\
                    font='思源宋体',\
                    fg='#0000ff',\
                    fs='14'
                    )
label.pack()
win.mainloop()
'''
#
'''
from tkinter import *

win=Tk()
l1=Label(win,text='label_1',width=30,height=1,bg='green',font=("Aeial",12))
l1.pack()
l2=Label(win,text='label_2',bg='red',font=("Arial",12))
l2['width']=30
l2['height']=2
l2.pack()
l3=Label(win,text='label_3',bg='blue',font=("Arial",12))
l3.configure(width=30,height=3)
l3.pack()
win.mainloop()
'''
#事件响应
'''
import tkinter
win = tkinter.Tk()
win.title("new")
win.geometry('320x180')
t1='\n xxx'

def mClick():
    l1=tkinter.Label(win,text=t1)
    l1.pack()
Btn=tkinter.Button(win,text='click me!!!',command=mClick)
Btn.pack()
win.mainloop()
'''
#图片浏览
import tkinter as tk,os
class Application(tk.Frame):
    url=r'/Users/fangzeqiang/images'
    def __int__(self,master=None):
        self.files=os.listdir(url)
        self.index=0             #加载第一张图片
        self.img=tk.PhotoImage(file=url+'\\'+self.files[self.index])
        tk.Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def creatWidgets(self):
        self.lblImage=tk.Label(self,width=500,height=500)
        self.lblImage['image']=self.img
        self.lblImage.pack()
        self.frame=tk.Frame()
        self.frame.pack() #放到框架内
        self.btnPrev=tk.Button(self.frame,text='Previous',command=self.prev)
        self.btnPrev.pack(side=tk.LEFT)
        elf.btnNext=tk.Button(self.frame,text='Next',command=self.next)
        self.btnPrev.pack(side=tk.RIGHT)
    #回调函数
    def prev(self):
        self.showfile(-1)
    def next(self):
        self.showfile(1)
    def showfile(self,n):
        self.index+=n
        if self.index<0:self.index=len(self.files)-1
        if self.index>len(self.files)-1:self.index=0
        self.img=tk.PhotoImahe(file=url+'\\'+self.file[self.index])
        self.lblImage['image']=self.img

root=tk.Tk()
root.title("photo search")
app=Application(master=root)
app.mainloop()
