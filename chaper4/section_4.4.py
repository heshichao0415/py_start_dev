#字典  dict()
"""
字典与列表类似，也是可变序列，不过是无序的，所以也叫无序的可变序列。
保存方式为“键-对值”的形式
键是唯一的，而值可以有多个
特点：
1、通过键而不是通过索引来读取
2、字典是无序的，各项从左到右是随机排序的
3、字典是可变的
4、字典中的键必须是唯一的，不允许出现两次，如出现两次则后一个值会被记住
5、字典中的键是不可变的，可以使用数字，字符串或者元组，，但是不能使用列表
"""

# d = {'k1': 2, 'k1': 4, 'k2': 3}
# print(d)           #{'k1': 4, 'k2': 3}、重复出现的 key 会用最后一次出现的相同 key 对应的值 ，做为这个key的值

"""
zip()函数：
用于将多个列表或元组对应位置的元素组合为元组、并返回包含这些内容的zip对象。
如想获取元组，可以将zip对象使用tuple()函数转化为元组
想要得到列表，则可以使用list()函数将其转化为列表
"""
# name = ['科比', '乔丹', '奥胖']
# sign = ['双鱼座', '射手座', '水瓶座']
#
# a = dict(zip(name, sign))
# b = tuple(zip(name, sign))
# c = list(zip(name, sign))
# print(a)        #输出：{'奥胖': '水瓶座', '科比': '双鱼座', '乔丹': '射手座'}
# print(b)        #输出：(('科比', '双鱼座'), ('乔丹', '射手座'), ('奥胖', '水瓶座'))
# print(c)        #输出：[('科比', '双鱼座'), ('乔丹', '射手座'), ('奥胖', '水瓶座')]

#获取某个键值对的值、通过 key来映射value，采用‘字典名[key值]’获取key值对应的value；
# d1 = {'k1': 1, 'k2': 2, 'k3': 3}
# print(d1['k2'])
"""
Python也可以通过get()方法获取指定键的值
语法：
dictname.get(key[,default])
参数：
dictname：字典对象
key：指定键
default：可选项，用于当指定“键”不存在时，返回一个默认值，如果省略则返回空
"""
# d1 = {'k1': 3, 'k2': 2, 'k4': 6, 'k3': 7}
# a = d1.get('k2', '字典没有这个键')
# print(a)      #2
# b = d1.get('k6', '字典没有这个键')
# print(b)           #字典没有这个键
#
# print(d1['k5'])    #如果不用get()方法，当没有这个键的时候会抛出异常

"""
遍历字典：
items()方法：
可以获取字典的"键-值对"列表
语法：
dictname.items() 返回值为可遍历的（键-对值）的元组列表
通过for循环遍历该字典列表，获取键和值
"""
# d1 = {'k1': 3, 'k2': 2, 'k4': 6, 'k3': 7}
# a = d1.items()
# print(a)     #dict_items([('k4', 6), ('k1', 3), ('k3', 7), ('k2', 2)])
# for item in d1.items():
#     print(item)
#     #输出为：('k3', 7) ('k2', 2) ('k1', 3) ('k4', 6)
# for key, value in d1.items():
#     print(key, '的值为：', value, end=' ')
#     #输出为：k3 的值为： 7 k4 的值为： 6 k2 的值为： 2 k1 的值为： 3

"""
删除字典？？
如果想删除字典的全部元素，可以使用clear(),将字典变为空字典
pop()方法删除并返回指定“键”的元素
popitem()方法删除并返回字典中的一个元素（随机）
"""
# d = {'k1': 'a', 'k2': 'b', 'k3': 1, 'k4': 3}
# d.clear()
# print(d)
# print(d.pop('k2'))    #返回 b
# print(d)              #返回 {'k3': 1, 'k4': 3, 'k1': 'a'}
# print(d.popitem())      #随机删除一个键对值
# print(d)

#增加一组键对值
# d1={'k1':1,'k2':2,'k3':3}
# d1['k4']=4 #增加一个键对值：k4’
# print(d1)    #输出：{'k3': 3, 'k1': 1, 'k4': 4, 'k2': 2}

#修改键对值？？
# d1={'k1':1,'k2':2,'k3':3}
# d1['k3']=8  #更新键对值‘k3’为8
# print(d1)

#字典推导
# import random
# d = {i: random.randint(10, 100) for i in range(1, 5)}
# print('生成的字典为：', d)   #生成的字典为： {1: 53, 2: 41, 3: 83, 4: 88}

# name = ['科比', '詹姆斯', '刘德华', '省帅']
# sign = ['双鱼座', '射手座', '天秤座', '狮子座']
# dictname = {i:j for i, j in zip(name, sign)}
# print(dictname)  #{'詹姆斯': '射手座', '刘德华': '天秤座', '省帅': '狮子座', '科比': '双鱼座'}




