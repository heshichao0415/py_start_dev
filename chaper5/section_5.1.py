#字符串常用操作

#使用+运算符可完成对多个字符串的拼接
# str1 = '我今天一共走了'
# number = 50000
# str2 = '步'
# print(str1 + str(number) + str2)

#len()函数计算长度
# str1 = '神奇的9083你付;款'
# print(len(str1))

#encode()计算字符串占用的字节数
# str1 = '神奇的9083你付;款'
# print('str1所占用的字节数为：', len(str1.encode()), '字节')             #23字节

#截取字符串
"""
字符串也属于序列，也可以用切片的方法
string[start : end : step]
string：表示要截取的字符串
start：表示要截取的第一个字符串的索引（包括该字符）
end：表示要截取的最后一个字符的索引（不包括该字符）
step:表示切片的步长
"""
# str1 = '人生苦短，及时行乐'
# sub = str1[1]
# sub2 = str1[5:]
# sub3 = str1[:5]
# sub4 = str1[2: 5]
# # print(sub)
# # print(sub2)
# # print(sub3)
# # print(sub4)
# print(sub + '\n' + sub2 + '\n' + sub3 + '\n' + sub4 + '\n')

#分割、合并字符串
"""
split()函数
str.split(sep, maxsplit)
参数：
str：表示要分割的字符串
sep：用于指定分隔符，可以包含多个字符，默认None即所有空字符串（包括空格、换行、”\n“、制表符”\t“等）
maxsplit：可选参数，用于指定分割的次数，如果不指定或为-1，则分割次数没有限制，否则返回结果列表的元素个数
"""
# str1 = '我是 一个_大灰狼_安排-love>>> www.baidu.com'
# print('原字符串为：', str1)
# a = str1.split()
# print(a)
# b = str1.split('>>>')
# print(b)
# c = str1.split('_')[1]
# print(c)           #结果: 大灰狼
# d = str1.split('>')
# print(d)
# #返回结果为列表(list)

#合并字符串
#合并字符串与拼接字符串不同、合并字符串会将多个字符串采用固定的分隔符链接在一起
# strnew = string.join(iterable)
"""
参数：
string：字符串类型，用于指定合并时的分隔符
iterable：可迭代对象，该迭代对象中的所有元素（字符串）将被合并为一个新的字符串
# """
# list1 = ['我的名字', '叫省帅', '请访问', '我的地址']
# strnow = '@-@'.join(list1)
# print(strnow)
#输出：我的名字@-@叫省帅@-@请访问@-@我的地址

"""
检索字符串：
1、count()方法：
用于检索指定字符串在另一个字符串中出现的次数
语法：
str.count(sub[, start[, end]])
参数：
str：要检索的字符串
sub：表示要检索的子字符串
start, end 表示开始和结束的位置，不指定的话就是从开头到结尾检索
"""
# str1 = '我的名字叫省帅，请记住我哦，我爱你们哈'
# a = str1.count('我')
# print(a)            #结果为3，表示我出现了3次
# b = str1.count('我', 0, 11)
# print(b)              #结果为 1

"""
2、find()方法：
用于检索是否包含含有指定的子字符串，如果不存在则返回-1，否则返回首次出现该字符串的索引
语法：
str.find(sub, start, end)
start, end 表示开始和结束的位置，不指定的话就是从开头到结尾检索
"""
# str1 = '我的名字叫省帅，请记住我哦，我爱你们哈'
# a = str1.find('数')
# print(a)              #不存在，返回为-1
# b = str1.find('我')
# print(b)                #返回为 0

"""
3、index()方法：
跟find()类似，不过不同的是，当指定字符串不存在的时候会抛出异常，语法结构一样
str.index(sub, start, end)
4、startswith()方法：
用于检索字符串是否以指定子字符串开头，如果是则返回True,否则返回False
语法：
str.startswith(sub, start, end）
5、endswith()方法：
用于检索字符串是否以指定的子字符串结尾，是True,否False
"""
# str1 = '我的名字叫省帅，请记住我哦，我爱你们哈'
# a = str1.startswith('我')
# print(a)           #True
# b = str1.startswith('wo')
# print(b)             #False
# c = str1.startswith('我', 11, 18)
# print(c)            #True
# d = str1.endswith('哈')
# print(d)            #True

"""
字符大小写转换：
lower()和upper()
lower()方法：将字符串中的大写字母转换为小写字母
upper()方法：将字符串中的小写字母转换为大写字母
"""
# str1 = 'This is my First LOVE,省帅'
# a = str1.lower()
# print(a)             #this is my first love,省帅
# b = str1.upper()
# print(b)             #THIS IS MY FIRST LOVE,省帅

"""
去除字符串中的空格和特殊字符
1、strip()方法用于去掉字符串左、右两侧的空格和特殊字符
str.strip([chars])
chars：可选参数，用于指定要去除的字符，可以指定多个。不设置的话，默认空格，制表符，换行符等等
2、lstrip()方法用于去掉字符串左侧的空格和特殊字符串
3、rstrip()方法用于去掉字符串右侧的空格和特殊字符串
"""
# str1 = 'http://www.baidu.com@'
# a = str1.strip('@')
# print(a)            #http://www.baidu.com

"""
字符串的编码转换
encode()
解码：decode()
Python中，有两种常用的字符串类型，分别为"str"和"bytes"
str表示字符串
bytes表示二进制数据
"""
# str1 = '白衣渡江'
# a = str1.encode(encoding='utf-8')        #采用UTF-8编码，转换
# b = str1.encode('GBK')          #采用GBK编码转换
# print(a)    # b'\xe7\x99\xbd\xe8\xa1\xa3\xe6\xb8\xa1\xe6\xb1\x9f'
# print(b)    # b'\xb0\xd7\xd2\xc2\xb6\xc9\xbd\xad'
# c = a.decode('utf-8')          #通过utf-8格式解码
# print(c)    #白衣渡江
# d = b.decode('GBK')            #通过GBK格式解码
# print(d)    #白衣渡江



