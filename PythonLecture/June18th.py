import threading
def fun(i):
    print("thread id =%d\n"%i)
def main():
    for i in range(1,10):
        t=threading.Thread(target=fun,args=(i,))
        t.start()
if __name__=="__main__":
    main()

import threading
import time

class Mythread(threading.Thread):
    tickets=10
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while(1):
            if(self.tickets>0):
                self.tickets=self.tickets-1
                print(self.name,"sell the tickets' num is",self.tickets)
            else:
                exit()

def main():
    t1=Mythread()
    t1.start()
    t2=Mythread()
    t2.start()

if __name__ == "__main__":
    main()


def func1(x,y):
    for i in range(x,y):
        print(i)
    time.sleep(10)

def main():
    t1=threading.Thread(target=func1,args=(15,20))
    t1.start()
    t2=threading.Thread(target=func1,args=(5,10))
    t2.start()


