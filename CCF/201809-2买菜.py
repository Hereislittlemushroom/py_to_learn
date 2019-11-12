n = int(input())
H,W=[],[]     # 小H与W的各个装车的时间段
for i in range(n):
    H.append(list(map(int,input().split())))
for i in range(n):
    W.append(list(map(int,input().split())))

timeLine = max(H[n-1][1],W[n-1][1])-1  # 最长时间, -1是因为从0开始算，最长时间为15，则时间段为0-14

flag = [0 for x in range(timeLine)]  # 用于记录每个时间段H与W的搬运情况
                                     # 如果任意一人在这段时间搬运，则+1

for i in range(n):
    for j in range(H[i][0],H[i][1]):
        flag[j-1] += 1               # 注意这里的j-1，因为题目是从1开始算，而这里是从0开始，故要j-1
for i in range(n):
    for j in range(W[i][0],W[i][1]):
        flag[j-1] += 1
        
print(flag.count(2))  # 小H和小W都在的时段个数
                      # 2表示二者在此时都在搬运，可以聊天
