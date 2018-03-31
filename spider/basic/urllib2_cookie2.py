# coding:utf-8
# urllib2_cookielibtest2.py
#访问网站获得cookie,把cookie保存在cookie中
import cookielib
import urllib2
# 设置保存 cookie 的⽂件，同级⽬录下的 cookie.txt
filename = '../files/cookie.txt'
# 声明⼀个 LWPCookieJar(有 save 实现)对象实例来保存 cookie，之后写⼊⽂件
cookie = cookielib.LWPCookieJar(filename)
# 利⽤urllib2 库的 HTTPCookieProcessor 对象来创建 cookie 处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过 handler 来构建 opener
opener = urllib2.build_opener(handler)
# 创建⼀个请求，原理同 urllib2 的 urlopen
response = opener.open("http://www.baidu.com")
# 保存 cookie 到⽂件，且忽略 cookie 失效限制
cookie.save(ignore_discard=True, ignore_expires=True)