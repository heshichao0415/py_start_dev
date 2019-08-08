#基本文件操作
"""
创建和打开文件
在python中，想要操作文件需要先创建或者打开指定的文件并创建文件对象
通过内置的open()函数实现
语法：
file = open(filename, mode)
filename ：文件名，同一目录下可以直接写文件名即可，否则需要指定完整路径
mode : 可选参数，指定打开的模式
模式有哪些？
r ：只读
rb ：以二进制格式打开文件，并且采用只读模式
r+ ：打开文件后，可以读取文件内容，也可以写入新的内容覆盖原有内容
rb+ ：以二进制格式打开文件，并且采用读写模式
w ：以只写模式打开文件
wb ：以二进制格式打开文件，并且采用只写模式
w+ ：打开文件后，先清空原有内容，使其变为一个空文件，对这个空文件有读写权限
wb+ ：以二进制打开文件，并且采用读写模式
a ：追加（新内容写到已有内容之后）
ab ：以二进制模式打开，并且采用追加模式
a+ ：以读写模式打开文件，
ab+ ：二进制打开，追加
"""
# file = open("f:\\py_start\\message.txt", 'w')      #创建文件message.txt
# file.write('this is my first file')   #写入内容
# file.close()    #关闭文件，一定要调用close()关闭文件，否则写入的内容不会保存到文件中

#以二进制打开非文本文件，如图像，视频等
# file = open("f:\\py_start\\images\\me.png", 'rb')
# print(file)          #<_io.BufferedReader name='f:\\py_start\\images\\me.png'>

#打开文件是指定编码方式
#在使用open()函数打开文件时，默认采用GBK编码，当被打开的文件不是GBK编码时，将会抛出异常
#解决办法？第一：修改文件的编码，第二：打开文件时，指定编码方式
#例如：
# file = open("f:\\py_start\\message.txt", 'r', encoding='utf-8')   #采用utf-8编码格式打开文件

#with语句打开文件
"""
打开文件后，要即使的将其关闭，否则会带来意向不到的后果
如果打开文件时抛出了异常，那么将导致文件不能被及时关闭
所以可以使用Python的with语句来解决这些问题
"""
# with open("f:\\py_start\\message.txt", 'w', encoding='utf-8') as file:
#     file.write('测试with语句')
# print('测试完毕')

#写入文件write()语句，上面有阐述，这里不再写
# with open("f:\\py_start\\message.txt", 'a', encoding='utf-8') as file:
#     file.write('\n追加一条信息写入到已有内容的最后')
# print("测试完毕")

#读取文件read()语句
#read(size) --> size可选参数，用于指定要读取的字符个数，如省略，则一次性读取所有内容
# with open("f:\\py_start\\message.txt", 'r', encoding='utf-8') as file:
#     string = file.read()
#     print(string)

#读取一行
"""
在使用read()方法读取文件时，如果文件很大，一次性读取全部内容到内存，容易导致内存不足
所以通常采用逐行读取
readline()方法用于每次读取一行数据
"""
# with open("f:\\py_start\\message.txt", 'r', encoding='utf-8') as file:
#     number = 0
#     while True:
#         number += 1
#         line = file.readline()
#         if line == "":
#             break
#         print(number, line, end="\n")

#读取全部行 readlines()
#类似read()方法，不过返回的是一个字符串列表,同时换行符也读出来了\n
# with open("f:\\py_start\\message.txt", 'r', encoding='utf-8') as file:
#     a = file.readlines()
#     print(a)
#     #输出：['测试with语句追加一条信息写入到已有内容的最后追加一条信息写入到已有内容的最后\n',
#     # '追加一条信息写入到已有内容的最后\n', '追加一条信息写入到已有内容的最后']

# with open("f:\\py_start\\message.txt", 'r', encoding='utf-8') as file:
#     messageall = file.readlines()
#     for message in messageall:
#         print(message)      #这样就没有了换行符了

