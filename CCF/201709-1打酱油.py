n = int(input())

five= n//50
three = (n-five*50)//30
one = n//10 - five*5 - three*3

print(int(five*7+three*4+one))
