# coding:utf-8
# urllib2_cookielibtest2.py
# 读取本地cookie并通过cookie访问
import cookielib
import urllib2
# 创建 LWPCookieJar(有 load 实现)实例对象
cookie = cookielib.LWPCookieJar()
# 从⽂件中读取 cookie 内容到变量，忽略 cookie 的使⽤时效
cookie.load('../files/cookie.txt', ignore_discard=True, ignore_expires=True)
# 创建请求的 request
req = urllib2.Request("http://www.baidu.com")
# 利⽤urllib2 的 build_opener⽅法创建⼀个 opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()