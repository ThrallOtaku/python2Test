# coding:utf-8

from selenium import webdriver
# 调用键盘按键按操作,各种按键都可以在Keys里找到
from selenium.webdriver.common.keys import Keys
import time

# 指定PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS()

driver.get("http://www.baidu.com")

data = driver.find_element_by_id("wrapper").text
print(data)

print(driver.title)

#生曾当前页面快照并保存
driver.save_screenshot("baidu.png")

driver.find_element_by_id("kw").send_keys(u"长毛象")

driver.find_element_by_id("su").click()

driver.save_screenshot("changmaoxiaong.png")

#打印网页选然后的源代码
print("打印网页选然后的源代码")
print driver.page_source

#获取当前页面的cookie
print driver.get_cookies()

#ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")

#ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"X")

#输入框重新输入内容
driver.find_element_by_id("kw").send_keys("yincheng")

time.sleep(2)
print("模拟enter回车")
driver.find_element_by_id("su").send_keys(Keys.RETURN)

print("清除输入框内容")
driver.find_element_by_id("kw").clear()

driver.save_screenshot("yincheng.png")

print("获取当前url")
print(driver.current_url)

# 关闭当前页
driver.close()
# 关闭浏览器
driver.quit()

