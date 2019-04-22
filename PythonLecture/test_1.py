from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     target = 'http://www.360doc.com/content/18/0321/11/51484742_738963449.shtml'
     req = requests.get(url = target)
     html = req.text
     bf = BeautifulSoup(html)
     texts = bf.find_all('div', class_ = 'showtxt') 
     print(texts)

'''
alist=[3,4,5,6]
print(alist[-15:3]) #左闭右开
print(alist[::])
alist([1::2])
'''
'''
#字典类
dict={'a':1,'b':2,'c':3}
print(dict)
dict['c']=12
print(dict)
#dict.clear()
#print(dict)
dict={1:{'a':1},2:{'b':2},3:{'c':3}} #delete one word from dictionary
del dict[1]['a']
print(dict.items())
'''
'''
#集合
a={'boy'}
#print(a)
a.add('python')
#print(a)

a=set([1,2,3,4])
b=set([1,2,3,2])
#print(a|b)
print(a-b)
'''