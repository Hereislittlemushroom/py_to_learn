from tkinter import Tk,Label
root = Tk()
# 80x80为窗体大小，10+10为窗口显示位置
root.geometry('80x80+10+10')
root.title('窗体的布局')
# 左右方式布局
L1=Label(root, text = 'L1', bg = 'red')
L1.pack(fill = 'y', side = 'left')
L2=Label(root, text = 'L2', bg = 'green')
L2.pack(fill = 'both', side = 'right')
L3=Label(root, text = 'L3', bg = 'blue')
L3.pack(fill = 'x', side = 'left') 
 
