#函数
#def functionname([parameterlist]):
# parameterlist为可选参数，用于指定函数中传递的参数，日过没有，则表示该函数没有参数，在调用时也不指定
#调用函数，也就是执行函数
#基本语法格式：  functionname(parameterlist)
# def function():
#     a = 1
#     b = 2
#     print(a+b)
# function()           #调用函数

#函数传参

"""
形式传参：在定义函数时，函数名后面括号中的参数为‘形式参数’
实际参数：在调用一个函数时，函数名后面括号中的参数为‘实际参数’，也就是将函数的调用
者提供给函数的参数称为实际参数
----
根据实际参数的类型不同，可分为将实际参数的值传递给形式参数、和、将实际参数的引用传递给形式参数两种情况
1、当实际参数为不可变对象的时候、进行值传递
2、当实际参数为可变对象的时候、进行的是引用传递
实际上：值传递和引用传递的基本区别就是，进行值传递后，改变形式参数的值，实际参数的值不变；
而进行引用传递后，改变形式参数的值，实际参数的值也一同改变。
可变参数：字典（dict）、列表（list）、集合（set）
不可变参数：字符串（str）、float、数值型（number）、元组（tuple）
"""
#定义函数
# def demo(obj):
#     # obj += obj
#     print("原值:", obj)
#     obj += obj
# #调用函数
# print("=========值传递=========")
# mot = "请叫我省帅"
# print("函数调用前的值：", mot)
# demo(mot)                  #采用不可变对象---字符串
# print("函数调用后的值：", mot)    #请叫我省帅
#
# print("=========引用传递========")
# list1 = ['德玛', '亚索']
# print("函数调用前的值：", list1)
# demo(list1)                 #采用可变对象---列表
# print("函数调用后的值：", list1)    #['德玛', '亚索', '德玛', '亚索']

#从上面的执行效果中可以看出、在进行值传递是，改变形式参数的值后，实际参数的值不改变；
#在进行引用传递时，改变形式参数的值后，实际参数的值也发送了改变

#再来一个实例：
# def fun_bmi(person, height, weight):
#     """
#     :param person:姓名
#     :param height: 身高， 单位：米
#     :param weight: 体重， 单位：千克
#     :return:
#     """
#     print(person + '的身高：' + str(height) + '米 \t 体重：' + str(weight) + '千克')
#     bmi = weight/(height * height)
#     print(person + "的BMI指标为：" + str(bmi))
#     #判断身材是否合理
#     if bmi < 18.5:
#         print("你的体重过轻 ~@_@~ \n")
#     elif bmi >= 18.5 and bmi <24.9:
#         print("正常范围，注意保持（-_-) \n")
#     elif bmi >= 24.9 and bmi < 29.9:
#         print("你的体重过重 ~@_@~ \n")
#     else:
#         print("肥胖 ^@_@^ \n")
# # *******************调用函数**********************
# fun_bmi("省帅", 1.85, 65)
# fun_bmi("大帅", 1.70, 52)

"""
上面代码：
1、定义一个根据身高、体重计算BMI指数的函数fun_bmi(),在定义函数时指定变量person、height、weight称为形式参数
2、在函数fun_bmi()中根据形式参数的值计算BMI指数，并输出结果
3、在调用fun_bmi()函数时，指定“省帅”、1.85和65等都是实际参数，在函数执行时，这些值将被传递给对应的形式参数
"""

#位置参数
"""
数量必须与定义时一致、位置必须与定义时一致
位置参数也称：必备参数，是必须按照正确的顺序传递到函数中，即调用时的数量和位置必须和定义时是一样的
1、在调用函数时、指定的实际参数的数量必须与形式参数的数量一致，否则就会抛出TypeError异常、提示缺少必要的位置参数
2、在调用函数时、指定的实际参数的位置必须与形式参数位置一致，否则将产生以下两种结果：
（1）：抛出异常：TypeError异常
（2）：产生的结果与预期不符
关键字参数：
关键字参数是指使用形式参数的名字来确定输入的参数值，通过该方式指定实际参数时、不再需要与形式参数的位置完全一致
只要将参数名写正确即可，这样可以避免用户需要牢记参数位置的麻烦
"""
# def fun_bmi(person, height, weight):
#     """
#     :param person:姓名
#     :param height: 身高， 单位：米
#     :param weight: 体重， 单位：千克
#     :return:
#     """
#     print(person + '的身高：' + str(height) + '米 \t 体重：' + str(weight) + '千克')
#     bmi = weight/(height * height)
#     print(person + "的BMI指标为：" + str(bmi))
#     #判断身材是否合理
#     if bmi < 18.5:
#         print("你的体重过轻 ~@_@~ \n")
#     elif bmi >= 18.5 and bmi <24.9:
#         print("正常范围，注意保持（-_-) \n")
#     elif bmi >= 24.9 and bmi < 29.9:
#         print("你的体重过重 ~@_@~ \n")
#     else:
#         print("肥胖 ^@_@^ \n")
# *******************调用函数**********************
# fun_bmi("省帅", 1.85)    #缺少参数传递、抛出TypeError异常
#结果： TypeError: fun_bmi() missing 1 required positional argument: 'weight'
# fun_bmi(65, '省帅', 1.85)   #参数位置不对抛出异常
# fun_bmi("省帅", 65, 1.85)   #参数位置不对，结果与实际情况不符
#由于在调用函数时，传递的实际参数位置与形式参数的位置不一致时，并不是总会抛出异常，所以确定好位置，否则参数BUG，还不容易被发现
# fun_bmi(height=1.85, weight=65, person='省帅')  #关键字参数、不需要与形式参数位置一致

#为参数设置默认值
"""
调用函数时：
如果没有指定某个参数将抛出异常，为了解决这个问题，我们可以为参数设置默认值，即在定义函数时
直接指定形式参数的默认值，这样，当没有传入参数时，则直接使用定义函数时设置的默认值
语法：
def functionname(....., [parameter1 = defaultvalue1]):
    [functionbody]
参数：
functionname：函数名
parameter1 = defaultvalue1：可选参数，用于指定向函数中传递的参数，并设置默认值defaultvalue1
functionbody：函数体
注意：在定义函数的时候，指定默认值的形式参数必须在所有参数的最后，否则将产生语法错误
"""
#代码：
# def fun_bmi(height, weight, person = '路人'):  #指定默认值的形式参数在所有参数最后
#     """
#     :param person:姓名
#     :param height: 身高， 单位：米
#     :param weight: 体重， 单位：千克
#     :return:
#     """
#     print(person + '的身高：' + str(height) + '米 \t 体重：' + str(weight) + '千克')
#     bmi = weight/(height * height)
#     print(person + "的BMI指标为：" + str(bmi))
#     #判断身材是否合理
#     if bmi < 18.5:
#         print("你的体重过轻 ~@_@~ \n")
#     elif bmi >= 18.5 and bmi <24.9:
#         print("正常范围，注意保持（-_-) \n")
#     elif bmi >= 24.9 and bmi < 29.9:
#         print("你的体重过重 ~@_@~ \n")
#     else:
#         print("肥胖 ^@_@^ \n")
# # **************函数调用**************
# fun_bmi(1.75, 60)    #调用函数不指定person参数，传递默认值
"""
输出：
路人的身高：1.75米 	 体重：60千克
路人的BMI指标为：19.591836734693878
正常范围，注意保持（-_-) 
"""
# fun_bmi(1.75, 60, '省帅')   #调用函数时指定了person参数，传递指定的person参数，不再传递默认值，如果没有指定则传递默认值
"""
输出：
省帅的身高：1.75米 	 体重：60千克
省帅的BMI指标为：19.591836734693878
正常范围，注意保持（-_-) 
"""
"""
在Python中，可以使用“函数名.__defaults__”查看函数的默认值
其结果是一个元组，
"""
# print(fun_bmi.__defaults__)    #查看函数默认值
#输出：('路人',)    结果是一个元组
#注意一点：定义函数时、为形式参数设置默认值要牢记一点，默认参数必须指向“不可变对象”
# def demo(obj=[]):   #定义函数并为参数obj指定默认值
#     print("obj的值：", obj)
#     obj.append(1)
# *********调用demo()函数***********
# demo()  #结果：obj的值： []
#如果连续两次调用呢？
# demo()    #结果：obj的值： []
# demo()    #结果：obj的值： [1]
#从上面结果可以看到，这显示不是想象中的结果，为了防止出现这种情况，最好使用None作为可变对象的默认值
# def demo(obj=None):
#     if obj == None:
#         obj = []
#     print("obj的值为：", obj)
#     obj.append(1)
# # ********函数调用**********
# demo()      #结果：obj的值为： []
# demo()      #结果：obj的值为： []
#所以：定义函数时、为形式参数设置默认值要牢记一点，默认参数必须指向“不可变对象”，否则使用None

#可变参数
"""
在python中、还可以定义可变参数，可变参数也称不定长参数，即传入函数中的实际参数可以是任意多个
定义参数时，主要有两种形式：一种是*parameter,另一种情况：**parameter
1、*parameter
这种形式表示接收任意多个实际参数并将其放到一个元组中
"""
#例如、定义一个函数，让其可以接受任意多个实际参数
# def printcoffee(*coffeename):
#     print('\n我喜欢的咖啡有：')
#     for item in coffeename:
#         print(item)
# *********函数调用*********
# printcoffee('蓝山')
# printcoffee('蓝山', '卡布奇洛', '摩卡')
#如果想使用一个已存在的列表作为函数的可变参数，可以在列表的名称前加“*”
# params = ['蓝山', '卡布奇洛', '摩卡']
# printcoffee(*params)







