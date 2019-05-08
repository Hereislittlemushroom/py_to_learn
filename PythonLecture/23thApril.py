'''
class Vector:
	def __init__(self,a,b):
		self.a=a;self.b=b
	def __str__(self):
		return 'Vector(%d,%d)'%(self.a,self.b)
	def __add__(self,other):
		return Vector(self.a + other.a , self.b + other.b)
    

if __name__ == "__main__":
    v1=Vector(2,10)
    print(v1)
    v2=Vector(5,-2)
    print(str(v2))
    print(v1+v2)
'''

#编写类 扑克牌

import random as rd
class Hearts_Game():
    #牌的属性：正反面，牌的种类，数字 
    cardList=[]#卡组
    playerOwn=[]#玩家 包括ID,手上的牌
    #初始化牌组
    def Generate(self):
        i=0
        j=0
        number=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        kind=['红','黑','梅','方']
        for i in range(13):
            #kind种类有黑桃..红心，number从A2..K，side正面为face反面back
            for j in range(4):
                self.cardList.append({'number':number[i],'kind':kind[j],'side':'back'})
    #打乱顺序
    def upsetCard(self):
        rd.shuffle(self.cardList)
    #牌手属性：牌手名字，手上牌数
    def Player(self):
    #发牌方法：随机 固定张数 发牌顺序
if __name__ == "__main__":
    h1=Hearts_Game()
    h1.Generate()
    h1.upsetCard()
    for i in range(len(h1.cardList)):
        print(h1.cardList[i])
    