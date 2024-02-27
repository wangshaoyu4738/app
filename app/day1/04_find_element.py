from appium import webdriver
import time


desired_caps = {}
# 平台名称
desired_caps['platformName'] = 'Android'
# 平台版本
desired_caps['platformVersion'] = '7.1.2'
# 设备号
desired_caps['deviceName'] = '127.0.0.1:62001'
# 应用的包名
desired_caps['appPackage'] = 'com.android.settings'
# 代表启动的界面
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.find_element_by_id("com.android.settings:id/search").click()
driver.find_element_by_class_name("android.widget.ImageButton").click()
driver.find_element_by_xpath("//*[contains(@text,'WLA')]").click()

title = driver.find_elements_by_id("com.android.settings:id/title")
title[1].click()
title = driver.find_elements_by_class_name("android.widget.TextView")
title[3].click()
data = driver.find_elements_by_xpath("//*[contains(@class,'android.widget.TextView')]")
data[3].click()

time.sleep(3)
driver.close_app()
driver.quit()















