"""
from turtle import Turtle
p=Turtle()
p.speed(1)
p.pensize(100)
p.fillcolor("red")
p.begin_fill()
for i in range(5):
    p.forward(200)
    p.right(144)
p.end_fill()
"""
"""
import turtle

turtle.hideturtle()
turtle.speed(1)
turtle.pensize(3)
turtle.penup()
turtle.goto(-200,-50) #goto去到指定坐标
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill
turtle.circle(40,steps=3) #step三角形设置为3，正方形为4
turtle.end_fill()

turtle.pensize(3)
turtle.penup()
turtle.goto(-100,-50) #goto去到指定坐标
turtle.pendown()
turtle.circle(40,steps=4) #step三角形设置为3，正方形为4

turtle.pensize(3)
turtle.penup()
turtle.goto(10,-50) #goto去到指定坐标
turtle.pendown()
turtle.circle(40,steps=5) #step三角形设置为3，正方形为4

turtle.pensize(3)
turtle.penup()
turtle.goto(100,-50) #goto去到指定坐标
turtle.pendown()
turtle.circle(40,steps=6) #step三角形设置为3，正方形为4

turtle.pensize(3)
turtle.penup()
turtle.goto(200,-50) #goto去到指定坐标
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.pendown()
turtle.circle(40) #step三角形设置为3，正方形为4
turtle.end_fill()
"""
"""
#画蟒蛇
import turtle
turtle.setup(650,350,200,200) #width height windows'position
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(30)
turtle.pencolor("blue")
turtle.seth(-40) #turtle启动方向
for i in range(4):      #重点看循环体
    turtle.circle(40,80) #40是一个半径
    turtle.circle(-40,80) #80是弧度
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
"""
#三部分
#表盘
#文本
#指针 分针时针秒针

from turtle import *
from datetime import *

def SetupClock(radius):
    reset()
    pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 ==0:
            forward(20)
            Skip(-radius-20)
        else:
            dot(5)
            Skip(-radius)
        right(6)
def Skip(step):
    penup()
    forward(step)
    pendown()

def mkHand(name,length):
    reset()
    Skip(-length*0.1)
    begin_poly()
    forward(length*1.1)
    end_poly()
    handForm=get_poly()
    register_shape(name,handForm)

def Init():
    global secHand, minHand,hurHand,printer
    mode("logo")
    mkHand("secHand",125)
    mkHand("minHand",130)
    mkHand("hurHand",90)
    secHand=Turtle()
    secHand.shape("secHand")
    minHand=Turtle()
    minHand.shape("minHand")
    hurHand=Turtle()
    hurHand.shape("hurHand")
    for hand in secHand,minHand,hurHand:
        hand.shapesize(1,1,3)
        hand.speed(0)
    printer=Turtle()
    printer.hideturtle()
    printer.penup()

    def Tick():
        t=datetime.today()
        second=t.second+t.microsecond*0.000001
        minute=t.minute+second/60.0
        hour=t.hour+minute/60.0
        secHand.setheading(6*second) #设置偏转角度
        minHand.setheading(6*minute)
        hurHand.setheading(30*hour)

        tracer(False)
        printer.forward(65)
        printer.write(Week(t),align="center",
                      font=("Courier",14,"bold"))
        printer.back(130)
        printer.write(Date(t),align="center",
                      font=("Courier",14,"bold"))
        printer.home()
        tracer(True)
        ontimer(Tick,100)

def Week(t):
    week=["Mo","Tu","Wed","Th","Fr","Sa","Su"]
    return week[t.weekday()]

def Date(t):
    y=t.year
    m=t.mouth
    d=t.day
    return "%s%d%d"%(y,m,d)

if __name__ == "__main__":
    tracer(False)
    Init()
    SetupClock(160)
    tracer(True)
    Tick()
    mainloop()