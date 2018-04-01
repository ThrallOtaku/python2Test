# coding:utf-8

import requests

#r=requests.get('https://kyfw.12306.cn/otn/',verify=False)
r=requests.get('https://kyfw.12306.cn/otn/',verify=True)

print r.text