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

# 通过元素定位方式敲击屏幕
# el = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
# TouchAction(driver).tap(el).perform()
# 通过坐标方式敲击屏幕，WLAN坐标:x=149,y=324
# TouchAction(driver).tap(x=149, y=324).perform()

# 模拟手指按下屏幕,按就要对应着离开  wait(2000) 长按时间毫秒 release() 松开
# el = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
# TouchAction(driver).press(el).wait(2000).release().perform()

# 通过元素定位方式长按元素
# TouchAction(driver).long_press(el, duration=5000).release().perform()

# 手指滑动
el1 = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
el2 = driver.find_element_by_xpath("//*[contains(@text,'更多')]")
TouchAction(driver).press(el1).wait(1000).move_to(el2).release().perform()

# 绘制图案四个坐标 1:(244,967) 2:(723,967) 3:(723,1442) 4:(244,1916)
TouchAction(driver).press(x=244, y=967).wait(100).move_to(x=479, y=0).wait(100) \
    .move_to(x=0, y=475).wait(100).move_to(x=-479, y=474).release().perform()









time.sleep(3)
driver.close_app()
driver.quit()













