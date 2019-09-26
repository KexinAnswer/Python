# hello word
# print("Hello word!")
# 动态类型
# Python中的变量不需要声明，直接定义就可以
# 会在初始化的时候决定变量的 "类型"
# 使用 = 来进行初始化和复制操作
# counter = 0
# miles = 1000.0
# name = 'Bob'
# kilometers = 1.609*miles
# print(counter)
# print(miles)
# print(name)
# print(kilometers)
# python中不支持 ++/-- 操作， 只能写成 +=
# 动态类型， 同一个变量可以复制成不同类型的值
# a = 100
# print(a)
# a = 'hehe'
# print(a)
'''
a = 1
type(1)

a = 1000 * 1000 * 1000 * 1000 * 1000
print(a)

a = 10 + 5j
print(a)
'''

# a = 'hehe'
# b = "hehe"
# c = '''hehe'''
# print(a)
# print(b)
# print(c)

# a = 'My name is zyh"'
# print(a)

# a = 'My name is \n "zyh"'
# print(a)

# pystr = 'hehe'
# print(pystr[:])

# a = 'hehe'
# b = 'haha'
# c = a + b
# print(c)
#
# d = a*4
# print(d)
#
# e = a * b wrong
# print(e)

# a = 'hehe'
# type(a[0])
# print(len(a))

# a = 100
# print(a)
# pystr = 'a = %d'
# print(pystr)
# res = pystr % a
# print(res)

# a = 100
# pystr = 'a = %d'
# print("a = %d" % a)

# a = True
# print(a)
#
# b = a + 1
# print(b)

# name = input('Enter name : ')
# print(name)

# a = 1
# b = 2
# / 是精确除法
# print(a/b)
# // 是 整除
# print(a//b)

# ** 是乘方运算
# a = 2.3
# b = 10
# print(a**b)

# python 支持逻辑运算符 and or not
# print(2 < 4 and 2 == 4)
# print(2 < 4 or 2 == 4)
# print(not 6.2 < 6)
# print('hehe' != 'haha')
# print('hehe' < 'haha')

# [] 表示列表 () 表示元组
# 列表和元组可以保存任意数量，任意类型的python对象
# 可以使用下标来访问里面的元素， 下标从 0 开始 ， 最后一个下标为 -1

# alist = [1,2,3,4]
# print(alist)
# atuple = (1,2,3,4)
# print(atuple)
# print(alist[0:-1])

# a = [1, 'haha']
# print(a[0])
# print(a[1])
# print(a[:])

# 列表和元组的唯一区别就是，列表中的元素可以修改，但是元组中的元素不能修改
# a = [1,2,3,4]
# a[0] = 'heh'
# print(a)

# b = (1,2,3,4)
# b[0] = 100
# print(b)

# a = {'ip' : '127.0.0.1'}
# print(a['ip'])

# a = 100
# print(id(a))
# a = 200
# print(id(a))

# a = 2
# if a == 1:
#     print('true')
# else:
#     print('false')

# while 循环
# i = 0
# while i < 10:
#     print( 'loop %d' % i)
#     i += 1

# for 循环
# a = 'hehe'
# for c in a:
#     print(c)

# a = [1,2,3,4]
# for n in a:
#     print(n)

# a = {'ip':'127.0.0.1','port':'80'}
# for it in a:
#     print(it, a[it])

# 内建函数 range 能够生成一个数字组成的列表，方便进行for循环遍历

# for i in range(0,3):
#    print(i)

# range 函数其实有三个参数，前两个参数分别表示了一个前必后开的区间
#       第三个参数表示 step 每次迭代的步长

# for i in range(0,100,2):
#     print(i)
#     if(i == 20):
#         break
# pass 表示空语句

# 使用 for 循环将生成的值放在一个列表当中
# 生成 [0,4) 的主子平方序列
# squared = [x ** 2 for x in range(0,4)]
# print(squared)
#
# evens = [x for x in range(0,10) if x%2 == 1]
# print(evens)
#
# # 函数
# def Add(x,y):
#     return x+y
# print(Add(1,2))

# 理解 形参 和 实参 ： 形参相当于数学中的未知数， 实参就是给未知数确定具体的数值
# python 中没有重载这个概念， 相同名名字的函数 会覆盖前面的函数

# def Fun():
#     print('aaa')
#
# def Fun():
#     print('bbb')
#
# Fun()
#
# # python 支持默认参数 函数的参数可以具备默认值
#
# def Func(a = 1):
#     print(a)
#
# Func()

#  def GetPoint():
#      return 100,200
#
#  # x,y = GetPoint()
#  # print(x,y)
#
#  _ , y = GetPoint()
#  print(y)
#


