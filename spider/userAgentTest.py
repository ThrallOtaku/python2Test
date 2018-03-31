#coding:utf-8  #中文注释的时候需要引入这个
import urllib2

url = "http://www.baidu.com"
# IE 9.0 的 User-Agent
header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

request = urllib2.Request(url, headers=header)
# 也可以通过调⽤Request.add_header() 添加/修改⼀个特定的 header
request.add_header("Connection","keep-alive")

response = urllib2.urlopen(url)

html = response.read()
print html
