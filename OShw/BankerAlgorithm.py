#银行家算法
#python
import copy

def add(a:list,b:list):
    return [a[i]+b[i] for i in range(len(a))]

def minus(a:list,b:list):
    return [a[i]-b[i] for i in range(len(a))]

def can(ava:list,need:list):
    for i in range(len(ava)):
        if ava[i]<need[i]:
            return False
    return True

class p:
    count=0#进程数
    sysmax=[0,0,0]#系统最大资源数
    sysava=[0,0,0]#系统当前可用资源数
    def __init__(self,max,need=None):
        if need is None:
            need=max
        p.count+=1
        self.max=max#单个进程总需要资源量量
        self.need=need#单个进程仍需的资源量
        self.id=p.count#进程编号
        p.sysava=minus(add(p.sysava,self.need),self.max)


    def setsysmax(max:list):
        p.sysava=add(p.sysava,minus(max,p.sysmax))
        p.sysmax=max

    def canrun(self):
        return can(p.sysava,self.need)

    def run(self):
        if self.canrun():
            p.sysava=add(p.sysava,minus(self.max,self.need))
            self.need=[0,0,0]
            return True
        else:
            return False

    def finish(self):
        for i in self.need:
            if i!=0:
                return False
        return True

    def bankrun(plist:list):
        #以银行家算法运行程序，会改变进程状况
        priority=[]
        tmplist=plist[:]
        while len(tmplist)>0:
            found=False
            for pr in tmplist:
                found=pr.run()
                if found:
                    tmplist.remove(pr)
                    priority.append(pr)
                    break
            if not found:
                return False,priority
        return True,priority

    def bankcheck(plist:list):
        #以银行家算法检查，不会改变进程状况
        tmp=p.sysava
        tmplist=copy.deepcopy(plist)
        while len(tmplist)>0:
            found=False
            for pr in tmplist:
                found=pr.run()
                if found:
                    tmplist.remove(pr)
                    break
            if not found:
                p.sysava=tmp
                return False
        p.sysava=tmp
        return True


    def allot(self,plist:list,al=[0,0,0]):
        self.need=minus(self.need,al)
        p.sysava=minus(p.sysava,al)
        if p.bankcheck(plist):
            return True
        else:
            self.need=add(self.need,al)
            p.sysava=add(p.sysava,al)
            return False


    def __str__(self):
        return "{i}\tmax:{max}\tneed:{need}".format(
            i=self.id,
            max=",".join([str(x) for x in self.max]),
            need=",".join(str(x) for x in self.need))

    def __repr__(self):
        return repr(self.__str__())

if __name__ == '__main__':
    p.setsysmax([10,5,7])
    pl=[
    ([7,5,3],[7,4,3]),
    ([3,2,2],[1,2,2]),
    ([9,0,2],[6,0,0]),
    ([2,2,2],[0,1,1]),
    ([4,3,3],[4,3,1])
    ]
    plist=[]
    for i in pl:
        plist.append(p(i[0],i[1]))
    for pr in plist:
        print(pr)
    print("------------------------------------")
    print(plist[0].allot(plist,[0,1,1]))
    print("------------------------------------")
    finish,priority=p.bankrun(plist)
    print(finish)
    for pr in priority:
        print(pr)
