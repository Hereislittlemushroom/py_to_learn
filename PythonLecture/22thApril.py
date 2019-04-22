class fruit:
    def __init__(self, *args, **kwargs):
        self.__color='r'
        self.price=1

if __name__ == "__main__":
    apple=fruit()
    print(apple._fruit__color)

#对象销毁
#通过id来测试内存使用情况

#内置类属性
__dict__    #字典
__doc__
__name__
__module__

#python2 与 python3

#总结python2差异性，面试可能会问到
#二者在对属性的实现和处理方式不一样
#python2在增加新的数据成员时会隐藏同名已有属性

#python2中属性