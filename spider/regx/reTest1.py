# coding:utf-8
import re

# r 表示字符串重的准一字符全部失效
#\d 表示数字
# +表示重复出现上一次1次或者n次
#\.表示.
# *表示重复上一次的0次或者n次
#整个正则的含义是匹配小数
pattern=re.compile(r'\d+\.\d*')

result=pattern.findall("13123.12312,'qfasdf',13123,123.25")

for item in result:
    print item
