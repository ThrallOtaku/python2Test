# coding:utf-8

import urllib2
import jsonpath
import json
import chardet

url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
html = response.read()

# 把json转换为python对象
jsonObj = json.loads(html)

citylist = jsonpath.jsonpath(jsonObj, '$..name')
idList=jsonpath.jsonpath(jsonObj, '$..id')
print(citylist)

fp = open('city.json', 'w')

# encodig ，utf-8，默认是ascii
content = json.dumps(citylist, ensure_ascii=False)
idlistStr=json.dumps(idList,ensure_ascii=False)

print "这里开始打印dumps之后的cities"
print content
print(idlistStr)

fp.write(content.encode('utf-8'))
fp.close()
