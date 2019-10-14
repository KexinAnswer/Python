# for-in 循环
# 用 for 循环实现 1~100 求和
# sum = 0;
# for x in range(101):
#     sum += x
# print(sum)

# 用 for 实现 1~100 偶数和
# sum = 0
# for x in range(2,101,2):
#     sum += x
# print(sum)

# 猜数字游戏
# import random
# answer = random.randint(1,100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入:'))
#     if number > answer:
#         print('猜大了')
#     elif number < answer:
#         print('猜小了')
#     else:
#         print('猜对了！')
#         break
# print('一共猜了 7 次')
# if(counter > 7):
#     print('智商明显不足')


# 输出 乘法口诀表
# for i in range(1,9):
#   for j in range(1,i+1):
#      print('%d * %d = %d' % (j,i,j*i), end='\t');
#   print();


# 输入一个正整数判断是不是素数

# num = int(input('请输入一个正整数:'))
# flag = True;
# for i in range(2,num):
#     print(i)
#     if num % i == 0:
#         flag = False
#         break
# print(flag)

# 输入两个正整数，计算他们的最大公约数和最小公倍数

# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     x, y = y, x
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d最大公约数是%d' % (x, y, factor))
#         print('%d和%d最小公倍数是%d' % (x, y, x * y // factor))
#         break
# 

row = int(input('row = '))
for i in range(0,row+1):
    print('i = %d' % i)
    for j in range(0, i+i):
        print('j = %d' % j)
        print('*', end='')
    print()