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
python2在增加新的数据成员时会隐藏同名已有属性

python2中属性

python3中对私有属性保护的更好
python3封装性更好

接收实例化过程中传入的所有数据
why 关键字 self 可以定义别的关键字不会报错

###python动态性
混入性，可以增加新的属性和行为

```python

import types
class Person(object):
    def __init__(self, *args, **kwargs):
        assert isinstance(name,str),'name must be string'#断点检测
        self.name=name
    def
zhang=Person()
zhang.sing=types.MethodType()
zhang.walk=...
#很重要可以直接在外部新增方法，体现了动态性
```
###析构方法
属性销毁 类销毁

###静态方法
```python
@classmethod
@staticmethod
```

可以用类名调用类的方法
###期末作业
书写图形用户界面