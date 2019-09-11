'''
　　在一条街上有n个卖菜的商店，按1至n的顺序排成一排，这些商店都卖一种蔬菜。
　　第一天，每个商店都自己定了一个价格。店主们希望自己的菜价和其他商店的一致，
   第二天，每一家商店都会根据他自己和相邻商店的价格调整自己的价格。
   具体的，每家商店都会将第二天的菜价设置为自己和相邻商店第一天菜价的平均值（用去尾法取整）。
　　注意，编号为1的商店只有一个相邻的商店2，编号为n的商店只有一个相邻的商店n-1，其他编号为i的商店有两个相邻的商店i-1和i+1。
　　给定第一天各个商店的菜价，请计算第二天每个商店的菜价。
输入格式
　　输入的第一行包含一个整数n，表示商店的数量。
　　第二行包含n个整数，依次表示每个商店第一天的菜价。
输出格式
　　输出一行，包含n个正整数，依次表示每个商店第二天的菜价。
样例输入
8
4 1 3 1 6 5 17 9
样例输出
2 2 1 3 4 9 10 13
数据规模和约定
　　对于所有评测用例，2 ≤ n ≤ 1000，第一天每个商店的菜价为不超过10000的正整数。
'''

# pay attention to the difference between 'arr2 = arr1' and 'arr2 = arr1.copy()'
# deep copy VS shallow copy

n = int(input().strip())
price1,price2 = [],[]

price1 = input().split()
price1 = list(map(int,price1))
price2 = price1.copy()

for i in range(1,n-1):
    price2[i] = (price1[i-1] + price1[i] + price1[i+1]) // 3

price2[0],price2[n-1] = (price1[0] + price1[1]) // 2 , (price1[n-2] + price1[n-1]) // 2

for i in price2:
    print(i,end=' ')
