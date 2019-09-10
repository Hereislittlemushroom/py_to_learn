n = int(input())
count = 0
listH = []

for i in range(n):
    a,b = input().split()
    a,b = int(a),int(b)
    listH.append([a,b])
    
def compare(a,b,c,d):
    if  a>=c and b<=d:
        return int(b-a)
    elif a<=c and b<=d:
        return int(b-c)
    elif a>=c and b>=d:
        return int(d-a)
    elif a<=c and b>=d:
        return int(d-c)
    else:
        return 0
#pay attention to the "=" in judging method !!!
    
for i in range(n):
    c,d = input().split()
    c,d = int(c),int(d)
    a,b = listH[i][0],listH[i][1]
    count += compare(a,b,c,d)

print(count)

    
