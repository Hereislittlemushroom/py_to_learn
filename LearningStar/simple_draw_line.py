import numpy as np
import matplotlib.pyplot as plt
 
"""x=[0,1]
y=[0,1]
plt.figure()
plt.plot(x,y)
plt.show()
#plt.savefig("easyplot.jpg")
"""
x=np.linspace(0,2*np.pi,50)
"""
plt.plot(x,np.sin(x),'r-+',x,np.sin(2*x),'b-.')
plt.show()
"""
"""
颜色： 蓝色 - 'b' 绿色 - 'g' 红色 - 'r' 青色 - 'c' 品红 - 'm' 黄色 - 'y' 黑色 - 'k'（'b'代表蓝色，所以这里用黑色的最后一个字母） 白色 - 'w' 线： 
直线 - '-' 虚线 - '--' 点线 - ':' 点划线 - '-.' 常用点标记 点 - '.' 像素 - ',' 圆 - 'o' 方形 - 's' 三角形 - '^'
"""
"""
plt.subplot(2,1,1)
plt.plot(x,np.sin(x),'bo')
plt.subplot(2,1,2)
plt.plot(x,np.cos(x),'g')
plt.show()
"""
y=np.sin(x)
plt.scatter(x,y)
plt.show()