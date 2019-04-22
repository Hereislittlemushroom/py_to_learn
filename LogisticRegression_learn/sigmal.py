import matplotlib.pyplot as plt
import numpy as np
 
def Sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))
 
x= np.arange(-10, 10, 0.1)
h = Sigmoid(x)            #Sigmoid函数
plt.plot(x, h)
plt.axvline(0.0, color='k')   #坐标轴上加一条竖直的线（0位置）
plt.axhspan(0.0, 1.0, facecolor='1.0', alpha=1.0, ls='dotted')  
plt.axhline(y=0.5, ls='dotted', color='k')  #在y=0.5的地方加上黑色虚线
plt.yticks([0.0,  0.5, 1.0])  #y轴标度
plt.ylim(-0.1, 1.1)       #y轴范围
plt.show()  

"""
二. LogisticRegression回归算法
LogisticRegression回归模型在Sklearn.linear_model子类下，调用sklearn逻辑回归算法步骤比较简单，即：
    (1) 导入模型。调用逻辑回归LogisticRegression()函数。
    (2) fit()训练。调用fit(x,y)的方法来训练模型，其中x为数据的属性，y为所属类型。
    (3) predict()预测。利用训练得到的模型对数据集进行预测，返回预测结果
"""
 
from sklearn.datasets import load_iris   #导入数据集iris
iris = load_iris()  #载入数据集
print (iris.data) #data里面是四个特征变量，有150个样本，就是150行特征变量。一行是一个样本
print (iris.data.shape   ) #返回(150, 4)，说明有150行，4列内容。
print (iris.target) #target 是类别，总共有三类，分别是0,1,2
"""
iris里有两个属性iris.data，iris.target。data是一个矩阵，每一列代表了萼片或花瓣的长宽，一共4列，每一列代表某个被测量的鸢尾植物，一共采样了150条记录。

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris    #导入数据集iris
  
#载入数据集  
iris = load_iris()  
print (iris.data) #data里面是四个特征变量，有150个样本，就是150行特征变量。一行是一个样本,每行4个变量
print (iris.target) #target 是类别，总共有三类，分别是0,1,2
 
#获取花卉两列数据集  
DD = iris.data  
X = [x[0] for x in DD]  #x 表示DD的每一行行，X[0]表示从每行中取出第一个数据，结果X表示所有行的,
print (X[:50])  
Y = [x[1] for x in DD]  #Y表示第二列所有行
#print (Y)  
  
#plt.scatter(X, Y, c=iris.target, marker='x')
plt.scatter(X[:50], Y[:50], color='red', marker='o', label='setosa') #前50个样本
plt.scatter(X[50:100], Y[50:100], color='blue', marker='x', label='versicolor') #中间50个
plt.scatter(X[100:], Y[100:],color='green', marker='+', label='Virginica') #后50个样本
plt.legend(loc=2) #左上角
plt.show()
 
3. 逻辑回归分析
 
从图中可以看出，数据集线性可分的，可以划分为3类，分别对应三种类型的鸢尾花，下面采用逻辑回归对其进行分类预测。前面使用X=[x[0] for x in DD]获取第一列数据，Y=[x[1] for x in DD]获取第二列数据，这里采用另一种方法，iris.data[:, :2]获取其中两列数据（两个特征），完整代码如下：
 
 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris   
from sklearn.linear_model import LogisticRegression 
 
#载入数据集
iris = load_iris()   
print("iris.data[0] is :",iris.data[0])       #数据的第一行内容
print("iris.data[:2] is:",iris.data[:2])      #数据的第一行和第二行内容
#iris.data是一个150*4的矩阵，第一个：决定了取出多少行，第二个：决定了取出多少列
X = iris.data[:, :2]   #获取花卉两列数据集，：表示从开始到结束，相当于取了150行，：2表示包含0,1两列；结果就是取了150行的0,1两列
#print("X is:",X[:6])
Y = iris.target           
 
#逻辑回归模型，初始化逻辑回归模型并进行训练，C=1e5表示目标函数。
lr = LogisticRegression(C=1e5)  
lr.fit(X,Y)
 
#步长h（设置为0.02），meshgrid函数生成两个网格矩阵，
h = 0.02
 
'''
获取的鸢尾花两列数据，对应为花萼长度和花萼宽度，每个点的坐标就是(x,y)。 先取X二维数组的第一列（长度）的最小值、最大值和步长h（设置为0.02）生成数组，
再取X二维数组的第二列（宽度）的最小值、最大值和步长h生成数组， 最后用meshgrid函数生成两个网格矩阵xx和yy，如下所示：
'''
x_min = X[:, 0].min() - 0.5 #：表示所有行，0表示第一列
print("x_min is:",x_min)
x_max = X[:, 0].max() + 0.5
print("x_max is:",x_max)
y_min= X[:, 1].min() - 0.5
print("y_min is:",y_min)
 
y_max = X[:, 1].max() + 0.5         #：表示所有行，1表示第2列
print("y_max is:",y_max)
 
'''
xx = np.meshgrid(np.arange(x_min, x_max, h))
yy = np.meshgrid(np.arange(y_min, y_max, h))
'''
#x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
#y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h)) #用meshgrid函数生成两个网格矩阵xx和yy
print("np.arange_x is:",np.arange(x_min,x_max,h))  #先取X二维数组的第一列（长度）的最小值、最大值和步长h（设置为0.02）生成一维数组
print("np.arange_y is :",np.arange(y_min,y_max,h))  #先取Y二维数组的第一列（长度）的最小值、最大值和步长h（设置为0.02）生成数组
print("the number of np.arange_y is:",len(np.arange(y_min, y_max, h)))  #171个
 
print("xx are:\n",xx[:5])
 
print("the lines of xx is:",len(xx))  #171个
#print("xx,yy are:\n",xx,yy)
#调用ravel()函数将xx和yy的两个矩阵转变成一维数组，由于两个矩阵大小相等，因此两个一维数组大小也相等。np.c_[xx.ravel(), yy.ravel()]是获取二维数组
Z = lr.predict(np.c_[xx.ravel(), yy.ravel()]) 
print("xx.ravel() is:",xx.ravel())
 
print("the number of xx.ravel is",len(xx.ravel()))  #39501个
print("Z is:",Z)
print("the length of Z is:",len(Z)) #39501个
#总结下：上述操作是把第一列花萼长度数据按h取等分作为行，并复制多行得到xx网格矩阵；再把第二列花萼宽度数据按h取等分，作为列，并复制多列得到yy网格矩阵；
#最后将xx和yy矩阵都变成两个一维数组，调用np.c_[]函数组合成一个二维数组进行预测。
Z = Z.reshape(xx.shape) #调用reshape()函数修改形状，将其Z转换为两个特征（长度和宽度），则39501个数据转换为171*231的矩阵。
print("the length of Z1 is:",len(Z)) #171个
 
plt.figure(1, figsize=(8,6))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired) #调用pcolormesh()函数将xx、yy两个网格矩阵和对应的预测结果Z绘制在图片上
#可以发现输出为三个颜色区块，分布表示分类的三类区域。cmap=plt.cm.Paired表示绘图样式选择Paired主题
 
#绘制散点图
plt.scatter(X[:50,0], X[:50,1], color='red',marker='o', label='setosa')
plt.scatter(X[50:100,0], X[50:100,1], color='blue', marker='x', label='versicolor')
plt.scatter(X[100:,0], X[100:,1], color='green', marker='s', label='Virginica') 
 
plt.xlabel('Sepal length')  #X轴标签
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())  #x轴范围
plt.ylim(yy.min(), yy.max())   #y轴范围
plt.xticks(()) #x轴标度
plt.yticks(()) ##没有y轴标度
plt.legend(loc=2) #左上角绘制图标
plt.show()
"""