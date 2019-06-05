class FIFO:
    pageLost=0
    success=0
    fail=0

    def __init__(self,*args,size=None):

        if len(args)!=0:
            self.FIFO=list(args)
            self.size=len(self.FIFO)
            if isinstance(size,int):
                self.size=max(self.size,size)
        else :
            self.size=size 
            self.FIFO=[] 

    def pop(self):
        if self.FIFO[0] == None:
            return "cannot pop, list is empty"
        else:
            return self.FIFO.pop(0)
         
    def push(self,page):
        self.FIFO.append(page)

    def visit(self,page):
        if len(self.FIFO)<self.size:
            self.push(page)
            self.success+=1
        else:
            self.pop()
            self.push(page)
            self.fail+=1
        print(self.__str__())

    def insert(self,data):
        
        for i in data:
            self.visit(i)
        print(self.loss())
            
    def __str__(self):
        return str(self.FIFO)
    
    def loss(self):
        if self.fail+self.success !=0:
            self.pageLost=self.fail/(self.fail+self.success)
        return str(self.pageLost)
    
    __repr__ = __str__

class LRU:
    pass

if __name__ == "__main__":
    q=FIFO(7,0,size=3)
    q.pop()
    q.pop()

    data = []
    print("enter the order list, end this by letter 'a'")
    while True:
        try:
            input_A = int(input("Input: "))
            if input_A=='a':
                break
            else:
                data +=[input_A]
        except:
            break
    
    q.insert(data)

