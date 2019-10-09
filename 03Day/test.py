# 分支结构

# if 语句
# username = input('请输入用户名：')
# password = input('请输入口令：')
# # 用户名是 'admin' 密码是'123456' 则验证成功否则什么验证失败
# if username == 'admin' and password == '123456':
#     print('身份验证成功')
# else:
#     print('身份验证失败')

# 分段函数求值
#         3x - 5 (x>1)
# f(x) =  x + 3 (-1 <= x <= 1)
#         5x + 3 (x < -1)

# x = int(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# elif -1 <= x <= 1:
#     y = x + 3
# else:
#     y = 5 * x + 3
# print(y)

# Practice
# 英制单位英寸和公里单位厘米互换
# value = float(input('请输入长度:'))
# unit = input('单位:')
# if unit == 'in' or unit == '英寸':
#     print('%f英寸 = %f厘米' % (value, value * 2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%f厘米 = %f英寸' % (value, value / 2.54))
# else:
#     print('请输入有效单位')

# 百分制成绩转换为等级制成绩
# 要求： 如果输入的成绩在90分以上  输出 A
# 要求： 如果输入的成绩在80 - 90  输出 B
# 要求： 如果输入的成绩在70 - 80  输出 C
# 要求： 如果输入的成绩在60 - 70  输出 D
# 要求： 如果输入的成绩在60分以下  输出 E

# grade = int(input('请输入成绩：'))
# if grade >= 90:
#     print('A')
# elif 80 <= grade < 90:
#     print('B')
# elif 70 <= grade < 80:
#     print('C')
# elif 60 <= grade < 70:
#     print('D')
# else:
#     print('E')

# 输入三条边长，如果能构成三角形就计算周长和面积
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and b + c > a and a + c > b:
    print('周长:' , a + b + c)
    p = (a + b + c) / 2
    area = (p * (p-a) * (p-b) * (p-c)) ** 0.5
    print('面积:' , area)
else:
    print('构不成三角形')

