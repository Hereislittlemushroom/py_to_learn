def inputPcb():
    i = 0
    pcb=[]
    n = int(input("请输入你的进程数目："))
    while(i < n):
        print("-------------------------------------")
        pID = chr(65+i)#将进程名命名为A,B,C,D,...
        print("请输入进程%s信息："%pID)
        arriveTime = int(input("到达时间:\t"))
        serviceTime = int(input("服务时间:\t"))
        piror = int(input("优先级:\t"))
        #进程名，到达时间，服务时间，开始，完成，周转，带权周转，优先级
        pcb.append([pID, arriveTime, serviceTime, 0, 0, 0, 0, piror]) 
        #id, arrivetime, servicetime have occupied 0,1,2 poistion in array pcb
        i += 1
    return pcb
if __name__ == "__main__":
    inputPcb()