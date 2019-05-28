import tkinter
win=tkinter.Tk()
win.title("标签示例")
win.geometry('250x120')
label=tkinter.Label(win,\
                    text='欢迎进入Python',\
                    font='宋体',\
                    fg='#0000ff',bg='red')
label.pack()


text_label = tkinter.Label(win, text='标签1')
text_label.pack(side=tkinter.LEFT)  # 字在左边
new_text_label = tkinter.Label(win, text='标签2')
new_text_label.pack(side=tkinter.RIGHT)  # 在右边


win.mainloop()
