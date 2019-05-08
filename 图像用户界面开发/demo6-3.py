import tkinter 
win = tkinter.Tk()       # 定义一个窗体
win.title('最简单窗体')  # 定义窗体标题
win.geometry('400x200')  # 定义窗体的大小400x200像素

t='\n 五一快乐，祝大家玩的开心'

def mClick():
    label1=tkinter.Label(win,text=t)
    label1.pack()

btn = tkinter.Button(win, text ='点击我!',command=mClick)  # 在窗体中添加按钮
btn.pack()
win.mainloop()
