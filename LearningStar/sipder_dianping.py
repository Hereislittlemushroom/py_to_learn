import urllib.request 
url = "http://woodenrobot.me/2016/02/27/Hexo%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2%EF%BC%88%E4%B8%80%EF%BC%89%E2%80%94%E2%80%94%20%E5%89%8D%E6%9C%9F%E5%87%86%E5%A4%87/"
webPage=urllib.request.urlopen(url) 
data = webPage.read() #读取
data = data.decode('utf-8') #设置读取的字符编码
print(data) #打印读取的内容
print(type(webPage)) 
print(webPage.geturl()) #当前页的url
print(webPage.info()) 
print(webPage.getcode())