n,l,t = map(int,input().split())
a = []
ball = []
a = list(map(int,input().split()))

for i in range(n):
    ball.append({'position':0,'direction':0})

# give every ball a position!
for i in range(n):
    ball[i]['position'] = a[i]
