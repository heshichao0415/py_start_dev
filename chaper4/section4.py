#序列应用

#切片，范围取值
#获取一个区间中的元素，用[开始下标：结束下标]形式表示，结束下标的元素不包含在内
# a = [1,2,3,4,5,6,7,]
# print(a[1:3])         #输出下标为1,2的元素，不包括3哦

#获取一个区间中的元素，有间隔的情况，用[开始下标：结束下标：间隔数量]形式表示
# a = [1,2,3,4,5,6,7,8]
# print(a[1:5:2])        #输出结果[2, 4]

#序列可相加，不会去重
# a = [1,2,3]
# b = [2,3,4]
# print(a+b)               #输出[1,2,3,2,3,4]

#列表
#删除列表
# list = [1,2,3]
# del list                   #用del删除列表
# print(list)

# import datetime
# now = datetime.datetime.now()         #获取当前时间
# print(now)
#
# weak = now.weekday()      #这里说说weekday()函数，weekday()方法则是从日期时间对象中获取星期，其值为0-6
#                             # 0代表星期一，1代表星期二，以此类推
# print(weak)

#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
#enumerate /I'nju:mei,ret/
# tem = ['湖人', '火箭', '马刺', '勇士', '掘金', '骑士']
# for index, item in enumerate(tem):
#     print(index, item)

# tem = ['湖人', '火箭', '马刺', '勇士', '掘金', '骑士']
# for index, item in enumerate(tem):
#     if index % 2 == 0:
#         print(item + "\t\t", end=' ')    #end=''表示不换行输出
#     else:
#         print(item + "\n")       #\n 换行输出

#这里有必要说说一些特殊的符号
"""
\ (在行尾时)            续行符
\\                      反斜杠
\'                      单引号
\"                      双引号
\n                      换行
\v                      纵向制表符
\t                      横向制表符
\r                      回车
还有个八进制\012， 十六进制\x0a 都是代表换行
"""

"""
列表元素的增加append(), 添加一个（单个数据）数据（任何类型）至列表的最后
列表名.insert（下标值（m），数据（n）） 在m位置前面插入数据n     insert--插入值；
extend(), 将一个列表中的值，全部添加到另外一个列表
"""
# list = ['a', 'b', 'c', 'd']
# list.insert(2, 5)                  #在c前面添加5
# print(list)

"""
修改列表的元素、直接通过下标修改
"""
# a = [1,2,3,4]
# a[1] = '我爱你'
# print(a)                         #[1, '我爱你', 3, 4]

"""
删除元素：
列表名.remove（数据）删除列表中第一个发现的指定数据 、根据元素值删除；
列表名.pop（下标）删除指定下标处的元素并返回该元素
del 列表名[下标]，也是通过下标来删除
"""
# a = [1,2,3,4,5,6,7,8]
# a.remove(1)             #删除元素1
# a.pop(-1)               #根据下标删除最后一个元素
# del a[-1]               #根据下标删除最后一个元素
# print(a)

# list = [1,1,1,2,3,4]
# num = list.count(1)          #list.count(1) 计算元素1在列表list中出现的次数，同时也用于判断元素是否存在
# print(num)

"""
index()方法可以获取元素在列表中首次出现的位置（即索引）
基本语法：
listname.index(obj)
listname: 列表名
obj:要查找的对象
"""
# a = [1,2,3,4,4,4,5]
# num = a.index(4)
# print(num)            #输出3

"""
sum()函数？？
用于统计数值列表中各元素的和
"""
# a = [1,10,20,44,21,41,21,43]
# num = sum(a)
# print(num)              #总和201， sum()只针对数字列表

"""
列表的排序：
listname.sort(reverse=False\True, key=None)    该方法会改变原列表的排列顺序
reverse的值为True表示降序排列、为False表示升序排列
key:例如在排序的时候不区分大小写可设置为key=str.lower

内置方法：sorted(listname, reverse=True\False)  此方法不会改变原列表的顺序
"""
# list = [3,9,1,6,10,2]
# list.sort(reverse=True)
# print(list)
# a = sorted(list, reverse=True)
# print(list)

"""
列表推导式
list = [Exception for var in range()]
Exception : 表达式，用于生生新列表的元素
var: 循环量
range:生成的var量
"""
# import random
# list = [random.randint(1, 50) for i in range(1, 11)]
# print("生成的随机数为：", list)

# a = [10, 30, 60, 25]
# b = [float(n*0.5) for n in a]
# print('原价为：', a)
# print('打五折后的价格为：', b)
#不一一举例了 大概就是这样的情况哦

"""
二维列表？
简单说就是列表中包含列表：
[[1,2], [2,3], [2,5]]
"""
# list = []
# for i in range(4):
#     list.append([])
#     for j in range(5):
#         list[i].append(j)        创建二维列表
# print(list)

#整个练习
# str1 = '千山飞鸟尽'
# str2 = '万径人踪灭'
# str3 = '孤舟远笠翁'
# str4 = '独钓寒江雪'
# verse = [list(str1), list(str2), list(str3), list(str4)]
# print("---- 横版 ----")
# for i in range(4):
#     for j in range(5):
#         if j == 4:
#             print(verse[i][j])
#         else:
#             print(verse[i][j], end=" ")




