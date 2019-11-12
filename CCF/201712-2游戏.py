# 最小差值

# 方法一
n,k = map(int,input().split())
numList = list(range(1,n+1))
num = 1

while len(numList)>0:
    keys_del = []
    for key,value in enumerate(numList):
        if(num%k == 0 or num%10 == k):
            keys_del.append(key)
        num += 1
    acount = 0

    for key in keys_del:
        del numList[key-acount]
        acount+=1
        if(len(numList)==1):
            print(numList[0])

# 方法二

s = input().split()
n = int(s[0])
k = int(s[1])
a = [1 for i in range(0,n)] # 有n个人，1表示存活，0表示淘汰
total = sum(a)
num = 0
 
while total > 1:
    for i in range(0,len(a)):
        if a[i] != 0:
            num += 1
        if (num % k == 0) or (num % 10 == k):
            a[i] = 0
            total = sum(a)
            if total == 1:
                break
 
index = a.index(1) # 找出1的下标，这步是关键，运用index功能
print(index+1)
