#pcb[]={'ID':'A','arrivalTime':0,'serviceTime':4,'prior':4,'finishTime':5,'RTime':2,'WRTime':2}
#输入函数
def inputEg():
        pcb=[]
        pcb.append(['A', 0, 4, 0, 0, 0, 0, 5]) 
        pcb.append(['B', 1, 3, 0, 0, 0, 0, 3])
        pcb.append(['C', 2, 5, 0, 0, 0, 0, 4])
        pcb.append(['D', 3, 2, 0, 0, 0, 0, 1])
        pcb.append(['E', 4, 4, 0, 0, 0, 0, 2])
    return pcb

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
#先进先服务算法
def FCFS(pcb):
    n=len(pcb)#n为进程数
    #对列表按照到达时间进行升序排序  x:x[1]为依照到达时间进行排序
    pcb.sort(key = lambda x:x[1], reverse = False )
    #计算开始、完成时间
    for i in range(n):
        if(i == 0):
            startTime = int(pcb[i][1])
            pcb[i][3] = startTime                  #the start time of process i 
            pcb[i][4] = startTime + int(pcb[i][2]) #the finish time of process i
 
        elif(i > 0 and int(pcb[i - 1][4]) < int(pcb[i][1])):
            #if the later process comes in after the former one finished
            startTime = int(pcb[i][1])                       
            #just come in without waiting
            pcb[i][3] = startTime
            pcb[i][4] = startTime + int(pcb[i][2])
 
        else:                                                
            #else
            startTime = pcb[i - 1][4]                        
            #the later one is required to wait till the former one finished
            pcb[i][3] = startTime                           
            pcb[i][4] = startTime + int(pcb[i][2])
        i += 1
    
    #计算周转、带权周转时间
    for i in range(n):
        pcb[i][5] = float(pcb[i][4] - int(pcb[i][1])) 
        pcb[i][6] = float(pcb[i][5] / int(pcb[i][2]))
        i += 1

    #计算平均周转时间和平均带权周转时间
    SzzTime = 0
    SdqzzTime = 0
    for i in range(n):
        SzzTime = float(SzzTime + float(pcb[i][5]))
        SdqzzTime = float(SdqzzTime + float(pcb[i][6]))
        AzzTime = float(SzzTime / n)
        AdqzzTime = float(SdqzzTime / n)

    #输出结果，按照开始时间进行排序
    pcb.sort(key = lambda x:x[3], reverse = False)
    print("运行结果:")
    for i  in range(n):
        print("进程: %s\t完成时间: %d\t周转时间: %d\t带权周转时间: %.2f" \
                  % (pcb[i][0], int(pcb[i][4]), int(pcb[i][5]), float(pcb[i][6])))
        i += 1
    print("本次调度的平均周转时间为：\t%.2f" % float(AzzTime))
    print("本次调度的平均带权周转时间为：\t%.2f" % float(AdqzzTime))
#最短作业优先算法
def SJF(pcb):
    n=len(pcb)
    pcb = pcb
    i = 1
    k = 0
    # 对列表按照到达时间进行升序排序  x:x[1]为依照到达时间进行排序
    pcb.sort(key = lambda x: x[1], reverse = False)
 
    #定义列表的第一项内容
    startTime0 = int(pcb[0][1])
    pcb[0][3] = startTime0
    pcb[0][4] = startTime0 + int(pcb[0][2])
    pcb[0][5] = int(pcb[0][4]) - int(pcb[0][1])
    pcb[0][6] = float(pcb[0][5]) / int(pcb[0][2])
 
    # 对后背队列按照服务时间排序
    temp_pcb = pcb[1:n]   #切片 临时存放后备队列  n为进程数
    temp_pcb.sort(key=lambda x: x[2], reverse=False)#排序
    pcb[1:n] = temp_pcb
 
    #进行计算
    """
    首先考虑当排序后的首个进程到达时间大于前一进程的时间，则需要选出后继进程中服务时间最短且到达时间最近的一个，即使用逐个替换的方法
    由于可能不能一次替换成功，所以使用while循环在每次替换之后进行查询，可能需要进行多次循环，直到选出下一个合适的进程
    如果是最后一个进程出现此类情况，则直接对其进行计算，用K值避免对最后一个进程的两次计算
    """
    while(i < n):
        h = 1
        # 比较到达时间和前一者的完成时间，判断是否需要进行重新排序
        while(int(pcb[i][1]) >= int(pcb[i - 1][4])):
            if(i == n-1):    #当最后一个进程的到达时间大于前一个进程的完成时间
                startTime = pcb[i][1]
                pcb[i][3] = startTime
                pcb[i][4] = startTime + int(pcb[i][2])
                pcb[i][5] = int(pcb[i][4]) - int(pcb[i][1])
                pcb[i][6] = float(pcb[i][5]) / int(pcb[i][2])
                k = 1      #设置参数对比，避免一重循环之后再对末尾进程重新计算
                break
            else:      #对进程顺序进行调换
                temp_sjf_pcb = pcb[i]
                pcb[i] = pcb[i + h]
                pcb[i + h] = temp_sjf_pcb
                h += 1
 
                """
                如果后面的所有进程的到达时间都大于第 i 个进程的完成时间
                则重新将i之后的进程按照服务时间排序，直接对其进行计算，同时i += 1,直接开始后面的计算              
                """
                if( h >= n - i - 1):
                    temp_pcb2 = pcb[i:n]
                    temp_pcb2.sort(key=lambda x: x[1], reverse=False)   # 后续队列重新按照到达时间顺序进行排序
                    pcb[i:n] = temp_pcb2
 
                    pcb[i][3] = int(pcb[i][1])
                    pcb[i][4] = int(pcb[i][1]) + int(pcb[i][2])
                    pcb[i][5] = int(pcb[i][4]) - int(pcb[i][1])
                    pcb[i][6] = float(pcb[i][5]) / int(pcb[i][2])
 
                    temp_pcb2 = pcb[i + 1:n]
                    temp_pcb2.sort(key=lambda x: x[2], reverse=False)  # 重新按照服务时间排序
                    pcb[i + 1:n] = temp_pcb2
                    h = 1
                    i += 1
                else:
                 continue
        if(k == 1):
            break
        else:
            startTime = pcb[i - 1][4]
            pcb[i][3] = startTime
            pcb[i][4] = startTime + int(pcb[i][2])
            pcb[i][5] = int(pcb[i][4]) - int(pcb[i][1])
            pcb[i][6] = float(pcb[i][5]) / int(pcb[i][2])
 
            i += 1
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
        print("进程 %s\t完成时间: %d\t周转时间: %d\t带权周转时间: %.2f" \
              % (pcb[i][0], int(pcb[i][4]), int(pcb[i][5]), float(pcb[i][6])))
        i += 1
    print("本次调度的平均周转时间为：\t%.2f" % float(AzzTime))
    print("本次调度的平均带权周转时间为：\t%.2f" % float(AdqzzTime))
#优先级调度算法
def PSA(pcb):
    n=len(pcb);i = 1;k = 0
    #对就绪队列按照优先级排序
    temp_pcb = pcb[0:n]   #存放就绪队列到temp n为进程数
    temp_pcb.sort(key=lambda x: x[7], reverse=False)#按优先级排序
    pcb[0:n] = temp_pcb
    #定义列表的第一项内容
    startTime0 = int(pcb[0][1])
    pcb[0][3] = startTime0                      #到达时间
    pcb[0][4] = startTime0 + int(pcb[0][2])     #完成时间=开始时间+服务时间
    pcb[0][5] = int(pcb[0][4]) - int(pcb[0][1]) #周转时间
    pcb[0][6] = float(pcb[0][5]) / int(pcb[0][2])#带权周转时间
    #进行计算
    '''
    while(i < n):
        h = 1
        #比较到达时间和前一者的完成时间，判断是否需要进行重新排序
        while(int(pcb[i][1]) >= int(pcb[i - 1][4])):
            if(i == n-1):    #当最后一个进程的到达时间大于前一个进程的完成时间
                startTime = pcb[i][1]
                pcb[i][3] = startTime
                pcb[i][4] = startTime + int(pcb[i][2])
                pcb[i][5] = int(pcb[i][4]) - int(pcb[i][1])
                pcb[i][6] = float(pcb[i][5]) / int(pcb[i][2])
                k = 1      #设置参数对比，避免一重循环之后再对末尾进程重新计算
                break
            else:      #对进程顺序进行调换
                temp_sjf_pcb = pcb[i]
                pcb[i] = pcb[i + h]
                pcb[i + h] = temp_sjf_pcb
                h += 1
                """
                如果后面的所有进程的到达时间都大于第 i 个进程的完成时间
                则重新将i之后的进程按照服务时间排序，直接对其进行计算，同时i += 1,直接开始后面的计算              
                """
                if( h >= n - i - 1):
                    temp_pcb2 = pcb[i:n]
                    temp_pcb2.sort(key=lambda x: x[1], reverse=False)   # 后续队列重新按照到达时间顺序进行排序
                    pcb[i:n] = temp_pcb2
 
                    pcb[i][3] = int(pcb[i][1])
                    pcb[i][4] = int(pcb[i][1]) + int(pcb[i][2])
                    pcb[i][5] = int(pcb[i][4]) - int(pcb[i][1])
                    pcb[i][6] = float(pcb[i][5]) / int(pcb[i][2])
 
                    temp_pcb2 = pcb[i + 1:n]
                    temp_pcb2.sort(key=lambda x: x[2], reverse=False)  # 重新按照服务时间排序
                    pcb[i + 1:n] = temp_pcb2
                    h = 1
                    i += 1
                else:
                 continue
        if(k == 1):
            break
        else:
            startTime = pcb[i - 1][4]
            pcb[i][3] = startTime
            pcb[i][4] = startTime + int(pcb[i][2])
            pcb[i][5] = int(pcb[i][4]) - int(pcb[i][1])
            pcb[i][6] = float(pcb[i][5]) / int(pcb[i][2])
    
            i += 1
    '''
    for i in range(n):
        if(i == 0):
            startTime = int(pcb[i][1])
            pcb[i][3] = startTime                  #the start time of process i 
            pcb[i][4] = startTime + int(pcb[i][2]) #the finish time of process i
 
        elif(i > 0 and int(pcb[i - 1][4]) < int(pcb[i][1])):
            #if the later process comes in after the former one finished
            startTime = int(pcb[i][1])                       
            #just come in without waiting
            pcb[i][3] = startTime
            pcb[i][4] = startTime + int(pcb[i][2])
 
        else:                                                
            #else
            startTime = pcb[i - 1][4]                        
            #the later one is required to wait till the former one finished
            pcb[i][3] = startTime                           
            pcb[i][4] = startTime + int(pcb[i][2])
        i += 1

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
#主函数
if __name__ == "__main__":
    #pcb=[]
    pcb=inputEg()
    while(True):
        option=int(input("choose your method to start( 1.FCFS / 2.SJF / 3.SPF):"))
        if(option==1):
            FCFS(pcb)
            break
        if(option==2):
            SJF(pcb)
            break
        if(option==3):
            PSA(pcb)
            break