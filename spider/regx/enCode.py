# coding:utf-8
import chardet
import json

urf8str="你好转码"

#UTF8 转换为unicode
unicodeStr=urf8str.decode("UTF-8")

#unicode转换为gbk
gbkData=unicodeStr.encode("GBK")

#gbk转换为unicode
unicodeStr =gbkData.decode("gbk")

#unicode转换为UTF-8
utf8Str=unicodeStr.encode("utf-8")

dictStr = {"city": "北京", "name": "⼤猫"}
print(chardet.detect(json.dumps(dictStr)))
print(chardet.detect(json.dumps(dictStr,ensure_ascii=False)))

