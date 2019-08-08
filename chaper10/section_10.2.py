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
path = os.path.dirname(os.path.realpath(__file__))
print(path)     #返回：F:\py_start\chaper10
