# coding:utf-8
import urllib2

request = urllib2.Request("http://www.asdfasdf.com")
#首先捕获子类异常,如果没有那么捕获父类异常
try:
    urllib2.urlopen(request)
except urllib2.HTTPError,err:
    #print("httperror")
    print err.code
except urllib2.URLError,err:
    #print("urlError")
    print err
else:
    print "good"


#http error  404

