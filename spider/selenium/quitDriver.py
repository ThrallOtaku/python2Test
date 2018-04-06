# coding:utf-8

from selenium import webdriver
# 调用键盘按键按操作,各种按键都可以在Keys里找到
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
# 关闭当前页
driver.close()
# 关闭浏览器
driver.quit()