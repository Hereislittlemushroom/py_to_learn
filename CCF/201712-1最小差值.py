n = int(input())
li = list(map(int,input().split()))
li.sort() #列表排序
difference = list(map(lambda x,y:y-x,li[:-1],li[1:]))#后一项减去前一项的差值
print(min(difference))
