# coding:utf-8  #该python文件的编码格式
import urllib
import urllib2

url = "http://www.baidu.com/s"
word = {"wd": "拉勾"}
# urllib 仅可以接受 URL，⽽ urllib2 可以接受⼀个设置了 headers 的
# Request 类实例。这表示我们可以伪装⾃⼰的 User Agent 字符串等。
word = urllib.urlencode(word)  # 转换成 url 编码格式（字符串）
newurl = url + "?" + word  # url⾸个分隔符就是 ?
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/51.0.2704.103 Safari/537.36"}
request = urllib2.Request(newurl, headers=headers)
response = urllib2.urlopen(request)
print response.read()

# 关于urlEncode 说明
# 将字典按 URL 编码转换，汉字部分先转成 GBK 编码，然后把 \x 替换成 %
# In [3]: urllib.urlencode(word)
# Out[3]: "wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2"
# 把 % 替换成 \x，变回 GBK 编码，打印出来
# In [4]: print urllib.unquote("wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%
# A2")
# wd=拉勾
