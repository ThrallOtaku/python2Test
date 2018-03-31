# coding:utf-8

import urllib2

proxyWork = True

# 定义两个代理模式
# 需要使用ccproxy 才能直接用代理服务器访问
httpProxyHandler = urllib2.ProxyHandler({"http": "124.88.67.81:80"})
print(httpProxyHandler.proxies)
nullProxyHandler = urllib2.ProxyHandler({})
print(nullProxyHandler.proxies)

if proxyWork:
    opener=urllib2.build_opener(httpProxyHandler)
else:
    opener=urllib2.build_opener(nullProxyHandler)

# 如果这么写，之后的 urlopen 将使⽤这个 opener
#urllib2.install_opener(opener)
#response = urlopen("http://www.baidu.com/")

response=opener.open("http://www.baidu.com")

html=response.read()

print(html)
