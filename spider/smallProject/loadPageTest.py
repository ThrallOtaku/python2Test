# coding:utf-8
import urllib2


def loadPage(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()
    return html


def tiebaSpider(url, beginPage, endPage):
    user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; " \
                 "Windows NT 6.1; Trident / 5.0;"  # IE9.0 的 User-Agent
    headers = {"User-Agent": user_agent}
    for i in range(beginPage, endPage + 1):
        pn = 50 * (i - 1)
        html = loadPage(url + str(pn))
        print(html)


def writeFile(fileName, text):
    '''内容写入本地文件'''
    print("正在存储文件" + fileName)
    f = open(fileName, "w+")
    f.write(text)
    f.close()


if __name__ == '__main__':
    tiebaUrl = str(raw_input("请输入贴吧地址:"))
    beginPage = int(raw_input("请输入开始页数:"))
    endPage = int(raw_input("请输入结束页数:"))
    tiebaSpider(tiebaUrl, beginPage, endPage)
