#目录操作
#os模块、os模块是Python内置的与操作系统功能和文件系统相关的模块
import os    #导入os模块
#name :用于获取操作系统类型
# print(os.name)    #"nt"表示windows操作系统、"posix"表示linux、Unix、Mac OS操作系统

#linesep ：用于获取当前操作系统上的换行符
# print(os.linesep)

#sep ：用于获取当前系统所使用的路径分隔符
# print(os.sep)

#路径
#getcwd()返回当前的工作目录
# print(os.getcwd())    #输出当前目录，也是相对路径，相对路径就是依赖当前工作目录的

#绝对路径、指在使用文件时指定文件的实际路径，他不依赖于当前工作目录，abspath()方法
# print(os.path.abspath(r'py_start\message.txt'))  #获取‘py_start\message.txt' 绝对路径
#输出：F:\py_start\chaper10\py_start\message.txt

#拼接路径 join()方法
# a = os.path.join(r'f:\py_start\chaper10', 'message.txt')
# print(a)     #输出：f:\py_start\chaper10\message.txt

#判断目录是否存在？
#exists()方法
#os.path.exists(path)
# path = os.path.exists("f:/py_start/chaper10")  #也可以判断文件是否存在"f:/py_start/chaper10/message.txt"
# print(path)     #存在返回True 、不存在返回False

#split()方法
#把路径分割成 dirname 和 basename，返回一个元组
# a = os.path.split("f:/py_start/message.txt")[0]
# print(a)

#relpath()方法
#返回path的真实路径
# path = os.path.realpath(__file__)      #返回当前文件的路径
# print(path)

#dirname(path)从一个路径中提取文件路径，不包括文件名
# path = os.path.dirname(os.path.realpath(__file__))
# print(path)     #返回：F:\py_start\chaper10

#isdir()判断路径是否为目录
#创建目录
"""
1、创建一级目录
os.mkdir(path, mode=0o777)
path：用于指定要创建的目录，可以使用绝对路径，也可以使用相对路径
mode：用于指定数值模式，默认0777
"""
# import os
# os.mkdir(r'f:\py_start\test_os_mkdir')     #在f:\py_start路径下创建test_os_mkdir目录

#可在创建目录前判断此目录是否已存在
# import os
# path = 'f:\\py_start\\test_os_mkdir'
# if not os.path.exists(path):
#     os.mkdir(path)
#     print("目录创建成功！")
# else:
#     print("该目录已经存在！")

#创建多级目录
#makedirs()
#os.makedirs(name, mode=0o777)
# os.makedirs(r'f:\py_start\test_os\mkdir')  #创建f:\py_start\test_os\mkdir 目录

#删除目录 rmdir()且要目录为空才行
# import os
# os.rmdir(r'f:\py_start\test_os_mkdir')  #删除f:\py_start\test_os_mkdir目录

#删除目录前，判断目录是否存在
# import os
# path = r'f:\py_start\test_os_mkdir'
# if os.path.exists(path):
#     os.rmdir(path)
#     print("删除目录成功")
# else:
#     print("该目录不存在")

"""
使用rmdir只可删除空目录
如果想删除非空目录的话？？可以使用python的内置函数shutil的rmtree()函数
"""
# import shutil
# shutil.rmtree("f:\\py_start\\test_os_mkdir")     #删除非空目录

#遍历目录  os.walk()
# import os
# tuples = os.walk('f:\\py_start')   #遍历f:\\py_start目录
# for tuple in tuples:              #通过for循环输出目录
#     print(tuple)

#删除文件操作os.remove()
# import os
# os.remove("xxxx.txt")        #删除当前目录下的xxx.txt文件

#获取文件的基本信息os.stat()
# import os
# file = os.stat("xxxx.txt")     #获取xxx.txt文件的基本信息


