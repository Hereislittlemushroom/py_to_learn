def count(r,y,g,n):
    a,b,ans,light = 0,0,0,[r,g,y] 
    # light[0] is red, light[1] is green, light[2] is yellow
    # sum为红绿灯变换一周的总时长
    # sum_time = light[0]+light[1]+light[2]
    sum_time = sum(light)
    for i in range(n):
        a,b = input().split()
        a,b= int(a),int(b)
        
        if a == 0:
            ans += b
        else:
            if a == 1:
                a = 0
            elif a == 3:
                a = 1
            b = (light[a]-b+ans) % sum_time
            while b > light[a]:
                b -= light[a]
                a = (a+1) % 3
            if a == 0:
                ans += (light[a] - b)
            elif a == 2:
                ans += (light[a] - b + light[0])
    return ans

if __name__ == "__main__":
    r,y,g = input().split()
    r,y,g = int(r),int(y),int(g)
    n = int(input())
    sum_time = count(r,y,g,n)
    print(sum_time)
