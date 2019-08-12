from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
from pymysql import *

LARGE_FONT = ("Verdana", 20)


def add():
    r = messagebox.askokcancel('消息框', '添加学生信息成功...')
    print('添加学生信息:', r)


def delete():
    r = messagebox.askokcancel('消息框', '删除学生信息成功...')
    print('删除学生信息:', r)


def update():
    r = messagebox.askokcancel('消息框', '修改学生信息成功...')
    print('修改学生信息:', r)


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.wm_title("学生信息管理系统")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # 循环功能界面
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # 切换，提升当前 tk.Frame z轴顺序（使可见）！！此语句是本程序的点睛之处


# 主页面
class StartPage(tk.Frame):
    """
    主页
    """
    def __init__(self, parent, root):
        super().__init__(parent)
        root.update_idletasks()
        label = tk.Label(self, text="学生信息管理系统", font=LARGE_FONT)
        label.pack(pady=100)
        ft2 = tkFont.Font(size=16)
        Button(self, text="添加学生信息", font=ft2, command=lambda: root.show_frame(PageOne), width=30, height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self, text="删除学生信息", font=ft2, command=lambda: root.show_frame(PageTwo), width=30, height=2).pack()
        Button(self, text="修改学生信息", font=ft2, command=lambda: root.show_frame(PageThree), width=30, height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self, text="所有学生信息", font=ft2, command=lambda: root.show_frame(PageFour), width=30, height=2).pack()
        Button(self, text='退出系统', height=2, font=ft2, width=30, command=root.destroy, fg='white', bg='gray', activebackground ='black', activeforeground='white').pack()


# 添加学生信息
class PageOne(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="添加学生信息", font=LARGE_FONT)
        label.pack(pady=100)

        ft3 = tkFont.Font(size=14)
        ft4 = tkFont.Font(size=12)
        Label(self, text='学生学号：', font=ft3).pack(side=TOP)
        global e1
        e1 = StringVar()
        Entry(self, width=30, textvariable=e1, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='学生姓名：', font=ft3).pack(side=TOP)
        global e2
        e2 = StringVar()
        Entry(self, width=30, textvariable=e2, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='学生性别：', font=ft3).pack(side=TOP)
        global e3
        e3 = StringVar()
        Entry(self, width=30, textvariable=e3, font=ft3, bg='Ivory').pack(side=TOP)
        Button(self, text="返回首页", width=8, font=ft4, command=lambda: root.show_frame(StartPage)).pack(pady=20)
        Button(self, text="确定保存", width=8, font=ft4, command=self.save).pack(side=TOP)

    def save(self):
        num = str(e1.get())
        name = str(e2.get())
        gender = str(e3.get())
        print(num, name, gender)
        # 创建Connection连接
        conn = connect(host='localhost', port=3306, database='students_info', user='root', password=' ',
                       charset='utf8')
        # 获得Cursor对象
        cs1 = conn.cursor()
        # 向数据库中添加学生信息
        count = cs1.execute("INSERT INTO students(stu_id,name,gender) VALUES('%d','%s','%s');" % (int(num), name, gender))
        print(count)
        # 提交数据库
        conn.commit()

        # 关闭Cursor对象
        cs1.close()
        # 关闭Connection对象
        conn.close()

        # 提示用户
        add()


# 删除学生信息
class PageTwo(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="删除学生信息", font=LARGE_FONT)
        label.pack(pady=100)

        ft3 = tkFont.Font(size=14)
        ft4 = tkFont.Font(size=12)
        Label(self, text='请输入你要删除的学生学号：', font=ft3).pack(side=TOP)
        global e4
        e4 = StringVar()
        Entry(self, width=30, textvariable=e4, font=ft3, bg='Ivory').pack(side=TOP)
        Button(self, text="确定删除", width=8, font=ft4, command=self.del1).pack(pady=20)
        Button(self, text="返回首页", width=8, font=ft4, command=lambda: root.show_frame(StartPage)).pack()
        # button1 = ttk.Button(self, text="回到首页", command=lambda: root.show_frame(StartPage)).pack()
        # button2 = ttk.Button(self, text="去到第一页", command=lambda: root.show_frame(PageOne)).pack()

    def del1(self):
        num2 = str(e4.get())
        # with open('student_infor.txt', 'r') as f:
        #     lines=f.readlines()
        #     with open('student_infor.txt', 'w') as f_w:
        #         for line in lines:
        #             if num2 in line:
        #                 continue
        #             f_w.write(line)

        # 创建Connection连接
        conn = connect(host='localhost', port=3306, database='students_info', user='root', password=' ',
                       charset='utf8')
        # 获得Cursor对象
        cs1 = conn.cursor()

        count = cs1.execute("DELETE FROM students_info.students where stu_id=%d" % int(num2))
        print(count)
        # 提交数据库
        conn.commit()
        # 提示用户修改信息成功
        update()

        # 关闭Cursor对象
        cs1.close()
        # 关闭Connection对象
        conn.close()

        # 提示用户
        delete()


# 修改学生信息
class PageThree(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        tk.Label(self, text="修改学生信息", font=LARGE_FONT).pack(pady=100)

        ft3 = tkFont.Font(size=14)
        ft4 = tkFont.Font(size=12)
        Label(self, text='请输入你要修改的学生学号：', font=ft3).pack(side=TOP)
        self.e5 = StringVar()
        Entry(self, width=30, textvariable=self.e5, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='学生姓名：', font=ft3).pack(side=TOP)
        self.e6=StringVar()
        Entry(self, width=30, textvariable=self.e6, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='学生性别：', font=ft3).pack(side=TOP)
        self.e7=StringVar()
        Entry(self, width=30, textvariable=self.e7, font=ft3, bg='Ivory').pack(side=TOP)
        Button(self, text="确定修改", width=8, font=ft4, command=self.modify).pack(pady=20)
        Button(self, text="返回首页", width=8, font=ft4, command=lambda: root.show_frame(StartPage)).pack()

    def modify(self):
        num3 = str(self.e5.get())
        name3 = str(self.e6.get())
        score3 = str(self.e7.get())

        # 创建Connection连接
        conn = connect(host='localhost', port=3306, database='students_info', user='root', password='python',
                       charset='utf8')
        # 获得Cursor对象
        cs1 = conn.cursor()
        # 向数据库中修改学生信息
        count = cs1.execute("SELECT * from students where stu_id=%d;" % int(num3))
        print(count)

        count1 = cs1.execute("SELECT * from students where name='%s';" % name3)
        print(count1)

        if count != 0:
            count = cs1.execute("update students set stu_id=%d,name='%s',gender='%s' where stu_id=%d;" % (int(num3), name3, score3, int(num3)))
            print(count)
            # 提交数据库
            conn.commit()
            # 提示用户修改信息成功
            update()

            # 关闭Cursor对象
            cs1.close()
            # 关闭Connection对象
            conn.close()

        elif count1 != 0:

            count = cs1.execute("update students set stu_id=%d,name='%s',gender='%s' where name='%s';" % (int(num3), name3, score3, name3))
            print(count)
            # 提交数据库
            conn.commit()
            # 提示用户修改信息成功
            update()

            # 关闭Cursor对象
            cs1.close()
            # 关闭Connection对象
            conn.close()

        else:
            r = messagebox.askokcancel('消息框', '没有该学生...')
            print('没有该学生信息:', r)

        # 提示用户
        update()


# 查询学生成绩
class PageFour(tk.Frame):

    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="查询学生姓名", font=LARGE_FONT)
        label.pack(pady=100)
        tree_data = ttk.Treeview()
        ft4 = tkFont.Font(size=12)
        # 滚动条

        scro = Scrollbar(self)

        scro.pack(side=RIGHT, fill=Y)
        lista = Listbox(self, yscrollcommand=scro.set, width=50)

        # f = open('student_infor.txt', 'r')
        text = ("                 %-16s%-16s%-16s" % ("学号", "姓名", "性别"))

        # 创建Connection连接
        conn = connect(host='localhost', port=3306, database='students_info', user='root', password=' ',
                       charset='utf8')
        # 获得Cursor对象
        cs1 = conn.cursor()
        # 向数据库中添加学生信息
        count = cs1.execute("SELECT stu_id,name,gender from students_info.students;")
        print(count)
        ret = cs1.fetchall()
        print(ret)

        list = []
        for i in ret:
            list.append(i)
        print(list)
        x = 0
        for i in list:
            text1 = ("                %-16s%-16s%-16s" % (i[0], i[1], i[2]))
            lista.insert(0, text1)
            x += 1
        lista.insert(0, text)
        lista.pack()
        Button(self, text="返回首页", width=8, font=ft4, command=lambda: root.show_frame(StartPage)).pack(pady=40)

        # 关闭Cursor对象
        cs1.close()
        # 关闭Connection对象
        conn.close()


if __name__ == '__main__':
     # 实例化Application
     app = Application()


     # 主消息循环:
     app.mainloop()
