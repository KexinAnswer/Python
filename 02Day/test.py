# 变量的使用
# 使用变量保存数据并进行算数运算
# a = 321
# b = 123
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

# 使用 type() 检查变量类型
# a = 100
# b = 12.345
# c = 1 + 5j
# d = 'hello word'
# e = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b , a+b))
# print('%d - %d = %d' % (a, b , a-b))
# print('%d * %d = %d' % (a, b , a*b))
# print('%d / %d = %d' % (a, b , a/b))
# print('%d // %d = %d' % (a, b , a//b))
# print('%d %% %d = %d' % (a, b , a%b))
# print('%d ** %d = %d' % (a, b , a**b))

# 复制运算符和符合赋值运算符
# a = 10
# b = 3
# a += b  # a = a + b
# a *= a+2  # a = a * (a+2)
# print(a) # 195

# 比较、逻辑和运算身份符的使用
# flag0 = 1 == 1
# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# flag5 = not(1 != 2)
# print('flag0 = ', flag0)
# print('flag1 = ', flag1)
# print('flag2 = ', flag2)
# print('flag3 = ', flag3)
# print('flag4 = ', flag4)
# print('flag5 = ', flag5)
# print(flag1 is True)
# print(flag2 is not False)

# Practice

# 讲华氏温度转换为摄氏温度
# 华氏温度到摄氏温度的转换公式 $ C = (F- 32) \div 1.8 $
# f = float(input('请输入华氏温度'))
# C = (f-32) / 1.8
# print('%0.1f华氏度 = %0.1f摄氏度' % (f , C))

# 输入圆的半径计算周长和面积
# 周长 perimeter = 2 * Π * r
# 面积 area = Π * r ^ 2
# import math
# r = float(input('请输入圆的半径>'))
# perimeter = 2 * math.pi * r
# area = math.pi * (r ** 2)
# print('周长: %0.2f' % perimeter)
# print('面积: %0.2f' % area)

# 输入年份判断是不是闰年

# year = int(input('请输入年份'))
# print((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

# 字符串常用操作
str1 = 'hello world'
print('字符串长度>', len(str1))
print('字符串首字母大写>', str1.title())
print('字符串变大写>', str1.upper())
print('字符串是不是大写>', str1.isupper())
print('字符串是不是以 hello 开头>', str1.startswith('hello'))
print('字符串是不是以 hello 结尾>', str1.endswith('hello'))
str2 = '- 张宇航'
str3 = str1.title() + ' ' + str2.lower()
print(str3)


