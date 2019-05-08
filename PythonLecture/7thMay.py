'''
from tkinter import *

root=Tk()

def add():
    pass
def substract():
    pass
def multiply():
    pass
def divide():
    pass
def openfile():
    a=filedialog.askopenfilename()
    print(a)
def choosecolor():
    a=colorchooser.askcolor()
    print(a)

menubar=Menu(root) #创造窗体容器
root.config(menu=menubar)

menu_1=Menu(menubar,tearoff=0)
menubar.add_cascade(label='操作',menu=menu_1)

menu_1.add_command(label='+',command=add())
menu_1.add_command(label='-',command=substract())
menu_1.add_separator()
menu_1.add_command(label='%',command=multiply())
menu_1.add_command(label='*',command=divide())
menu_1.add_command(label='openfile',command=openfile())
menu_1.add_command(label='choosecolor',command=choosecolor())

exitMenu=Menu(menubar,tearoff=0)

root['menu']=menubar
root.mainloop()
'''

'''
from tkinter import *
def callback(event):
    print(event.x,event.y)
    s=(event.x,event.y)
    txt.set(s)

win = Tk()
win.geometry('200x200')
win.title('click event')
frame=Frame(win,width=200,height=100,bg='cyan')
frame.bind('<Button-1>',callback)#响应函数,<>里的是具体事件
frame.pack()
txt=StringVar()
L=Label(win,width=20,textvariable=txt)
L.pack()
win.mainloop()
'''

'''
from tkinter import *
def key_action(event):
    print(repr(event.char))
    s=event.char
    txt.set(s)
def callback(event):
    L.focus_set()

win = Tk()
win.title('keyboard')
txt=StringVar()
L=Label(win,width=20,textvariable=txt,font='song -36 bold',bg='white')
L.bind("<KeyPress>",key_action)
L.bind("<Button-1>",callback)
L.pack()
win.mainloop()
'''