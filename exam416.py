def Sorted(list):
    u=[]
    temp=list[::]    #复制原列表
    while temp:
        Min=min(temp)
        u.append(Min)
        temp.remove(Min)
    return u
print(sorted([1,5,4,3,8]))
