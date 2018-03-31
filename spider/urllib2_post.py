# coding:utf-8
import urllib2
import urllib

output = open("lagou.json", "w")
page = 1
# POST 请求要传送的数据
formdata = "first=false&pn=" + str(page) + "&kd=xxx"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/51.0.2704.103 Safari/537.36"}
request = urllib2.Request("http://www.lagou.com/jobs/positionAjax.json?"
                          "px=new&needAddtionalResult=false", headers=headers)
# 通过 request.add_data() 将 data 数据传进⼊request 内
request.add_data(formdata)
# print request.get_data()
response = urllib2.urlopen(request)
print response.code
# print resHtml
output.write(response.read())
output.close()
