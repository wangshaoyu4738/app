from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction

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


el1 = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
el2 = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
# 存储上滑到WLAN
driver.drag_and_drop(el2, el1)
time.sleep(2)
# el3 = driver.find_element_by_xpath("//*[contains(@text,'用户')]")
# 注意 这次使用drag_and_drop方法，传入的"存储定位"仍使用其原始在屏幕上的位置，所以是由存储滑动到用户才可以上滑，否则需要重新"定位存储"
# 存储上滑倒用户位置
# driver.drag_and_drop(el2, el3)
# 点击安全按钮
driver.find_element_by_xpath("//*[contains(@text,'安全')]").click()
# 点击屏幕锁定方式按钮
driver.find_element_by_xpath("//*[contains(@text,'屏幕锁定')]").click()
# 点击图案按钮
driver.find_element_by_xpath("//*[contains(@text,'图案')]").click()
# 绘制图案四个坐标 1:(244,967) 2:(723,967) 3:(723,1442) 4:(244,1916)
TouchAction(driver).press(x=105, y=452).move_to(x=271, y=452).wait(100).move_to(x=435, y=452).wait(100).move_to(x=-435, y=616).release().perform()


time.sleep(3)
driver.close_app()
driver.quit()

