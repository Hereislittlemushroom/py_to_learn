n = int(input().strip())
arr = input().split()
# convert the string into int
arr = list(map(int,arr))
temp = arr[n//2-1] + arr[n//2]
middle = (temp//2 if temp % 2 == 0 else temp/2) if n % 2 == 0 else arr[(n-1)//2]
print(arr[n-1],middle,arr[0]) if arr[n-1]>=arr[0] else print(arr[0],middle,arr[n-1])
