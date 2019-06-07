import tkinter         # 引入tkinter库
from tkinter import *  # 从tkinter库中引入所有类型成员

#定义横条框架
def frame(root,side):  # 外部会输入root,side两个参数
    f=Frame(root)      # 将tkinter里的Frame类实例化为一个f对象
    f.pack(side=side,expand=YES,fill=BOTH)  
                       # 调用Frame类方法pack设置GUI框架
                       # 其中fill=BOTH表示宽度会自适应窗体大小
                       # 而expand=YES表示该横条样式扩展至整个空白区
    return f           # 方法返回Frame类对象

#按钮样式与风格
def button(root,side,text,command=None): 
    # 定义button构建方法，root等参数都由外部输入
    btn=Button(root,text=text,font=('思源宋体','12'),command=command)
    # 实例化Button类,font设置文本字体与大小
    btn.pack(side=side,expand=YES,fill=BOTH)
    # 该Button类对象按自适应窗体大小生成
    return btn
    # 返回该Button类
    
#继承Frame类，初始化
class Calculator(Frame):

    def calc(self,display):     # 定义计算方法
        display.set(eval(display.get()))
        # 将输出框中字符转化成可运算的式子进行计算
        # display也设置成显示计算结果
    def __init__(self):
        Frame.__init__(self)    # GUI整体框架初始化
        self.pack(expand= YES,fill=BOTH)
        # 整体框架设置成自适应窗体大小
        self.master.title('Calculator')
        # 窗体名设置为Calculator
        display=StringVar()                

        # 定义显示数字结果的文本框
        Entry(self,relief = SUNKEN,\
        font=('思源宋体','20','bold'),textvariable = display).\
        pack(side=TOP,expand=YES,fill=BOTH) 
        
        # 定义清除按钮
        # 实现清除按钮的功能
        # 按下button的命令为设display为空字符串                                 
        clearF = frame(self,TOP)
        button(clearF,LEFT,'清除',lambda w = display:w.set(''))
        

        for key in ('123+','456-','789*','.0=/'):
            # 添加横条框架和里面的按钮
            keyF=frame(self,TOP)# 定义向顶端对齐的横条框架
            for char in key:                
                if char=='=':
                    btn = button(keyF,LEFT,char)
                    # 当按钮的事件变为松开按钮时，调用calc方法进行运算
                    btn.bind('<ButtonRelease-1>',\
                    lambda e,s=self, w=display:s.calc(w),'+')
                else:                       
                    # 如果按下的按键不是‘=’，则在display中显示该字符
                    btn=button(keyF,LEFT,char,\
                    lambda w=display,c=char:w.set(w.get()+c))

#主函数
if __name__ == "__main__":
    print('ok')
    Calculator().mainloop() # GUI主体函数循环
    
 