# 输入 M 和 N 计算(M,N)

# m = int(input('m = '))
# n = int(input('n = '))
#
# fm = 1
# for num in range(1, m+1):
#     fm *= num
#
# fn = 1
# for num in range(1, n+1):
#     fn *= num
#
# fmn = 1
# for num in range(1, m-n+1):
#     fmn *= num
# print(fm//fn//fmn)

# 定义函数
# 在 python 中 可以使用 def 关键字来定义函数，和变量一样也有一个响亮的名字
# 而命名规则跟变量的命名规则是一致的。 在函数后面的圆括号中可以放置传递给函数的参数
# 这一点和数学上的函数非常相似，程序中函数的参数就相当于是数学上说的函数的自变量
# 而函数执行完成后我们可以通过 return 关键字来返回一个值，这相当于数学上说的因便力量

# def factorial(num):
#     result = 1
#     for n in range(1, num+1):
#         result *= n
#     return n
#
# m = int(input('m = '))
# n = int(input('n = '))
# print(factorial(m) // factorial(n) // factorial(m-n))

# 函数的参数
# 函数是绝大多数编程语言中都支持的一个代码的 “构建块” ，但是python中的函数与其他语言
# 中的函数韩式由很多不太相同的地方， 其中一个显著的区别就是 Python 对函数参数的处理。
# 在 Python 中， 函数的参数可以有默认值，也支持使用可变参数，所以 Python并不需要像其他
# 语言一样支持函数的重载，因为我们在定义一个函数的时候可以让他有多种不同的使用方式

# from random import randint
# def roll_dice(n = 2):
#     # 摇色子
#     total = 0
#     for _ in range(n):
#         total += randint(1,6)
#
#     return total
# def add(a = 0, b = 0, c = 0):
#     # 三个数相加
#     return a + b + c
#
# # 如果没有指定参数那么使用默认值摇两颗色子
# print(roll_dice())
# # 摇三色色子
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1,2))
# print(add(1,2,3))

# 用模块管理函数
# 对于任何一种编程语言来说，给变量、函数这样的标识符起名字都是一个让人头疼的问题，
# 因为我们会遇到命名冲突这种尴尬情况。 最简单的场景就是在同一个.py文件中定义了两个
# 同名函数， 由于 Python 没有函数重载的改变，那么后面的定义会覆盖之前的定义
# 也就意味着两个函数同名函数实际上只有一个是存在的

#def foo():
#    print('hello world')
#
#def foo():
#    print('goodbye world')
#
#foo()

# 练习
# 实现计算最大公约数 和 最小公倍数的函数

#def gcd(x, y):
#    (x, y) = (, x) if x > y else (x , y)
#    for factor
#print(gcd(num1, num2))
#print(gcd(num1, num2))
#print(lcm(num1, num2))


#num = 2
#sum = 1
#for i in range(1, 101):
#    sum *= num
#print(sum)


# num1 = int(input('num1 = '))
# num2 = int(input('num2 = '))
#
# (num1, num2) = (num2, num1) if num1 > num2 else (num1, num2)
# print(num1, num2)

def gcd(x, y):
    (x, y) = (x, y) if x > y else (y, x)
    while()



# from threading import Thread
# def sum(num):
#     sum = 0;
#     for i in range(1, num+1):
#         sum += i
#     print('sum = %d' % sum)
#
# def jsum(num):
#     sum = 0
#     for i in range(1, num+1, 2):
#         sum += i
#     print('Jsum = %d' % sum)
#
# def Fsum(num):
#     sum = 0
#     for i in range(1, num+1):
#         sum = sum + i ** 2
#     print('Fsum = %d' % sum)
#
# num = 1000000
# t1 = Thread(target=sum, args=('num',))
# t1.start()
# t2 = Thread(target=jsum, args=('num',))
# t2.start()
# t3 = Thread(target=Fsum, args=('num',))
# t3.start()
# t1.join()
# t2.join()
# t3.join()

#print(Fsum(100000))


