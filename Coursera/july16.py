import numpy as np

mylist = [1,2,3]
x = np.array(mylist)
x

y = np.array([4,5,6])
y

m = np.array([[7,8,9],[10,11,12]])
m

m.shape

n = np.arange(0, 30, 2) # 左闭右开
n

o = np.linspace(0,4,9)
o

np.ones((3,2))

np.zeros((2,3))

np.eye(3)

np.diag(y)

np.array([1,2,3]*3)

np.repeat([1,2,3],3)

import numpy as np
p = np.ones([2, 3], int)
p

np.vstack([p,2*p])

# Operations

x + y 
x * y
x**2
x.dot(y)


import numpy as np
z = np.array([y, y**2])
z

z.shape

z.T

z.T.shape

z.dtype
z = z.astype('f')
z.dtype

a = np.array([-4,-2,1,3,5])
a.sum()
a.max()
a.min()
a.mean() # 平均数
a.std() # 标准差

# Indexing or Slicing

import numpy as np
s = np.arange(13)**2 # 0 ~ 12
s

s[0],s[4],s[0:3]

s[1:5]
s[-4:]
s[-5::-2]


r = np.arange(36)
r.resize(6,6)
r

r[2,2] # (3,3)
r[3, 3:6]
r[:2,:-1]
r[-1,::2]

r[r > 30] = 30
r

r2 = r[:3,:3]
r2

r2[:] = 0
r2

r_copy = r.copy()
r_copy

# iterating over arrays

test = np.random.randint(0, 10, (4, 3))
