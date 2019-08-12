n = int(input().strip())
a , s1 = 1 , []
def reEval(s1):
    temp = s1.replace('x','*')
    temp1 = temp.replace('/','//')
    return eval(temp1) == 24
for i in range(n):
    s1.append(str(input().strip()))
for i in range(n):
    print("Yes" if reEval(s1[i]) else "No")
