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
driver.close_app()

driver.start_activity('io.manong.developerdaily', 'io.toutiao.android.ui.activity.MainActivity')
driver.find_element_by_xpath('//*[contains(@text,"我的")]').click()
driver.find_element_by_id('io.manong.developerdaily:id/login_btn').click()
time.sleep(3)
driver.find_element_by_xpath('//*[contains(@text,"使用邮箱登录/注册")]').click()
driver.find_element_by_xpath('//*[contains(@text,"邮箱")]').send_keys('11111')
driver.find_element_by_xpath('//*[contains(@text,"密码")]').send_keys('111')
driver.find_element_by_xpath('//*[contains(@text,"登录")]').click()


time.sleep(3)

driver.quit()

