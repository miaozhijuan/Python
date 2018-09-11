
# -*- coding: UTF-8 -*-

# @Time : 2018/7/23 15:31
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 04-集合.py
# @Software : PyCharm

'''

集合也是一种容器类型的数据额类型（序列）：数据放在{}中，多个之间用逗号隔开：{1,2，‘a’}
集合是无序的（不能通过索引去取值），可变（可以增删改），元素不能重复


集合可以进行数学中集合相关的操作：判断是否包含，求交集，并集，差集，补集
'''

# 1,怎么声明一个变量
''' 
a.声明一个变量，赋一个集合值
'''
set0 = set()  # 创建一个空的集合
set1 = {1, 2, 3, 2, 2}
print(set1, type(set1))
'''
b.将其他的数据类型转换成集合
'''
set2 = set('abc12333hh')  # 将其他数据转换成几个，自带一个去重的功能
print(set2)
set3 = set([12, 'abc', 'hh', 23, 56, 'abcdefg'])
print(set3)
print(list(set3))
print('================================')
# 2.增删改查
'''
a.查：遍历
注意：集合没有办法单独获取某一个元素
'''
for item in set2:
    print(item)

'''
b.增 集合.add(元素)：在指定的集合中添加指定的元素

'''

set1 = {1, 2, 3}
set1.add(100)
print(set1)


# 集合1.update（集合2）：将集合2中的元素添加到集合1中，自动去重
set1.update({'abc', 'ss', 1, 2})
print(set1)

'''c.删'''
# 集合。remove（元素）：在指定的集合中删除指定的元素
set1.remove('ss')
print(set1)

# pop 删除是随机删除一个
set1.pop()
print(set1)

# 3.判断是否包含
'''
集合1 >= 集合2   ----判断集合1中是否包含集合2
集合1 <= 集合2   ----判断集合2中是否包含集合1
'''
print({1, 2, 3, 4} >= {1, 4})  # True
print({1, 2, 3, 4} <= {1, 2})  # False

# 4.数学的集合运算
'''求并集：| '''
print({1, 2, 3} | {2, 3, 4, 5})

'''求交集： & '''
print({1, 2, 3} & {2, 3, 4, 5})

'''求差集： - '''
print({1, 2, 3} - {2, 3, 4, 5})

'''求补集： ^ '''
print({1, 2, 3} ^ {2, 3, 4, 5})




# 5.其他方法
'''clear:清空集合'''
set1 = {1, 2, 3}
set1.clear()
print(set1, type(set1))

'''len:获取集合中元素的个数'''
set1 = {1, 2, 3}
print(len(set1))


# 1.写一个程序
'''
a.用一个变量来保存一个班级的学生信息（姓名，学号，成绩（英语，体育，美术））
b.可以给这个班级添加学生
c.根据姓名删除一个指定的学生信息
d.根据姓名删除一个指定的学生信息
e.查看班级的所有学生信息
f.求指定的学生平均成绩

'''

# 2 尝试写学生管理系统
