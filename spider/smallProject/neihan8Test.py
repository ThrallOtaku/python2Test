# coding:utf-8

import urllib2
import re


class Spider:
    """内涵段子爬虫"""

    # 类的成员方法需要添加额外参数self
    def loadPage(self, page):
        url = "http://www.neihan8.com/article/list_5_" + str(page) + ".html"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                                 "AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/51.0.2704.103 Safari/537.36"}
        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req)

        html = response.read()
        # 处理抓到的中文字符集
        gbk_html = html.decode('gbk').encode('utf-8')

        # re.S表示将所有的字符串进行整体的普配
        pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>', re.S)
        item_list = pattern.findall(gbk_html)
        return item_list

    def writeToFile(self, text):
        myFile = open("../../files/duanzi.txt", "a")
        myFile.write(text)
        myFile.close()


if __name__ == "__main__":
    # print("按下回车开始")
    # raw_input()
    mySpider = Spider()
    # 这里可以设计成输入哪一页加载哪一页或者继续继续继续...
    item_list = mySpider.loadPage(2)
    for item in item_list:
        mySpider.writeToFile("===========")
        item = item.replace("<p>", "").replace("</p>", "").replace("<br />", "")
        mySpider.writeToFile(item)
