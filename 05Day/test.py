# 水仙花数

# num = int(input("请输入一个数->"))
# res = num
# sum = 0
#  
# for i in range(0, 3):
#     num1 = num % 10
#     num = num // 10 
#     sum = sum + num1 ** 3
# print(sum)
# print(res)
# if(sum == res):
#     print('是水仙花数')
# else:
#     print('不是水仙花数')

# 正整数的反转

# num = int(input('请输入一个正整数:'))
# 
# reversed_num = 0
# print(type(reversed_num))
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num = num // 10
# print(reversed_num)

# 百钱百鸡问题
# 公鸡5元一只，母鸡3元一只，小鸡1元三只,用 100块买 100 只鸡，问公鸡、母鸡、小鸡有多少只

# for i in range(0, 20):
#     for j in range(0, 33):
#         k = 100 - i - j
#         if 5 * i + 3 * j + k / 3 == 100:
#             print('公鸡 %d 只， 母鸡 %d 只， 小鸡 %d 只' % (i, j, k))


# from random import randint
# 
# money = 1000
# print(type(money))
# while money > 0:
#     print('你的总资产为:', money)
#     needs_go_on = False
#     while True:
#         debt = int(input('请下注:'))
#         if 0 < debt <= money:
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print('玩家摇出了%d点' % first)
#     if first == 7 or first == 11:
#         print('玩家胜!')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜!')
#         money -= debt
#     else:
#         needs_go_on = True
#     while needs_go_on:
#         needs_go_on = False
#         current = randint(1, 6) + randint(1, 6)
#         print('玩家摇出了%d点' % current)
#         if current == 7:
#             print('庄家胜')
#             money -= debt
#         elif current == first:
#             print('玩家胜')
#             money += debt
#         else:
#             needs_go_on = True
# print('你破产了，游戏结束！')


# 斐波那契数列

# def Feb(num):
#     if num == 1 or num == 2:
#         return 1
#     a = 1
#     b = 1
#     c = 2
#     i = 3
#     while i <= num:
#         c = a + b
#         a = b
#         b = c
#         i = i + 1
#     print('c = %d' % c)
#     return c
#
# num = int(input('请输入一个正整数'))
# print(num)
# res = Feb(num)
# print(res)

# n = int(input('请输入一个正整数:'))
# if n <= 2:
#     print('num = 1')
# else:
#     i = 3
#     a = 1
#     b = 1
#     c = a + b
#     while i <= n:
#         c = a + b
#         a = b
#         b = c
#         i = i + 1
#     print('num = %d' % c)


# 输出 100 以内素数

# def isPrime(num):
#     #print(int(num ** 0.5))
#     for i in range(2, int(num ** 0.5)+1, 1):
#         if num % i == 0:
#             return -1
#     return 1
#
# for i in range(100):
#     if isPrime(i) == 1:
#         print(i)

# 找出 10000 以内的完美

def perfectNum(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == num:
        return sum
    else:
        return -1

for i in range(2,10001):
    if perfectNum(i) > 0:
        print(i)

