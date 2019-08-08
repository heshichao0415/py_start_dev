#程序异常
#常见的异常
"""
NameError ：尝试访问一个没有声明的变量引发的错误
IndexError ：索引超出序列范围引发的错误
IndentationError ：缩进错误
ValueError ：传入的值错误
KeyError ：请求一个不存在的字典关键字引发错误
IOError ：输入输出错误（如果读取文件不存在）
ImportError ：当import语句无法找到模块或from无法在模块中找到相应的名称是引发的错误
AttributeError ：尝试访问未知的对象属性引发的错误
TypeError ：类型不合适引发的错误
MemoryError ：内存不足
ZeroDivisionError ：除数为0引发的错误
"""
#异常处理语句
"""
try......except捕获异常
如果在except后面不指定异常名称，则表示捕获全部异常
使用try......except语句捕获异常后，当程序出错时，输出错误信息后，程序会继续执行
try.....except...else语句
用于指定当try语句块中没有发生异常时要执行的else语句块，当try语句中的块发生异常时将不会执行else中的语句
try....except....finally语句
完整的异常处理语句，无论程序中有无异常产生，finally代码块中的代码都会被执行
"""
# def division():
#     "测试：分苹果"
#     print("\n============分苹果了===========\n")
#     apple = int(input("请输入苹果的个数："))
#     children = int(input("请输入来了几个小朋友："))
#     result = apple // children
#     remain = apple - result * children          #剩余的苹果
#     if remain > 0:
#         print(apple, "个苹果，平均分给", children, "个小朋友，每个人分了", result, "个，剩下", remain, "个。")
#     else:
#         print(apple, "个苹果，平均分给", children, "个小朋友，每个人分了", result, "个。")
# if __name__ == "__main__":
#     try:
#         division()
#     except ZeroDivisionError:
#         print("\n出错了 ~-~ --苹果不能被0个小朋友分！")
#     except ValueError as e:
#         print("输入错误：", e)
#     else:
#         print("分苹果顺利完成......")
#     finally:
#         print("进行了一次分苹果操作")

"""
raise语句抛出异常
如果某个函数或者方法可能会产生异常，但是不想在当前函数或方法中处理异常，则可以使用raise语句抛出异常
语法：
raise[exceptionName(reason)]
exceptionName : 为可选参数，用于指定抛出的异常名称
reason ：对异常的相关描述
"""
# def division():
#     "测试：分苹果"
#     print("\n============分苹果了===========\n")
#     apple = int(input("请输入苹果的个数："))
#     children = int(input("请输入来了几个小朋友："))
#     if apple < children:
#         raise ValueError("苹果太少，不够分啊........")          #使用raise抛出异常
#     result = apple // children
#     remain = apple - result * children          #剩余的苹果
#     if remain > 0:
#         print(apple, "个苹果，平均分给", children, "个小朋友，每个人分了", result, "个，剩下", remain, "个。")
#     else:
#         print(apple, "个苹果，平均分给", children, "个小朋友，每个人分了", result, "个。")
# if __name__ == "__main__":
#     try:
#         division()
#     except ZeroDivisionError:
#         print("\n出错了 ~-~ --苹果不能被0个小朋友分！")
#     except ValueError as e:
#         print("输入错误：", e)
#     else:
#         print("分苹果顺利完成......")
#     finally:
#         print("进行了一次分苹果操作")

#使用assert语句调试程序