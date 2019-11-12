n,L,t = map(int,input().split())
pos = list(map(int,input().split()))
dire = [1]*n

for i in range(t):
    for i in range(n): # 判断每个小球此刻的方向,和位置的改变
        if(pos[i] == L):
            dire[i] = -1
        if(pos[i] == 0):
            dire[i] = 1
        pos[i] += dire[i] #每个位置按照方向去改变！
        
    for i in range(n): # 判断小球间是否碰撞
        for j in range(i+1,n):
            if(pos[i]==pos[j]): #当前小球与其后一个小球的位置是否重叠
                dire[i]=-dire[i] #当前小球改变方向
                dire[j]=-dire[j] #后一个小球也改变方向
                
print(" ".join(str(i) for i in pos))
