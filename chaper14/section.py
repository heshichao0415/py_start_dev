#网络爬虫
"""
网络爬虫基本工作流程：
1、获取初始的URL，该URL是用户自己制定的初始爬取的网页
2、爬取对应URL地址的网页时，获取新的URL地址
3、将新的URL地址放入URL队列中
4、从URL队列中读取新的URL，然后依据新的URL爬取网页
5、设置停止条件
"""

#urllib模块
"""
urllib是Python自带模块、该模块提供了一个urlopen()方法
通过该方法指定URL发送网络请求来获取数据
urllib提供的子模块有：
urllib.request：该模块定义了打开URL（主要是HTTP）的方法和类，例如、身份验证、重定向、cookie等
urllib.error：该模块主要包含异常类、基本的异常时URLError
urllib.parse：该模块定义的功能分为两大类：URL解析和URL引用
urllib.robotparser：该模块用于解析robots.txt文件
"""
#通过urllib.request模块实现发送请求并读取网页内容的简单示例如下：
# import urllib.request          #导入模块
# #打开指定需要爬取的网页
# response = urllib.request.urlopen("http://www.baidu.com")
# html = response.read()          #读取网页代码
# print(html)                     #打印读取内容
#上面示例中，通过get请求方式获取百度的网页内容
#下面通过使用urllib.request模块的post请求实现获取网页信息的内容
# import urllib.parse
# import urllib.request
# #将数据使用urlencode编码处理，再使用encoding设置为utf-8编码
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# #打开指定需要爬取的网页
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# html = response.read()          #读取网页代码
# print(html)                     #打印读取内容
#http://httpbin.org/post练习网站，可以使用urllib的一个站点，可以模拟各种请求

#urlencode、可以把key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串

#Urllib3模块
"""
Urllib3是一个功能强大，条例清晰，用于HTTP客户端的python库
Urllib3提供了很多Python标准库里所没有的重要特性：
1、线程安全
2、连接池
3、客户端SSL/TLS验证
4、使用大部分编码上传文件
5、Helpers用于重试请求并处理HTTP重定向
6、支持gzip和deflate编码
7、支持HTTP和SOCKS代理
8、100%的测试覆盖率
"""
# import urllib3
# #创建PoolManager对象，用于处理与线程的连接以及线程安全的所有细节
# http = urllib3.PoolManager()
# #对需要爬取的网页发送请求
# response = http.request('GET', 'http://www.baidu.com')
# print(response.data)       #打印读取内容
# #post请求实现获取网页信息内容
# response = http.request('POST', 'http://httpbin.org/post', fields={'word': 'hello'})

#request模块
#使用request实现HTTP请求时要比urllib模块简化很多
# import requests
# response = requests.get("http://www.baidu.com")
# print(response.status_code)         #打印状态码
# print(response.url)                 #打印请求的URL
# print(response.headers)             #打印头部信息
# print(response.cookies)             #打印cookie信息
# print(response.text)                #以文本形式打印网页源代码
# print(response.content)             #以字节流形式打印网页源码
#以POST请求方式，发送HTTP网络请求
# import requests
# data = {'word': 'hello'}               #表单参数
# #对需要爬取的网页发送请求
# response = requests.post("http://httpbin.org/post", data=data)
# print(response.content)            #以字节流的形式打印网页源码
"""
requests()方法还提供了以下请求方式：
requests.put()     PUT请求
requests.delete()         DELETE请求
requests.head()            HEAD请求
requests.options()          OPTIONS请求
"""
#如果URL地址中参数是跟在“？”的后面，例如：httpbin.org/get?key=val。requests模块提供了传递参数的方式
#使用params关键字参数
# import requests
# payload = {'key1': 'value1', 'key2': 'value2'}
# response = requests.get("http://httpbin.org/get", params=payload)
# print(response.content)

#请求headers处理
"""
有时候我们在请求一个网页内容时，无论用post还是get请求都会出现403错误，
这是因为，这些网站做了反爬虫设置、从而拒绝了用户访问、
此时可以通过模拟浏览器的头部信息来进行访问，这样就能解决反爬虫设置的问题了
"""
# import requests
# url = 'https://www.baidu.com'
# #创建头部信息
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
# response = requests.get(url, headers=headers)
# print(response.content)

#网络超时
#在访问一个网页时，如果该网页长时间未响应，系统就会判断该网页超时
#代码模拟一个网络超时请求
# import requests
# #循环发送请求50次
# for a in range(0, 50):
#     try:
#         #设置超时时间为0.5秒
#         response = requests.get('https://www.baidu.com', timeout=0.05)
#         print(response.status_code)
#     except Exception as a:                 #捕获异常
#         print("异常" + str(a))             #打印异常信息
#打印异常信息为： 异常HTTPSConnectionPool(host='www.baidu.com', port=443): Read timed out. (read timeout=0.05)

# import requests
# #导入requests.exceptions模块中的3中异常类
# from requests.exceptions import ReadTimeout, HTTPError, RequestException
# #循环50次请求
# for a in range(0, 50):
#     try:
#         #设置超时时间0.05秒
#         response = requests.get("https://www.baidu.com", timeout=0.05)
#         print(response.status_code)
#     except ReadTimeout:
#         print('timeout')            #超时异常
#     except HTTPError:
#         print('httperror')          #HTTP异常
#     except RequestException:
#         print('reqerror')           #请求异常

#代理服务
"""
在爬取网页的过程中、经常会出现不久前可以爬取的网页现在无法爬取了，这是因为你的IP被爬取网站的服务器屏蔽了。
此时代理服务器可以为你解决这个问题
设置代理时，首选需要找到代理地址，
"""
# import requests
# #设置代理ip与对应的端口号
# proxy = {'http': '122.114.31.177:808',
#          'https': '122.114.31.177:8080'}
# #对需要爬取的网页发送请求
# response = requests.get('http://www.mingrisoft.com/', proxies=proxy)
# print(response.content)

#HTML解析之Beautiful Soup
"""
Beautiful Soup是一个用于从HTML和XML文件中提取数据的python库
Beautiful Soup提供一些简单的函数用来处理导航，搜索，修改分析树等功能
Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为UTF-8编码
安装Beautiful Soup4
pip install beautifulsoup4
"""
from bs4 import BeautifulSoup          #导入BeautifulSoup库
#创建模拟HTML代码的字符串
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
#创建一个Beautiful Soup对象，获取页面正文
# soup = BeautifulSoup(html_doc, features='lxml')     #指定解析为lxml，最后通过打印的方式将解析的HTML代码显示在控制台
# print(soup)

#如果是将html_doc字符串，保存在beautifule_test.html中，可以通过打开HTML文件的方式进行代码的解析
# soup = BeautifulSoup(open('beautiful_test.html'), 'lxml')
# print(soup.prettify())           #通过prettify()方法进行代码的格式化处理

#网络爬虫开发常用框架
"""
Scrapy框架，开源框架，不需要担心收费的问题
Crawley框架，Python开发出来的框架
特点：
1、基于Eventlet构建的高速网络爬虫框架
2、数据可存储在关系数据库中，如：mysql,oracle,SQLite等
3、可以将爬取的数据导入为json,XML格式。
4、支持非关系型数据库，如：Couchdb和Mongodb
5、支持命令行工具
6、可以使用你喜欢的工具进行数据提取，如：Xpath或Pyquery工具
7、支持使用cookie登录或访问那些只有登录才可以访问的网页
Crawley的官网：http://project.crawley-cloud.com
PySpider爬虫框架，采用python语言编写，分布式框架
特点：
1、Python脚本控制，可以用任何你喜欢的HTML解析包（内置pyquery)
2、WEB界面编写调试脚本，停止脚本，监控执行状态，查看活动历时，获取结果产出
3、支持MYSQL,SQLlit等等数据库
4、支持RabbitMQ、Beanstalk、redis等作为消息队列
5、支持爬取javaScript的页面
6、强大的调度控制、支持超时重爬及优先级设置
6、组件可替换，支持单机、分布式部署，支持Docker部署
PySpider源码地址：https://github.com/binux/pyspider/releases
开发文档地址为：http://docs.pyspider.org/
"""





