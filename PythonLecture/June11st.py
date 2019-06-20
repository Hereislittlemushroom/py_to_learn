import pandas as pd
s = pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
print(s)
print("index",s.index)

a=pd.Series(25,index=["a","b","c","d","e"])
print(a)

#use dictionary to implement
dic_1={'a':10,'b':15,'c':20,'d':25,'e':30}
print(dic_1)

b=pd.Series(dic_1)
print(b)
c=pd.Series(dic_1,index=['c','a','b','f'])
print(c)

import numpy as np
d=pd.Series(np.arange(5))
print(d)

n=pd.Series(np.arange(5),index=np.arange(9,4,-1))
print(n) 

#Series 列表 字典 数组 
#可以用np.arrange处理

import pandas as pd
test_a=pd.Series([10,9,8,6,7],["a","b","d","c","e"])
print(test_a)
print(test_a.index)
print(test_a.values)
print(test_a['b'])
#自动索引 vs 自定义索引
#切片方式也可以处理
test_a[:3]
test_a[test_a>test_a.median()] #大于中间数？
'b' in test_a
0 in test_a
#Series的操作方式有点像ndarray
#可否想加处理
test_b=pd.Series([1,2,3],['c','a','b'])
test_a+test_b

# DataFrame可以由 一维二维的ndarray创建
import numpy as np
n=pd.DataFrame(np.arange(10).reshape(2,5))
n
test_dic={'1':pd.Series([1,2,3],index=['a','b','c']),'2':pd.Series([10,12,14,16],index=['a','b','c','d'])}
test_dic

m=pd.DataFrame(test_dic)
m

test_dic1={"one":[1,2,3,4],"two":[9,8,7,6]}
k=pd.DataFrame(test_dic1,index=['a','b','c','d'])
k

# test_dic2={"one":{'a':1}}

# df=pd.DataFrame(,index=map(str,range(10)))

import matplotlib
import random 

plt = matplotlib()
df['A']=pd.Series(list(range(len(df))))
df=pd.DataFrame(np.random.rand(10,4),columns=['a','b','c'])
df.plot(kind='bar')
plt.show()

import 
