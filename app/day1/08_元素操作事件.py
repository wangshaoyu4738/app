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

# 找到存储和更多坐标    移动的是坐标, 只能操作显示的元素
save = driver.find_element_by_xpath("//*[contains(@text,'存储')]").location
more = driver.find_element_by_xpath("//*[contains(@text,'更多')]").location
# 滑动
driver.swipe(save['x'], save['y'], more['x'], more['y'])
time.sleep(3)

el1 = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
# 定位到WLAN菜单栏
el2 = driver.find_element_by_xpath("//*[contains(@text,'安全')]")
# 执行滚动操作  滚动操作只能操作显示的元素
driver.scroll(el1, el2)
time.sleep(3)

el1 = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
# 定位到WLAN菜单栏
el2 = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
# 执行长按拖动操作
driver.drag_and_drop(el1, el2)

# 将应用放置到后台,模拟热启动
# 进入设置,将app至于后台5s
driver.background_app(5)

driver.close_app()
driver.quit()

