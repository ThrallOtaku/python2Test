# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
try:
    #等到id="myDynamicElement"出现
    element=WebDriverWait(driver,10)\
        .until(EC.presence_of_all_elements_located(By.ID,"myDynamicElement"))
finally:
    driver.quit()
#如果不写参数，程序默认会0.5s调用一次里查看元素是否已经生成，
#如果本来元素就存在，那么会立即返回


#隐式等待
#就是简单设置一个等待时间
#如果如果不设置，默认等待时间为0
driver.implicitly_wait(10)
driver.get('http://www.baidu.com/loading')








