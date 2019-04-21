import re
# match telNum
telNumber ='''Suppose my phone no. is 16605190086, yours is 18061751579, his is 05922291846.'''
usefulNumber=re.findall(r'\d{10,11}',telNumber)
if usefulNumber:
    print(usefulNumber)
# match email
str=''' xiaoming@1.com  xiaohong@.com   xiaohuang123@3.com  xiaoyu@123.com  xiao2lv@123.com     xiaofang@139.com    leishen.com     fangzeqiang@.sdw.com.compile    '''
usefulEmail=re.findall(r"[a-z0-9]*@[0-9]+.[a-z]+",str)
if usefulEmail:
    print(usefulEmail)
#match the date
str1=" aldb153 2019-03-26 14:30:00 2019-03-12 09:30:1O "
usefulDate=re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",str1)
if usefulDate:
    print(usefulDate)
#match the voca
str2=""" The shortest way 124 to do many 23111 things is to do 1689 only one thing 246 at a time"""
usefulVoca=re. findall("[a-zA-z]+", str2)
if usefulVoca:
    print(usefulVoca)