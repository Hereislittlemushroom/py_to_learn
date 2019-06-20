# multithreading
# like wheel of fotune
# 执行代码还可响应键盘鼠标事件 如Windows Indexing Services
# 线程 OS可以调度的 最小单位
# 线程没有自己独立的地址空间 ？
# 线程的生命周期 五个状态
# 多线程的优点 运行速度加快 可以释放珍贵的内存资源

import _thread
import time

def print_time(threadName, delay):
    count =0
    while count<5:
        time.sleep(delay)
        count+=1
        print("%s:%s"(threadName,time.ctime(time.time())))
    threadName.exit()

try:
    _thread.start_new_thread(print_time,("Thread-1",2,))
    _thread.start_new_thread(print_time,("Thread-2",4,))
except:
    print("ERROR")

# threading 模块
# stack_size()
# Lock Rlock类
# 创建thread对象后可以用start方法调用
# 构建方法 构建子类 or 构造函数

# 用Tread子类程序来模拟航班系统，一个窗口用一个线程表示
import threading
class Mythread(threading.Thread):
    tickets=10
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while(1):
            if(self.tickets>0):
                self.tickets=self.tickets-1
                print(self.name,"sys :",self.tickets," number")
            else:
                print("sold out")
                exit()
t1=Mythread()
t1.start()
t1.join()
t2=Mythread()
t2.start()
# t2.join()
"""   
class students:
    id=2120162016
    name='方xx'
21  
stu1=students()
stu2=students()

array=[stu1,stu2]

array[0]=
"""