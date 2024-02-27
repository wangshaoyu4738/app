from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
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

WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.ID, 'com.android.settings:id/search')))


time.sleep(3)
driver.close_app()
driver.quit()

