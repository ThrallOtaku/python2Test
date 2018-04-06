# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("http://www.douban.com")

#输入账号密码
driver.find_element_by_name("form_email").send_keys()