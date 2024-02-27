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

# 获取当前手机的时间
print(driver.device_time)
# 获取手机宽高
print(driver.get_window_size())
# 模拟系统键值操作,比如home键,音量键,返回键等.
# keycode：发送给设备的关键代码
for i in range(3):
    driver.keyevent(24)
# 打开手机通知栏
driver.open_notifications()
# 获取当前手机网络模式
print(driver.network_connection)
# 设置手机网络为飞行模式.
driver.set_network_connection(1)
# 截取 手机当前屏幕,保存指定格式图片到指定位置
import os
driver.get_screenshot_as_file(os.getcwd() + os.sep + './screen.png')


time.sleep(3)
driver.close_app()
driver.quit()






