import urllib.request
import chardet
import re
import os
path = os.path.split(os.path.realpath(__file__))[0]
path1 = os.path.join(path, 'images')
page = urllib.request.urlopen('http://photo.sina.com.cn/')
htmlCode = page.read() #获取网页源代码
# print(chardet.detect(htmlCode)) #打印返回网页的编码方式
# print(htmlCode.decode('utf-8')) #打印网页源代码
data = htmlCode.decode('utf-8')
# pageFile = open('pageCode.txt', 'wb')#以写的方式打开pageCode.txt
# pageFile.write(htmlCode)#写入
# pageFile.close()#开了记得关
reg = r'src="(.+?\.jpg)"'#正则表达式  ,,匹配以src="开头然后接一个或多个任意字符(非贪婪)，以.jpg" 结尾的字符串
reg_img = re.compile(reg)#编译一下，运行更快
imglist = reg_img.findall(data)#进行匹配
x = 0
for img in imglist:
    print(img)
    urllib.request.urlretrieve('%s' % img, '%s\\%s.jpg' % (path1, x))      #路径加文件名，保存在指定文件夹下
    x += 1

