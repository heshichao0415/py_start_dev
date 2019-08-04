#python 正则表达式

"""
定位符？？
定位符就是用来描述字符串的边界，"^"表示行的开始，"$"表示行的结尾
例如：
^tm
该表达式表示要匹配字符串tm的开始位置是行头
如“tm equal tomorrow moon”则可以匹配
"""
#元字符
"""
.   : 匹配除换行符以外的任意字符
\w  :匹配字母、数字、下划线或汉字
\W  ；匹配除字母、数字、下划线或汉字以外的字符
\s  : s是小写、表示任意空白字符串包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]
\S  : S是大写、表示不是空白符的任意字符
\b  : 在正则表达式中表示单词的开头或结尾，空格、标点、换行都算是单词的分割。
而“\b”自身又不会匹配任何字符，它代表的只是一个位置。所以单词前后的空格标点之类不会出现在结果里
\d  :匹配数字
"""

#限定符
"""
?   : 匹配前面的字符零次或一次，，也叫惰性匹配
+   ：匹配前面的字符一次或多次
*   ：表示任意数量的连续字符串 –又叫通配符
{n} : 匹配前面的字符n次  例如：go{2}gle,该表达式只匹配google
{n,}: 匹配前面的字符最少n次   例如：go{2,}gle,  匹配范围google到goo....gle
{n,m}: 匹配前面的字符最少n次，最多m次  例如：play{0,2}可以匹配pla,play,playy三种情况
[]   : 在正则表达式中，[]表示满足括号中任一字符。比如“[hi]”，它就不是匹配“hi”了，而是匹配“h”或者“i”
[^a] :这种情况呢？，表示除了a以外的任意字符、[^abcd]就是除 abcd 以外的任意字符。
所以^也可以叫排除符，[^a-z A-Z]用于匹配不是字母的字节
"""
#选择字符
"""
|  :“|”相当于 python 中“or”的作用，它连接的两个表达式，只要满足其中之一，就会被算作匹配成功
一些特殊的情况？
()在正则表达式里也有着特殊的含义，所以要匹配字符"("，需要用"\("
"""
#re模块
"""
match()方法
用于从字符串的开始处进行匹配，如果在起始位置匹配成功，则返回match对象，否则返回None
1、match对象中包含了匹配值的位置和匹配数据；
2、要获取起始位置用start()方法
3、要获取结束位置用end()方法
4、通过span()方法可以返回匹配位置的元组
5、通过string属性可以获取要匹配的字符串
6、通过group()获取匹配的数据
语法格式：
re.match(pattern, string, [flags])
参数：
pattern：表达模式字符串，由要匹配的正则表达式转换而来
string：表示要匹配的字符串
flags：可选参数，表示标志位，用于控制匹配方式、如是否区分大小写，常用的标志如下：
I ：执行不区分字母大小写的匹配
M ：
S ：
X ： 忽略模式字符串中未转义的空格和注释
"""
#举例：匹配字符串是否以“mr_”开头
# import re
# pattern = r'MR_\w+'
# string = 'MR_SHOP mr_shop'
# match = re.match(pattern, string, flags=0)
# print(match)   #返回:<_sre.SRE_Match object; span=(0, 7), match='MR_SHOP'>
# print('匹配值的起始位置为：', match.start())   # 匹配值的起始位置为： 0
# print('匹配值的结束位置为：', match.end())      #匹配值的结束位置为： 7
# print('匹配位置的元组为：', match.span())      # 匹配位置的元组为： (0, 7)
# print('要匹配的字符串为：', match.string)      # 要匹配的字符串为： MR_SHOP mr_shop
# print('匹配的数据为：', match.group())         # 匹配的数据为： MR_SHOP

#再来一个实例
#验证输入的手机号是否为中国移动的号码
# import re
# pattern = r'(13[4-9]\d{8})$|(15[01289]\d{8})$'          #定义一个正则表达式
# count = 1
# while count > 0:
#     mobile = input('请输入一个11位数的手机号：')
#
#     match = re.match(pattern, mobile, flags=0)
#     if match == None:
#         print(mobile, '不是有效的中国移动手机号码')
#         continue
#     else:
#         print(mobile, '是有效的中国移动手机号码')
#         continue

"""
search()方法
用于在整个字符串搜索第一个匹配的值，如果匹配，返回match对象，否则返货None
语法：
re.search(pattern, string, [flags])
"""
#例子：
#搜索第一个以“mr_”开头的字符串，
# import re
# pattern = r'mr_\w+'
# string = 'MR_SHOP mr_shop'
# match = re.search(pattern, string, flags=0)
# print(match)   # <_sre.SRE_Match object; span=(8, 15), match='mr_shop'>

# import re
# pattern = r'(黑客)|(抓包)|(监听)'
# about = '我是一名程序猿，我喜欢看黑客方面的书籍，研究一下Python'
# match = re.search(pattern, about)
# print(match)    #<_sre.SRE_Match object; span=(12, 14), match='黑客'>

"""
findall()方法
用于在整个字符串中搜索所有符合正则表达式的字符串，并以列表的形式返回
语法：
re.findall(pattern, string, [flags])
"""
# import re
# pattern = r'mr_\w+'
# string = 'MR_SHOP mr_shop'
# match = re.findall(pattern, string, flags=re.I)   #不区分大小写
# match1 = re.findall(pattern, string)
# print(match)     #['MR_SHOP', 'mr_shop']
# print(match1)    #['mr_shop']

# import re
# pattern = r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
# str1 = '127.0.0.1 192.168.21.123'
# match = re.findall(pattern, str1)
# for i in match:
#     print(i[0])

#替换字符串
"""
sub()方法
用于实现字符串替换
语法格式：
re.sub(pattern, repl, string, count, flags)
pattern：表示模式字符串
repl：表示替换的字符串
string：表示要被查找的字符串
count：可选参数，表示模式匹配后替换的最大次数，默认0，表示替换所有的匹配
flags：可选参数，表示标志位.....之前说过
"""
#例如隐藏中奖的手机号码
# import re
# pattern = r'1[34578]\d{9}'
# string = '中奖号码为：474939385 联系电话为：13627364746'
# result = re.sub(pattern, '1**********', string)
# print(result)    #中奖号码为：474939385 联系电话为：1**********

# import re
# pattern = r'黑客|抓包|监听'
# string = '我叫省帅，我喜欢玩网络，当黑客才是王道'
# sub = re.sub(pattern, '@_@', string)        #替换黑客
# print(sub)     #输出：我叫省帅，我喜欢玩网络，当@_@才是王道

#使用正则表达式分割字符串
"""
split()方法
用于实现根据正则表达式分割字符串，并以列表的形式返回
语法：
re.split(pattern, string,[maxsplit],[flags])
pattern：......
string: .........
maxsplit: 可选参数，表示最大的拆分次数
flags:可选参数....同上
"""
# import re
# pattern = r'[?|&]'    #r'[?&]'一样
# url = 'http://www.mingrisoft.com/login.jsp?username="me"&password=1234'
# result = re.split(pattern, url)
# print(result)  #输出：['http://www.mingrisoft.com/login.jsp', 'username="me"', 'password=1234']

# import re
# str1 = "@科比 @乔丹 @省帅"
# pattern = r'\s*@'
# list = re.split(pattern, str1)
# print(list)   #['', '科比', '乔丹', '省帅']

