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
"""
在python中，可以通过@property（装饰器）将一个方法转换为属性，从而实现用于计算的属性
将方法转换为属性后，可以直接通过方法名来访问方法，而不需要在添加一对小括号（）
"""
# class Rect:
#     def __init__(self, width, heigth):
#         self.width = width
#         self.height = heigth
#
#     @property                      #装饰器
#     def area(self):
#         return self.width*self.height
#
# a = Rect(800, 600)
# print("面积为：", a.area)    #a.area   不加装饰器的话就要用a.area()

#通过property装饰的属性不能重新赋值
# class TVshow:
#     list_film = ["战狼", "红海行动", "熊出没", "变形记"]
#     def __init__(self, show):
#         self.__show = show                 #私有属性
#
#     @property
#     def show(self):
#         return self.__show
#
#     @show.setter               #设置setter方法，让属性可以修改
#     def show(self, value):
#         if value in TVshow.list_film:
#             self.__show = "你选择了《" + value + "》，稍后即将播出"
#         else:
#             self.__show = "你点播的电影不存在"
#
# tvshow = TVshow("战狼")
# print("正在播放：《", tvshow.show, "》")
# print("你可以从", tvshow.list_film, "中选择要点播的电影")
# tvshow.show = "捉妖记2"    # "红海行动"     修改属性
# print(tvshow.show)           #获取属性

#继承
"""
在面向对象编程中，被继承的类称为父类或者基类，新的类称为子类或派生类
"""
# class Fruit:                      #父类
#     color = "绿色"
#     def harvest(self, color):
#         print("水果是：" + color + '的')
#         print("水果已经收获........")
#         print("水果原来是:" + Fruit.color + "的！")
#
# class Apple(Fruit):                #派生类
#     color = "红色"
#     def __init__(self):
#         print("我是苹果")
# # ***************调用函数****************
# apple = Apple()
# apple.harvest(apple.color)              #调用基类的harvest()方法

#方法重写
#在派生类中可以对父类的方法进行重写
# class Fruit:                      #父类
#     color = "绿色"
#     def harvest(self, color):
#         print("水果是：" + color + '的')
#         print("水果已经收获........")
#         print("水果原来是:" + Fruit.color + "的！")
#
# class Apple(Fruit):                #派生类
#     color = "红色"
#     def __init__(self):
#         print("我是苹果")
#
# class Orange(Fruit):
#     color = "橙色"
#     def __init__(self):
#         print("\n我是橘子")
#     def harvest(self, color):
#         print("水果是：" + color + '的')
#         print("橘子已经收获........")
#         print("水果原来是:" + Fruit.color + "的！")
# # ***********调用函数************
# apple = Apple()
# apple.harvest(apple.color)              #调用基类的harvest()方法
# orange = Orange()
# orange.harvest(orange.color)            #重写后的方法进行调用，只对于本派生类生效哦

#派生类中调用基类的__init__()方法
"""
在派生类中定义__init__()方法时，不会自动调用基类的__init__()方法
因此，要让派生类调用基类的__init__()方法时，要进行必要的初始化，需要在派生类中使用super()函数
"""
# class Fruit:
#     def __init__(self, color='绿色'):
#         self.color = color                #定义类属性
#
#     def harvest(self):
#         print("水果原来是：" + self.color + "的！")
#
# class Apple(Fruit):
#     def __init__(self):
#         print("我是苹果")
#         super().__init__()       #调用基类__init__()方法，，没有这行代码是不行的
#
# apple = Apple()
# apple.harvest()

#例子：
# class Fruit:                                 #基类
#     def __init__(self, color='绿色'):
#         Fruit.color = color              #属性
#
#     def harvest(self, color):
#         print("水果是：" + color + "的！")
#         print("水果已经收获.......")
#         print("水果原来是：" + Fruit.color + "的！")
# class Apple(Fruit):
#     color = "红色"
#     def __init__(self):
#         print("我是苹果")
#         super().__init__()
# class Sapodilla(Fruit):
#     def __init__(self, color):
#         print("\n我是人参果")
#         super().__init__(color)
#     #重写harvest()方法：
#     def harvest(self, color):
#         print("人参果是：" + color + "的！")
#         print("人参果已经收获.......")
#         print("人参果原来是：" + Fruit.color + "的！")
# # ***********函数调用***********
# apple = Apple()
# apple.harvest(apple.color)
# sapodilla = Sapodilla("白色")
# sapodilla.harvest("黄金色带紫色条纹")


# class Fruit:
#     def __init__(self, color):
#         self.color = color
#     # @property
#     def apple(self):
#         print("苹果的颜色是：", self.color)
# class Apple(Fruit):
#     def __init__(self):
#         print("我是橘子")
#         super().__init__('白色')
#
# if __name__ == "__main__":
#     a = Apple()
#     a.apple()

