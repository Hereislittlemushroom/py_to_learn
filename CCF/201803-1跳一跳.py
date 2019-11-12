step = list(map(int,input().split()))
score = 0
last = 1

for i in step:
    if i==0:
        break
    elif i==1 :
        last = 1
        score += i
    else:
        if last==1:
            last = 2
        else:
            last += 2
        score += last
    
print(score)
