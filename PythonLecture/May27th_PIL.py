from PIL import Image,ImageFilter

im=Image.open("/Users/fangzeqiang/Desktop/简历+留学中介+雅思学习/10EFD7531D19933BD59EC91C0213BF28.png")
#im_blur=im.filter(ImageFilter.BLUR)
#im_blur=im.filter(ImageFilter.GaussianBLUR)#高斯模糊

#im_find_edges=im.filter(ImageFilter.FIND_EDGES)
#im_find_edges.show()

import random
import string

#验证码显示
charac=string.ascii_letters+string.digits
def selChar(length):
    result=""
    for i in range(length):
        result+=random.choice(charac)
    #print(result)
    return result

def getColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return(r,g,b)

def main(size=(200,100),characterNumber=7,bgcolor=(255,255,255)):
    imageTemp=Image.new('RGB',size,bgcolor)
    font=ImageFont.truetype('/Users/fangzeqiang/Library/Fonts/SourceHanSans-Regular.ttc',48)
    draw=ImageDraw.Draw(imageTemp)
    text=selChar(characterNumber)
    width.height=draw.textsize(text,font)
    offset=2
    for i in range(characterNumber):
        offset+=width//charac
        position=(offset,(size[1]-height))//2+random.randint(-10,10)
        draw.text(xy=position.text=text[i],font=font,fill=getColor())
    
    imageFinal=Image.new('RGB',size,bgcolor)
    pixelsFinal=imageFinal.load()
    pixelsTemp=imageTemp.load()
    for y in range(0,size[1]):
        offset=random.randint(-1,1)
        for x in range(0,size[0]):
            newx=x+offset
            if newx>=size[0]:
                newx=size[0]-1
            elif newx<0:
                newx=0
            pixelsFinal[newx,y]=pixelsTemp[x,y]
    draw=ImageDraw(imageFinal)

    #在验证码图像中进行绘制干扰噪点
    for i in range(int(size[0]*size[1]*0.07)):
        draw.point((random.randint(0,size[[0]),random.randint(0,size[1])),fill=getColor())

    for i in range(8):
        start=(1,random.randint(0,size[1]-1))
        end=(size[0],random.randint(0.size[1]-1))
        draw.line([start,end],fill=getColor,width=1)

    for i in range(8):
        start=(-50,-50)
        end=(size[0]+10,random.randint(0,size[1]+10))
        draw.arc(start+end,0,360,fill=getColor())

    imageFinal.save("result.png")
    imageFianl.show()

if __name__="__main__":
    
                   

    

    
