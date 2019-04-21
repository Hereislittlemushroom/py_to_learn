def priorSort(sumTime,i,pcb):
    j=i
    n=len(pcb)
    for j in range(n):
        pcb[j][8]=sumTime                         #待会改一波pcb范围
        pcb[j][7]=(pcb[j][8]+pcb[j][2])/pcb[j][2] #计算当前进程及以后的响应比
    #优先级 = (作业已等待时间 + 作业的服务时间) / 作业的服务时间
    #对i-n就绪队列重新按照优先级排序
    j=i
    for j in range(n):
        temp_pcb = pcb[i:n]                       #切片，存放就绪队列到temp n为进程数
        temp_pcb.sort(key=lambda x: x[7], reverse=False)#按优先级排序
        pcb[i:n] = temp_pcb
    return pcb

def HRRN(pcb):
    n=len(pcb)
    i = 0
    sumTime=0
    #定义列表的第一项内容

    #进行计算
    print("调度过程：")
    for i in range(n):
        if(i == 0):
            startTime = int(pcb[i][1])             #运行第一个进程时，开始时间等于它进入的时间
            pcb[i][3] = startTime                  #the start time of process i 
            pcb[i][4] = startTime + int(pcb[i][2]) #the finish time of process i
            print("当前时间: %d\t当前进程 %s\t当前响应比: %d\t等待时间: %d"%(pcb[i][3],pcb[i][0],pcb[i][7],pcb[i][8]))
            continue
        sumTime=sumTime + pcb[i-1][4]                       #第i个进程后包括其第i个本身的等待时间
        pcb=priorSort(sumTime,i,pcb)
        if(i > 0 and int(pcb[i - 1][4]) < int(pcb[i][1])):
            #如果当前进程的进入时间晚于前一个进程的完成的时间
            startTime = int(pcb[i][1])             #则需要等待，其开始时间等于当前进程进入时间
            pcb[i][3] = startTime
            pcb[i][4] = startTime + int(pcb[i][2])
        if(i > 0 and int(pcb[i - 1][4]) >= int(pcb[i][1])):                                                
            #如果当前进程进入时间早于前一个进程的完成时间
            startTime = pcb[i - 1][4]              #则不用等待，其开始时间等于上一个进程的完成时间          
            pcb[i][3] = startTime                           
            pcb[i][4] = startTime + int(pcb[i][2])
        print("当前时间: %d\t当前进程 %s\t当前响应比: %d\t等待时间: %d"%(pcb[i][3],pcb[i][0],pcb[i][7],pcb[i][8]))
    
    #计算周转、带权周转时间
    j=0
    for j in range(n):
        pcb[j][5] = float(pcb[j][4] - int(pcb[j][1])) 
        pcb[j][6] = float(pcb[j][5] / int(pcb[j][2]))

    # 计算平均周转时间和平均带权周转时间
    SzzTime = 0
    SdqzzTime = 0
    for i in range(n):
        SzzTime = float(SzzTime + float(pcb[i][5]))
        SdqzzTime = float(SdqzzTime + float(pcb[i][6]))
        AzzTime = float(SzzTime / n)
        AdqzzTime = float(SdqzzTime / n)
    # 输出结果，按照开始时间进行排序
    pcb.sort(key=lambda x: x[3], reverse=False)
    print("运行结果:")
    for i in range(n):
        print("进程 %s\t 优先级: %d\t完成时间: %d\t周转时间: %d\t带权周转时间: %.2f" \
              % (pcb[i][0], int(pcb[i][7]),int(pcb[i][4]), int(pcb[i][5]), float(pcb[i][6])))
        i += 1
    print("本次调度的平均周转时间为:\t%.2f" % float(AzzTime))
    print("本次调度的平均带权周转时间为:\t%.2f" % float(AdqzzTime))

if __name__ == "__main__":
    pcb=[]
    pcb.append(['A', 0, 4, 0, 0, 0, 0, 5, 0]) 
    pcb.append(['B', 1, 3, 0, 0, 0, 0, 3, 0])
    pcb.append(['C', 2, 5, 0, 0, 0, 0, 4, 0])
    pcb.append(['D', 3, 2, 0, 0, 0, 0, 1, 0])
    pcb.append(['E', 4, 4, 0, 0, 0, 0, 2, 0])
    HRRN(pcb)
