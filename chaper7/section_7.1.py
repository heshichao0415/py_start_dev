#python面向对象
"""
对象、是一个抽象概念、英文称“object”
在python中、一切都是对象、即不仅是具体的事物称为对象、字符串、函数等也都是对象
这说明python天生就是面向对象的

类：
（class）
class Classname:
    statement              #类体

Classname：用于指定类名，一般使用大写字母开头
定义了类，然后就是创建类的实例
创建类的实例语法：
Classname(parameter)
Classname：必选参数，类名。用来指定具体的类
parameter：是可选参数，当创建一个类时，没有创建__init__()方法，或者__init__()方法只有一个self参数时,parameter可以省略

创建__init__()方法
在创建类后，可以手动创建一个__init__()方法，该方法是一个特殊的方法，每当创建一个类的新实例时，Python会自动执行它
__init__()方法必须包含一个self参数，并且必须是第一个参数，self参数是一个指向实例本身的引用，用于访问类中的属性和方法
在方法调用时会自动传递实际参数self，因此当__init__()方法只有一个参数时，在创建类的实例时，就不需要指定实际参数了
"""
# class Geese:
#     def __init__(self):     #构造方法
#         print('我是省帅')
# a = Geese()    #我是省帅

#在__init__()方法中，除了self参数外，还可以自定义一些参数，参数间使用逗号隔开
# class Geese:
#     def __init__(self, beak, wing, claw):      #构造方法
#         print('省帅的爱好:')
#         print(beak)
#         print(wing)
#         print(claw)
# a = '篮球'
# b = '耍'
# c = '打麻将'
# d = Geese(a, b, c)     #创建实例

#类属性，类属性是指定义在类中，并且在函数体外的属性，类属性可以在类的所有实例之间共享值，也就是说在所有实例化的对象中公用
#类属性可以通过类名称或者实例名访问
# class Geese:
#     neck = '我'       #类属性
#     wing = '你'       #类属性
#     leg = '他'        #类属性
#     def __init__(self):
#         print('我的类属性')
#         print(Geese.wing)       #属出类属性
#         print(Geese.leg)        #输出类属性
#         print(Geese.neck)       #输出类属性
# print(Geese.neck)            #通过类名访问类属性
# a = Geese()          #通过实例名访问类属性

#实例属性
#实例属性是指定义在类的方法中的属性，只作用于当前实例中，且只能通过实例名访问，不能通过类名访问
# class Geese:
#     def __init__(self):           #实例方法（相当于构造方法）
#         self.neck = '脖子长'             #定义实例属性
#         self.wing = '翅膀频率高'         #定义实例属性
#         self.leg = '行走自如'            #定义实例属性
#         print('我的实例属性有：')
#         print(self.neck)
#         print(self.wing)
#         print(self.leg)
# a = Geese()          #通过实例名访问实例属性
# print(Geese.neck)     #不能通过类名访问
#访问限制
"""
1、首尾双下划线表示定义特殊方法，一般是系统定义名字，如__init__()
2、以单下划线开头的表示protected（保护）类的成员、只允许类本身和子类进行访问，但是不能使用“from module import *”语句导入
3、双下划线开头，表示私有类的成员，只允许定义该方法的类本身进行访问，而且也不能通过类的实例进行访问
但是可以通过“类的实例名.__类名__xxx”方式访问
"""
#定义保护属性
# class Swan:
#     _neck = '脖子长'
#     def __init__(self):
#         print("__init__():", Swan._neck)      #在实例方法中访问保护属性
# swan = Swan()
# print("直接访问：", swan._neck)    #通过实例名访问保护属性

#私有属性
# class Swan:
#     __neck = '脖子长'         #双下划线，定义私有属性
#     def __init__(self):
#         print("__init__():", Swan.__neck)       #在实例方法中访问私有属性
# swan = Swan()
# print("加入类名访问：", swan._Swan__neck)    #通过“实例名._类名__xxxx”方式访问私有属性
# print("直接访问：", swan.__neck)          #私有属性不能通过实例名访问，出错

#属性（property）
