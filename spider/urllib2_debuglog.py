# coding:utf-8

import urllib2

# http debug
httpHandler =urllib2.HTTPHandler(debuglevel=1)
# https debug
httpsHandler=urllib2.HTTPSHandler(debuglevel=1)

# 同时使用两种不同的debug log模式
opener=urllib2.build_opener(httpHandler,httpsHandler)

urllib2.install_opener(opener)

response=urllib2.urlopen("http://www.baidu.com")