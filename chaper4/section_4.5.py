#集合 set
"""
存储唯一性的多个数据（任何数据类型）
元素必须唯一，数据是无序的(无序可变序列)
"""

#集合元素的增加add()
# s3 = {1, 2, 3, 4}
# s3.add(8)
# print(s3)
#添加的元素只能使用字符串，数字，以及布尔型的True或者False等，不能使用列表，元组等可迭代对象

#集合元素的删除
#使用del删除整个集合
#pop()方法或者remove()方法删除一个元素
#clear()清空集合
# s = {'明日花绮罗', 5, 3, '省帅'}
# s.remove(5)     #删除5,remove()删除指定的值
# print(s)

# s.pop()        #随机删除一个值
# print(s)

# s.clear()     #清空集合
# # print(s)

#集合的运算
#交集运算符& 、并集运算| 、差集运算- 、补集运算^

#交集运算&：取两个集合同有（相同）的部分；
# t1 = {1, 2, 3, 4, 5, 6}
# t2 = {4, 5, 6, 7, 8, 9}
# print(t1 & t2)         #{4, 5, 6}

#差集运算-：去到与另外一个集合相同的部分；
# t1 = {1, 2, 3, 4, 5, 6}
# t2 = {4, 5, 6, 7, 8, 9}
# print(t1-t2)
#输出结果：{1, 2, 3} --去掉相同的部分4,5,6
# print(t2-t1)
# 输出结果：{8, 9, 7} --去掉相同的部分4,5,6
# print(t1^t2)  #--去掉重复的部分，留下不同（特有）的部分
#输出结果：{1, 2, 3, 7, 8, 9}

#并集运算|：联合两个集合中的所有元素；
# t1 = {1, 2, 3, 4, 5, 6}
# t2 = {4, 5, 6, 7, 8, 9}
# print(t1 | t2)  #--还是去掉了重复的数据，集合所拥有的特征
#输出结果：{1, 2, 3, 4, 5, 6, 7, 8, 9}


"""
总结：
可变：列表（list）、字典（dict)、集合(set)
不可变：元组(tuple)
可重复：列表（list）、元组（tuple）、字典（dict）
不可重复：集合（set）
有序：列表（list）、元组（tuple）
无序：字典（dict）、集合（set）
"""

