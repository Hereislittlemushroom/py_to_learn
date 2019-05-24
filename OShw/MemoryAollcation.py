#!/usr/bin/env python 
#coding=utf-8
import copy
class node(object):
    def __init__(self,start,end,length,state=1,ID=0):
        self.start=start
        self.end=end
        self.length=length
        self.state=state    ##state为1：内存未分配
        self.Id=ID       ##ID为0是未分配，其余为任务编号
 
def showList(list):
    print ("空闲分区如下").decode('utf-8').encode('gb2312')
    id=1
    for i in range(0,len(list)):
        p=list[i]
        if p.state == 1:
            print (id,' :start ', p.start, " end ", p.end, " length ", p.length)
            id += 1
#首次适应算法
def alloc1(taskID,Tasklength,list):
    for i in range(0,len(list)):
        p=list[i]
        if p.state==1 and p.length>Tasklength:
            node2 = node(p.start + Tasklength, p.end, p.length - Tasklength, 1, 0)
            a = node(p.start, p.start + Tasklength - 1, Tasklength, state=0, ID=taskID)
            del list[i]
            list.insert(i,node2)
            list.insert(i,a)
            showList(list)
            return
        if p.state==1 and p.length==Tasklength:
            p.state=0
            showList(list)
            return
    print "内存空间不足"
 
def free1(taskID,li):
 
    for i in range(0,len(li)):
        p=li[i]
        if p.Id==taskID:
            p.state=1
            x=i
            break
    #向前合并空闲块
    if x-1>0:
        if li[x-1].state==1:
            a=node(li[x-1].start,li[x].end,li[x-1].length+li[x].length,1,0)
            del li[x-1]
            del li[x-1]
            li.insert(x-1,a)
            x=x-1
    #向后合并空闲块
    if x+1<len(li):
        if li[x+1].state==1:
            a=node(li[x].start,li[x+1].end,li[x].length+li[x+1].length,1,0)
            del li[x]
            del li[x]
            li.insert(x,a)
    showList(li)
 
##最佳适应算法
def bubble_sort(list):
    # 冒泡排序
    count = len(list)
    for i in range(0, count):
        for j in range(i + 1, count):
            if list[i].length < list[j].length:
                list[i], list[j] = list[j], list[i]
    return list
 
def alloc2(taskID,Tasklength,li):
    q=copy.copy(li)
    q=bubble_sort(q)
    s = -1
    ss12 = -1
    for i in range(0, len(q)):
        p = q[i]
        if p.state == 1 and p.length > Tasklength:
            s = p.start
        elif p.state == 1 and p.length == Tasklength:
            ss12 = p.start
    if s == -1 and ss12 == -1:
        print "内存空间不足"
        return
    for i in range(0, len(li)):
        p = li[i]
        if p.start==s:
            node2 = node(p.start + Tasklength, p.end, p.length - Tasklength, 1, 0)
            a = node(p.start, p.start + Tasklength - 1, Tasklength, state=0, ID=taskID)
            del li[i]
            li.insert(i, node2)
            li.insert(i, a)
            showList(li)
            return
        elif p.start==ss12:
            p.state = 0
            showList(li)
            return
 
a=node(0,639,640,state=1,ID=0)
b=[]
b.append(a)
print type(b)
print "输入0运行首次适应算法，输入1运行最佳适应算法"
x = raw_input()
x = float(x)
if x==0:
    alloc1(1,130,b)
    alloc1(2,60,b)
    alloc1(3,100,b)
    free1(2,b)
    alloc1(4,200,b)
    free1(3,b)
    free1(1,b)
    alloc1(5,140,b)
    alloc1(6,60,b)
    alloc1(7,50,b)
    free1(6,b)
elif x==1:
    alloc2(1,130,b)
    alloc2(2,60,b)
    alloc2(3,100,b)
    free1(2,b)
    alloc2(4,200,b)
    free1(3,b)
    free1(1,b)
    alloc2(5,140,b)
    alloc2(6,60,b)
    alloc2(7,50,b)
    free1(7,b)
    free1(6,b)