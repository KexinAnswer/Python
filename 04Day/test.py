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
#for i in range(1,9):
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


