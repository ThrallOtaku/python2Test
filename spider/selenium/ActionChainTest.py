# coding:utf-8

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver =webdriver.PhantomJS()
# 鼠标移动到ac位置
ac=driver.find_element_by_xpath('element')
ActionChains(driver).move_to_element(ac).perform()

#在ac位置单击
ac =driver.find_element_by_xpath("elementA")
ActionChains(driver).move_to_element(ac).click(ac).perform()

#在ac位置双击
ac =driver.find_element_by_xpath("elementB")
ActionChains(driver).move_to_element(ac).double_click(ac).perform()

#在ac位置右击
ac =driver.find_element_by_xpath("elementC")
ActionChains(driver).move_to_element(ac).context_click(ac).perform()

#在ac位置左键单击hold住
ac =driver.find_element_by_xpath("elementF")
ActionChains(driver).move_to_element(ac).click_and_hold(ac).perform()

#将ac1拖拽到ac2位置
ac1=driver.find_element_by_xpath('elementD')
ac2=driver.find_element_by_xpath('elementE')
ActionChains(driver).drag_and_drop(ac1,ac2).perform()


#找到name的选项卡
select =Select(driver.find_element_by_name('status'))
#三种不同的方式选择select选项卡
select.select_by_index(1)
select.select_by_value("0")
select.select_by_visible_text(u"未审核")
#全部取消
select.deselect_all()

alert=driver.switch_to.alert

driver.switch_to.window("this is window name")

#前进
#后退
driver.forward()
driver.back()

for cookie in driver.get_cookies():
    print(cookie['name'],cookie['value'])

driver.delete_cookie("cookieName")
driver.delete_all_cookies()








