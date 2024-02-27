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

time.sleep(3)
driver.close_app()
driver.quit()

