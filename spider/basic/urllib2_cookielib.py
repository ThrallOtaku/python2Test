# coding:utf-8

import urllib2
import cookielib

# cookie 对象
cookie =cookielib.CookieJar()

handler=urllib2.HTTPCookieProcessor(cookie)

opener=urllib2.build_opener(handler)

response=opener.open("http://www.baidu.com")

cookies=""
for item in cookie:
    cookies=cookies+item.name+"="+item.value+";"

# 舍去最后一位分号
print cookies[:-1]