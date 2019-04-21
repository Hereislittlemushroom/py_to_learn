#练习1
#m=11223
"""
print("|%d|"%m)
print("|%8d|"%m)
print("|%-8d|"%m)
print("|%08d|"%m)
print("|%-08d|"%m) #注意没有0
"""
#练习2
"""
print("|%f|"%m)
print("|%8.1f|"%m)
print("|%8.2f|"%m)
print("|%-8.1f|"%m)
print("|%-8.0f|"%m)
"""
#练习3
"""
m="abcde"
print("|%s|"%m) #s for string?
print("|%8s|"%m)
print("|%-8s|"%m)
"""
#练习？ 位运算符练习
"""
print("0b11110000<<4 the result is :",bin(0b11110000<<4)) #what does bin mean ?
print("0b11110000>>4 the result is :",bin(0b11110000>>4))
print("0b1111111100000000 & 0b1111000011110000 the result is :",bin(0b1111111100000000 & 0b1111000011110000))
print("0b1111111100000000 | 0b1111000011110000 tri :",bin(0b1111111100000000 | 0b1111000011110000))
print("0b1111111100000000 ^ 0b1111000011110000 tri :",bin(0b1111111100000000 ^ 0b1111000011110000))
"""
#练习4 列表
"""
a=10
b=20
list=[1,2,3,4,5]
if(a in list):
    print("1-variable a is in the list")
else:
    print("1-variable a is not in the list")
if( b not in list):
    print("2-variable b is not in the list")    
else:
    print("2-variable b is in the list")
#修改a值
a=2
if(a in list):
    print("3-variable a is in the list")
else:
    print("3-variable a is not in the list")
"""
#练习5
"""
p=(4,78,23,34)
print("X:{0[0]};Y:{0[1]};Z:{0[2]};T:{0[3]}".format(p))

weather=[("monday","rainy"),("tuesday","sunny"),("wednesday","sunny"),("thursday","rainy"),("friday","cloudy")]
formatter="weather of '{0[0]}' is '{0[1]}'".format
for item in map(formatter,weather):
    print(item)
"""
#练习6 计算平均成绩
"""
name= input("enter your name: ")
math=eval(input(" enter your math score: "))
chi=eval(input("please enter your chinese score: "))
com=eval(input("enter your computer score: "))
aver=(math+chi+com)/3
print(name,": the average score is ", aver)
"""
#练习7 计算表面积与体积
"""
R = eval(input("enter the radius of the sphere : "))
V=(4/3)*3.14*(R**3)
S=4*3.14*(R**2)
print("the volume of the sphere is : ",V)
print("the surface area of the sphere is : ",S)
"""


#习题1
"""
s="ajldjlajfdljfddd"
set1=set(s) #直接用集合取出不重复的元素
set1=list(set1)
set1.sort()
print("".join(set1))
#习题2
s="ajldjlajfdljfddd"
print(s[-3]) # 用的什么索引？？？
#习题3
length=len(s)
print(length) #用内置的方法
#习题4
s="abcd1234"
print(s.replace('c','C',-1))
"""

#练习9 insert用法,append用法
I = ['B','U','T']
I.insert(1,'J')
print(I)

I.append('U')
print(I)

#练习10
aList=[3,4,5,6,7,9,11,13,15,17]
aList[::]
[3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
aList[::-1]
[17, 15, 13, 11, 9, 7, 6, 5, 4, 3]
aList[::2]
[3, 5, 7, 11, 15]
aList[1::2]
[4, 6, 9, 13, 17]
aList[3:6]
[6, 7, 9]

aList[0:100]
[3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
aList[100:]
[]
aList[-15:3]
[3, 4, 5]
len(aList)
10
aList[3:-5]
[6, 7]
 
