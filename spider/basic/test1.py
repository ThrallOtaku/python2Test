#! python2
#fiddler 打开的情况下执行报错
import urllib2

response = urllib2.urlopen("http://www.baidu.com")
html = response.read()

print html
