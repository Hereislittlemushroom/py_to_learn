r,y,g = input().split()

r = int(r)
y = int(y)
g = int(g)

n = int(input())

sum_t = 0 # the whole time consum on the road
k,t = [],[]

def count(k:int,t:int,sum_t:int,r,y,g):
    if k == 1:
        sum_t += t
    elif k == 2:
        sum_t += (t + r)
    elif k == 3:
        return sum_t
    else:
        sum_t = sum_t + t
    return sum_t

for i in range(n):
    arr = []
    arr = input().split()
    arr = list(map(int,arr))
    sum_t = count(arr[0],arr[1],sum_t,r,y,g)

print(sum_t)

