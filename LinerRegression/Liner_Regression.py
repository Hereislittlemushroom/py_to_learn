import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_table(r'/Users/fangzeqiang/Desktop/py_to_learn/LinerRegression/house_price.txt')#读取训练集
with open(r'/Users/fangzeqiang/Desktop/py_to_learn/LinerRegression/house_price.txt') as file:
    f=file.read().split('\n')
    
x=[]
y=[]

for i in f:
    tmp=i.split(',')                #传数据给x,y轴
    x.append(float(tmp[0]))
    y.append(float(tmp[1]))

plt.scatter(x, y,  color='red')     #绘制散点图

Xsum=0.0
X2sum=0.0
Ysum=0.0
XY=0.0
n=len(x)
for i in range(n):
    Xsum+=x[i]
    Ysum+=y[i]
    XY+=x[i]*y[i]
    X2sum+=x[i]**2
k=(Xsum*Ysum/n-XY)/(Xsum**2/n-X2sum)#斜率
b=(Ysum-k*Xsum)/n                   #截距
print('the line is y=%f*x+%f' % (k,b) )
                                    #打印回归模型函数
for j in range(n):
    y[j]=x[j]*k+b
plt.plot(x,y)                       #绘制回归模型图
#plt.show()                          #函数呈现

