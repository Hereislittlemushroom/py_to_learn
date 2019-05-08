import tkinter
win=tkinter.Tk()
win.title('最简单窗体')
win.geometry('320x180')
t1='\n 五一快乐，祝大家玩的开心'

def mClick():
    label1=tkinter.Label(win,text=t1)
    label1.pack()
Btn=tkinter.Button(win,text="点击我！",command=mClick)
Btn.pack()
win.mainloop()
