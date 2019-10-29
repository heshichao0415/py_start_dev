# a = c =100
# print(id(a))
# print(id(c))         #id()来获取变量的内存地址
# a = 100
# b = 'abc'
# # print(a+b) #错误         print(str(a)+b)  正确
# c = '''     ぇ
#              |
#           ___|_
#          =-007^___|
#          __beautiful_girl(中国)
#          [0000000！＊？/】
# '''
# print(c)
# b = 'dsfsfs' \
#     'sfsfms' \
#     'sfsmlfmsl' \
#     'sfmslkfm' \
#     'sfslmfl'
# print(b)
# f = '\\b'
# # print(f)
# a = '我爱余情\x0a爱情'   #八进制\012或者十六进制\x0a都代表换行
# print(a)
# a = '[1,2],[3,4]'
# print(eval(a))
# print(list(eval(a)))
# print(list(a))
# print(a)
# a = input('请输入整数')
# if type(a) == int:
#
#     print('你的整体高度为：' + str(30))
# else:
#     print('请输入整数哦！不能输入字母哈')

# a = 'h'
# if type(a) == int:
#     print('OK')
# else:
#     print('error')
# a = input('请输入整数')
# print(type(a))

# a = int(input('请输入一个数字'))
# print('充值成功，你本次充值的金额为%s' % a)

# a = float(input('请输入父亲的身高：'))
# b = float(input('请输入母亲的身高：'))
# print('预测儿子的身高为：%s' % ((a+b)*0.54))

# a = int(input('请输入当天的行走步数：'))
# print('今天共消耗卡路里：%s (即%s千卡)' % (a*28, a*28/1000))

# a = 1
# while a <= 9:
#     c = a
#     while c <= 9:
#         s = '%s*%s=%s'% (a,c,a*c)
#         print(s, end='\t')
#         c += 1
#     a += 1
#     print()
# result = 0
# for i in range(1,101):        #累加功能，用到了变量的可变性
#     result += i
# print(result)

# for number in range(1,101):
#     if number % 3 == 2 and number % 5 == 3:
#         print(number, end=' ')


# for i in range(1,101):
#     print(i, end=' ')

# a = '我喜欢余情小姐姐'
# for i in a:
#     print(i)

# for i in range(1, 10):
#     for a in range(1, i+1):
#         print('%s*%s=%s' % (i, a, i*a), end=' ')
#     print()

# i = 1
# while i < 20:
#     i = i + 1
#     if i % 2 != 0:
#         continue
#     print(i, end=' ')

# total = 99
# for number in range(1,100):
#     if number % 7 == 0:
#         continue                  #continue调过循环，进入下一次循环
#     else:
#         string = str(number)
#         if string.endswith('7'):
#             continue
#     total -= 1
# print("从1数到99共拍腿", total,"次。")
# count = 0
# for i in range(1, 100):
#     if i % 7 == 0 or str(i).endswith('7'):
#         count += 1
# print(count, '次')

# a = input('查询能量请输入能量来源！退出程序请输入0\n'
#           '能用来源如下：\n'
#           '生活缴费,行走捐，共享单车，线下支付，网络购票\n'
#           '请输入查询：')
# if a == '行走捐':
#     print('200g')
# elif a == '生活缴费':
#     print('100g')
# elif a == '共享单车':
#     print('300g')
# elif a == '线下支付':
#     print('400g')
# elif a == '网络购票':
#     print('500g')
# elif a == '0':
#     print('已退出')
# else:
#     print('输入错误！请按提示输入')

# import random
# i = 0
# while i >= 0:
#     a = int(input('请输入一个1~10之间的任意一个数'))
#     c = random.randint(1, 10)
#     if c == a:
#         print('恭喜你，你赢了，猜中的数字是', str(a))
#         break
#     elif a > c:
#         print('太大，请重新输入')
#         continue
#     else:
#         print('太小，请重新输入')
#         continue

# print('欢迎回来，请开始游戏......')
# print('请输入(中心，音乐块，微信支付块):')
# count = 0
# while count >= 0:
#     a = input('请输入')
#     if a == '音乐块':
#         print('你的分数为：30分')
#         continue
#     elif a == '中心':
#         print('你的分数为：32分')
#         continue
#     elif a == '微信支付块':
#         print('你的分数为：42分')
#         continue
#     else:
#         print('你的分数为：1分')
#         continue

# import random
# print('-----------------------10086查询功能----------------------')
# print('输入1，查询当前余额')
# print('输入2，查询当前剩余流量')
# print('输入3，查询当前剩余通话时间')
# print('输入0，退出自助查询系统')
# a = 1
# while a > 0:
#     i = int(input())
#     if i == 1:
#         print('当前余额为：%s元' % random.randint(100, 300))
#         continue
#     elif i == 2:
#         print('当前剩余流量为：%sG' % random.randint(1, 10))
#         continue
#     elif i == 3:
#         print('当前剩余通话为：%s分钟' % random.randint(100, 300))
#         continue
#     elif i == 0:
#         print('退出自助查询系统')
#         break
#     else:
#         print('输入有误，请输入正确的查询代码！')
#         continue

# import redis
#
# pool = redis.ConnectionPool(host='127.0.0.1', port='6379', decode_responses=True, db=0)
# r = redis.Redis(connection_pool=pool)
# print('ok')

# r.lpush('name', 1,2,3,4,5,6,7,8,9,0)
# a = r.lrange('name', 0, -1)
# module_list = []
# for i in range(5):
#         modules = r.rpop('name')  # 删除并返回列表最后一个值，当列表不存在时返回None
#         if modules is not None:
#             module_list.append(modules)
# print(module_list)
# print(a)
# import time
# a = time.strftime("%Y-%m-%d %H:%M:%S")  #获取当前时间，并显示为易懂格式
# print(a)
# c = time.time()
# print(c)
# d = time.localtime(time.time())
# print(d)
import json
a = {'a': 1, 'b': 2}
print(type(a))
b = json.dumps(a)
print(type(b))
print(b)
c = json.loads(b)
print(type(c))